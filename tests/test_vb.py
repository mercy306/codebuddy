"""Unit and integration tests for the Visual Basic sandbox runner and curriculum."""

import pytest
from bot.codelab.vb_sandbox import run_student_vb_code, wrap_student_vb_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_vb import VB_TUTOR_CHAPTERS


def test_vb_wrap_code():
    snippet = 'Console.WriteLine("Hello VB")'
    wrapped = wrap_student_vb_code(snippet)
    assert "Module Program" in wrapped
    assert "Sub Main()" in wrapped
    assert snippet in wrapped


def test_vb_run_snippet():
    res = run_student_vb_code('Console.WriteLine("Visual Basic Running")')
    assert res.success is True
    assert res.output == "Visual Basic Running"


def test_vb_variables_and_math():
    code = """
    Dim a As Integer = 25
    Dim b As Integer = 75
    Console.WriteLine(a + b)
    """
    res = run_student_vb_code(code)
    assert res.success is True
    assert res.output == "100"


def test_vb_if_condition():
    code = """
    Dim score As Integer = 90
    If score >= 50 Then
        Console.WriteLine("Pass")
    End If
    """
    res = run_student_vb_code(code)
    assert res.success is True
    assert res.output == "Pass"


def test_vb_error_handling():
    code = "x = 10"  # Missing Dim
    res = run_student_vb_code(code)
    assert res.success is False
    assert "Variable Not Declared" in res.friendly_explanation_en
    assert "ተለዋዋጩ አልታወቀም" in res.friendly_explanation_am


def test_vb_curriculum_chapters():
    chapters = get_all_tutor_chapters("vb")
    assert len(chapters) == 7
    assert chapters[0].id == "vb_ch1"
    assert chapters[6].id == "vb_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("vb_ch1")
    assert ch1 is not None
    assert ch1.track == "vb"

    next_id = get_next_tutor_chapter_id("vb_ch1")
    assert next_id == "vb_ch2"

    last_next = get_next_tutor_chapter_id("vb_ch7")
    assert last_next is None
