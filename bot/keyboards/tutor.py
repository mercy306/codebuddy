"""Keyboards for interactive conversational tutor engine."""

from __future__ import annotations

from typing import Set, Optional, List
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.tutor.models import TutorChapter, TutorStep, StepType
from bot.tutor.content import get_all_tutor_chapters
from bot.strings import DEFAULT_LANGUAGE


OPTION_LETTERS = ("A", "B", "C", "D")


def get_tutor_chapters_keyboard(
    completed_chapters: Set[str],
    lang: str = DEFAULT_LANGUAGE,
    track: str = "python",
) -> InlineKeyboardMarkup:
    """Build inline keyboard listing all tutor chapters for the active track."""
    keyboard: List[List[InlineKeyboardButton]] = []
    chapters = get_all_tutor_chapters(track)

    for ch in chapters:
        is_done = ch.id in completed_chapters
        icon = "✅" if is_done else "🧑‍🏫"
        title = ch.get_title(lang)
        button_text = f"{icon} {title}"
        keyboard.append([
            InlineKeyboardButton(text=button_text, callback_data=f"tutor:start:{ch.id}")
        ])

    # Track switcher rows (up to 2 per row)
    all_tracks = [
        ("python", "🐍 Python" if lang == "en" else "🐍 ፓይተን"),
        ("javascript", "🌐 JavaScript" if lang == "en" else "🌐 ጃቫስክሪፕት"),
        ("html", "📄 HTML" if lang == "en" else "📄 ኤችቲኤምኤል"),
        ("css", "🎨 CSS" if lang == "en" else "🎨 ሲኤስኤስ"),
        ("sql", "🗄️ SQL" if lang == "en" else "🗄️ ኤስኪውኤል"),
        ("java", "☕ Java" if lang == "en" else "☕ ጃቫ"),
        ("csharp", "⚡ C#" if lang == "en" else "⚡ ሲ ሻርፕ"),
        ("typescript", "🔷 TypeScript" if lang == "en" else "🔷 ታይፕስክሪፕት"),
        ("bash", "🐧 Linux Bash" if lang == "en" else "🐧 ሊኑክስ ባሽ"),
        ("vb", "💎 Visual Basic" if lang == "en" else "💎 ቪዥዋል ቤዚክ"),
        ("perl", "🐪 Perl 5" if lang == "en" else "🐪 ፐርል 5"),
        ("php", "🐘 PHP" if lang == "en" else "🐘 ፒኤችፒ"),
        ("c", "🇨 C Language" if lang == "en" else "🇨 ሲ ቋንቋ"),
        ("react", "⚛️ React" if lang == "en" else "⚛️ ሪያክት"),
        ("react_native", "📱 React Native" if lang == "en" else "📱 ሪያክት ኔቲቭ"),
        ("angular", "🅰️ Angular" if lang == "en" else "🅰️ አንጉላር"),
        ("vue", "💚 Vue.js" if lang == "en" else "💚 ቪው ጄኤስ"),
        ("express", "🚂 Express.js" if lang == "en" else "🚂 ኤክስፕረስ"),
        ("django", "🎸 Django" if lang == "en" else "🎸 ዲጃንጎ"),
    ]






    other_tracks = [
        InlineKeyboardButton(text=title, callback_data=f"tutor:track:{t_id}")
        for t_id, title in all_tracks
        if t_id != track
    ]

    # Chunk into rows of 2
    for i in range(0, len(other_tracks), 2):
        keyboard.append(other_tracks[i : i + 2])

    back_text = "🏠 Main Menu" if lang == "en" else "🏠 ዋና ማውጫ"
    keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data="tutor:exit")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)



def get_tutor_step_keyboard(
    chapter_id: str,
    step_index: int,
    step: TutorStep,
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build interactive keyboard according to the current tutor step type."""
    keyboard: List[List[InlineKeyboardButton]] = []

    if step.step_type == StepType.EXPLANATION:
        next_text = "Got it! Next ▶" if lang == "en" else "ተረድቻለሁ! ቀጣይ ▶"
        keyboard.append([
            InlineKeyboardButton(text=next_text, callback_data=f"tutor:step:{chapter_id}:{step_index + 1}")
        ])
    elif step.step_type == StepType.CONCEPT_CHECK:
        options = step.options_am if lang == "am" and step.options_am else (step.options_en or [])
        for idx, opt_text in enumerate(options):
            letter = OPTION_LETTERS[idx] if idx < len(OPTION_LETTERS) else str(idx + 1)
            btn_text = f"{letter}) {opt_text}"
            keyboard.append([
                InlineKeyboardButton(text=btn_text, callback_data=f"tutor:opt:{chapter_id}:{step_index}:{idx}")
            ])
    elif step.step_type == StepType.CODE_PROMPT:
        hint_text = "💡 Need a hint?" if lang == "en" else "💡 ፍንጭ ይፈልጋሉ?"
        keyboard.append([
            InlineKeyboardButton(text=hint_text, callback_data=f"tutor:hint:{chapter_id}:{step_index}")
        ])

    exit_text = "❌ Exit Tutor" if lang == "en" else "❌ አስተማሪውን አቁም"
    keyboard.append([
        InlineKeyboardButton(text=exit_text, callback_data="tutor:exit")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_tutor_concept_retry_keyboard(
    chapter_id: str,
    step_index: int,
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build retry keyboard when student picks an incorrect concept check option."""
    retry_text = "🔄 Try Again" if lang == "en" else "🔄 እንደገና ሞክር"
    exit_text = "❌ Exit Tutor" if lang == "en" else "❌ አስተማሪውን አቁም"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=retry_text, callback_data=f"tutor:step:{chapter_id}:{step_index}")],
            [InlineKeyboardButton(text=exit_text, callback_data="tutor:exit")],
        ]
    )


def get_tutor_completion_keyboard(
    chapter_id: str,
    next_chapter_id: Optional[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build completion keyboard offering next chapter, all chapters, or exit."""
    keyboard: List[List[InlineKeyboardButton]] = []

    if next_chapter_id:
        next_text = "🚀 Next Chapter" if lang == "en" else "🚀 ቀጣዩ ምዕራፍ"
        keyboard.append([
            InlineKeyboardButton(text=next_text, callback_data=f"tutor:start:{next_chapter_id}")
        ])

    chapters_text = "📚 All Chapters" if lang == "en" else "📚 ሁሉም ምዕራፎች"
    menu_text = "🏠 Main Menu" if lang == "en" else "🏠 ዋና ማውጫ"

    keyboard.append([
        InlineKeyboardButton(text=chapters_text, callback_data="tutor:chapters")
    ])
    keyboard.append([
        InlineKeyboardButton(text=menu_text, callback_data="tutor:exit")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
