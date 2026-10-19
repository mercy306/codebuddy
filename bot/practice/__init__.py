"""Practice module for interactive challenges and quizzes."""

from bot.practice.models import QuizQuestion
from bot.practice.data import (
    QUIZZES,
    get_all_quizzes,
    get_quiz,
    get_quizzes_by_module,
    get_next_quiz_id,
    get_total_quizzes_count,
)

__all__ = [
    "QuizQuestion",
    "QUIZZES",
    "get_all_quizzes",
    "get_quiz",
    "get_quizzes_by_module",
    "get_next_quiz_id",
    "get_total_quizzes_count",
]
