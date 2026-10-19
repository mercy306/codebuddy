"""Unit tests for localized strings and translation parity."""

from bot.strings import (
    STRINGS,
    SUPPORTED_LANGUAGES,
    LANG_EN,
    LANG_AM,
    DEFAULT_LANGUAGE,
    get_string,
)


def test_all_keys_have_both_en_and_am() -> None:
    """Ensure complete translation parity between English and Amharic."""
    required_keys = [
        "welcome",
        "choose_language",
        "language_selected",
        "main_menu_title",
        "btn_learn",
        "btn_practice",
        "btn_progress",
        "btn_settings",
        "btn_change_language",
        "btn_reset_progress",
        "btn_start_first_lesson",
        "reset_success_alert",
        "learn_content",
        "learn_modules_title",
        "lessons_list_title",
        "btn_complete_lesson",
        "btn_lesson_completed",
        "btn_next_lesson",
        "btn_prev_lesson",
        "btn_back_to_lessons",
        "btn_back_to_modules",
        "lesson_completed_alert",
        "practice_hub_title",
        "practice_content",
        "progress_content",
        "settings_content",
        "help",
        "unknown_message",
    ]

    for key in required_keys:
        assert key in STRINGS, f"Key '{key}' is missing from STRINGS"
        for lang in SUPPORTED_LANGUAGES:
            assert lang in STRINGS[key], f"Language '{lang}' missing for key '{key}'"
            assert len(STRINGS[key][lang].strip()) > 0, f"Key '{key}' in '{lang}' is empty"


def test_get_string_fallback() -> None:
    """Verify get_string fallback behavior."""
    # Existing key with valid language
    assert "Welcome" in get_string("welcome", LANG_EN)
    assert "እንኳን" in get_string("welcome", LANG_AM)

    # Invalid language falls back to default (en)
    assert "Welcome" in get_string("welcome", "fr")

    # Missing key returns formatted string fallback
    assert get_string("non_existent_key") == "[non_existent_key]"
