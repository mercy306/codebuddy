"""Automated tests for practice arena, interactive quizzes, and scoring."""

import pytest
from aiogram.types import InlineKeyboardMarkup

from bot.database import Database
from bot.strings import LANG_EN, LANG_AM
from bot.practice import (
    get_all_quizzes,
    get_quiz,
    get_next_quiz_id,
    get_total_quizzes_count,
)
from bot.handlers.practice import (
    handle_practice_command,
    handle_practice_menu_callback,
    handle_quiz_list_callback,
    handle_view_quiz_callback,
    handle_quiz_answer_callback,
)
from tests.conftest import create_mock_message, create_mock_callback_query


def test_quizzes_content_and_bilingual_parity() -> None:
    """Verify quiz definitions and English/Amharic translation completeness."""
    quizzes = get_all_quizzes()
    assert len(quizzes) >= 6
    assert get_total_quizzes_count() >= 6

    for q in quizzes:
        assert q.get_question("en") != ""
        assert q.get_question("am") != ""
        assert len(q.get_options("en")) >= 3
        assert len(q.get_options("am")) >= 3
        assert len(q.get_options("en")) == len(q.get_options("am"))
        assert 0 <= q.correct_index < len(q.get_options("en"))
        assert q.get_explanation("en") != ""
        assert q.get_explanation("am") != ""


@pytest.mark.asyncio
async def test_quiz_database_persistence(test_db: Database) -> None:
    """Test recording correct and incorrect quiz attempts."""
    user_id = 77777

    # Initial state
    solved = await test_db.get_solved_quizzes(user_id)
    assert len(solved) == 0

    # Record incorrect attempt on q1
    await test_db.record_quiz_attempt(user_id, "q1", is_correct=False)
    correct_count, total = await test_db.get_quiz_stats(user_id)
    assert correct_count == 0
    assert total == 1

    # Record correct retry on q1
    await test_db.record_quiz_attempt(user_id, "q1", is_correct=True)
    correct_count, total = await test_db.get_quiz_stats(user_id)
    assert correct_count == 1
    assert total == 1
    solved = await test_db.get_solved_quizzes(user_id)
    assert "q1" in solved


@pytest.mark.asyncio
async def test_practice_command_opens_hub(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Verify /practice displays the practice arena hub."""
    msg = create_mock_message("/practice", sample_user, sample_chat)
    await handle_practice_command(msg, test_db)

    msg.answer.assert_called_once()
    _, kwargs = msg.answer.call_args
    assert "Practice Arena" in kwargs["text"]
    assert isinstance(kwargs["reply_markup"], InlineKeyboardMarkup)


@pytest.mark.asyncio
async def test_quiz_view_handler(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Viewing a quiz card shows question, code block, and option buttons."""
    cb = create_mock_callback_query("quiz:view:q2", sample_user, sample_chat)
    await handle_view_quiz_callback(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.edit_text.assert_called_once()
    _, kwargs = parent_msg.edit_text.call_args
    assert "Challenge 2" in kwargs["text"]
    assert "print(10 + 20)" in kwargs["text"]

    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "quiz:ans:q2:0" in callbacks
    assert "quiz:ans:q2:1" in callbacks
    assert "quiz:menu" in callbacks


@pytest.mark.asyncio
async def test_quiz_correct_answer_flow(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Selecting the right answer rewards the user and persists to database."""
    # For q2: print(10 + 20) -> correct index is 1 (30)
    cb = create_mock_callback_query("quiz:ans:q2:1", sample_user, sample_chat)
    await handle_quiz_answer_callback(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.edit_text.assert_called_once()
    _, kwargs = parent_msg.edit_text.call_args
    assert "Correct!" in kwargs["text"]
    assert "Explanation" in kwargs["text"]

    # Verify database recorded correct attempt
    solved = await test_db.get_solved_quizzes(sample_user.id)
    assert "q2" in solved

    # Check Next Challenge button
    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "quiz:view:q3" in callbacks


@pytest.mark.asyncio
async def test_quiz_incorrect_answer_flow(
    test_db: Database, sample_user, sample_chat
) -> None:
    """Selecting wrong answer provides friendly encouragement and retry."""
    # For q2: wrong option is 0 ("10 + 20")
    cb = create_mock_callback_query("quiz:ans:q2:0", sample_user, sample_chat)
    await handle_quiz_answer_callback(cb, test_db)

    cb.answer.assert_called_once()
    parent_msg = cb.message
    parent_msg.edit_text.assert_called_once()
    _, kwargs = parent_msg.edit_text.call_args
    assert "Not quite" in kwargs["text"]

    callbacks = [btn.callback_data for row in kwargs["reply_markup"].inline_keyboard for btn in row]
    assert "quiz:view:q2" in callbacks
