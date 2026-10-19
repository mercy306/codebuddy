"""Models for the interactive conversational tutor system."""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Callable


class StepType(str, Enum):
    """Type of interactive tutor step."""

    EXPLANATION = "explanation"
    CODE_PROMPT = "code_prompt"
    CONCEPT_CHECK = "concept_check"


@dataclass(frozen=True)
class TutorStep:
    """A single interactive dialogue turn from the teacher bot."""

    id: str
    step_type: StepType
    # Content in English and Amharic
    message_en: str
    message_am: str
    # If CODE_PROMPT: expected stdout or validator keyword
    expected_code_output: Optional[str] = None
    expected_code_contains: Optional[str] = None
    hint_en: Optional[str] = None
    hint_am: Optional[str] = None
    # If CONCEPT_CHECK: options and correct index
    options_en: Optional[List[str]] = None
    options_am: Optional[List[str]] = None
    correct_option_index: Optional[int] = None
    success_message_en: Optional[str] = None
    success_message_am: Optional[str] = None

    def get_message(self, lang: str = "en") -> str:
        return self.message_am if lang == "am" else self.message_en

    def get_hint(self, lang: str = "en") -> str:
        if lang == "am":
            return self.hint_am or ""
        return self.hint_en or ""

    def get_success_message(self, lang: str = "en") -> str:
        if lang == "am":
            return self.success_message_am or "በጣም ጎበዝ! በትክክል ሰርተዋል።"
        return self.success_message_en or "🎉 Excellent job! That was correct!"


@dataclass(frozen=True)
class TutorChapter:
    """A learning chapter made up of sequential interactive tutor steps."""

    id: str
    order: int
    title_en: str
    title_am: str
    description_en: str
    description_am: str
    steps: List[TutorStep]
    track: str = "python"

    def get_title(self, lang: str = "en") -> str:
        return self.title_am if lang == "am" else self.title_en

    def get_step(self, index: int) -> Optional[TutorStep]:
        if 0 <= index < len(self.steps):
            return self.steps[index]
        return None
