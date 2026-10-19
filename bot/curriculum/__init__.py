"""Curriculum package for beginner programming courses."""

from bot.curriculum.models import Lesson, Module
from bot.curriculum.data import (
    MODULES,
    get_all_modules,
    get_module,
    get_lesson,
    get_adjacent_lessons,
    get_total_lessons_count,
)

__all__ = [
    "Lesson",
    "Module",
    "MODULES",
    "get_all_modules",
    "get_module",
    "get_lesson",
    "get_adjacent_lessons",
    "get_total_lessons_count",
]
