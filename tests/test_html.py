"""Tests for HTML code validator, curriculum, and tutor track."""

from __future__ import annotations

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import StorageKey

from bot.database import Database
from bot.codelab.html_checker import run_student_html_code
from bot.tutor.content_html import (
    get_all_html_chapters,
    get_html_tutor_chapter,
    get_next_html_tutor_chapter_id,
)
from bot.tutor.models import StepType
from bot.handlers.tutor import (
    handle_switch_track,
    handle_student_step_code,
    TutorStates,
)
from tests.conftest import create_mock_message, create_mock_callback_query


@pytest.fixture
def fsm_context(sample_user, sample_chat) -> FSMContext:
    """Provide a real FSMContext with in-memory storage."""
    storage = MemoryStorage()
    key = StorageKey(bot_id=1, chat_id=sample_chat.id, user_id=sample_user.id)
    return FSMContext(storage=storage, key=key)


def test_html_checker_valid_code():
    """Verify valid HTML creates accurate text preview."""
    res = run_student_html_code("<h1>Welcome</h1><p>This is a paragraph.</p>")
    assert res.success is True
    assert "# Welcome" in res.output
    assert "This is a paragraph." in res.output


def test_html_checker_unclosed_tag_error():
    """Verify unclosed tag returns friendly error."""
    res = run_student_html_code("<h1>Welcome")
    assert res.success is False
    assert res.friendly_explanation_en is not None
    assert "Unclosed" in res.friendly_explanation_en


def test_html_checker_mismatched_tag_error():
    """Verify mismatched closing tag returns helpful explanation."""
    res = run_student_html_code("<h1>Welcome</h2>")
    assert res.success is False
    assert res.friendly_explanation_en is not None
    assert "Mismatch" in res.friendly_explanation_en


def test_html_checker_self_closing_tags():
    """Verify void tags like <img> and <input> render cleanly."""
    res = run_student_html_code('<img src="pic.jpg" alt="Profile Photo">')
    assert res.success is True
    assert "[Image: Profile Photo]" in res.output


def test_html_curriculum_integrity():
    """Verify all 7 HTML chapters have valid structure and bilingual parity."""
    chapters = get_all_html_chapters()
    assert len(chapters) == 7

    for ch in chapters:
        assert ch.id.startswith("html_ch")
        assert ch.track == "html"
        assert ch.title_en and ch.title_am
        assert ch.description_en and ch.description_am
        assert len(ch.steps) >= 3

        for step in ch.steps:
            assert step.id
            assert step.message_en and step.message_am
            if step.step_type == StepType.CONCEPT_CHECK:
                assert step.options_en and len(step.options_en) >= 2
                assert step.correct_option_index is not None
            elif step.step_type == StepType.CODE_PROMPT:
                assert step.expected_code_output is not None
                assert step.hint_en and step.hint_am


@pytest.mark.asyncio
async def test_html_track_switching_and_submission(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test switching to HTML track and submitting valid HTML code."""
    # Switch to HTML track
    cb = create_mock_callback_query("tutor:track:html", sample_user, sample_chat)
    await handle_switch_track(cb, test_db, fsm_context)

    cb.answer.assert_called_once()
    assert await test_db.get_user_track(sample_user.id) == "html"

    # Set up FSM state for html_ch1 step 1 (<h1>Welcome to My Website</h1>)
    await fsm_context.set_state(TutorStates.waiting_for_step_code)
    await fsm_context.update_data(chapter_id="html_ch1", step_index=1)

    # Submit valid HTML
    msg = create_mock_message("<h1>Welcome to My Website</h1>", sample_user, sample_chat)
    await handle_student_step_code(msg, test_db, fsm_context)

    # 2 answers: Output card and next step
    assert msg.answer.call_count == 2
    args, kwargs = msg.answer.call_args_list[0]
    assert "# Welcome to My Website" in kwargs["text"]
