"""CodeLab handlers for hands-on code writing and execution."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.codelab.challenges import (
    get_all_challenges,
    get_challenge,
    get_next_challenge_id,
)
from bot.codelab.sandbox import run_student_code
from bot.keyboards import (
    get_codelab_menu_keyboard,
    get_challenge_view_keyboard,
    get_challenge_result_keyboard,
    get_challenge_list_keyboard,
)

logger = logging.getLogger(__name__)
router = Router(name="codelab_router")


class CodeLabStates(StatesGroup):
    """FSM states for code submission."""

    waiting_for_code = State()


def format_challenge_card(challenge, lang: str = DEFAULT_LANGUAGE) -> str:
    """Format a coding challenge prompt card."""
    title = challenge.get_title(lang)
    prompt = challenge.get_prompt(lang)

    instructions = (
        "\n\n👉 *Write your code in the chat below and send it:* ⌨️"
        if lang == "en"
        else "\n\n👉 *ኮድዎን ከዚህ በታች ባለው የጽሁፍ ሳጥን ውስጥ ጽፈው ይላኩ፦* ⌨️"
    )

    return f"💻 *{title}*\n\n{prompt}{instructions}"


@router.message(Command("codelab"))
@router.callback_query(F.data == "code:menu")
async def handle_codelab_menu(
    event: Message | CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Display CodeLab hands-on coding hub."""
    await state.clear()
    user = event.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    intro_text = (
        "💻 *CodeLab: Write Real Python Code!*\n\n"
        "Here you don't just answer multiple-choice questions—you *write real code*!\n\n"
        "CodeBuddy will run your code in a safe sandbox and evaluate your output."
        if lang == "en"
        else (
            "💻 *የኮድ መጻፊያ ማዕከል (CodeLab)*\n\n"
            "እዚህ ምርጫ ብቻ ሳይሆን *እውነተኛ የፓይተን ኮድ በራስዎ ይጽፋሉ*!\n\n"
            "ኮድበዲ የጻፉትን ኮድ ያሂዳል፣ ስህተት ካለ ያርማል፣ ውጤቱንም ይፈትሻል።"
        )
    )

    keyboard = get_codelab_menu_keyboard(lang)

    if isinstance(event, CallbackQuery):
        await event.answer()
        if event.message and isinstance(event.message, Message):
            await event.message.edit_text(
                text=intro_text,
                reply_markup=keyboard,
                parse_mode="Markdown",
            )
    else:
        await event.answer(
            text=intro_text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data == "code:list")
async def handle_challenge_list(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Display all coding challenges with completion badges."""
    await state.clear()
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    completed_ids = await db.get_completed_code_challenges(user_id) if user_id else set()
    challenges = get_all_challenges()
    keyboard = get_challenge_list_keyboard(challenges, completed_ids, lang)

    title = "📋 *Code Writing Challenges:*" if lang == "en" else "📋 *የኮድ መጻፊያ ፈተናዎች፦*"

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=title,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("code:view:"))
async def handle_view_challenge(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Display an individual coding challenge and enter waiting state."""
    if not callback.data:
        await callback.answer()
        return

    challenge_id = callback.data.split(":", 2)[2]
    challenge = get_challenge(challenge_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if not challenge:
        await callback.answer("Challenge not found", show_alert=True)
        return

    # Enter waiting for code state
    await state.set_state(CodeLabStates.waiting_for_code)
    await state.update_data(challenge_id=challenge.id)

    text = format_challenge_card(challenge, lang)
    keyboard = get_challenge_view_keyboard(challenge.id, lang)

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("code:hint:"))
async def handle_show_hint(callback: CallbackQuery, db: Database) -> None:
    """Show the hint for the current challenge."""
    if not callback.data:
        await callback.answer()
        return

    challenge_id = callback.data.split(":", 2)[2]
    challenge = get_challenge(challenge_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if challenge:
        hint = challenge.get_hint(lang)
        alert_header = "💡 Hint:" if lang == "en" else "💡 ፍንጭ፦"
        await callback.answer(f"{alert_header} {hint}", show_alert=True)
    else:
        await callback.answer()


@router.callback_query(F.data == "code:cancel")
async def handle_cancel_coding(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Cancel code writing mode and clear state."""
    await state.clear()
    await handle_codelab_menu(callback, db, state)


@router.message(CodeLabStates.waiting_for_code)
async def handle_student_code_submission(
    message: Message, db: Database, state: FSMContext
) -> None:
    """Evaluate submitted code, execute in sandbox, and provide instant feedback."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    state_data = await state.get_data()
    challenge_id = state_data.get("challenge_id")
    challenge = get_challenge(challenge_id) if challenge_id else None

    if not challenge:
        await state.clear()
        await message.answer("Session expired. Please select a challenge again.")
        return

    student_code = message.text or ""

    # Execute safely in sandbox
    result = run_student_code(student_code)

    # 1. Execution Failure (SyntaxError, NameError, forbidden builtin)
    if not result.success:
        friendly_error = (
            result.friendly_explanation_am if lang == "am" else result.friendly_explanation_en
        )
        response_text = (
            f"❌ *Code Did Not Run Successfully*\n\n"
            f"💡 *What went wrong:*\n{friendly_error}\n\n"
            f"🔄 *Try again! Fix your code and send it below:*"
            if lang == "en"
            else (
                f"❌ *ኮድዎ በተሳካ ሁኔታ አልሰራም*\n\n"
                f"💡 *ምን ተሳሳተ?*\n{friendly_error}\n\n"
                f"🔄 *እንደገና ይሞክሩ! አስተካክለው ከዚህ በታች ይላኩ፦*"
            )
        )
        await message.answer(
            text=response_text,
            reply_markup=get_challenge_view_keyboard(challenge.id, lang),
            parse_mode="Markdown",
        )
        return

    # 2. Execution Succeeded - Check Output Against Challenge Goal
    is_correct = challenge.check_solution(result.output)

    if is_correct:
        # Save to database
        await state.clear()
        if user_id:
            await db.record_code_challenge_completion(user_id, challenge.id, student_code)

        next_id = get_next_challenge_id(challenge.id)
        result_keyboard = get_challenge_result_keyboard(next_id, challenge.id, lang)

        celebration = (
            f"🎉 *Fantastic! Your code ran perfectly!*\n\n"
            f"🖥️ *Program Output:*\n"
            f"```text\n{result.output.strip()}\n```\n\n"
            f"🌟 You wrote real working Python code!"
            if lang == "en"
            else (
                f"🎉 *በጣም ድንቅ! ኮድዎ በትክክል ሰርቷል!*\n\n"
                f"🖥️ *የፕሮግራሙ ውጤት፦*\n"
                f"```text\n{result.output.strip()}\n```\n\n"
                f"🌟 እውነተኛ የፓይተን ኮድ በተሳካ ሁኔታ ጽፈዋል!"
            )
        )

        await message.answer(
            text=celebration,
            reply_markup=result_keyboard,
            parse_mode="Markdown",
        )
    else:
        # Code ran, but output did not match expectation
        hint = challenge.get_hint(lang)
        mismatch_text = (
            f"⚠️ *Almost there!*\n\n"
            f"Your code ran, but the output was:\n"
            f"```text\n{result.output.strip()}\n```\n"
            f"Expected output:\n"
            f"```text\n{challenge.expected_output.strip()}\n```\n\n"
            f"💡 *Hint:* {hint}\n\n"
            f"👇 Fix your code and send it again:"
            if lang == "en"
            else (
                f"⚠️ *ትንሽ ነው የቀረው!*\n\n"
                f"ኮድዎ ሰርቷል፣ ነገር ግን ያመጣው ውጤት፦\n"
                f"```text\n{result.output.strip()}\n```\n"
                f"የሚጠበቀው ውጤት፦\n"
                f"```text\n{challenge.expected_output.strip()}\n```\n\n"
                f"💡 *ፍንጭ፦* {hint}\n\n"
                f"👇 አስተካክለው እንደገና ይላኩ፦"
            )
        )

        await message.answer(
            text=mismatch_text,
            reply_markup=get_challenge_view_keyboard(challenge.id, lang),
            parse_mode="Markdown",
        )
