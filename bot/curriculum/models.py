"""Data models for curriculum modules and lessons."""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Lesson:
    """Represents a single bite-sized programming lesson."""

    id: str
    module_id: str
    order: int
    title_en: str
    title_am: str
    content_en: str
    content_am: str

    def get_title(self, lang: str = "en") -> str:
        return self.title_am if lang == "am" else self.title_en

    def get_content(self, lang: str = "en") -> str:
        return self.content_am if lang == "am" else self.content_en


@dataclass(frozen=True)
class Module:
    """Represents a learning module containing multiple lessons."""

    id: str
    order: int
    title_en: str
    title_am: str
    description_en: str
    description_am: str
    lessons: List[Lesson]

    def get_title(self, lang: str = "en") -> str:
        return self.title_am if lang == "am" else self.title_en

    def get_description(self, lang: str = "en") -> str:
        return self.description_am if lang == "am" else self.description_en

    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        for lesson in self.lessons:
            if lesson.id == lesson_id:
                return lesson
        return None
