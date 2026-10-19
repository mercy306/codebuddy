"""Keyboards for curriculum module and lesson navigation."""

from __future__ import annotations

from typing import Set, Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.curriculum.models import Module, Lesson
from bot.curriculum.data import get_all_modules
from bot.strings import get_string, DEFAULT_LANGUAGE


def get_modules_keyboard(
    completed_lessons: Set[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build inline keyboard listing all learning modules with completion status."""
    keyboard = []
    modules = get_all_modules()

    for mod in modules:
        mod_lesson_ids = {l.id for l in mod.lessons}
        is_module_completed = mod_lesson_ids.issubset(completed_lessons) and len(mod_lesson_ids) > 0
        icon = "✅" if is_module_completed else "📖"
        title = mod.get_title(lang)
        button_text = f"{icon} {title}"
        keyboard.append([InlineKeyboardButton(text=button_text, callback_data=f"learn:mod:{mod.id}")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_lessons_keyboard(
    module: Module,
    completed_lessons: Set[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build inline keyboard listing lessons inside a specific module."""
    keyboard = []

    for lesson in module.lessons:
        is_done = lesson.id in completed_lessons
        icon = "✅" if is_done else "⚪"
        title = lesson.get_title(lang)
        button_text = f"{icon} {title}"
        keyboard.append([InlineKeyboardButton(text=button_text, callback_data=f"learn:les:{lesson.id}")])

    # Back to all modules
    back_text = get_string("btn_back_to_modules", lang)
    keyboard.append([InlineKeyboardButton(text=back_text, callback_data="learn:modules")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_lesson_navigation_keyboard(
    lesson: Lesson,
    is_completed: bool,
    prev_id: Optional[str],
    next_id: Optional[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build navigation keyboard for viewing a lesson."""
    keyboard = []

    # Row 1: Mark completed button
    if is_completed:
        comp_btn_text = get_string("btn_lesson_completed", lang)
    else:
        comp_btn_text = get_string("btn_complete_lesson", lang)

    keyboard.append([
        InlineKeyboardButton(text=comp_btn_text, callback_data=f"learn:comp:{lesson.id}")
    ])

    # Row 2: Prev / Next pagination
    nav_row = []
    if prev_id:
        prev_text = get_string("btn_prev_lesson", lang)
        nav_row.append(InlineKeyboardButton(text=prev_text, callback_data=f"learn:les:{prev_id}"))

    if next_id:
        next_text = get_string("btn_next_lesson", lang)
        nav_row.append(InlineKeyboardButton(text=next_text, callback_data=f"learn:les:{next_id}"))

    if nav_row:
        keyboard.append(nav_row)

    # Row 3: Back to module lessons
    back_text = get_string("btn_back_to_lessons", lang)
    keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data=f"learn:mod:{lesson.module_id}")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
