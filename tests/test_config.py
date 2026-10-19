"""Unit tests for configuration loader and token security."""

import pytest
from bot.config import Config


def test_config_missing_token_raises_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """Config.load() must raise ValueError if BOT_TOKEN is empty or missing."""
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    with pytest.raises(ValueError, match="BOT_TOKEN is missing or empty"):
        Config.load()


def test_config_valid_and_masked_token(monkeypatch: pytest.MonkeyPatch) -> None:
    """Config must mask sensitive bot token properly."""
    monkeypatch.setenv("BOT_TOKEN", "1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ")
    monkeypatch.setenv("DATABASE_PATH", "custom/test.db")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    cfg = Config.load()
    assert cfg.bot_token == "1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ"
    assert str(cfg.database_path) == "custom\\test.db" or str(cfg.database_path) == "custom/test.db"
    assert cfg.log_level == "DEBUG"

    # Token must never be printed unmasked
    assert cfg.masked_token.startswith("1234...")
    assert cfg.masked_token.endswith("...wxYZ")
    assert "ABCdefGHIjklMNOpqr" not in cfg.masked_token
