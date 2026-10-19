"""Keyboards package."""

from bot.keyboards.language import get_language_inline_keyboard
from bot.keyboards.menu import (
    get_main_menu_keyboard,
    get_settings_keyboard,
    get_onboarding_keyboard,
)
from bot.keyboards.learn import (
    get_modules_keyboard,
    get_lessons_keyboard,
    get_lesson_navigation_keyboard,
)
from bot.keyboards.practice import (
    get_practice_menu_keyboard,
    get_quiz_keyboard,
    get_quiz_result_keyboard,
    get_quiz_list_keyboard,
)
from bot.keyboards.codelab import (
    get_codelab_menu_keyboard,
    get_challenge_view_keyboard,
    get_challenge_result_keyboard,
    get_challenge_list_keyboard,
)
from bot.keyboards.tutor import (
    get_tutor_chapters_keyboard,
    get_tutor_step_keyboard,
    get_tutor_concept_retry_keyboard,
    get_tutor_completion_keyboard,
)

__all__ = [
    "get_language_inline_keyboard",
    "get_main_menu_keyboard",
    "get_settings_keyboard",
    "get_onboarding_keyboard",
    "get_modules_keyboard",
    "get_lessons_keyboard",
    "get_lesson_navigation_keyboard",
    "get_practice_menu_keyboard",
    "get_quiz_keyboard",
    "get_quiz_result_keyboard",
    "get_quiz_list_keyboard",
    "get_codelab_menu_keyboard",
    "get_challenge_view_keyboard",
    "get_challenge_result_keyboard",
    "get_challenge_list_keyboard",
    "get_tutor_chapters_keyboard",
    "get_tutor_step_keyboard",
    "get_tutor_concept_retry_keyboard",
    "get_tutor_completion_keyboard",
]
