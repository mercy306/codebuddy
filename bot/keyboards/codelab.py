"""Keyboards for the hands-on CodeLab writing challenges."""

from __future__ import annotations

from typing import List, Set, Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.codelab.challenges import CodingChallenge
from bot.strings import DEFAULT_LANGUAGE


def get_codelab_menu_keyboard(lang: str = DEFAULT_LANGUAGE) -> InlineKeyboardMarkup:
    """Build hub keyboard for hands-on code writing."""
    start_text = "⚡ Start Coding (Challenge 1)" if lang == "en" else "⚡ ኮድ መጻፍ ጀምር (ፈተና 1)"
    list_text = "📋 All Code Challenges" if lang == "en" else "📋 የፈተናዎች ዝርዝር"
    back_text = "🔙 Practice Hub" if lang == "en" else "🔙 የልምምድ ማዕከል"

    keyboard = [
        [InlineKeyboardButton(text=start_text, callback_data="code:view:c1")],
        [InlineKeyboardButton(text=list_text, callback_data="code:list")],
        [InlineKeyboardButton(text=back_text, callback_data="quiz:menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_challenge_view_keyboard(
    challenge_id: str,
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build keyboard shown when waiting for student code submission."""
    hint_text = "💡 Show Hint" if lang == "en" else "💡 ፍንጭ አሳይ"
    cancel_text = "❌ Cancel" if lang == "en" else "❌ ሰርዝ"

    keyboard = [
        [
            InlineKeyboardButton(text=hint_text, callback_data=f"code:hint:{challenge_id}"),
            InlineKeyboardButton(text=cancel_text, callback_data="code:cancel"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_challenge_result_keyboard(
    next_id: Optional[str],
    current_id: str,
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build keyboard shown after code evaluation."""
    keyboard = []

    if next_id:
        next_text = "Next Challenge ▶" if lang == "en" else "ቀጣይ ፈተና ▶"
        keyboard.append([
            InlineKeyboardButton(text=next_text, callback_data=f"code:view:{next_id}")
        ])

    retry_text = "🔄 Try Again" if lang == "en" else "🔄 እንደገና ሞክር"
    list_text = "📋 Code Challenges" if lang == "en" else "📋 የፈተናዎች ዝርዝር"

    keyboard.append([
        InlineKeyboardButton(text=retry_text, callback_data=f"code:view:{current_id}"),
        InlineKeyboardButton(text=list_text, callback_data="code:list"),
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_challenge_list_keyboard(
    challenges: List[CodingChallenge],
    completed_ids: Set[str],
    lang: str = DEFAULT_LANGUAGE,
) -> InlineKeyboardMarkup:
    """Build list of all coding challenges with completion icons."""
    keyboard = []
    for ch in challenges:
        icon = "✅" if ch.id in completed_ids else "⚪"
        btn_text = f"{icon} {ch.get_title(lang)}"
        keyboard.append([
            InlineKeyboardButton(text=btn_text, callback_data=f"code:view:{ch.id}")
        ])

    back_text = "🔙 CodeLab Menu" if lang == "en" else "🔙 የኮድ ማዕከል"
    keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data="code:menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
