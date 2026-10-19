"""Help command handler."""

from __future__ import annotations

import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.database import Database
from bot.strings import get_string, DEFAULT_LANGUAGE
from bot.keyboards import get_main_menu_keyboard

logger = logging.getLogger(__name__)
router = Router(name="help_router")


@router.message(Command("help"))
async def handle_help(message: Message, db: Database) -> None:
    """Handle /help command with instructions in the user's preferred language."""
    user = message.from_user
    user_id = user.id if user else 0

    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE
    help_text = get_string("help", lang)
    menu_keyboard = get_main_menu_keyboard(lang)

    await message.answer(
        text=help_text,
        reply_markup=menu_keyboard,
        parse_mode="Markdown",
    )
    logger.info("Sent /help response to user %s in language '%s'", user_id, lang)
