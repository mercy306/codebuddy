"""Unit and integration tests for the PHP sandbox runner and curriculum."""

import pytest
from bot.codelab.php_sandbox import run_student_php_code, wrap_student_php_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_php import PHP_TUTOR_CHAPTERS


def test_php_wrap_code():
    snippet = 'echo "Hello PHP";'
    wrapped = wrap_student_php_code(snippet)
    assert wrapped.startswith("<?php")
    assert snippet in wrapped


def test_php_run_snippet():
    res = run_student_php_code('echo "Hello PHP";')
    assert res.success is True
    assert res.output == "Hello PHP"


def test_php_variables_and_concatenation():
    code = """
    $name = "Abebe";
    echo "Hello " . $name;
    """
    res = run_student_php_code(code)
    assert res.success is True
    assert res.output == "Hello Abebe"


def test_php_math_and_numbers():
    code = """
    $item = 40;
    $shipping = 10;
    echo $item + $shipping;
    """
    res = run_student_php_code(code)
    assert res.success is True
    assert res.output == "50"


def test_php_associative_array():
    code = """
    $member = ["role" => "Editor"];
    echo $member["role"];
    """
    res = run_student_php_code(code)
    assert res.success is True
    assert res.output == "Editor"


def test_php_function_execution():
    code = """
    function makeBadge($user) {
        return "Verified: " . $user;
    }
    echo makeBadge("Liya");
    """
    res = run_student_php_code(code)
    assert res.success is True
    assert res.output == "Verified: Liya"


def test_php_syntax_error_handling():
    code = 'echo "Missing semicolon"'
    res = run_student_php_code(code)
    assert res.success is False
    assert "Missing Closing Bracket or Semicolon" in res.friendly_explanation_en
    assert "የመዝጊያ ቅንፍ ወይም ሴሚኮለን ጎድሏል" in res.friendly_explanation_am


def test_php_curriculum_chapters():
    chapters = get_all_tutor_chapters("php")
    assert len(chapters) == 7
    assert chapters[0].id == "php_ch1"
    assert chapters[6].id == "php_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("php_ch1")
    assert ch1 is not None
    assert ch1.track == "php"

    next_id = get_next_tutor_chapter_id("php_ch1")
    assert next_id == "php_ch2"

    last_next = get_next_tutor_chapter_id("php_ch7")
    assert last_next is None
