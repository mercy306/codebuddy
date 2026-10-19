"""Tests for interactive conversational tutor engine."""

from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import StorageKey

from bot.database import Database
from bot.tutor.models import TutorChapter, TutorStep, StepType
from bot.tutor.content import (
    get_all_tutor_chapters,
    get_tutor_chapter,
    get_next_tutor_chapter_id,
)
from bot.keyboards.tutor import (
    get_tutor_chapters_keyboard,
    get_tutor_step_keyboard,
    get_tutor_concept_retry_keyboard,
    get_tutor_completion_keyboard,
)
from bot.handlers.tutor import (
    handle_tutor_menu,
    handle_start_chapter,
    handle_tutor_step_callback,
    handle_tutor_hint_callback,
    handle_tutor_concept_option,
    handle_student_step_code,
    handle_tutor_exit,
    TutorStates,
)
from tests.conftest import create_mock_message, create_mock_callback_query


@pytest.fixture
def fsm_context(sample_user, sample_chat) -> FSMContext:
    """Provide a real FSMContext with in-memory storage."""
    storage = MemoryStorage()
    key = StorageKey(bot_id=1, chat_id=sample_chat.id, user_id=sample_user.id)
    return FSMContext(storage=storage, key=key)


def test_tutor_content_integrity():
    """Verify tutor chapters and steps contain valid data in both languages."""
    chapters = get_all_tutor_chapters()
    assert len(chapters) >= 2

    for ch in chapters:
        assert ch.id
        assert ch.title_en and ch.title_am
        assert ch.description_en and ch.description_am
        assert len(ch.steps) >= 3

        for step in ch.steps:
            assert step.id
            assert step.message_en and step.message_am
            if step.step_type == StepType.CONCEPT_CHECK:
                assert step.options_en and len(step.options_en) >= 2
                assert step.correct_option_index is not None
                assert 0 <= step.correct_option_index < len(step.options_en)
            elif step.step_type == StepType.CODE_PROMPT:
                assert step.expected_code_output is not None or step.expected_code_contains is not None
                assert step.hint_en and step.hint_am


@pytest.mark.asyncio
async def test_tutor_database_operations(test_db: Database, sample_user):
    """Test getting, setting, and resetting tutor progress in database."""
    user_id = sample_user.id

    # Initially step 0, not completed
    step_idx, is_done = await test_db.get_tutor_progress(user_id, "ch1")
    assert step_idx == 0
    assert not is_done

    # Update progress to step 3
    await test_db.set_tutor_progress(user_id, "ch1", step_index=3, is_completed=False)
    step_idx, is_done = await test_db.get_tutor_progress(user_id, "ch1")
    assert step_idx == 3
    assert not is_done

    # Mark completed
    await test_db.set_tutor_progress(user_id, "ch1", step_index=6, is_completed=True)
    step_idx, is_done = await test_db.get_tutor_progress(user_id, "ch1")
    assert is_done
    completed = await test_db.get_completed_tutor_chapters(user_id)
    assert "ch1" in completed

    # Reset progress
    await test_db.reset_user_progress(user_id)
    step_idx, is_done = await test_db.get_tutor_progress(user_id, "ch1")
    assert step_idx == 0
    assert not is_done
    assert len(await test_db.get_completed_tutor_chapters(user_id)) == 0


def test_tutor_keyboards():
    """Verify tutor keyboard generation for explanation, concept check, and code prompt."""
    chapters_kb = get_tutor_chapters_keyboard({"ch1"}, lang="en")
    assert len(chapters_kb.inline_keyboard) >= 2

    ch1 = get_tutor_chapter("ch1")
    assert ch1 is not None

    # Step 0: Explanation
    step0_kb = get_tutor_step_keyboard(ch1.id, 0, ch1.steps[0], lang="en")
    button_data = [btn.callback_data for row in step0_kb.inline_keyboard for btn in row]
    assert f"tutor:step:{ch1.id}:1" in button_data

    # Step 1: Code prompt
    step1_kb = get_tutor_step_keyboard(ch1.id, 1, ch1.steps[1], lang="en")
    button_data1 = [btn.callback_data for row in step1_kb.inline_keyboard for btn in row]
    assert f"tutor:hint:{ch1.id}:1" in button_data1

    # Retry keyboard
    retry_kb = get_tutor_concept_retry_keyboard(ch1.id, 2, lang="en")
    assert any(btn.callback_data == f"tutor:step:{ch1.id}:2" for row in retry_kb.inline_keyboard for btn in row)

    # Completion keyboard
    comp_kb = get_tutor_completion_keyboard(ch1.id, "ch2", lang="en")
    assert any(btn.callback_data == "tutor:start:ch2" for row in comp_kb.inline_keyboard for btn in row)


@pytest.mark.asyncio
async def test_handle_tutor_menu(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test /tutor command displays chapters overview."""
    msg = create_mock_message("/tutor", sample_user, sample_chat)
    await handle_tutor_menu(msg, test_db, fsm_context)

    msg.answer.assert_called_once()
    args, kwargs = msg.answer.call_args
    assert "Tutor" in kwargs["text"]
    assert kwargs["reply_markup"] is not None


@pytest.mark.asyncio
async def test_handle_start_chapter(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test launching chapter 1 step 0."""
    cb = create_mock_callback_query("tutor:start:ch1", sample_user, sample_chat)
    await handle_start_chapter(cb, test_db, fsm_context)

    cb.message.edit_text.assert_called_once()
    args, kwargs = cb.message.edit_text.call_args
    assert "Chapter 1" in kwargs["text"]


@pytest.mark.asyncio
async def test_handle_tutor_hint_callback(test_db: Database, sample_user, sample_chat):
    """Test clicking hint button displays popup alert."""
    cb = create_mock_callback_query("tutor:hint:ch1:1", sample_user, sample_chat)
    await handle_tutor_hint_callback(cb, test_db)

    cb.answer.assert_called_once()
    args, kwargs = cb.answer.call_args
    assert kwargs.get("show_alert") is True
    assert "print" in kwargs.get("text", "").lower()


@pytest.mark.asyncio
async def test_handle_tutor_concept_option(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test answering a concept check question correctly and incorrectly."""
    # ch1 step 2 is concept check ("Why wrap inside quotes?"), correct index is 0
    # 1. Correct answer
    cb_correct = create_mock_callback_query("tutor:opt:ch1:2:0", sample_user, sample_chat)
    await handle_tutor_concept_option(cb_correct, test_db, fsm_context)

    cb_correct.answer.assert_called()
    cb_correct.message.edit_text.assert_called_once()

    # 2. Incorrect answer
    cb_wrong = create_mock_callback_query("tutor:opt:ch1:2:1", sample_user, sample_chat)
    await handle_tutor_concept_option(cb_wrong, test_db, fsm_context)

    cb_wrong.message.edit_text.assert_called_once()
    args, kwargs = cb_wrong.message.edit_text.call_args
    assert "Not quite" in kwargs["text"] or "ልክ አይደለም" in kwargs["text"]


@pytest.mark.asyncio
async def test_handle_student_step_code_flow(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test submitting code during CODE_PROMPT step: syntax error, mismatch, and success."""
    # Set up FSM state for ch1 step 1 (expected print("Hello"))
    await fsm_context.set_state(TutorStates.waiting_for_step_code)
    await fsm_context.update_data(chapter_id="ch1", step_index=1)

    # 1. Syntax Error
    msg_err = create_mock_message('print("Hello"', sample_user, sample_chat)
    await handle_student_step_code(msg_err, test_db, fsm_context)
    msg_err.answer.assert_called_once()
    args, kwargs = msg_err.answer.call_args
    assert "Oops" in kwargs["text"] or "ስህተት" in kwargs["text"]

    # State should remain waiting_for_step_code
    assert await fsm_context.get_state() == TutorStates.waiting_for_step_code.state

    # 2. Output mismatch
    msg_mismatch = create_mock_message('print("World")', sample_user, sample_chat)
    await handle_student_step_code(msg_mismatch, test_db, fsm_context)
    msg_mismatch.answer.assert_called_once()
    args, kwargs = msg_mismatch.answer.call_args
    assert "Almost there" in kwargs["text"] or "ተቃርበዋል" in kwargs["text"]

    # 3. Successful match
    msg_success = create_mock_message('print("Hello")', sample_user, sample_chat)
    await handle_student_step_code(msg_success, test_db, fsm_context)

    # Success card + next step rendered
    assert msg_success.answer.call_count == 2
    first_call_args, first_call_kwargs = msg_success.answer.call_args_list[0]
    assert "Hello" in first_call_kwargs["text"]


@pytest.mark.asyncio
async def test_handle_tutor_exit(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test exiting tutor session cleans up state."""
    await fsm_context.set_state(TutorStates.waiting_for_step_code)
    cb = create_mock_callback_query("tutor:exit", sample_user, sample_chat)

    await handle_tutor_exit(cb, test_db, fsm_context)

    assert await fsm_context.get_state() is None
    cb.message.answer.assert_called_once()
    args, kwargs = cb.message.answer.call_args
    assert "exited" in kwargs["text"] or "ወጥተዋል" in kwargs["text"]
