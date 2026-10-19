"""Unit and integration tests for the Linux Bash sandbox runner and curriculum."""

import pytest
from bot.codelab.bash_sandbox import run_student_bash_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_bash import BASH_TUTOR_CHAPTERS


def test_bash_basic_echo():
    code = 'echo "Linux Bash live"'
    res = run_student_bash_code(code)
    assert res.success is True
    assert res.output == "Linux Bash live"


def test_bash_variables_and_math():
    code = """
    a=20
    b=30
    echo $(( a + b ))
    """
    res = run_student_bash_code(code)
    assert res.success is True
    assert res.output == "50"


def test_bash_if_condition():
    code = """
    score=95
    if [ $score -ge 80 ]; then
        echo "High Score"
    fi
    """
    res = run_student_bash_code(code)
    assert res.success is True
    assert res.output == "High Score"


def test_bash_error_handling():
    code = "fake_cmd_not_existing"
    res = run_student_bash_code(code)
    assert res.success is False
    assert "Command Not Found" in res.friendly_explanation_en
    assert "ትዕዛዙ አልተገኘም" in res.friendly_explanation_am


def test_bash_curriculum_chapters():
    chapters = get_all_tutor_chapters("bash")
    assert len(chapters) == 7
    assert chapters[0].id == "bash_ch1"
    assert chapters[6].id == "bash_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("bash_ch1")
    assert ch1 is not None
    assert ch1.track == "bash"

    next_id = get_next_tutor_chapter_id("bash_ch1")
    assert next_id == "bash_ch2"

    last_next = get_next_tutor_chapter_id("bash_ch7")
    assert last_next is None
