"""Interactive practice arena and quiz handlers."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.practice import (
    get_all_quizzes,
    get_quiz,
    get_next_quiz_id,
)
from bot.keyboards import (
    get_practice_menu_keyboard,
    get_quiz_keyboard,
    get_quiz_result_keyboard,
    get_quiz_list_keyboard,
)

logger = logging.getLogger(__name__)
router = Router(name="practice_router")


def format_quiz_card(quiz, lang: str = DEFAULT_LANGUAGE) -> str:
    """Format a quiz question card for Telegram."""
    header = f"🎯 *Challenge {quiz.order}*\n\n"
    question = quiz.get_question(lang)

    body = f"{header}{question}"
    if quiz.code_snippet:
        body += f"\n\n```python\n{quiz.code_snippet}\n```"

    instruction = (
        "\n\n👇 *Select your answer below:*"
        if lang == "en"
        else "\n\n👇 *መልስዎን ከዚህ በታች ይምረጡ፦*"
    )
    return body + instruction


@router.message(Command("practice"))
async def handle_practice_command(message: Message, db: Database) -> None:
    """Handle /practice command to open practice arena."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    text = get_string("practice_hub_title", lang)
    keyboard = get_practice_menu_keyboard(lang)

    await message.answer(
        text=text,
        reply_markup=keyboard,
        parse_mode="Markdown",
    )


@router.callback_query(F.data == "quiz:menu")
async def handle_practice_menu_callback(callback: CallbackQuery, db: Database) -> None:
    """Return to practice menu."""
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    text = get_string("practice_hub_title", lang)
    keyboard = get_practice_menu_keyboard(lang)

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data == "quiz:list")
async def handle_quiz_list_callback(callback: CallbackQuery, db: Database) -> None:
    """List all available quizzes with solved status."""
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    solved_ids = await db.get_solved_quizzes(user_id) if user_id else set()
    quizzes = get_all_quizzes()
    keyboard = get_quiz_list_keyboard(quizzes, solved_ids, lang)

    title = "📋 *Practice Challenges:*" if lang == "en" else "📋 *የልምምድ ፈተናዎች፦*"

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=title,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("quiz:view:"))
async def handle_view_quiz_callback(callback: CallbackQuery, db: Database) -> None:
    """Display an individual quiz question."""
    if not callback.data:
        await callback.answer()
        return

    quiz_id = callback.data.split(":", 2)[2]
    quiz = get_quiz(quiz_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if not quiz:
        await callback.answer("Quiz not found", show_alert=True)
        return

    text = format_quiz_card(quiz, lang)
    keyboard = get_quiz_keyboard(quiz, lang)

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("quiz:ans:"))
async def handle_quiz_answer_callback(callback: CallbackQuery, db: Database) -> None:
    """Check chosen quiz answer, record attempt, and display explanation."""
    if not callback.data:
        await callback.answer()
        return

    parts = callback.data.split(":")
    if len(parts) < 4:
        await callback.answer()
        return

    quiz_id = parts[2]
    try:
        chosen_idx = int(parts[3])
    except ValueError:
        await callback.answer()
        return

    quiz = get_quiz(quiz_id)
    if not quiz:
        await callback.answer()
        return

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    is_correct = quiz.is_correct(chosen_idx)

    # Persist attempt to SQLite
    if user_id:
        await db.record_quiz_attempt(user_id, quiz.id, is_correct)

    next_quiz_id = get_next_quiz_id(quiz.id)
    result_keyboard = get_quiz_result_keyboard(quiz, next_quiz_id, lang)

    if is_correct:
        status_line = (
            "🎉 *Correct! Excellent work!*"
            if lang == "en"
            else "🎉 *ትክክል ነው! በጣም ጎበዝ!*"
        )
    else:
        status_line = (
            "❌ *Not quite, but good try!*"
            if lang == "en"
            else "❌ *አልተሳካም፣ ነገር ግን ጥሩ ሙከራ ነው!*"
        )

    explanation = quiz.get_explanation(lang)
    response_text = (
        f"{status_line}\n\n"
        f"💡 *Explanation:*\n{explanation}"
        if lang == "en"
        else f"{status_line}\n\n💡 *ማብራሪያ፦*\n{explanation}"
    )

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=response_text,
            reply_markup=result_keyboard,
            parse_mode="Markdown",
        )
