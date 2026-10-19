"""Configuration loader for CodeBuddy bot."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env file if present
load_dotenv()


@dataclass(frozen=True)
class Config:
    """Application configuration."""

    bot_token: str
    database_path: Path
    log_level: str

    @classmethod
    def load(cls) -> Config:
        """Load configuration from environment variables."""
        token = os.getenv("BOT_TOKEN", "").strip()
        if not token:
            raise ValueError(
                "BOT_TOKEN is missing or empty. Please set it in your .env file."
            )

        db_path_str = os.getenv("DATABASE_PATH", "data/codebuddy.db").strip()
        db_path = Path(db_path_str)

        log_level = os.getenv("LOG_LEVEL", "INFO").strip().upper()

        return cls(
            bot_token=token,
            database_path=db_path,
            log_level=log_level,
        )

    @property
    def masked_token(self) -> str:
        """Return masked token safe for display or logging."""
        if len(self.bot_token) <= 8:
            return "***"
        return f"{self.bot_token[:4]}...{self.bot_token[-4:]}"
