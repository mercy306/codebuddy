"""Tests for JavaScript sandbox executor and curriculum."""

from __future__ import annotations

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import StorageKey

from bot.database import Database
from bot.codelab.js_sandbox import (
    check_js_safety,
    get_friendly_js_error,
    run_student_js_code,
)
from bot.tutor.content_js import (
    get_all_js_chapters,
    get_js_tutor_chapter,
    get_next_js_tutor_chapter_id,
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


def test_js_sandbox_execution():
    """Verify executing valid JS produces accurate stdout."""
    res = run_student_js_code('console.log("Hello from Test");')
    assert res.success is True
    assert res.output.strip() == "Hello from Test"

    res_math = run_student_js_code("let a = 10; let b = 20; console.log(a + b);")
    assert res_math.success is True
    assert res_math.output.strip() == "30"


def test_js_sandbox_security_rules():
    """Verify forbidden words are caught by safety filter."""
    unsafe_samples = [
        "const fs = require('fs');",
        "import os from 'os';",
        "process.exit(1);",
        "eval('console.log(1)');",
        "new Function('return 1')();",
    ]
    for code in unsafe_samples:
        is_safe, err_en, err_am = check_js_safety(code)
        assert is_safe is False
        assert err_en is not None
        assert err_am is not None

        res = run_student_js_code(code)
        assert res.success is False


def test_js_friendly_errors():
    """Verify JS runtime and syntax errors are converted into friendly messages."""
    res_ref = run_student_js_code("console.log(unknownVar);")
    assert res_ref.success is False
    assert res_ref.friendly_explanation_en is not None
    assert "Reference" in res_ref.friendly_explanation_en

    res_syn = run_student_js_code("console.log('unclosed string);")
    assert res_syn.success is False
    assert res_syn.friendly_explanation_en is not None
    assert "Syntax" in res_syn.friendly_explanation_en


def test_js_curriculum_integrity():
    """Verify all 7 JavaScript chapters and steps have bilingual parity and valid structure."""
    chapters = get_all_js_chapters()
    assert len(chapters) == 7

    for ch in chapters:
        assert ch.id.startswith("js_ch")
        assert ch.track == "javascript"
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
async def test_user_track_database_persistence(test_db: Database, sample_user):
    """Test setting and getting user learning track in SQLite."""
    user_id = sample_user.id

    # Default is python
    assert await test_db.get_user_track(user_id) == "python"

    # Switch to javascript
    await test_db.set_user_track(user_id, "javascript")
    assert await test_db.get_user_track(user_id) == "javascript"

    # Switch back to python
    await test_db.set_user_track(user_id, "python")
    assert await test_db.get_user_track(user_id) == "python"


@pytest.mark.asyncio
async def test_handle_switch_track_callback(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test switching learning tracks via callback."""
    cb = create_mock_callback_query("tutor:track:javascript", sample_user, sample_chat)
    await handle_switch_track(cb, test_db, fsm_context)

    cb.answer.assert_called_once()
    assert await test_db.get_user_track(sample_user.id) == "javascript"


@pytest.mark.asyncio
async def test_handle_js_student_code_submission(test_db: Database, sample_user, sample_chat, fsm_context):
    """Test submitting real JavaScript code during a JS tutor step."""
    await fsm_context.set_state(TutorStates.waiting_for_step_code)
    await fsm_context.update_data(chapter_id="js_ch1", step_index=1)

    # Submit valid JS
    msg = create_mock_message('console.log("Hello Web!");', sample_user, sample_chat)
    await handle_student_step_code(msg, test_db, fsm_context)

    # 2 answers: Output card and next step
    assert msg.answer.call_count == 2
    args, kwargs = msg.answer.call_args_list[0]
    assert "Hello Web!" in kwargs["text"]
