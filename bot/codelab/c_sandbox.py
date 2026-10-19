"""Safe sandboxed C code compiler and executor using zig cc / clang with friendly bilingual errors."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult

DEFAULT_ZIG_PATHS = [
    r"C:\Users\bsd\AppData\Local\Microsoft\WinGet\Packages\zig.zig_Microsoft.Winget.Source_8wekyb3d8bbwe\zig-x86_64-windows-0.17.0\zig.exe",
]
TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

FORBIDDEN_C_TOKENS = {
    "system(",
    "fork(",
    "exec(",
    "execl(",
    "execv(",
    "popen(",
    "remove(",
    "unlink(",
    "socket(",
    "kill(",
}

FRIENDLY_C_ERRORS_EN = {
    "expected ';'": (
        "Missing Semicolon: Every statement in C must end with a semicolon `;`."
    ),
    "use of undeclared identifier": (
        "Undeclared Variable: In C, you must specify the type before using a variable (e.g. `int score = 100;`)."
    ),
    "format specifies type": (
        "Format Specifier Mismatch: Check that `%d` is used for integers, `%f` for decimals, and `%s` for strings in `printf`."
    ),
    "implicit declaration of function 'printf'": (
        "Missing Header: Remember to include `<stdio.h>` to use `printf()`."
    ),
    "expected '}'": (
        "Unclosed Curly Brace: Make sure every `{` has a matching closing `}`."
    ),
    "expected ')'": (
        "Unclosed Parenthesis: Make sure every `(` has a matching closing `)`."
    ),
}

FRIENDLY_C_ERRORS_AM = {
    "expected ';'": (
        "ሴሚኮለን `;` ጎድሏል፦ በ C ቋንቋ ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን መጨረስ አለበት።"
    ),
    "use of undeclared identifier": (
        "ተለዋዋጩ አልታወቀም፦ በ C ውስጥ ተለዋዋጭ ከመጠቀምዎ በፊት አይነቱን መግለጽ አለብዎት (ለምሳሌ፦ `int score = 100;`)።"
    ),
    "format specifies type": (
        "የፎርማት ምልክት ስህተት፦ በ `printf` ውስጥ ለሙሉ ቁጥር `%d`፣ ለአስርዮሽ `%f`፣ ለጽሁፍ `%s` መጠቀሙን ያረጋግጡ።"
    ),
    "implicit declaration of function 'printf'": (
        "የላይብረሪ ስህተት፦ `printf()` ለመጠቀም `#include <stdio.h>` መካተቱን ያረጋግጡ።"
    ),
    "expected '}'": (
        "ያልተዘጋ የፈረንሳይ ቅንፍ፦ እያንዳንዱ `{` የሚዘጋበት `}` እንዳለው ያረጋግጡ።"
    ),
    "expected ')'": (
        "ያልተዘጋ ቅንፍ፦ እያንዳንዱ `(` የሚዘጋበት `)` እንዳለው ያረጋግጡ።"
    ),
}


def get_c_compiler_executable() -> Optional[Tuple[str, str]]:
    """Return compiler path and mode ('zig_cc' or 'clang' or 'gcc')."""
    which_gcc = shutil.which("gcc")
    if which_gcc:
        return which_gcc, "gcc"
    which_clang = shutil.which("clang")
    if which_clang:
        return which_clang, "clang"

    for path in DEFAULT_ZIG_PATHS:
        if os.path.isfile(path):
            return path, "zig_cc"

    which_zig = shutil.which("zig")
    if which_zig:
        return which_zig, "zig_cc"

    return None


def wrap_student_c_code(code_str: str) -> str:
    """Ensure student snippet is a complete compilable C program."""
    raw = code_str.strip()
    if "main(" in raw:
        # User defined their own main function
        headers = ""
        if "#include <stdio.h>" not in raw:
            headers += "#include <stdio.h>\n"
        if "#include <stdlib.h>" not in raw:
            headers += "#include <stdlib.h>\n"
        return headers + raw + "\n"

    # Wrap snippet inside standard main()
    return (
        "#include <stdio.h>\n"
        "#include <stdlib.h>\n"
        "#include <string.h>\n\n"
        "int main(void) {\n"
        f"    {raw}\n"
        "    return 0;\n"
        "}\n"
    )


def _get_friendly_c_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_C_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_C_ERRORS_AM[pattern]
    return (
        f"C Compiler Error:\n{raw_err}",
        f"የሲ (C) ማቀናበሪያ ስህተት፦\n{raw_err}",
    )


def run_student_c_code(code_str: str) -> ExecutionResult:
    """Compile and execute student C code."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty C code",
            friendly_explanation_en="Please write some C code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የሲ (C) ኮድ ይጻፉ!",
        )

    for token in FORBIDDEN_C_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    compiler_info = get_c_compiler_executable()
    if not compiler_info:
        return ExecutionResult(
            success=False,
            output="",
            error_message="C compiler not found",
            friendly_explanation_en="C compiler is currently not available on this server.",
            friendly_explanation_am="የሲ (C) ኮምፓይለር በዚህ ሰርቨር ላይ ለጊዜው አልተገኘም።",
        )

    compiler_path, mode = compiler_info
    full_source = wrap_student_c_code(raw)

    temp_dir = tempfile.mkdtemp()
    c_source_file = os.path.join(temp_dir, "student.c")
    exe_file = os.path.join(temp_dir, "student.exe")

    try:
        with open(c_source_file, "wb") as f:
            f.write(full_source.encode("utf-8"))

        if mode == "zig_cc":
            compile_cmd = [compiler_path, "cc", c_source_file, "-o", exe_file]
        else:
            compile_cmd = [compiler_path, c_source_file, "-o", exe_file]

        comp_proc = subprocess.run(
            compile_cmd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        if comp_proc.returncode != 0:
            clean_err = re.sub(r"C:[^\n:]+student\.c:", "Line ", comp_proc.stderr)
            en_msg, am_msg = _get_friendly_c_error(comp_proc.stderr)
            return ExecutionResult(
                success=False,
                output="",
                error_message=clean_err,
                friendly_explanation_en=en_msg,
                friendly_explanation_am=am_msg,
            )

        run_proc = subprocess.run(
            [exe_file],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = run_proc.stdout.strip()
        stderr = run_proc.stderr.strip()

        if run_proc.returncode != 0:
            clean_err = stderr or f"Process crashed with exit code {run_proc.returncode}"
            return ExecutionResult(
                success=False,
                output="",
                error_message=clean_err,
                friendly_explanation_en="Runtime Error: The program crashed during execution (e.g., segment fault or division by zero).",
                friendly_explanation_am="የማስኬድ ስህተት፦ ፕሮግራሙ በሚሰራበት ጊዜ ተቋርጧል (ለምሳሌ፦ ዜሮ ማካፈል ወይም የሜሞሪ ስህተት)።",
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
            error_message="C execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! If you wrote a loop, check that it can terminate.",
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
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
        except OSError:
            pass
