"""Practice quizzes and interactive questions in English and Amharic."""

from __future__ import annotations
from typing import List, Optional
from bot.practice.models import QuizQuestion

QUIZZES: List[QuizQuestion] = [
    QuizQuestion(
        id="q1",
        module_id="m1",
        order=1,
        question_en="What does the `print()` function do in Python?",
        question_am="በፓይተን ውስጥ የ `print()` ፈንክሽን ምን ያደርጋል?",
        options_en=[
            "Prints text onto physical paper 📄",
            "Displays text on the computer screen 💻",
            "Deletes files from the computer 🗑️",
            "Turns off the computer 🔌",
        ],
        options_am=[
            "ጽሁፍን በወረቀት ላይ ያትማል 📄",
            "ጽሁፍን በኮምፒውተር ማያ ገጽ ላይ ያሳያል 💻",
            "ፋይሎችን ከኮምፒውተሩ ይሰርዛል 🗑️",
            "ኮምፒውተሩን ያጠፋል 🔌",
        ],
        correct_index=1,
        explanation_en="In Python, `print()` outputs text or numbers directly to the screen for the user to see.",
        explanation_am="በፓይተን ውስጥ `print()` ጽሁፍን ወይም ቁጥሮችን በማያ ገጹ ላይ ለተጠቃሚው ያሳያል።",
    ),
    QuizQuestion(
        id="q2",
        module_id="m1",
        order=2,
        question_en="What will the following code output?",
        question_am="የሚከተለው ኮድ ምን ውጤት ያሳያል?",
        code_snippet="print(10 + 20)",
        options_en=[
            '"10 + 20"',
            "30",
            "1020",
            "Error",
        ],
        options_am=[
            '"10 + 20"',
            "30",
            "1020",
            "ስህተት (Error)",
        ],
        correct_index=1,
        explanation_en="Because 10 and 20 are numbers without quotation marks, Python calculates their sum (10 + 20 = 30).",
        explanation_am="10 እና 20 ያለ ጥቅስ ምልክት የተጻፉ ቁጥሮች ስለሆኑ፣ ፓይተን ድምራቸውን ያሰላል (10 + 20 = 30)።",
    ),
    QuizQuestion(
        id="q3",
        module_id="m2",
        order=3,
        question_en="What will be printed after running this code?",
        question_am="ይህንን ኮድ ካስኬዱ በኋላ ምን ይታያል?",
        code_snippet="score = 5\nscore = score + 3\nprint(score)",
        options_en=[
            "5",
            "3",
            "8",
            "53",
        ],
        options_am=[
            "5",
            "3",
            "8",
            "53",
        ],
        correct_index=2,
        explanation_en="`score` starts at 5. Then `5 + 3` is calculated (8) and stored back into `score`.",
        explanation_am="`score` መጀመሪያ 5 ነበር። ከዚያ `5 + 3` ተደምሮ 8 ይሆናል፣ እና 8 ወደ `score` ይመለሳል።",
    ),
    QuizQuestion(
        id="q4",
        module_id="m2",
        order=4,
        question_en="Which of the following correctly stores the text 'Abebe' in a variable named `user`?",
        question_am="'አበበ' የሚለውን ጽሁፍ `user` በሚባል ቫሪያብል ውስጥ በትክክል የሚያስቀምጠው የትኛው ነው?",
        options_en=[
            'user = "Abebe"',
            '"Abebe" = user',
            'user == "Abebe"',
            'print(user = "Abebe")',
        ],
        options_am=[
            'user = "አበበ"',
            '"አበበ" = user',
            'user == "አበበ"',
            'print(user = "አበበ")',
        ],
        correct_index=0,
        explanation_en="The variable name goes on the left, followed by `=`, and the string value inside quotes on the right.",
        explanation_am="የቫሪያብል ስም በግራ በኩል ይቀመጣል፣ በመቀጠል `=` ይመጣል፣ ከዚያም ጽሁፉ በጥቅስ ምልክት በቀኝ በኩል ይቀመጣል።",
    ),
    QuizQuestion(
        id="q5",
        module_id="m3",
        order=5,
        question_en="What will this program print?",
        question_am="ይህ ፕሮግራም ምን ያሳያል?",
        code_snippet=(
            "temperature = 30\n"
            "if temperature > 25:\n"
            '    print("Hot ☀️")\n'
            "else:\n"
            '    print("Cold ❄️")'
        ),
        options_en=[
            "Hot ☀️",
            "Cold ❄️",
            "Hot ☀️ and Cold ❄️",
            "Nothing",
        ],
        options_am=[
            "Hot ☀️",
            "Cold ❄️",
            "Hot ☀️ እና Cold ❄️",
            "ምንም አያሳይም",
        ],
        correct_index=0,
        explanation_en="Since 30 is greater than 25, the `if` condition is True, so it prints 'Hot ☀️'.",
        explanation_am="30 ከ 25 ስለሚበልጥ፣ የ `if` ሁኔታው እውነት ነው፤ ስለዚህ 'Hot ☀️'ን ያሳያል።",
    ),
    QuizQuestion(
        id="q6",
        module_id="m4",
        order=6,
        question_en="How many times will 'Hi' be printed?",
        question_am="'Hi' ስንት ጊዜ ይታያል?",
        code_snippet=(
            "for i in range(3):\n"
            '    print("Hi")'
        ),
        options_en=[
            "1 time",
            "2 times",
            "3 times",
            "4 times",
        ],
        options_am=[
            "1 ጊዜ",
            "2 ጊዜ",
            "3 ጊዜ",
            "4 ጊዜ",
        ],
        correct_index=2,
        explanation_en="`range(3)` creates 3 iterations (for 0, 1, and 2), printing 'Hi' 3 times.",
        explanation_am="`range(3)` 3 ድግግሞሾችን ይፈጥራል (0፣ 1 እና 2)፤ ስለዚህ 'Hi' 3 ጊዜ ይታያል።",
    ),
]


def get_all_quizzes() -> List[QuizQuestion]:
    """Return all practice quizzes sorted by order."""
    return sorted(QUIZZES, key=lambda q: q.order)


def get_quiz(quiz_id: str) -> Optional[QuizQuestion]:
    """Retrieve quiz question by identifier."""
    for q in QUIZZES:
        if q.id == quiz_id:
            return q
    return None


def get_quizzes_by_module(module_id: str) -> List[QuizQuestion]:
    """Retrieve all quiz questions belonging to a specific module."""
    return [q for q in QUIZZES if q.module_id == module_id]


def get_next_quiz_id(current_quiz_id: str) -> Optional[str]:
    """Get the next quiz ID in sequence."""
    quizzes = get_all_quizzes()
    for idx, q in enumerate(quizzes):
        if q.id == current_quiz_id:
            if idx + 1 < len(quizzes):
                return quizzes[idx + 1].id
            return None
    return None


def get_total_quizzes_count() -> int:
    """Return total count of available quizzes."""
    return len(QUIZZES)
