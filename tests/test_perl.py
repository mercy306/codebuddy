"""Unit and integration tests for the Perl sandbox runner and curriculum."""

import pytest
from bot.codelab.perl_sandbox import run_student_perl_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_perl import PERL_TUTOR_CHAPTERS


def test_perl_run_snippet():
    res = run_student_perl_code('print "Hello Perl\\n";')
    assert res.success is True
    assert "Hello Perl" in res.output


def test_perl_variables_and_math():
    code = """
my $a = 30;
my $b = 70;
print $a + $b, "\\n";
"""
    res = run_student_perl_code(code)
    assert res.success is True
    assert "100" in res.output


def test_perl_if_condition():
    code = """
my $score = 85;
if ($score >= 50) {
    print "Passed\\n";
}
"""
    res = run_student_perl_code(code)
    assert res.success is True
    assert "Passed" in res.output


def test_perl_syntax_error():
    code = "print Hello World"  # syntax error without quotes / semicolon
    res = run_student_perl_code(code)
    assert res.success is False
    assert "Perl Syntax Error" in res.friendly_explanation_en
    assert "የፐርል የሰዋሰው ስህተት" in res.friendly_explanation_am


def test_perl_curriculum_chapters():
    chapters = get_all_tutor_chapters("perl")
    assert len(chapters) == 7
    assert chapters[0].id == "perl_ch1"
    assert chapters[6].id == "perl_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("perl_ch1")
    assert ch1 is not None
    assert ch1.track == "perl"

    next_id = get_next_tutor_chapter_id("perl_ch1")
    assert next_id == "perl_ch2"

    last_next = get_next_tutor_chapter_id("perl_ch7")
    assert last_next is None
