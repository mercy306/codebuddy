"""Automated tests for language selection and menu navigation handlers."""

import pytest
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from bot.database import Database
from bot.strings import LANG_EN, LANG_AM
from bot.handlers.start import handle_start, handle_language_selection, handle_change_language_callback
from bot.handlers.help import handle_help
from bot.handlers.menu import (
    handle_menu_command,
    handle_settings,
    handle_learn,
    handle_practice,
    handle_progress,
)
from bot.handlers.fallback import handle_unknown_message
from tests.conftest import create_mock_message, create_mock_callback_query


@pytest.mark.asyncio
async def test_start_command_shows_welcome_and_language_keyboard(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Verify /start returns welcoming text and language selection buttons."""
    msg = create_mock_message("/start", sample_user, sample_chat)

    await handle_start(msg, test_db)

    msg.answer.assert_called_once()
    args, kwargs = msg.answer.call_args
    assert "Welcome to *CodeBuddy*" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], InlineKeyboardMarkup)

    # Check language buttons
    buttons = kwargs["reply_markup"].inline_keyboard[0]
    callbacks = [btn.callback_data for btn in buttons]
    assert "lang:en" in callbacks
    assert "lang:am" in callbacks


@pytest.mark.asyncio
async def test_language_selection_persists_to_db_and_shows_menu(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Selecting Amharic should save to SQLite and return menu in Amharic."""
    cb = create_mock_callback_query("lang:am", sample_user, sample_chat)

    await handle_language_selection(cb, test_db)

    # Verify callback answered
    cb.answer.assert_called_once()

    # Verify database persistence
    saved_lang = await test_db.get_user_language(sample_user.id)
    assert saved_lang == LANG_AM

    # Verify response message and ReplyKeyboardMarkup
    parent_msg = cb.message
    parent_msg.answer.assert_called_once()
    _, kwargs = parent_msg.answer.call_args
    assert "ቋንቋው ወደ *አማርኛ* ተቀይሯል" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], ReplyKeyboardMarkup)

    # Check menu buttons
    rows = kwargs["reply_markup"].keyboard
    button_texts = [btn.text for row in rows for btn in row]
    assert "📚 ተማር" in button_texts
    assert "💻 ልምምድ" in button_texts
    assert "📊 የእኔ እድገት" in button_texts
    assert "⚙️ ቅንብሮች" in button_texts


@pytest.mark.asyncio
async def test_language_selection_english(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Selecting English should save to SQLite and return menu in English."""
    cb = create_mock_callback_query("lang:en", sample_user, sample_chat)

    await handle_language_selection(cb, test_db)

    saved_lang = await test_db.get_user_language(sample_user.id)
    assert saved_lang == LANG_EN

    parent_msg = cb.message
    parent_msg.answer.assert_called_once()
    _, kwargs = parent_msg.answer.call_args
    assert "Language set to *English*" in kwargs["text"]

    rows = kwargs["reply_markup"].keyboard
    button_texts = [btn.text for row in rows for btn in row]
    assert "📚 Learn" in button_texts
    assert "💻 Practice" in button_texts
    assert "📊 My Progress" in button_texts
    assert "⚙️ Settings" in button_texts


@pytest.mark.asyncio
async def test_help_command_localized(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Test /help in user's saved language."""
    # First set language to Amharic
    await test_db.set_user_language(sample_user.id, LANG_AM)

    msg = create_mock_message("/help", sample_user, sample_chat)
    await handle_help(msg, test_db)

    msg.answer.assert_called_once()
    _, kwargs = msg.answer.call_args
    assert "የኮድበዲ አጋዥ መመሪያ" in kwargs["text"]
    assert "/start" in kwargs["text"]


@pytest.mark.asyncio
async def test_menu_navigation_buttons(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Test Learn, Practice, My Progress, and Settings responses."""
    # Learn
    msg_learn = create_mock_message("📚 Learn", sample_user, sample_chat)
    await handle_learn(msg_learn, test_db)
    _, kwargs = msg_learn.answer.call_args
    assert "Learn Programming" in kwargs["text"]

    # Practice
    msg_practice = create_mock_message("💻 Practice", sample_user, sample_chat)
    await handle_practice(msg_practice, test_db)
    _, kwargs = msg_practice.answer.call_args
    assert "Practice Arena" in kwargs["text"]

    # Progress
    msg_progress = create_mock_message("📊 My Progress", sample_user, sample_chat)
    await handle_progress(msg_progress, test_db)
    _, kwargs = msg_progress.answer.call_args
    assert "My Learning Progress" in kwargs["text"]

    # Settings
    msg_settings = create_mock_message("⚙️ Settings", sample_user, sample_chat)
    await handle_settings(msg_settings, test_db)
    _, kwargs = msg_settings.answer.call_args
    assert "Settings" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], InlineKeyboardMarkup)


@pytest.mark.asyncio
async def test_settings_change_language_flow(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Test clicking Change Language inside settings opens language buttons."""
    cb = create_mock_callback_query("settings:change_language", sample_user, sample_chat)
    await handle_change_language_callback(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.answer.assert_called_once()
    _, kwargs = parent_msg.answer.call_args
    assert "preferred language" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], InlineKeyboardMarkup)


@pytest.mark.asyncio
async def test_unknown_message_fallback(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Test fallback handler on arbitrary user input."""
    msg = create_mock_message("random text xyz", sample_user, sample_chat)
    await handle_unknown_message(msg, test_db)

    msg.answer.assert_called_once()
    _, kwargs = msg.answer.call_args
    assert "didn't recognize that message" in kwargs["text"]


@pytest.mark.asyncio
async def test_reset_progress_flow(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Test reset progress callback clears completed lessons and quiz stats."""
    from bot.handlers.start import handle_reset_progress

    await test_db.mark_lesson_completed(sample_user.id, "m1_l1")
    await test_db.record_quiz_attempt(sample_user.id, "q1", is_correct=True)

    cb = create_mock_callback_query("settings:reset_progress", sample_user, sample_chat)
    await handle_reset_progress(cb, test_db)

    # Check database was wiped clean
    completed_lessons = await test_db.get_completed_lessons(sample_user.id)
    assert len(completed_lessons) == 0

    solved_quizzes = await test_db.get_solved_quizzes(sample_user.id)
    assert len(solved_quizzes) == 0

    cb.answer.assert_called_once()

