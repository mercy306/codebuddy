"""Hands-on coding challenges for beginners."""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class CodingChallenge:
    """Represents a hands-on code writing challenge."""

    id: str
    order: int
    title_en: str
    title_am: str
    prompt_en: str
    prompt_am: str
    hint_en: str
    hint_am: str
    expected_output: str

    def get_title(self, lang: str = "en") -> str:
        return self.title_am if lang == "am" else self.title_en

    def get_prompt(self, lang: str = "en") -> str:
        return self.prompt_am if lang == "am" else self.prompt_en

    def get_hint(self, lang: str = "en") -> str:
        return self.hint_am if lang == "am" else self.hint_en

    def check_solution(self, stdout: str) -> bool:
        """Validate if the student's output matches expectations."""
        return stdout.strip() == self.expected_output.strip()


CHALLENGES: List[CodingChallenge] = [
    CodingChallenge(
        id="c1",
        order=1,
        title_en="Challenge 1: Your First Line of Code",
        title_am="ተግባራዊ ፈተና 1፦ የመጀመሪያው የኮድ መስመር",
        prompt_en=(
            "✍️ *Task:*\n"
            "Write a single line of Python code that prints:\n"
            '`Hello, CodeBuddy!` to the screen.'
        ),
        prompt_am=(
            "✍️ *ተግባር፦*\n"
            "`Hello, CodeBuddy!` የሚለውን ጽሁፍ በማያ ገጹ ላይ የሚያሳይ የአንድ መስመር የፓይተን ኮድ ይጻፉ።"
        ),
        hint_en='Use the `print()` function with quotes: `print("Hello, CodeBuddy!")`',
        hint_am='`print()`ን በመጠቀም በጥቅስ ምልክት ውስጥ ጽሁፉን ያስገቡ፦ `print("Hello, CodeBuddy!")`',
        expected_output="Hello, CodeBuddy!",
    ),
    CodingChallenge(
        id="c2",
        order=2,
        title_en="Challenge 2: Let Python Do Math",
        title_am="ተግባራዊ ፈተና 2፦ ፓይተን ሂሳብ እንዲሰራ ማድረግ",
        prompt_en=(
            "✍️ *Task:*\n"
            "Write code that prints the result of multiplying `25` by `4`.\n\n"
            "*(Hint: In Python, multiplication uses the asterisk `*` symbol).* "
        ),
        prompt_am=(
            "✍️ *ተግባር፦*\n"
            "`25` በ `4` ተባዝቶ የሚገኘውን ውጤት በማያ ገጹ ላይ የሚያሳይ ኮድ ይጻፉ።\n\n"
            "*(ማስታወሻ፦ በፓይተን የማባዛት ምልክት ኮከብ `*` ነው)*"
        ),
        hint_en="Write: `print(25 * 4)` (without quotes, so it calculates the math!)",
        hint_am="ያለ ጥቅስ ምልክት `print(25 * 4)` ብለው ይጻፉ!",
        expected_output="100",
    ),
    CodingChallenge(
        id="c3",
        order=3,
        title_en="Challenge 3: Variables in Action",
        title_am="ተግባራዊ ፈተና 3፦ ቫሪያብልን በተግባር መጠቀም",
        prompt_en=(
            "✍️ *Task:*\n"
            "Create a variable called `city` and store `\"Addis Ababa\"` inside it.\n"
            "Then, on a new line, print the `city` variable!"
        ),
        prompt_am=(
            "✍️ *ተግባር፦*\n"
            "`city` የሚባል ቫሪያብል ፈጥረው `\"Addis Ababa\"` የሚለውን ስም አስቀምጡበት።\n"
            "ከዚያም በአዲስ መስመር ላይ `city` ቫሪያብሉን `print()` አድርጉ!"
        ),
        hint_en='Line 1: `city = "Addis Ababa"`\nLine 2: `print(city)`',
        hint_am='መስመር 1፦ `city = "Addis Ababa"`\nመስመር 2፦ `print(city)`',
        expected_output="Addis Ababa",
    ),
    CodingChallenge(
        id="c4",
        order=4,
        title_en="Challenge 4: Repeating with a Loop",
        title_am="ተግባራዊ ፈተና 4፦ በ Loop መድገም",
        prompt_en=(
            "✍️ *Task:*\n"
            "Write a `for` loop that prints `I love coding!` exactly `3` times."
        ),
        prompt_am=(
            "✍️ *ተግባር፦*\n"
            "`I love coding!` የሚለውን ጽሁፍ `3` ጊዜ ደጋግሞ የሚያሳይ `for` loop ይጻፉ።"
        ),
        hint_en='Write:\n```python\nfor i in range(3):\n    print("I love coding!")\n```',
        hint_am='ይህንን ይጻፉ፦\n```python\nfor i in range(3):\n    print("I love coding!")\n```',
        expected_output="I love coding!\nI love coding!\nI love coding!",
    ),
]


def get_all_challenges() -> List[CodingChallenge]:
    """Return all code writing challenges sorted by order."""
    return sorted(CHALLENGES, key=lambda c: c.order)


def get_challenge(challenge_id: str) -> Optional[CodingChallenge]:
    """Retrieve challenge by ID."""
    for c in CHALLENGES:
        if c.id == challenge_id:
            return c
    return None


def get_next_challenge_id(current_id: str) -> Optional[str]:
    """Get the subsequent coding challenge ID."""
    all_ch = get_all_challenges()
    for idx, c in enumerate(all_ch):
        if c.id == current_id:
            if idx + 1 < len(all_ch):
                return all_ch[idx + 1].id
            return None
    return None


def get_total_challenges_count() -> int:
    """Return total count of code writing challenges."""
    return len(CHALLENGES)
