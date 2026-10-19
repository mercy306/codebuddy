"""Menu navigation handlers for Learn, Practice, My Progress, and Settings."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE, STRINGS, build_progress_card
from bot.keyboards import (
    get_main_menu_keyboard,
    get_settings_keyboard,
    get_modules_keyboard,
    get_practice_menu_keyboard,
)
from bot.curriculum import get_total_lessons_count
from bot.practice import get_total_quizzes_count

logger = logging.getLogger(__name__)
router = Router(name="menu_router")

# Collect text variations for menu buttons across all supported languages
LEARN_BUTTON_TEXTS = {STRINGS["btn_learn"][lang] for lang in STRINGS["btn_learn"]}
PRACTICE_BUTTON_TEXTS = {STRINGS["btn_practice"][lang] for lang in STRINGS["btn_practice"]}
PROGRESS_BUTTON_TEXTS = {STRINGS["btn_progress"][lang] for lang in STRINGS["btn_progress"]}
SETTINGS_BUTTON_TEXTS = {STRINGS["btn_settings"][lang] for lang in STRINGS["btn_settings"]}


@router.message(Command("menu"))
async def handle_menu_command(message: Message, db: Database) -> None:
    """Handle /menu command to redisplay the main navigation menu."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    title = get_string("main_menu_title", lang)
    keyboard = get_main_menu_keyboard(lang)

    await message.answer(
        text=title,
        reply_markup=keyboard,
    )


@router.message(Command("settings"))
@router.message(F.text.in_(SETTINGS_BUTTON_TEXTS))
async def handle_settings(message: Message, db: Database) -> None:
    """Handle Settings button or /settings command."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    text = get_string("settings_content", lang)
    inline_kb = get_settings_keyboard(lang)

    await message.answer(
        text=text,
        reply_markup=inline_kb,
        parse_mode="Markdown",
    )


@router.message(F.text.in_(LEARN_BUTTON_TEXTS))
async def handle_learn(message: Message, db: Database) -> None:
    """Handle Learn button navigation by showing modules and lessons."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    completed = await db.get_completed_lessons(user_id) if user_id else set()
    text = get_string("learn_content", lang)
    inline_kb = get_modules_keyboard(completed, lang)

    await message.answer(
        text=text,
        reply_markup=inline_kb,
        parse_mode="Markdown",
    )


@router.message(F.text.in_(PRACTICE_BUTTON_TEXTS))
async def handle_practice(message: Message, db: Database) -> None:
    """Handle Practice button navigation by showing interactive challenge menu."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    text = get_string("practice_hub_title", lang)
    inline_kb = get_practice_menu_keyboard(lang)

    await message.answer(
        text=text,
        reply_markup=inline_kb,
        parse_mode="Markdown",
    )


@router.message(F.text.in_(PROGRESS_BUTTON_TEXTS))
async def handle_progress(message: Message, db: Database) -> None:
    """Handle My Progress button navigation with dynamic statistics."""
    user = message.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    completed_lessons = await db.get_completed_lessons(user_id) if user_id else set()
    total_lessons = get_total_lessons_count()

    solved_quizzes = await db.get_solved_quizzes(user_id) if user_id else set()
    total_quizzes = get_total_quizzes_count()

    progress_text = build_progress_card(
        completed_count=len(completed_lessons),
        total_count=total_lessons,
        solved_quizzes=len(solved_quizzes),
        total_quizzes=total_quizzes,
        lang=lang,
    )

    await message.answer(
        text=progress_text,
        reply_markup=get_main_menu_keyboard(lang),
        parse_mode="Markdown",
    )
