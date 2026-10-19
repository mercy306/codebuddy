"""Safe sandboxed PHP code executor using local PHP CLI with bilingual error translations."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult

DEFAULT_PHP_PATHS = [
    r"C:\xampp\php\php.exe",
    r"C:\tools\php\php.exe",
    r"C:\php\php.exe",
]
TIMEOUT_SECONDS = 3
MAX_OUTPUT_CHARS = 2000

FORBIDDEN_PHP_TOKENS = {
    "exec(",
    "system(",
    "passthru(",
    "shell_exec(",
    "proc_open(",
    "popen(",
    "`",
    "eval(",
    "unlink(",
    "rmdir(",
    "curl_exec(",
    "file_get_contents(",
    "file_put_contents(",
    "fopen(",
    "phpinfo(",
}

FRIENDLY_PHP_ERRORS_EN = {
    "syntax error, unexpected end of file": (
        "Missing Closing Bracket or Semicolon: You may have forgotten to close a `{` bracket or add a semicolon `;` at the end."
    ),
    "syntax error, unexpected token": (
        "PHP Syntax Error: Check your semicolons `;`, quotation marks `\"...\"`, and curly brackets `{ }`."
    ),
    "syntax error": (
        "PHP Syntax Error: Check your keywords, semicolons `;`, or variable prefixes (`$`)."
    ),
    "undefined variable": (
        "Undefined Variable: In PHP, variables must start with `$` (e.g., `$score = 100;`)."
    ),
    "call to undefined function": (
        "Function Not Found: Make sure you spelled the function name correctly or defined it first."
    ),
    "division by zero": (
        "Division by Zero: You cannot divide a number by 0 in mathematics or code!"
    ),
}

FRIENDLY_PHP_ERRORS_AM = {
    "syntax error, unexpected end of file": (
        "የመዝጊያ ቅንፍ ወይም ሴሚኮለን ጎድሏል፦ የፈረንሳይ ቅንፍ `{` መዝጋት ወይም በመጨረሻ ላይ ሴሚኮለን `;` ማድረግ ረስተው ሊሆን ይችላል።"
    ),
    "syntax error, unexpected token": (
        "የፒኤችፒ የሰዋሰው ስህተት (Syntax Error)፦ ሴሚኮለን `;`፣ የጥቅስ ምልክቶችን `\"...\"` እና ቅንፎችን `{ }` ያረጋግጡ።"
    ),
    "syntax error": (
        "የፒኤችፒ የሰዋሰው ስህተት፦ ቃላቶችን፣ ሴሚኮለን `;` ወይም የተለዋዋጭ ምልክትን (`$`) ያረጋግጡ።"
    ),
    "undefined variable": (
        "ተለዋዋጩ አልታወቀም፦ በፒኤችፒ ውስጥ ተለዋዋጮች በ `$` መጀመር አለባቸው (ለምሳሌ፦ `$score = 100;`)።"
    ),
    "call to undefined function": (
        "ፈንክሽኑ አልተገኘም፦ የፈንክሽኑን ስም በትክክል መጻፍዎን ወይም አስቀድመው መፍጠርዎን ያረጋግጡ።"
    ),
    "division by zero": (
        "ለዜሮ ማካፈል አይቻልም፦ ማንኛውንም ቁጥር ለ 0 ማካፈል በሂሳብም ሆነ በኮዲንግ የተከለከለ ነው!"
    ),
}


def get_php_executable() -> Optional[str]:
    """Find a usable php.exe path."""
    which_php = shutil.which("php")
    if which_php:
        return which_php
    for path in DEFAULT_PHP_PATHS:
        if os.path.isfile(path):
            return path
    return None


def wrap_student_php_code(code_str: str) -> str:
    """Ensure PHP code has opening <?php tag."""
    raw = code_str.strip()
    if not raw.startswith("<?php") and not raw.startswith("<?"):
        return f"<?php\n{raw}\n"
    return raw + "\n"


def _get_friendly_php_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_PHP_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_PHP_ERRORS_AM[pattern]
    return (
        f"PHP Error:\n{raw_err}",
        f"የፒኤችፒ ስህተት፦\n{raw_err}",
    )


def run_student_php_code(code_str: str) -> ExecutionResult:
    """Execute student PHP code safely using local php.exe."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty PHP code",
            friendly_explanation_en="Please write some PHP code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የፒኤችፒ (PHP) ኮድ ይጻፉ!",
        )

    for token in FORBIDDEN_PHP_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    php_exe = get_php_executable()
    if not php_exe:
        return ExecutionResult(
            success=False,
            output="",
            error_message="PHP runtime not found",
            friendly_explanation_en="PHP runtime is currently not available on this server.",
            friendly_explanation_am="የፒኤችፒ አስተርጓሚ በዚህ ሰርቨር ላይ ለጊዜው አልተገኘም።",
        )

    wrapped_code = wrap_student_php_code(raw)

    temp_php = None
    try:
        temp_php = tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".php",
            delete=False,
        )
        temp_php.write(wrapped_code.encode("utf-8"))
        temp_php.close()

        result = subprocess.run(
            [php_exe, "-d", "display_errors=1", temp_php.name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # Check for PHP errors in stdout or stderr
        combined = (stdout + "\n" + stderr).strip() if stderr else stdout

        if result.returncode != 0 or "Parse error:" in combined or "Fatal error:" in combined:
            raw_err = stderr if stderr else stdout
            # Filter out local temp file paths for cleanliness
            clean_err = re.sub(r"in\s+.*\.php\s+on\s+line", "on line", raw_err)
            en_msg, am_msg = _get_friendly_php_error(clean_err)
            return ExecutionResult(
                success=False,
                output="",
                error_message=clean_err,
                friendly_explanation_en=en_msg,
                friendly_explanation_am=am_msg,
            )

        if len(stdout) > MAX_OUTPUT_CHARS:
            stdout = stdout[:MAX_OUTPUT_CHARS] + "\n...[Output truncated]"

        return ExecutionResult(
            success=True,
            output=stdout,
            error_message=None,
        )

    except subprocess.TimeoutExpired:
        return ExecutionResult(
            success=False,
            output="",
            error_message="PHP execution timed out (>3s)",
            friendly_explanation_en="Execution timed out! If you wrote a loop, check that it can finish.",
            friendly_explanation_am="የኮድ ማስኬጃ ጊዜ አልቋል! ሉፕ (Loop) ጽፈው ከሆነ ማብቂያ እንዳለው ያረጋግጡ።",
        )
    except Exception as e:
        return ExecutionResult(
            success=False,
            output="",
            error_message=str(e),
            friendly_explanation_en=f"Execution error: {e}",
            friendly_explanation_am=f"የማስኬድ ስህተት፦ {e}",
        )
    finally:
        if temp_php and os.path.exists(temp_php.name):
            try:
                os.unlink(temp_php.name)
            except OSError:
                pass
