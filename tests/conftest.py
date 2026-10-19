"""Pytest fixtures and test helpers for CodeBuddy test suite."""

from __future__ import annotations

from pathlib import Path
from typing import AsyncGenerator
from unittest.mock import AsyncMock

import pytest
from aiogram.types import User, Chat, Message, CallbackQuery

from bot.database import Database


@pytest.fixture
async def test_db(tmp_path: Path) -> AsyncGenerator[Database, None]:
    """Provide an isolated, initialized temporary SQLite database for tests."""
    db_file = tmp_path / "test_codebuddy.db"
    db = Database(db_file)
    await db.init_db()
    yield db


@pytest.fixture
def sample_user() -> User:
    """Provide sample Telegram user."""
    return User(
        id=12345,
        is_bot=False,
        first_name="Abebe",
        last_name="Bikila",
        username="abebe_b",
        language_code="en",
    )


@pytest.fixture
def sample_chat() -> Chat:
    """Provide sample Telegram private chat."""
    return Chat(
        id=12345,
        type="private",
        first_name="Abebe",
        username="abebe_b",
    )


def create_mock_message(
    text: str,
    user: User,
    chat: Chat,
) -> Message:
    """Create a mock aiogram Message with AsyncMock answer method."""
    msg = Message.model_construct(
        message_id=99,
        date=1700000000,
        chat=chat,
        from_user=user,
        text=text,
    )
    # Bypass frozen pydantic model check
    object.__setattr__(msg, "answer", AsyncMock())
    object.__setattr__(msg, "edit_text", AsyncMock())
    object.__setattr__(msg, "edit_reply_markup", AsyncMock())
    return msg


def create_mock_callback_query(
    data: str,
    user: User,
    chat: Chat,
) -> CallbackQuery:
    """Create a mock aiogram CallbackQuery with AsyncMock methods."""
    parent_msg = create_mock_message(text="Original message", user=user, chat=chat)

    cb = CallbackQuery.model_construct(
        id="cb_999",
        from_user=user,
        chat_instance="chat_inst_1",
        message=parent_msg,
        data=data,
    )
    object.__setattr__(cb, "answer", AsyncMock())
    return cb
