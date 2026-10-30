"""Interactive conversational tutor handlers."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.codelab.sandbox import run_student_code, preprocess_mobile_code, outputs_match
from bot.codelab.js_sandbox import run_student_js_code
from bot.codelab.html_checker import run_student_html_code
from bot.codelab.css_checker import run_student_css_code
from bot.codelab.sql_checker import run_student_sql_code
from bot.codelab.java_sandbox import run_student_java_code
from bot.codelab.csharp_sandbox import run_student_csharp_code
from bot.codelab.ts_sandbox import run_student_ts_code
from bot.codelab.bash_sandbox import run_student_bash_code
from bot.codelab.vb_sandbox import run_student_vb_code
from bot.codelab.perl_sandbox import run_student_perl_code
from bot.codelab.php_sandbox import run_student_php_code
from bot.codelab.c_sandbox import run_student_c_code
from bot.codelab.react_sandbox import run_student_react_code
from bot.codelab.react_native_sandbox import run_student_react_native_code
from bot.codelab.angular_sandbox import run_student_angular_code
from bot.codelab.vue_sandbox import run_student_vue_code
from bot.codelab.express_sandbox import run_student_express_code
from bot.codelab.django_sandbox import run_student_django_code
from bot.tutor.content_sql import SQL_SEED_SCRIPT
from bot.tutor.models import TutorChapter, TutorStep, StepType






from bot.tutor.content import (
    get_all_tutor_chapters,
    get_tutor_chapter,
    get_next_tutor_chapter_id,
)
from bot.keyboards import (
    get_tutor_chapters_keyboard,
    get_tutor_step_keyboard,
    get_tutor_concept_retry_keyboard,
    get_tutor_completion_keyboard,
    get_main_menu_keyboard,
)

logger = logging.getLogger(__name__)
router = Router(name="tutor_router")


class TutorStates(StatesGroup):
    """FSM states for interactive tutor sessions."""

    waiting_for_step_code = State()


async def render_step(
    target: Message | CallbackQuery,
    user_id: int,
    chapter: TutorChapter,
    step_index: int,
    lang: str,
    state: FSMContext,
    edit: bool = False,
    db: Database | None = None,
) -> None:
    """Render a tutor step or chapter completion card."""
    if step_index >= len(chapter.steps):
        # Chapter completed!
        if db:
            await db.set_tutor_progress(user_id, chapter.id, step_index, is_completed=True)
        await state.clear()

        next_ch_id = get_next_tutor_chapter_id(chapter.id)
        if lang == "am":
            title = chapter.get_title("am")
            text = (
                f"🎉 *እንኳን ደስ አለዎት! {title}ን አጠናቀዋል!* 🎓\n\n"
                "በኮዲንግ እውቀትዎ ላይ ትልቅ እርምጃ ተራምደዋል።\n\n"
                "ቀጣዩን ምዕራፍ ለመቀጠል ዝግጁ ነዎት?"
            )
        else:
            title = chapter.get_title("en")
            text = (
                f"🎉 *Congratulations! You completed {title}!* 🎓\n\n"
                "You have taken huge strides in understanding code and writing instructions.\n\n"
                "Ready to continue to the next chapter?"
            )

        kb = get_tutor_completion_keyboard(chapter.id, next_ch_id, lang)
        if isinstance(target, CallbackQuery):
            if edit and target.message and isinstance(target.message, Message):
                await target.message.edit_text(text=text, reply_markup=kb, parse_mode="Markdown")
            elif target.message and isinstance(target.message, Message):
                await target.message.answer(text=text, reply_markup=kb, parse_mode="Markdown")
            await target.answer()
        else:
            await target.answer(text=text, reply_markup=kb, parse_mode="Markdown")
        return

    # In progress step
    if db:
        await db.set_tutor_progress(user_id, chapter.id, step_index, is_completed=False)

    step = chapter.steps[step_index]
    step_num = step_index + 1
    total_steps = len(chapter.steps)

    step_tag = (
        f"ደረጃ {step_num}/{total_steps}"
        if lang == "am"
        else f"Step {step_num}/{total_steps}"
    )

    header = f"🧑‍🏫 *{chapter.get_title(lang)}*\n📍 _{step_tag}_\n\n"
    text = f"{header}{step.get_message(lang)}"
    keyboard = get_tutor_step_keyboard(chapter.id, step_index, step, lang)

    if step.step_type == StepType.CODE_PROMPT:
        await state.set_state(TutorStates.waiting_for_step_code)
        await state.update_data(chapter_id=chapter.id, step_index=step_index)
    else:
        await state.clear()

    if isinstance(target, CallbackQuery):
        if edit and target.message and isinstance(target.message, Message):
            await target.message.edit_text(text=text, reply_markup=keyboard, parse_mode="Markdown")
        elif target.message and isinstance(target.message, Message):
            await target.message.answer(text=text, reply_markup=keyboard, parse_mode="Markdown")
        await target.answer()
    else:
        await target.answer(text=text, reply_markup=keyboard, parse_mode="Markdown")


def get_track_display_name(t: str, l: str) -> str:
    """Return friendly localized track title."""
    if t == "django":
        return "የዲጃንጎ ትምህርት (Django 🎸)" if l == "am" else "Django Python Full-Stack Track 🎸"
    if t == "express":
        return "የኤክስፕረስ ትምህርት (Express.js 🚂)" if l == "am" else "Express.js Backend Track 🚂"
    if t == "vue":
        return "የቪው ትምህርት (Vue.js 💚)" if l == "am" else "Vue.js Track 💚"
    if t == "angular":
        return "የአንጉላር ትምህርት (Angular 🅰️)" if l == "am" else "Angular Enterprise Track 🅰️"
    if t == "react_native":
        return "የሪያክት ኔቲቭ ትምህርት (React Native 📱)" if l == "am" else "React Native Mobile Track 📱"
    if t == "react":
        return "የሪያክት ትምህርት (React ⚛️)" if l == "am" else "React UI Track ⚛️"
    if t == "c":
        return "የሲ ቋንቋ ትምህርት (C 🇨)" if l == "am" else "C Language Track 🇨"
    if t == "php":
        return "የፒኤችፒ ትምህርት (PHP 🐘)" if l == "am" else "PHP Track 🐘"
    if t == "perl":
        return "የፐርል ትምህርት (Perl 🐪)" if l == "am" else "Perl Track 🐪"
    if t == "vb":
        return "የቪዥዋል ቤዚክ ትምህርት (Visual Basic 💎)" if l == "am" else "Visual Basic Track 💎"
    if t == "bash":
        return "የሊኑክስ ባሽ ትምህርት (Linux Bash 🐧)" if l == "am" else "Linux Bash Track 🐧"

    if t == "typescript":
        return "የታይፕስክሪፕት ትምህርት (TypeScript 🔷)" if l == "am" else "TypeScript Track 🔷"

    if t == "csharp":
        return "የሲ ሻርፕ ትምህርት (C# ⚡)" if l == "am" else "C# Track ⚡"

    if t == "java":
        return "የጃቫ ትምህርት (Java ☕)" if l == "am" else "Java Track ☕"
    if t == "sql":
        return "የኤስኪውኤል ትምህርት (SQL 🗄️)" if l == "am" else "SQL Database Track 🗄️"


    if t == "css":
        return "የሲኤስኤስ ትምህርት (CSS 🎨)" if l == "am" else "CSS Styling Track 🎨"
    if t == "html":
        return "የኤችቲኤምኤል ትምህርት (HTML 📄)" if l == "am" else "HTML Web Track 📄"
    if t == "javascript":
        return "የጃቫስክሪፕት ትምህርት (JavaScript 🌐)" if l == "am" else "JavaScript Track 🌐"
    return "የፓይተን ትምህርት (Python 🐍)" if l == "am" else "Python Track 🐍"



@router.message(Command("tutor"))
@router.callback_query(F.data == "tutor:chapters")
async def handle_tutor_menu(
    event: Message | CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Display interactive tutor chapters overview for active track."""
    await state.clear()
    user = event.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE
    track = await db.get_user_track(user_id) if user_id else "python"

    completed_chapters = await db.get_completed_tutor_chapters(user_id) if user_id else set()
    track_name = get_track_display_name(track, lang)

    if lang == "am":
        text = (
            f"🧑‍🏫 *የኮድበዲ የግል አስተማሪ — {track_name}*\n\n"
            "ከእኔ ጋር ደረጃ በደረጃ እየተነጋገሩ ኮዲንግን ይማሩ! "
            "ጽንሰ ሃሳቦችን እናስረዳዎታለን፣ ኮድ እንዲጽፉ እናደርጋለን፣ እንዲሁም በየመንገዱ እንረዳዎታለን።\n\n"
            "ለመጀመር ወይም ለመቀጠል ምዕራፍ ይምረጡ፦"
        )
    else:
        text = (
            f"🧑‍🏫 *CodeBuddy Personal Tutor — {track_name}*\n\n"
            "Learn programming through step-by-step dialogue with me! "
            "I'll explain concepts, have you write real code right here in the chat, "
            "and guide you every step of the way.\n\n"
            "Choose a chapter below to start or continue:"
        )

    keyboard = get_tutor_chapters_keyboard(completed_chapters, lang, track=track)

    if isinstance(event, CallbackQuery):
        await event.answer()
        if event.message and isinstance(event.message, Message):
            await event.message.edit_text(text=text, reply_markup=keyboard, parse_mode="Markdown")
    else:
        await event.answer(text=text, reply_markup=keyboard, parse_mode="Markdown")


@router.callback_query(F.data.startswith("tutor:track:"))
async def handle_switch_track(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Switch user's active learning track between Python, JavaScript, and HTML."""
    parts = callback.data.split(":")
    if len(parts) < 3:
        await callback.answer()
        return

    new_track = parts[2]
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if user_id:
        await db.set_user_track(user_id, new_track)

    track_name = get_track_display_name(new_track, lang)
    alert_msg = f"Switched to {track_name}!" if lang == "en" else f"ወደ {track_name} ተቀይሯል!"
    await callback.answer(alert_msg)

    completed_chapters = await db.get_completed_tutor_chapters(user_id) if user_id else set()

    if lang == "am":
        text = (
            f"🧑‍🏫 *የኮድበዲ የግል አስተማሪ — {track_name}*\n\n"
            "ከእኔ ጋር ደረጃ በደረጃ እየተነጋገሩ ኮዲንግን ይማሩ! "
            "ጽንሰ ሃሳቦችን እናስረዳዎታለን፣ ኮድ እንዲጽፉ እናደርጋለን፣ እንዲሁም በየመንገዱ እንረዳዎታለን።\n\n"
            "ለመጀመር ወይም ለመቀጠል ምዕራፍ ይምረጡ፦"
        )
    else:
        text = (
            f"🧑‍🏫 *CodeBuddy Personal Tutor — {track_name}*\n\n"
            "Learn programming through step-by-step dialogue with me! "
            "I'll explain concepts, have you write real code right here in the chat, "
            "and guide you every step of the way.\n\n"
            "Choose a chapter below to start or continue:"
        )

    keyboard = get_tutor_chapters_keyboard(completed_chapters, lang, track=new_track)
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(text=text, reply_markup=keyboard, parse_mode="Markdown")


@router.callback_query(F.data.startswith("tutor:start:"))
async def handle_start_chapter(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Start or resume a tutor chapter."""
    parts = callback.data.split(":")
    if len(parts) < 3:
        await callback.answer()
        return

    chapter_id = parts[2]
    chapter = get_tutor_chapter(chapter_id)
    if not chapter:
        await callback.answer("Chapter not found / ምዕራፉ አልተገኘም", show_alert=True)
        return

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    saved_step, is_completed = await db.get_tutor_progress(user_id, chapter_id)
    # If already completed or out of bounds, restart from step 0
    start_step = 0 if is_completed or saved_step >= len(chapter.steps) else saved_step

    await render_step(
        target=callback,
        user_id=user_id,
        chapter=chapter,
        step_index=start_step,
        lang=lang,
        state=state,
        edit=True,
        db=db,
    )


@router.callback_query(F.data.startswith("tutor:step:"))
async def handle_tutor_step_callback(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Advance to a specific step in the tutor chapter."""
    parts = callback.data.split(":")
    if len(parts) < 4:
        await callback.answer()
        return

    chapter_id = parts[2]
    step_index = int(parts[3])

    chapter = get_tutor_chapter(chapter_id)
    if not chapter:
        await callback.answer()
        return

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    await render_step(
        target=callback,
        user_id=user_id,
        chapter=chapter,
        step_index=step_index,
        lang=lang,
        state=state,
        edit=True,
        db=db,
    )


@router.callback_query(F.data.startswith("tutor:hint:"))
async def handle_tutor_hint_callback(
    callback: CallbackQuery, db: Database
) -> None:
    """Display hint for the current code prompt step."""
    parts = callback.data.split(":")
    if len(parts) < 4:
        await callback.answer()
        return

    chapter_id = parts[2]
    step_index = int(parts[3])

    chapter = get_tutor_chapter(chapter_id)
    if not chapter or step_index >= len(chapter.steps):
        await callback.answer()
        return

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    step = chapter.steps[step_index]
    hint = step.get_hint(lang)
    if not hint:
        hint = "No hint available for this step." if lang == "en" else "ለዚህ ደረጃ ምንም ፍንጭ የለም።"

    await callback.answer(text=hint, show_alert=True)


@router.callback_query(F.data.startswith("tutor:opt:"))
async def handle_tutor_concept_option(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Handle student answer to a concept check question."""
    parts = callback.data.split(":")
    if len(parts) < 5:
        await callback.answer()
        return

    chapter_id = parts[2]
    step_index = int(parts[3])
    chosen_opt = int(parts[4])

    chapter = get_tutor_chapter(chapter_id)
    if not chapter or step_index >= len(chapter.steps):
        await callback.answer()
        return

    step = chapter.steps[step_index]
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    is_correct = chosen_opt == step.correct_option_index

    if is_correct:
        await callback.answer("🎉 Correct! / ትክክል ነው!", show_alert=False)
        # Advance to next step
        await render_step(
            target=callback,
            user_id=user_id,
            chapter=chapter,
            step_index=step_index + 1,
            lang=lang,
            state=state,
            edit=True,
            db=db,
        )
    else:
        await callback.answer("Incorrect / አልተሳካም", show_alert=False)
        if lang == "am":
            retry_text = (
                "🤔 *ልክ አይደለም፣ ግን ጥሩ ሙከራ ነው!*\n\n"
                "አይጨነቁ፣ ኮዲንግ በመሞከር እና በመለማመድ ነው የሚለመደው። እንደገና እንሞክር!"
            )
        else:
            retry_text = (
                "🤔 *Not quite, but great effort!*\n\n"
                "Don't worry, trial and error is how we learn to code. Let's try again!"
            )

        kb = get_tutor_concept_retry_keyboard(chapter_id, step_index, lang)
        if callback.message and isinstance(callback.message, Message):
            await callback.message.edit_text(text=retry_text, reply_markup=kb, parse_mode="Markdown")


@router.message(TutorStates.waiting_for_step_code)
async def handle_student_step_code(
    message: Message, db: Database, state: FSMContext
) -> None:
    """Handle code typed by student in response to a tutor CODE_PROMPT step."""
    code_text = preprocess_mobile_code(message.text or "")

    # Check for cancellation or standard navigation commands
    if code_text.strip().startswith("/"):
        cmd = code_text.strip().split()[0].lower()
        if cmd in ("/cancel", "/exit", "/menu", "/start", "/help", "/tutor"):
            await state.clear()
            user = message.from_user
            user_id = user.id if user else 0
            lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE
            exit_msg = (
                "👋 Tutor paused. Returning to main menu."
                if lang == "en"
                else "👋 አስተማሪው ቆሟል። ወደ ዋናው ማውጫ ተመልሰዋል።"
            )
            await message.answer(exit_msg, reply_markup=get_main_menu_keyboard(lang))
            return

    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    state_data = await state.get_data()
    chapter_id = state_data.get("chapter_id")
    step_index = state_data.get("step_index", 0)

    chapter = get_tutor_chapter(chapter_id) if chapter_id else None
    if not chapter or step_index >= len(chapter.steps):
        await state.clear()
        return

    step = chapter.steps[step_index]

    # Execute student code in safe sandbox based on track
    if getattr(chapter, "track", "python") == "django":
        result = run_student_django_code(code_text)
    elif getattr(chapter, "track", "python") == "express":
        result = run_student_express_code(code_text)
    elif getattr(chapter, "track", "python") == "vue":
        result = run_student_vue_code(code_text)
    elif getattr(chapter, "track", "python") == "angular":
        result = run_student_angular_code(code_text)
    elif getattr(chapter, "track", "python") == "react_native":
        result = run_student_react_native_code(code_text)
    elif getattr(chapter, "track", "python") == "react":
        result = run_student_react_code(code_text)
    elif getattr(chapter, "track", "python") == "c":
        result = run_student_c_code(code_text)
    elif getattr(chapter, "track", "python") == "php":
        result = run_student_php_code(code_text)
    elif getattr(chapter, "track", "python") == "perl":
        result = run_student_perl_code(code_text)
    elif getattr(chapter, "track", "python") == "vb":
        result = run_student_vb_code(code_text)
    elif getattr(chapter, "track", "python") == "bash":
        result = run_student_bash_code(code_text)
    elif getattr(chapter, "track", "python") == "typescript":

        result = run_student_ts_code(code_text)
    elif getattr(chapter, "track", "python") == "csharp":

        result = run_student_csharp_code(code_text)
    elif getattr(chapter, "track", "python") == "java":

        result = run_student_java_code(code_text)
    elif getattr(chapter, "track", "python") == "sql":

        result = run_student_sql_code(code_text, setup_script=SQL_SEED_SCRIPT)
    elif getattr(chapter, "track", "python") == "css":
        result = run_student_css_code(code_text)
    elif getattr(chapter, "track", "python") == "html":
        result = run_student_html_code(code_text)
    elif getattr(chapter, "track", "python") == "javascript":
        result = run_student_js_code(code_text)
    else:
        result = run_student_code(code_text)



    if not result.success:
        # Code execution produced an error (syntax or runtime)
        error_msg = (
            result.friendly_explanation_am
            if lang == "am" and result.friendly_explanation_am
            else (result.friendly_explanation_en or result.error_message or "Syntax/Runtime Error")
        )
        hint = step.get_hint(lang)
        if lang == "am":
            response = (
                "❌ *ኮድዎን በማስኬድ ላይ ስህተት አጋጥሟል፦*\n\n"
                f"{error_msg}\n\n"
                f"💡 *ምክር፦* {hint}\n\n"
                "አይጨነቁ፣ ስህተት የኮዲንግ መማሪያ መንገድ ነው! እንደገና ጽፈው ይላኩ፦"
            )
        else:
            response = (
                "❌ *Oops, there was an issue running your code:*\n\n"
                f"{error_msg}\n\n"
                f"💡 *Tip:* {hint}\n\n"
                "Don't worry, fixing bugs is what programmers do! Try writing it again:"
            )

        await message.answer(
            text=response,
            reply_markup=get_tutor_step_keyboard(chapter.id, step_index, step, lang),
            parse_mode="Markdown",
        )
        return

    # Check output match
    student_output = result.output.strip()
    if step.expected_code_output is not None:
        expected = step.expected_code_output.strip()
        if not outputs_match(student_output, expected):
            hint = step.get_hint(lang)
            if lang == "am":
                response = (
                    "🔍 *ለማግኘት ተቃርበዋል! ኮድዎ ሰርቷል ግን ውጤቱ አልተመሳሰለም፦*\n\n"
                    f"የእርስዎ ውጤት፦ `{student_output}`\n"
                    f"የተጠበቀው ውጤት፦ `{expected}`\n\n"
                    f"💡 *ምክር፦* {hint}\n\n"
                    "እባክዎ እንደገና ይሞክሩ፦"
                )
            else:
                response = (
                    "🔍 *Almost there! Your code ran, but the output was slightly different:*\n\n"
                    f"Your output: `{student_output}`\n"
                    f"Expected output: `{expected}`\n\n"
                    f"💡 *Tip:* {hint}\n\n"
                    "Take another look and try again:"
                )

            await message.answer(
                text=response,
                reply_markup=get_tutor_step_keyboard(chapter.id, step_index, step, lang),
                parse_mode="Markdown",
            )
            return

    # Code succeeded and matched expectations!
    success_msg = step.get_success_message(lang)
    output_card = (
        f"🖥️ *ኮምፒውተሩ ያሳየው ውጤት፦*\n`{student_output}`\n\n{success_msg}"
        if lang == "am"
        else f"🖥️ *Computer Output:*\n`{student_output}`\n\n{success_msg}"
    )

    await message.answer(text=output_card, parse_mode="Markdown")

    # Advance to next step
    await render_step(
        target=message,
        user_id=user_id,
        chapter=chapter,
        step_index=step_index + 1,
        lang=lang,
        state=state,
        edit=False,
        db=db,
    )


@router.callback_query(F.data == "tutor:exit")
async def handle_tutor_exit(
    callback: CallbackQuery, db: Database, state: FSMContext
) -> None:
    """Exit tutor session and return to main menu."""
    await state.clear()
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if lang == "am":
        text = (
            "👋 ከአስተማሪው ክፍለ-ጊዜ ወጥተዋል!\n\n"
            "የሰሩት እድገት ተቀምጧል። በፈለጉት ጊዜ /tutor በማለት መቀጠል ይችላሉ።"
        )
    else:
        text = (
            "👋 You've exited the tutor session!\n\n"
            "Your progress has been saved. You can resume anytime by sending /tutor."
        )

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.answer(
            text=text,
            reply_markup=get_main_menu_keyboard(lang),
            parse_mode="Markdown",
        )
