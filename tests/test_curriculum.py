"""Unit tests for curriculum structure and lesson queries."""

from bot.curriculum import (
    get_all_modules,
    get_module,
    get_lesson,
    get_adjacent_lessons,
    get_total_lessons_count,
)


def test_modules_count_and_structure() -> None:
    """Verify standard modules exist with valid lessons."""
    modules = get_all_modules()
    assert len(modules) >= 4

    module_ids = [m.id for m in modules]
    assert "m1" in module_ids
    assert "m2" in module_ids
    assert "m3" in module_ids
    assert "m4" in module_ids

    total_lessons = get_total_lessons_count()
    assert total_lessons >= 8


def test_bilingual_titles_and_content_parity() -> None:
    """Ensure every module and lesson has non-empty English and Amharic text."""
    modules = get_all_modules()
    for mod in modules:
        assert mod.get_title("en") != ""
        assert mod.get_title("am") != ""
        assert mod.get_description("en") != ""
        assert mod.get_description("am") != ""

        for les in mod.lessons:
            assert les.get_title("en") != ""
            assert les.get_title("am") != ""
            assert les.get_content("en") != ""
            assert les.get_content("am") != ""
            # Ensure python snippets exist
            assert "```python" in les.get_content("en")
            assert "```python" in les.get_content("am")


def test_get_lesson_and_adjacent_lessons() -> None:
    """Verify lesson lookup and adjacent lesson traversal."""
    mod, les = get_lesson("m1_l1")
    assert mod is not None
    assert mod.id == "m1"
    assert les is not None
    assert les.id == "m1_l1"

    # m1_l1 is the first lesson, so prev is None, next is m1_l2
    prev_id, next_id = get_adjacent_lessons("m1_l1")
    assert prev_id is None
    assert next_id == "m1_l2"

    # m1_l2 should link to m1_l1 and m2_l1
    prev_2, next_2 = get_adjacent_lessons("m1_l2")
    assert prev_2 == "m1_l1"
    assert next_2 == "m2_l1"
