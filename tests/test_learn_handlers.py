"""Automated tests for curriculum learning handlers and progress tracking."""

import pytest
from aiogram.types import InlineKeyboardMarkup

from bot.database import Database
from bot.strings import LANG_EN, LANG_AM, build_progress_card
from bot.handlers.learn import (
    handle_learn_command,
    handle_show_modules_callback,
    handle_module_selected,
    handle_lesson_view,
    handle_lesson_completion,
)
from bot.handlers.menu import handle_progress
from tests.conftest import create_mock_message, create_mock_callback_query


@pytest.mark.asyncio
async def test_learn_command_displays_modules(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Verify /learn displays the modules inline keyboard."""
    msg = create_mock_message("/learn", sample_user, sample_chat)
    await handle_learn_command(msg, test_db)

    msg.answer.assert_called_once()
    _, kwargs = msg.answer.call_args
    assert "Curriculum" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], InlineKeyboardMarkup)

    # Check that module buttons are present
    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "learn:mod:m1" in callbacks
    assert "learn:mod:m2" in callbacks


@pytest.mark.asyncio
async def test_module_selection_lists_lessons(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Selecting a module displays its lesson buttons and back button."""
    cb = create_mock_callback_query("learn:mod:m1", sample_user, sample_chat)
    await handle_module_selected(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.edit_text.assert_called_once()
    _, kwargs = parent_msg.edit_text.call_args
    assert "Module 1" in kwargs["text"]

    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "learn:les:m1_l1" in callbacks
    assert "learn:les:m1_l2" in callbacks
    assert "learn:modules" in callbacks


@pytest.mark.asyncio
async def test_lesson_view_and_navigation(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Viewing a lesson displays lesson body and pagination buttons."""
    cb = create_mock_callback_query("learn:les:m1_l1", sample_user, sample_chat)
    await handle_lesson_view(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.edit_text.assert_called_once()
    _, kwargs = parent_msg.edit_text.call_args
    assert "Giving Instructions to Computers" in kwargs["text"]
    assert "print(" in kwargs["text"]

    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "learn:comp:m1_l1" in callbacks
    assert "learn:les:m1_l2" in callbacks
    assert "learn:mod:m1" in callbacks


@pytest.mark.asyncio
async def test_lesson_completion_persists_to_db(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Marking a lesson complete updates SQLite and alerts user."""
    cb = create_mock_callback_query("learn:comp:m1_l1", sample_user, sample_chat)
    await handle_lesson_completion(cb, test_db)

    cb.answer.assert_called_once()
    # Confirm alert message was provided
    assert "completed" in cb.answer.call_args[0][0].lower()

    # Check database
    is_done = await test_db.is_lesson_completed(sample_user.id, "m1_l1")
    assert is_done is True

    # Check updated reply markup
    parent_msg = cb.message
    parent_msg.edit_reply_markup.assert_called_once()


@pytest.mark.asyncio
async def test_progress_card_with_completed_lessons(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Completing lessons should reflect dynamically in My Progress."""
    await test_db.mark_lesson_completed(sample_user.id, "m1_l1")
    await test_db.mark_lesson_completed(sample_user.id, "m1_l2")

    msg = create_mock_message("📊 My Progress", sample_user, sample_chat)
    await handle_progress(msg, test_db)

    msg.answer.assert_called_once()
    _, kwargs = msg.answer.call_args
    assert "2 of 8" in kwargs["text"]
    assert "0 of 6" in kwargs["text"]
    assert "14%" in kwargs["text"]
    assert "█" in kwargs["text"]


def test_build_progress_card_amharic() -> None:
    """Verify progress card builds properly in Amharic."""
    card = build_progress_card(completed_count=4, total_count=8, lang=LANG_AM)
    assert "የእኔ የመማር እድገት" in card
    assert "4 ከ 8" in card
    assert "50%" in card
