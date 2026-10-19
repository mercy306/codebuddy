"""Data models for practice quizzes and code prediction challenges."""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class QuizQuestion:
    """Represents an interactive quiz question."""

    id: str
    module_id: str
    order: int
    question_en: str
    question_am: str
    options_en: List[str]
    options_am: List[str]
    correct_index: int
    explanation_en: str
    explanation_am: str
    code_snippet: Optional[str] = None

    def get_question(self, lang: str = "en") -> str:
        return self.question_am if lang == "am" else self.question_en

    def get_options(self, lang: str = "en") -> List[str]:
        return self.options_am if lang == "am" else self.options_en

    def get_explanation(self, lang: str = "en") -> str:
        return self.explanation_am if lang == "am" else self.explanation_en

    def is_correct(self, option_index: int) -> bool:
        return option_index == self.correct_index
