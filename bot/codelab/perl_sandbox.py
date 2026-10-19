"""Safe Perl 5 sandbox runner using Git Perl with friendly bilingual errors."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

PERL_PATH = r"C:\Program Files\Git\usr\bin\perl.exe"
TIMEOUT_SECONDS = 3
MAX_OUTPUT_CHARS = 2000

# Prohibit malicious calls
FORBIDDEN_PERL_TOKENS = {
    "system(",
    "exec(",
    "unlink",
    "rmdir",
    "`",
    "qx/",
    "qx{",
    "qx(",
    "socket",
    "fork",
    "kill",
}

FRIENDLY_PERL_ERRORS_EN = {
    "syntax error": (
        "Perl Syntax Error: Check your keywords, semicolons `;`, or variable prefixes (`$`, `@`, `%`)."
    ),
    "near \"print": (
        "Missing Semicolon: In Perl, every statement must end with a semicolon `;`."
    ),
    "requires explicit package name": (
        "Undeclared Variable: Declare your variables using `my $var` (e.g. `my $score = 100;`)."
    ),
    "unquoted string": (
        "Unquoted String: Text in Perl must be enclosed in quotes `\"...\"` or `'...'`."
    ),
    "can't locate object method": (
        "Perl Syntax Error: Make sure your text strings are surrounded with quotes `\"...\"` and statements end with semicolons `;`."
    ),
}

FRIENDLY_PERL_ERRORS_AM = {
    "syntax error": (
        "የፐርል የሰዋሰው ስህተት (Syntax Error)፦ ቃላቶችን፣ ሴሚኮለን `;` ወይም የተለዋዋጭ መለያዎችን (`$`, `@`, `%`) ያረጋግጡ።"
    ),
    "near \"print": (
        "ሴሚኮለን `;` ጎድሏል፦ በፐርል ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን መጨረስ አለበት።"
    ),
    "requires explicit package name": (
        "ተለዋዋጩ አልታወቀም፦ ተለዋዋጮችን በ `my $` ያስጀምሩ (ለምሳሌ፦ `my $score = 100;`)።"
    ),
    "unquoted string": (
        "ጥቅስ የሌለው ጽሁፍ፦ በፐርል ውስጥ ጽሁፎች በጥቅስ ምልክት `\"...\"` ወይም `'...'` ውስጥ መሆን አለባቸው።"
    ),
    "can't locate object method": (
        "የፐርል የሰዋሰው ስህተት፦ ጽሁፎችን በጥቅስ ምልክት `\"...\"` ማቀፍዎን እና መስመሩን በሴሚኮለን `;` መዝጋትዎን ያረጋግጡ።"
    ),
}


def _get_friendly_perl_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_PERL_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_PERL_ERRORS_AM[pattern]
    return (
        f"Perl Error:\n{raw_err}",
        f"የፐርል ስህተት፦\n{raw_err}",
    )


def run_student_perl_code(code_str: str) -> ExecutionResult:
    """Execute student Perl 5 code safely using perl.exe."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Perl code",
            friendly_explanation_en="Please write some Perl code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የፐርል (Perl) ኮድ ይጻፉ!",
        )

    for token in FORBIDDEN_PERL_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    temp_pl = None
    try:
        temp_pl = tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".pl",
            delete=False,
        )
        temp_pl.write(raw.encode("utf-8") + b"\n")
        temp_pl.close()

        result = subprocess.run(
            [PERL_PATH, temp_pl.name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0 or (stderr and not stdout):
            clean_err = stderr or "Perl execution failed."
            clean_err = re.sub(r"[A-Za-z]:\\[^\n]+\.pl", "script.pl", clean_err)
            en_expl, am_expl = _get_friendly_perl_error(clean_err)
            return ExecutionResult(
                success=False,
                output="",
                error_message=clean_err,
                friendly_explanation_en=en_expl,
                friendly_explanation_am=am_expl,
            )

        if len(stdout) > MAX_OUTPUT_CHARS:
            stdout = stdout[:MAX_OUTPUT_CHARS] + "\n...(output truncated)"

        return ExecutionResult(
            success=True,
            output=stdout,
        )

    except subprocess.TimeoutExpired:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Execution timed out",
            friendly_explanation_en="Your Perl program took too long to run. Did you create an infinite loop (`while (1)`)?",
            friendly_explanation_am="የፐርል ፕሮግራምዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ ፈጥረው ይሆን?",
        )
    except Exception as e:
        return ExecutionResult(
            success=False,
            output="",
            error_message=str(e),
            friendly_explanation_en=f"Execution error: {e}",
            friendly_explanation_am=f"የማስኬጃ ስህተት፦ {e}",
        )
    finally:
        if temp_pl and os.path.exists(temp_pl.name):
            try:
                os.unlink(temp_pl.name)
            except OSError:
                pass
