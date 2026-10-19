"""Unit and integration tests for the TypeScript sandbox runner and curriculum."""

import pytest
from bot.codelab.ts_sandbox import run_student_ts_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_ts import TYPESCRIPT_TUTOR_CHAPTERS


def test_ts_basic_execution():
    code = """
    let message: string = "TypeScript works!";
    console.log(message);
    """
    res = run_student_ts_code(code)
    assert res.success is True
    assert res.output == "TypeScript works!"


def test_ts_interface_and_math():
    code = """
    interface Item {
        name: string;
        price: number;
    }
    const itm: Item = { name: "Book", price: 15 };
    console.log(itm.name + " costs " + itm.price);
    """
    res = run_student_ts_code(code)
    assert res.success is True
    assert res.output == "Book costs 15"


def test_ts_syntax_error():
    code = "console.log('Unclosed quote);"
    res = run_student_ts_code(code)
    assert res.success is False
    assert "Syntax Error" in res.friendly_explanation_en
    assert "የሰዋሰው ስህተት" in res.friendly_explanation_am


def test_ts_curriculum_chapters():
    chapters = get_all_tutor_chapters("typescript")
    assert len(chapters) == 7
    assert chapters[0].id == "ts_ch1"
    assert chapters[6].id == "ts_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("ts_ch1")
    assert ch1 is not None
    assert ch1.track == "typescript"

    next_id = get_next_tutor_chapter_id("ts_ch1")
    assert next_id == "ts_ch2"

    last_next = get_next_tutor_chapter_id("ts_ch7")
    assert last_next is None
