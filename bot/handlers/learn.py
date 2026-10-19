"""Curriculum and interactive lesson handlers."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.curriculum import (
    get_all_modules,
    get_module,
    get_lesson,
    get_adjacent_lessons,
)
from bot.keyboards import (
    get_modules_keyboard,
    get_lessons_keyboard,
    get_lesson_navigation_keyboard,
)

logger = logging.getLogger(__name__)
router = Router(name="learn_router")


@router.message(Command("learn"))
async def handle_learn_command(message: Message, db: Database) -> None:
    """Handle /learn command to display curriculum modules."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    completed = await db.get_completed_lessons(user_id) if user_id else set()
    text = get_string("learn_modules_title", lang)
    keyboard = get_modules_keyboard(completed, lang)

    await message.answer(
        text=text,
        reply_markup=keyboard,
        parse_mode="Markdown",
    )


@router.callback_query(F.data == "learn:modules")
async def handle_show_modules_callback(callback: CallbackQuery, db: Database) -> None:
    """Return to modules list view."""
    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    completed = await db.get_completed_lessons(user_id) if user_id else set()
    text = get_string("learn_modules_title", lang)
    keyboard = get_modules_keyboard(completed, lang)

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("learn:mod:"))
async def handle_module_selected(callback: CallbackQuery, db: Database) -> None:
    """Display lessons list for a chosen module."""
    if not callback.data:
        await callback.answer()
        return

    module_id = callback.data.split(":", 2)[2]
    module = get_module(module_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if not module:
        await callback.answer("Module not found", show_alert=True)
        return

    completed = await db.get_completed_lessons(user_id) if user_id else set()
    title_template = get_string("lessons_list_title", lang)
    mod_title = module.get_title(lang)
    mod_desc = module.get_description(lang)

    text = f"{title_template.format(module_title=mod_title)}\n_{mod_desc}_"
    keyboard = get_lessons_keyboard(module, completed, lang)

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("learn:les:"))
async def handle_lesson_view(callback: CallbackQuery, db: Database) -> None:
    """Display an individual lesson card with interactive navigation."""
    if not callback.data:
        await callback.answer()
        return

    lesson_id = callback.data.split(":", 2)[2]
    mod, lesson = get_lesson(lesson_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if not lesson:
        await callback.answer("Lesson not found", show_alert=True)
        return

    is_completed = await db.is_lesson_completed(user_id, lesson.id) if user_id else False
    prev_id, next_id = get_adjacent_lessons(lesson.id)

    text = lesson.get_content(lang)
    keyboard = get_lesson_navigation_keyboard(
        lesson=lesson,
        is_completed=is_completed,
        prev_id=prev_id,
        next_id=next_id,
        lang=lang,
    )

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="Markdown",
        )


@router.callback_query(F.data.startswith("learn:comp:"))
async def handle_lesson_completion(callback: CallbackQuery, db: Database) -> None:
    """Mark a lesson complete and refresh the view with completion badge."""
    if not callback.data:
        await callback.answer()
        return

    lesson_id = callback.data.split(":", 2)[2]
    mod, lesson = get_lesson(lesson_id)

    user = callback.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if not lesson:
        await callback.answer()
        return

    # Mark as completed in SQLite
    if user_id:
        await db.mark_lesson_completed(user_id, lesson.id)

    prev_id, next_id = get_adjacent_lessons(lesson.id)
    text = lesson.get_content(lang)
    keyboard = get_lesson_navigation_keyboard(
        lesson=lesson,
        is_completed=True,
        prev_id=prev_id,
        next_id=next_id,
        lang=lang,
    )

    alert_text = get_string("lesson_completed_alert", lang)
    await callback.answer(alert_text, show_alert=False)

    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_reply_markup(reply_markup=keyboard)
