"""Unit tests for CodeLab sandboxed code execution and challenge validation."""

import pytest
from bot.codelab.sandbox import run_student_code, check_code_safety
from bot.codelab.challenges import (
    get_all_challenges,
    get_challenge,
    get_next_challenge_id,
    get_total_challenges_count,
)
from bot.database import Database


def test_sandbox_executes_valid_code() -> None:
    """Verify standard valid Python code runs and returns stdout."""
    res = run_student_code('print("Hello, CodeBuddy!")')
    assert res.success is True
    assert res.output.strip() == "Hello, CodeBuddy!"
    assert res.error_message is None


def test_sandbox_executes_math_and_variables() -> None:
    """Verify variables and calculations run properly."""
    code = (
        "x = 25\n"
        "y = 4\n"
        "print(x * y)"
    )
    res = run_student_code(code)
    assert res.success is True
    assert res.output.strip() == "100"


def test_sandbox_executes_loop() -> None:
    """Verify for loops execute correctly."""
    code = (
        "for i in range(3):\n"
        '    print("Python")'
    )
    res = run_student_code(code)
    assert res.success is True
    assert res.output.strip() == "Python\nPython\nPython"


def test_sandbox_friendly_syntax_error() -> None:
    """Syntax errors should return friendly beginner explanations."""
    # Missing closing quotation mark
    bad_code = 'print("Hello)'
    res = run_student_code(bad_code)
    assert res.success is False
    assert res.friendly_explanation_en is not None
    assert "quotation" in res.friendly_explanation_en.lower()


def test_sandbox_forbids_dangerous_imports() -> None:
    """Attempting to import modules must be intercepted safely."""
    bad_code = "import os\nprint(os.getcwd())"
    is_safe, err_en, err_am = check_code_safety(bad_code)
    assert is_safe is False
    assert "Importing" in err_en

    res = run_student_code(bad_code)
    assert res.success is False
    assert "Importing" in res.error_message


def test_sandbox_forbids_open_and_eval() -> None:
    """Attempting to call open() or eval() must be blocked."""
    bad_code = 'f = open("data.txt", "w")'
    is_safe, err_en, _ = check_code_safety(bad_code)
    assert is_safe is False
    assert "open()" in err_en

    res = run_student_code(bad_code)
    assert res.success is False


def test_challenges_content_and_bilingual_parity() -> None:
    """Verify all challenges have complete English and Amharic descriptions."""
    challenges = get_all_challenges()
    assert len(challenges) >= 4
    assert get_total_challenges_count() >= 4

    for ch in challenges:
        assert ch.get_title("en") != ""
        assert ch.get_title("am") != ""
        assert ch.get_prompt("en") != ""
        assert ch.get_prompt("am") != ""
        assert ch.get_hint("en") != ""
        assert ch.get_hint("am") != ""
        assert ch.expected_output != ""


def test_challenge_solution_checker() -> None:
    """Verify solution validation against expected output."""
    ch1 = get_challenge("c1")
    assert ch1 is not None

    # Correct solution
    assert ch1.check_solution("Hello, CodeBuddy!\n") is True
    # Lenient case and punctuation
    assert ch1.check_solution("hello, codebuddy!") is True
    assert ch1.check_solution("Hello, CodeBuddy") is True
    # Incorrect solution
    assert ch1.check_solution("Goodbye\n") is False


def test_sandbox_markdown_fences_and_mobile_features() -> None:
    """Verify code inside markdown fences or with mobile quirks executes cleanly."""
    res_fenced = run_student_code('```python\nprint("Hello")\n```')
    assert res_fenced.success is True
    assert res_fenced.output.strip() == "Hello"

    res_inline = run_student_code('`print("Hello")`')
    assert res_inline.success is True
    assert res_inline.output.strip() == "Hello"

    res_capital = run_student_code('Print("Hello")')
    assert res_capital.success is True
    assert res_capital.output.strip() == "Hello"


def test_sandbox_bare_expressions() -> None:
    """Verify bare strings and arithmetic produce visible output without print()."""
    res_str = run_student_code('"Hello, CodeBuddy!"')
    assert res_str.success is True
    assert res_str.output.strip() == "Hello, CodeBuddy!"

    res_math = run_student_code("25 * 4")
    assert res_math.success is True
    assert res_math.output.strip() == "100"


def test_outputs_match_typo_leniency() -> None:
    """Verify small single-letter typos are forgiven in outputs_match."""
    from bot.codelab.sandbox import outputs_match
    # Typo: 'Welcom' vs 'Welcome'
    assert outputs_match("# Welcom to my website", "# Welcome to My Website") is True
    # Pure numbers must not fuzzy match
    assert outputs_match("10", "20") is False


@pytest.mark.asyncio
async def test_database_code_challenge_persistence(test_db: Database) -> None:
    """Test saving and retrieving completed code writing challenges."""
    user_id = 99123

    # Initial state
    completed = await test_db.get_completed_code_challenges(user_id)
    assert len(completed) == 0

    # Save completion
    await test_db.record_code_challenge_completion(
        user_id=user_id,
        challenge_id="c1",
        submitted_code='print("Hello, CodeBuddy!")',
    )

    completed_after = await test_db.get_completed_code_challenges(user_id)
    assert "c1" in completed_after
    assert len(completed_after) == 1
