"""CodeLab package for real code writing exercises and execution."""

from bot.codelab.sandbox import run_student_code, ExecutionResult
from bot.codelab.challenges import (
    CodingChallenge,
    CHALLENGES,
    get_all_challenges,
    get_challenge,
    get_next_challenge_id,
    get_total_challenges_count,
)

__all__ = [
    "run_student_code",
    "ExecutionResult",
    "CodingChallenge",
    "CHALLENGES",
    "get_all_challenges",
    "get_challenge",
    "get_next_challenge_id",
    "get_total_challenges_count",
]
