"""Safe Linux Bash script sandbox runner using Git Bash."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

BASH_PATH = r"C:\Program Files\Git\bin\bash.exe"
TIMEOUT_SECONDS = 3
MAX_OUTPUT_CHARS = 2000

# Prohibit malicious commands
FORBIDDEN_BASH_TOKENS = {
    "rm -rf",
    "mkfs",
    ":(){ :|:& };:",
    "> /dev/sd",
    "dd if=",
    "chmod -R 777 /",
    "chown -R",
    "shutdown",
    "reboot",
}

FRIENDLY_BASH_ERRORS_EN = {
    "command not found": (
        "Command Not Found: Check your command spelling (e.g. `echo`, `for`, `if`)."
    ),
    "syntax error near unexpected token": (
        "Syntax Error: Check your `then`, `fi`, `do`, `done`, or semicolon `;` formatting."
    ),
    "unexpected EOF while looking for matching": (
        "Unclosed Quotes: You opened a quote `'` or `\"` but didn't close it."
    ),
    "unary operator expected": (
        "Missing Variable Value: In `[ $var -gt 0 ]`, the variable was empty. Check that you set it first."
    ),
    "syntax error: unexpected end of file": (
        "Incomplete Script: You opened an `if` without `fi`, or a `for` loop without `done`."
    ),
}

FRIENDLY_BASH_ERRORS_AM = {
    "command not found": (
        "ትዕዛዙ አልተገኘም (Command not found)፦ የትዕዛዙን ፊደላት ያረጋግጡ (ለምሳሌ፦ `echo`, `for`, `if`)።"
    ),
    "syntax error near unexpected token": (
        "የሰዋሰው ስህተት (Syntax Error)፦ `then`, `fi`, `do`, `done`, ወይም ሴሚኮለን `;` በትክክል መጻፋቸውን ያረጋግጡ።"
    ),
    "unexpected EOF while looking for matching": (
        "ያልተዘጋ ጥቅስ፦ የከፈቱትን ጥቅስ `'` ወይም `\"` መዝጋትዎን ያረጋግጡ።"
    ),
    "unary operator expected": (
        "ባዶ ተለዋዋጭ፦ በ `[ $var -gt 0 ]` ውስጥ ተለዋዋጩ ባዶ ሆኗል። አስቀድመው እሴት መስጠትዎን ያረጋግጡ።"
    ),
    "syntax error: unexpected end of file": (
        "ያልተጠናቀቀ ስክሪፕት፦ የ `if` ትዕዛዝዎን በ `fi`፣ ወይም የ `for` ሉፕዎን በ `done` መዝጋትዎን ያረጋግጡ።"
    ),
}


def _get_friendly_bash_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_BASH_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_BASH_ERRORS_AM[pattern]
    return (
        f"Bash Error:\n{raw_err}",
        f"የባሽ ስህተት፦\n{raw_err}",
    )


def run_student_bash_code(code_str: str) -> ExecutionResult:
    """Execute student Linux Bash commands safely using Git Bash."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Bash script",
            friendly_explanation_en="Please write some Bash commands before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የባሽ (Bash) ትዕዛዞችን ይጻፉ!",
        )

    for token in FORBIDDEN_BASH_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    temp_sh = None
    try:
        # Write script to temporary file with LF line endings
        temp_sh = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".sh",
            delete=False,
            newline="\n",
            encoding="utf-8",
        )
        temp_sh.write(raw + "\n")
        temp_sh.close()

        result = subprocess.run(
            [BASH_PATH, temp_sh.name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0 or (stderr and not stdout):
            clean_err = stderr or "Bash script failed."
            clean_err = re.sub(r"[A-Za-z]:\\[^\n]+\.sh", "script.sh", clean_err)
            en_expl, am_expl = _get_friendly_bash_error(clean_err)
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
            friendly_explanation_en="Your Bash script took too long to run. Did you create an infinite loop (`while true`)?",
            friendly_explanation_am="የባሽ ስክሪፕትዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ ፈጥረው ይሆን?",
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
        if temp_sh and os.path.exists(temp_sh.name):
            try:
                os.unlink(temp_sh.name)
            except OSError:
                pass
