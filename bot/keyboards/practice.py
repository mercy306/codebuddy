"""Keyboards for practice arena and interactive quizzes."""

from __future__ import annotations

from typing import Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.practice.models import QuizQuestion
from bot.strings import get_string, DEFAULT_LANGUAGE


OPTION_LETTERS = ("A", "B", "C", "D")


def get_practice_menu_keyboard(lang: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    """Build keyboard for practice arena hub."""
    tutor_text = "🧑‍🏫 Interactive Tutor (Step-by-Step)" if lang == "en" else "🧑‍🏫 በደረጃ የሚያስተምር (Tutor)"
    codelab_text = "✍️ Write Real Code (CodeLab)" if lang == "en" else "✍️ እውነተኛ ኮድ መጻፍ (CodeLab)"
    start_text = "⚡ Start Quizzes" if lang == "en" else "⚡ ፈተናዎችን ጀምር"
    browse_text = "📋 All Quizzes" if lang == "en" else "📋 ሁሉም ፈተናዎች"

    keyboard = [
        [InlineKeyboardButton(text=tutor_text, callback_data="tutor:chapters")],
        [InlineKeyboardButton(text=codelab_text, callback_data="code:menu")],
        [InlineKeyboardButton(text=start_text, callback_data="quiz:view:q1")],
        [InlineKeyboardButton(text=browse_text, callback_data="quiz:list")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_quiz_keyboard(
    quiz: QuizQuestion,
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build interactive options keyboard for a quiz question."""
    keyboard = []
    options = quiz.get_options(lang)

    for idx, opt_text in enumerate(options):
        letter = OPTION_LETTERS[idx] if idx < len(OPTION_LETTERS) else str(idx + 1)
        btn_text = f"{letter}) {opt_text}"
        keyboard.append([
            InlineKeyboardButton(text=btn_text, callback_data=f"quiz:ans:{quiz.id}:{idx}")
        ])

    back_text = "🔙 Practice Menu" if lang == "en" else "🔙 የልምምድ ማውጫ"
    keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data="quiz:menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_quiz_result_keyboard(
    quiz: QuizQuestion,
    next_quiz_id: Optional[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build keyboard after answering a quiz with Next Challenge and Retry."""
    keyboard = []

    if next_quiz_id:
        next_text = "Next Challenge ▶" if lang == "en" else "ቀጣይ ፈተና ▶"
        keyboard.append([
            InlineKeyboardButton(text=next_text, callback_data=f"quiz:view:{next_quiz_id}")
        ])

    retry_text = "🔄 Try Again" if lang == "en" else "🔄 እንደገና ሞክር"
    back_text = "📋 Practice Menu" if lang == "en" else "📋 የልምምድ ማውጫ"

    keyboard.append([
        InlineKeyboardButton(text=retry_text, callback_data=f"quiz:view:{quiz.id}"),
        InlineKeyboardButton(text=back_text, callback_data="quiz:menu"),
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_quiz_list_keyboard(
    quizzes: list[QuizQuestion],
    solved_ids: set[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build list of all quizzes with solved/unsolved status icons."""
    keyboard = []
    for q in quizzes:
        icon = "✅" if q.id in solved_ids else "⚪"
        text = f"{icon} Quiz {q.order}" if lang == "en" else f"{icon} ፈተና {q.order}"
        keyboard.append([
            InlineKeyboardButton(text=text, callback_data=f"quiz:view:{q.id}")
        ])

    back_text = "🔙 Practice Menu" if lang == "en" else "🔙 የልምምድ ማውጫ"
    keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data="quiz:menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
