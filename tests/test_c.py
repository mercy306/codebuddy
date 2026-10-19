"""Unit and integration tests for the C language sandbox runner and curriculum."""

import pytest
from bot.codelab.c_sandbox import run_student_c_code, wrap_student_c_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_c import C_TUTOR_CHAPTERS


def test_c_wrap_code_snippet():
    snippet = 'printf("Hello C!\\n");'
    wrapped = wrap_student_c_code(snippet)
    assert "#include <stdio.h>" in wrapped
    assert "int main(void)" in wrapped
    assert snippet in wrapped


def test_c_run_simple_snippet():
    res = run_student_c_code('printf("Hello C!\\n");')
    assert res.success is True
    assert "Hello C!" in res.output


def test_c_typed_variables_and_format_specifiers():
    code = """
    int score = 95;
    printf("Score: %d\\n", score);
    """
    res = run_student_c_code(code)
    assert res.success is True
    assert res.output == "Score: 95"


def test_c_arithmetic_math():
    code = """
    int a = 45;
    int b = 55;
    printf("%d\\n", a + b);
    """
    res = run_student_c_code(code)
    assert res.success is True
    assert res.output == "100"


def test_c_if_condition():
    code = """
    int temp = 30;
    if (temp > 25) {
        printf("Warm\\n");
    }
    """
    res = run_student_c_code(code)
    assert res.success is True
    assert res.output == "Warm"


def test_c_array_indexing():
    code = """
    int nums[3] = {10, 20, 30};
    printf("%d\\n", nums[1]);
    """
    res = run_student_c_code(code)
    assert res.success is True
    assert res.output == "20"


def test_c_full_program_with_functions():
    code = """
    #include <stdio.h>

    int addBonus(int score) {
        return score + 10;
    }

    int main(void) {
        printf("Final: %d\\n", addBonus(90));
        return 0;
    }
    """
    res = run_student_c_code(code)
    assert res.success is True
    assert res.output == "Final: 100"


def test_c_syntax_error_handling():
    code = 'printf("Missing semicolon")'  # no semicolon
    res = run_student_c_code(code)
    assert res.success is False
    assert "Missing Semicolon" in res.friendly_explanation_en
    assert "ሴሚኮለን `;` ጎድሏል" in res.friendly_explanation_am


def test_c_curriculum_chapters():
    chapters = get_all_tutor_chapters("c")
    assert len(chapters) == 7
    assert chapters[0].id == "c_ch1"
    assert chapters[6].id == "c_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("c_ch1")
    assert ch1 is not None
    assert ch1.track == "c"

    next_id = get_next_tutor_chapter_id("c_ch1")
    assert next_id == "c_ch2"

    last_next = get_next_tutor_chapter_id("c_ch7")
    assert last_next is None
