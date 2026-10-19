"""Tests for CSS validator, curriculum, and tutor track."""

from __future__ import annotations

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import StorageKey

from bot.database import Database
from bot.codelab.css_checker import run_student_css_code
from bot.tutor.content_css import (
    get_all_css_chapters,
    get_css_tutor_chapter,
    get_next_css_tutor_chapter_id,
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


def test_css_checker_valid_rules():
    """Verify valid CSS rule parses and outputs style summary."""
    res = run_student_css_code("h1 { color: blue; font-size: 20px; }")
    assert res.success is True
    assert "Style applied to <h1>" in res.output
    assert "color: blue" in res.output
    assert "font-size: 20px" in res.output


def test_css_checker_missing_braces():
    """Verify missing or mismatched curly braces return friendly errors."""
    res_no_brace = run_student_css_code("h1 color: blue;")
    assert res_no_brace.success is False
    assert "curly braces" in res_no_brace.friendly_explanation_en.lower()

    res_unclosed = run_student_css_code("h1 { color: blue;")
    assert res_unclosed.success is False
    assert "Unclosed" in res_unclosed.friendly_explanation_en


def test_css_checker_missing_colon():
    """Verify declaration without colon returns helpful guidance."""
    res = run_student_css_code("h1 { color blue; }")
    assert res.success is False
    assert "colon" in res.friendly_explanation_en.lower()


def test_css_curriculum_integrity():
    """Verify all 7 CSS chapters have valid structure and bilingual parity."""
    chapters = get_all_css_chapters()
    assert len(chapters) == 7

    for ch in chapters:
        assert ch.id.startswith("css_ch")
        assert ch.track == "css"
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
async def test_css_track_switching_and_submission(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test switching to CSS track and submitting valid CSS code."""
    # Switch to CSS track
    cb = create_mock_callback_query("tutor:track:css", sample_user, sample_chat)
    await handle_switch_track(cb, test_db, fsm_context)

    cb.answer.assert_called_once()
    assert await test_db.get_user_track(sample_user.id) == "css"

    # Set up FSM state for css_ch1 step 1 (h1 { color: blue; })
    await fsm_context.set_state(TutorStates.waiting_for_step_code)
    await fsm_context.update_data(chapter_id="css_ch1", step_index=1)

    # Submit valid CSS
    msg = create_mock_message("h1 {\n  color: blue;\n}\n", sample_user, sample_chat)
    await handle_student_step_code(msg, test_db, fsm_context)

    # 2 answers: Output card and next step
    assert msg.answer.call_count == 2
    args, kwargs = msg.answer.call_args_list[0]
    assert "color: blue" in kwargs["text"]
