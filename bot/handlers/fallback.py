"""Fallback handler for unhandled or unknown messages."""

from __future__ import annotations

import logging
from aiogram import Router
from aiogram.types import Message

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.keyboards import get_main_menu_keyboard

logger = logging.getLogger(__name__)
router = Router(name="fallback_router")


@router.message()
async def handle_unknown_message(message: Message, db: Database) -> None:
    """Respond politely to any unrecognized text or media."""
    user = message.from_user
    user_id = user.id if user else 0

    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE
    reply_text = get_string("unknown_message", lang)
    menu_keyboard = get_main_menu_keyboard(lang)

    await message.answer(
        text=reply_text,
        reply_markup=menu_keyboard,
    )
    logger.info(
        "Handled unrecognized input from user %s: '%s'",
        user_id,
        (message.text or "<non-text>")[:30],
    )
