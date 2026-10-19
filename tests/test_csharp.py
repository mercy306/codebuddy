"""Unit and integration tests for the C# sandbox runner and curriculum."""

import pytest
from bot.codelab.csharp_sandbox import run_student_csharp_code, wrap_student_csharp_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_csharp import CSHARP_TUTOR_CHAPTERS


def test_csharp_wrap_code():
    snippet = 'Console.WriteLine("Hello C#");'
    wrapped = wrap_student_csharp_code(snippet)
    assert "public class Program" in wrapped
    assert "public static void Main" in wrapped
    assert snippet in wrapped


def test_csharp_run_snippet():
    res = run_student_csharp_code('Console.WriteLine("C# Running");')
    assert res.success is True
    assert res.output == "C# Running"


def test_csharp_string_concatenation():
    code = """
    string hero = "Yared";
    Console.WriteLine("Hero: " + hero);
    """
    res = run_student_csharp_code(code)
    assert res.success is True
    assert res.output == "Hero: Yared"



def test_csharp_semicolon_error():
    res = run_student_csharp_code('Console.WriteLine("No Semicolon")')
    assert res.success is False
    assert "Missing Semicolon" in res.friendly_explanation_en
    assert "ሴሚኮለን" in res.friendly_explanation_am


def test_csharp_curriculum_chapters():
    chapters = get_all_tutor_chapters("csharp")
    assert len(chapters) == 7
    assert chapters[0].id == "cs_ch1"
    assert chapters[6].id == "cs_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("cs_ch1")
    assert ch1 is not None
    assert ch1.track == "csharp"

    next_id = get_next_tutor_chapter_id("cs_ch1")
    assert next_id == "cs_ch2"

    last_next = get_next_tutor_chapter_id("cs_ch7")
    assert last_next is None
