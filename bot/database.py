"""SQLite database layer for storing user preferences and state."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Dict, Any, Set, Tuple
import aiosqlite

from bot.strings import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES

logger = logging.getLogger(__name__)


class Database:
    """Async SQLite database manager."""

    def __init__(self, db_path: Path | str) -> None:
        self.db_path = Path(db_path)

    async def init_db(self) -> None:
        """Create database tables if they do not exist."""
        # Ensure directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    language_code TEXT NOT NULL DEFAULT 'en',
                    active_track TEXT NOT NULL DEFAULT 'python',
                    username TEXT,
                    first_name TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )
            try:
                await db.execute("ALTER TABLE users ADD COLUMN active_track TEXT NOT NULL DEFAULT 'python';")
            except Exception:
                pass
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS user_lessons (
                    user_id INTEGER NOT NULL,
                    lesson_id TEXT NOT NULL,
                    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, lesson_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                );
                """
            )
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS user_quiz_attempts (
                    user_id INTEGER NOT NULL,
                    quiz_id TEXT NOT NULL,
                    is_correct BOOLEAN NOT NULL,
                    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, quiz_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                );
                """
            )
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS user_code_challenges (
                    user_id INTEGER NOT NULL,
                    challenge_id TEXT NOT NULL,
                    is_completed BOOLEAN NOT NULL DEFAULT 1,
                    submitted_code TEXT,
                    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, challenge_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                );
                """
            )
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS user_tutor_progress (
                    user_id INTEGER NOT NULL,
                    chapter_id TEXT NOT NULL,
                    step_index INTEGER NOT NULL DEFAULT 0,
                    is_completed BOOLEAN NOT NULL DEFAULT 0,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, chapter_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                );
                """
            )
            await db.commit()
            logger.info("Database initialized successfully at %s", self.db_path)

    async def get_user_language(self, user_id: int) -> str:
        """Fetch user's preferred language code or return default."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                async with db.execute(
                    "SELECT language_code FROM users WHERE user_id = ?",
                    (user_id,),
                ) as cursor:
                    row = await cursor.fetchone()
                    if row and row["language_code"] in SUPPORTED_LANGUAGES:
                        return row["language_code"]
        except Exception as e:
            logger.error("Error retrieving user language for user %s: %s", user_id, e)

        return DEFAULT_LANGUAGE

    async def set_user_language(
        self,
        user_id: int,
        language_code: str,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
    ) -> None:
        """Insert or update user's language selection and profile."""
        if language_code not in SUPPORTED_LANGUAGES:
            language_code = DEFAULT_LANGUAGE

        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO users (user_id, language_code, username, first_name, updated_at)
                    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id) DO UPDATE SET
                        language_code = excluded.language_code,
                        username = coalesce(excluded.username, users.username),
                        first_name = coalesce(excluded.first_name, users.first_name),
                        updated_at = CURRENT_TIMESTAMP;
                    """,
                    (user_id, language_code, username, first_name),
                )
                await db.commit()
                logger.info("Updated language for user %s to '%s'", user_id, language_code)
        except Exception as e:
            logger.error("Error updating user language for user %s: %s", user_id, e)
            raise

    async def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Fetch complete user profile record."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                async with db.execute(
                    "SELECT * FROM users WHERE user_id = ?",
                    (user_id,),
                ) as cursor:
                    row = await cursor.fetchone()
                    if row:
                        return dict(row)
        except Exception as e:
            logger.error("Error fetching user profile for user %s: %s", user_id, e)
        return None

    async def get_user_track(self, user_id: int) -> str:
        """Fetch user's active learning track ('python', 'javascript', 'html', or 'css')."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                async with db.execute(
                    "SELECT active_track FROM users WHERE user_id = ?",
                    (user_id,),
                ) as cursor:
                    row = await cursor.fetchone()
                    if row and row["active_track"] in ("python", "javascript", "html", "css", "sql", "java", "csharp", "typescript", "bash", "vb", "perl", "php", "c", "react", "react_native", "angular", "vue", "express", "django"):
                        return row["active_track"]
        except Exception as e:
            logger.error("Error retrieving user track for user %s: %s", user_id, e)
        return "python"

    async def set_user_track(self, user_id: int, track: str) -> None:
        """Update user's active learning track."""
        if track not in ("python", "javascript", "html", "css", "sql", "java", "csharp", "typescript", "bash", "vb", "perl", "php", "c", "react", "react_native", "angular", "vue", "express", "django"):
            track = "python"







        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO users (user_id, active_track, updated_at)
                    VALUES (?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id) DO UPDATE SET
                        active_track = excluded.active_track,
                        updated_at = CURRENT_TIMESTAMP;
                    """,
                    (user_id, track),
                )
                await db.commit()
                logger.info("Updated track for user %s to '%s'", user_id, track)
        except Exception as e:
            logger.error("Error updating user track for user %s: %s", user_id, e)

    async def mark_lesson_completed(self, user_id: int, lesson_id: str) -> bool:
        """Mark a lesson as completed for a user. Returns True if newly added, False if already completed."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute(
                    """
                    INSERT OR IGNORE INTO user_lessons (user_id, lesson_id, completed_at)
                    VALUES (?, ?, CURRENT_TIMESTAMP)
                    """,
                    (user_id, lesson_id),
                )
                await db.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error("Error marking lesson %s complete for user %s: %s", lesson_id, user_id, e)
            return False

    async def get_completed_lessons(self, user_id: int) -> Set[str]:
        """Fetch the set of completed lesson IDs for a user."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT lesson_id FROM user_lessons WHERE user_id = ?",
                    (user_id,),
                ) as cursor:
                    rows = await cursor.fetchall()
                    return {row[0] for row in rows}
        except Exception as e:
            logger.error("Error retrieving completed lessons for user %s: %s", user_id, e)
            return set()

    async def is_lesson_completed(self, user_id: int, lesson_id: str) -> bool:
        """Check if a specific lesson is completed."""
        completed = await self.get_completed_lessons(user_id)
        return lesson_id in completed

    async def record_quiz_attempt(
        self, user_id: int, quiz_id: str, is_correct: bool
    ) -> None:
        """Record or update a user's quiz attempt result."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO user_quiz_attempts (user_id, quiz_id, is_correct, attempted_at)
                    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id, quiz_id) DO UPDATE SET
                        is_correct = excluded.is_correct,
                        attempted_at = CURRENT_TIMESTAMP;
                    """,
                    (user_id, quiz_id, is_correct),
                )
                await db.commit()
        except Exception as e:
            logger.error("Error recording quiz %s for user %s: %s", quiz_id, user_id, e)

    async def get_solved_quizzes(self, user_id: int) -> Set[str]:
        """Return the set of quiz IDs that the user answered correctly."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT quiz_id FROM user_quiz_attempts WHERE user_id = ? AND is_correct = 1",
                    (user_id,),
                ) as cursor:
                    rows = await cursor.fetchall()
                    return {row[0] for row in rows}
        except Exception as e:
            logger.error("Error fetching solved quizzes for user %s: %s", user_id, e)
            return set()

    async def get_quiz_stats(self, user_id: int) -> Tuple[int, int]:
        """Return tuple of (correct_count, total_attempted_count)."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    """
                    SELECT 
                        COALESCE(SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END), 0),
                        COUNT(*)
                    FROM user_quiz_attempts
                    WHERE user_id = ?
                    """,
                    (user_id,),
                ) as cursor:
                    row = await cursor.fetchone()
                    if row:
                        return row[0], row[1]
        except Exception as e:
            logger.error("Error fetching quiz stats for user %s: %s", user_id, e)
        return 0, 0

    async def record_code_challenge_completion(
        self, user_id: int, challenge_id: str, submitted_code: str
    ) -> None:
        """Record successful completion of a real coding challenge."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO user_code_challenges (user_id, challenge_id, is_completed, submitted_code, completed_at)
                    VALUES (?, ?, 1, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id, challenge_id) DO UPDATE SET
                        is_completed = 1,
                        submitted_code = excluded.submitted_code,
                        completed_at = CURRENT_TIMESTAMP;
                    """,
                    (user_id, challenge_id, submitted_code),
                )
                await db.commit()
                logger.info("Recorded code challenge %s for user %s", challenge_id, user_id)
        except Exception as e:
            logger.error("Error recording code challenge for user %s: %s", user_id, e)

    async def get_completed_code_challenges(self, user_id: int) -> Set[str]:
        """Return set of completed coding challenge IDs for user."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT challenge_id FROM user_code_challenges WHERE user_id = ? AND is_completed = 1",
                    (user_id,),
                ) as cursor:
                    rows = await cursor.fetchall()
                    return {row[0] for row in rows}
        except Exception as e:
            logger.error("Error fetching completed code challenges for user %s: %s", user_id, e)
            return set()

    async def get_tutor_progress(self, user_id: int, chapter_id: str) -> Tuple[int, bool]:
        """Fetch (step_index, is_completed) for a user on a given tutor chapter."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT step_index, is_completed FROM user_tutor_progress WHERE user_id = ? AND chapter_id = ?",
                    (user_id, chapter_id),
                ) as cursor:
                    row = await cursor.fetchone()
                    if row:
                        return row[0], bool(row[1])
        except Exception as e:
            logger.error("Error fetching tutor progress for user %s: %s", user_id, e)
        return 0, False

    async def set_tutor_progress(
        self, user_id: int, chapter_id: str, step_index: int, is_completed: bool = False
    ) -> None:
        """Upsert tutor progress for a user."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO user_tutor_progress (user_id, chapter_id, step_index, is_completed, updated_at)
                    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id, chapter_id) DO UPDATE SET
                        step_index = excluded.step_index,
                        is_completed = excluded.is_completed,
                        updated_at = CURRENT_TIMESTAMP;
                    """,
                    (user_id, chapter_id, step_index, 1 if is_completed else 0),
                )
                await db.commit()
        except Exception as e:
            logger.error("Error setting tutor progress for user %s: %s", user_id, e)

    async def get_completed_tutor_chapters(self, user_id: int) -> Set[str]:
        """Fetch the set of completed tutor chapter IDs for a user."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT chapter_id FROM user_tutor_progress WHERE user_id = ? AND is_completed = 1",
                    (user_id,),
                ) as cursor:
                    rows = await cursor.fetchall()
                    return {row[0] for row in rows}
        except Exception as e:
            logger.error("Error fetching completed tutor chapters for user %s: %s", user_id, e)
            return set()

    async def reset_user_progress(self, user_id: int) -> None:
        """Reset all completed lessons, quiz attempts, coding challenges, and tutor progress for a user."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute("DELETE FROM user_lessons WHERE user_id = ?", (user_id,))
                await db.execute("DELETE FROM user_quiz_attempts WHERE user_id = ?", (user_id,))
                await db.execute("DELETE FROM user_code_challenges WHERE user_id = ?", (user_id,))
                await db.execute("DELETE FROM user_tutor_progress WHERE user_id = ?", (user_id,))
                await db.commit()
                logger.info("Reset learning progress for user %s", user_id)
        except Exception as e:
            logger.error("Error resetting progress for user %s: %s", user_id, e)
