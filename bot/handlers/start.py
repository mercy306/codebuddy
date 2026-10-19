"""Start, onboarding, and language selection handlers."""

from __future__ import annotations

import logging
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from bot.database import Database
from bot.keyboards import (
    get_language_inline_keyboard,
    get_main_menu_keyboard,
    get_onboarding_keyboard,
)
from bot.strings import get_string, DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES

logger = logging.getLogger(__name__)
router = Router(name="start_router")


@router.message(CommandStart())
async def handle_start(message: Message, db: Database) -> None:
    """Handle /start command by sending a welcome message and language buttons."""
    user = message.from_user
    user_id = user.id if user else 0
    username = user.username if user else None

    # Get current saved language (if any) or default
    current_lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    welcome_text = get_string("welcome", current_lang)
    keyboard = get_language_inline_keyboard()

    await message.answer(
        text=welcome_text,
        reply_markup=keyboard,
        parse_mode="Markdown",
    )
    logger.info("Sent /start welcome to user %s (%s)", user_id, username)


@router.callback_query(F.data.startswith("lang:"))
async def handle_language_selection(callback: CallbackQuery, db: Database) -> None:
    """Handle user clicking a language button and guide them into Lesson 1.1."""
    user = callback.from_user
    user_id = user.id if user else 0
    username = user.username if user else None
    first_name = user.first_name if user else None

    if not callback.data:
        await callback.answer()
        return

    lang_code = callback.data.split(":", 1)[1]
    if lang_code not in SUPPORTED_LANGUAGES:
        lang_code = DEFAULT_LANGUAGE

    # Save to SQLite database
    if user_id:
        await db.set_user_language(
            user_id=user_id,
            language_code=lang_code,
            username=username,
            first_name=first_name,
        )

    await callback.answer()

    confirmation_text = get_string("language_selected", lang_code)
    menu_title = get_string("main_menu_title", lang_code)
    combined_text = f"{confirmation_text}\n\n{menu_title}"

    menu_keyboard = get_main_menu_keyboard(lang_code)

    if callback.message and isinstance(callback.message, Message):
        await callback.message.answer(
            text=combined_text,
            reply_markup=menu_keyboard,
            parse_mode="Markdown",
        )

    logger.info("User %s selected language '%s'", user_id, lang_code)


@router.callback_query(F.data == "settings:change_language")
async def handle_change_language_callback(
    callback: CallbackQuery, db: Database
) -> None:
    """Handle 'Change Language' button click from settings."""
    user = callback.from_user
    user_id = user.id if user else 0
    current_lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    prompt_text = get_string("choose_language", current_lang)
    keyboard = get_language_inline_keyboard()

    await callback.answer()
    if callback.message and isinstance(callback.message, Message):
        await callback.message.answer(
            text=prompt_text,
            reply_markup=keyboard,
        )


@router.message(Command("reset"))
@router.callback_query(F.data == "settings:reset_progress")
async def handle_reset_progress(
    event: Message | CallbackQuery, db: Database
) -> None:
    """Reset user progress and provide a fresh start from the beginning."""
    user = event.from_user
    user_id = user.id if user else 0
    lang = await db.get_user_language(user_id) if user_id else DEFAULT_LANGUAGE

    if user_id:
        await db.reset_user_progress(user_id)

    alert_text = get_string("reset_success_alert", lang)
    onboarding_inline = get_onboarding_keyboard(lang)

    if isinstance(event, CallbackQuery):
        await event.answer(alert_text, show_alert=True)
        if event.message and isinstance(event.message, Message):
            await event.message.answer(
                text=alert_text,
                reply_markup=onboarding_inline,
            )
    else:
        await event.answer(
            text=alert_text,
            reply_markup=onboarding_inline,
        )
    logger.info("User %s reset progress to the beginning", user_id)
