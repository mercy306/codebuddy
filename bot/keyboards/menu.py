"""Keyboards for the main menu and navigation."""

from __future__ import annotations

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from bot.strings import get_string, DEFAULT_LANGUAGE


def get_main_menu_keyboard(lang: str = DEFAULT_LANGUAGE) -> ReplyKeyboardMarkup:
    """Build reply keyboard for main menu navigation."""
    btn_learn = KeyboardButton(text=get_string("btn_learn", lang))
    btn_practice = KeyboardButton(text=get_string("btn_practice", lang))
    btn_progress = KeyboardButton(text=get_string("btn_progress", lang))
    btn_settings = KeyboardButton(text=get_string("btn_settings", lang))

    keyboard = [
        [btn_learn, btn_practice],
        [btn_progress, btn_settings],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_onboarding_keyboard(lang: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    """Build inline keyboard guiding beginner immediately into Lesson 1.1."""
    start_lesson_text = get_string("btn_start_first_lesson", lang)
    browse_text = get_string("btn_back_to_modules", lang)

    buttons = [
        [InlineKeyboardButton(text=start_lesson_text, callback_data="learn:les:m1_l1")],
        [InlineKeyboardButton(text=browse_text, callback_data="learn:modules")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_settings_keyboard(lang: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    """Build inline keyboard for settings options."""
    buttons = [
        [
            InlineKeyboardButton(
                text=get_string("btn_change_language", lang),
                callback_data="settings:change_language",
            )
        ],
        [
            InlineKeyboardButton(
                text=get_string("btn_reset_progress", lang),
                callback_data="settings:reset_progress",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
