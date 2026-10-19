"""Unit and integration tests for the Java sandbox runner and curriculum."""

import pytest
from bot.codelab.java_sandbox import run_student_java_code, wrap_student_java_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_java import JAVA_TUTOR_CHAPTERS


def test_java_wrap_student_code():
    snippet = 'System.out.println("Hello");'
    wrapped = wrap_student_java_code(snippet)
    assert "public class Main" in wrapped
    assert "public static void main" in wrapped
    assert snippet in wrapped


def test_java_run_snippet():
    res = run_student_java_code('System.out.println("Java Runs!");')
    assert res.success is True
    assert res.output == "Java Runs!"


def test_java_variables_and_math():
    code = """
    int a = 15;
    int b = 35;
    System.out.println(a + b);
    """
    res = run_student_java_code(code)
    assert res.success is True
    assert res.output == "50"


def test_java_semicolon_error():
    res = run_student_java_code('System.out.println("Missing semi")')
    assert res.success is False
    assert "Missing Semicolon" in res.friendly_explanation_en
    assert "ሴሚኮለን" in res.friendly_explanation_am


def test_java_curriculum_chapters():
    chapters = get_all_tutor_chapters("java")
    assert len(chapters) == 7
    assert chapters[0].id == "java_ch1"
    assert chapters[6].id == "java_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("java_ch1")
    assert ch1 is not None
    assert ch1.track == "java"

    next_id = get_next_tutor_chapter_id("java_ch1")
    assert next_id == "java_ch2"

    last_next = get_next_tutor_chapter_id("java_ch7")
    assert last_next is None
