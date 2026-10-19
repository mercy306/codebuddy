"""Unit tests for SQLite database operations."""

import pytest
from bot.database import Database
from bot.strings import DEFAULT_LANGUAGE, LANG_EN, LANG_AM


@pytest.mark.asyncio
async def test_get_user_language_default_for_new_user(test_db: Database) -> None:
    """Non-existent users should default to DEFAULT_LANGUAGE (en)."""
    lang = await test_db.get_user_language(user_id=999999)
    assert lang == DEFAULT_LANGUAGE


@pytest.mark.asyncio
async def test_set_and_get_user_language(test_db: Database) -> None:
    """Setting user language should persist and be retrievable."""
    user_id = 1001

    # Set to Amharic
    await test_db.set_user_language(
        user_id=user_id,
        language_code=LANG_AM,
        username="test_am",
        first_name="Almaz",
    )
    lang = await test_db.get_user_language(user_id)
    assert lang == LANG_AM

    user_data = await test_db.get_user(user_id)
    assert user_data is not None
    assert user_data["user_id"] == user_id
    assert user_data["language_code"] == LANG_AM
    assert user_data["username"] == "test_am"
    assert user_data["first_name"] == "Almaz"

    # Update to English
    await test_db.set_user_language(
        user_id=user_id,
        language_code=LANG_EN,
    )
    lang_updated = await test_db.get_user_language(user_id)
    assert lang_updated == LANG_EN


@pytest.mark.asyncio
async def test_unsupported_language_fallback(test_db: Database) -> None:
    """Passing an unsupported language code should safely fall back to default."""
    user_id = 1002
    await test_db.set_user_language(
        user_id=user_id,
        language_code="es",  # Spanish not yet supported
    )
    lang = await test_db.get_user_language(user_id)
    assert lang == DEFAULT_LANGUAGE
