"""Keyboards for language selection."""

from __future__ import annotations

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.strings import LANG_EN, LANG_AM


def get_language_inline_keyboard() -> InlineKeyboardMarkup:
    """Return inline keyboard with English and Amharic language options."""
    buttons = [
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data=f"lang:{LANG_EN}"),
            InlineKeyboardButton(text="🇪🇹 አማርኛ", callback_data=f"lang:{LANG_AM}"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
