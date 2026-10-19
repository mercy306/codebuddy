"""Safe C# sandbox runner using Microsoft Visual C# Compiler (csc.exe)."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

CSC_PATH = "C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe"
TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

# Prohibit malicious system calls
FORBIDDEN_CSHARP_TOKENS = {
    "Process.Start",
    "Environment.Exit",
    "File.Write",
    "File.Delete",
    "Directory.Delete",
    "Socket",
    "TcpClient",
    "WebClient",
    "HttpClient",
    "Registry",
    "DllImport",
}

FRIENDLY_CSHARP_ERRORS_EN = {
    "does not exist in the current context": (
        "C# cannot find that variable or name. Check your spelling and make sure it was declared first."
    ),
    "; expected": (
        "Missing Semicolon: Every statement in C# must end with a semicolon `;`."
    ),
    "} expected": (
        "Missing Closing Bracket: Check that every opening brace `{` has a matching closing brace `}`."
    ),
    ") expected": (
        "Missing Parenthesis: Check that every opening parenthesis `(` has a matching closing `)`."
    ),
    "cannot implicitly convert type": (
        "Type Mismatch: C# is strongly typed! You tried to assign one data type to a different type."
    ),
    "index was outside the bounds": (
        "Index Out of Bounds: You tried to access an item position that does not exist in the array."
    ),
}

FRIENDLY_CSHARP_ERRORS_AM = {
    "does not exist in the current context": (
        "ያልታወቀ ስም ወይም ተለዋዋጭ፦ የተየቡትን ቃል ፊደላት ያረጋግጡ፤ እንዲሁም ተለዋዋጩ አስቀድሞ መፈጠሩን ያረጋግጡ።"
    ),
    "; expected": (
        "ሴሚኮለን `;` ጎድሏል፦ በC# ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን `;` መጨረስ አለበት።"
    ),
    "} expected": (
        "ያልተዘጋ ቅንፍ፦ እያንዳንዱ የተከፈተ የፈረንሳይ ቅንፍ `{` በትክክል መዘጋቱን `}` ያረጋግጡ።"
    ),
    ") expected": (
        "ያልተዘጋ ቅንፍ፦ እያንዳንዱ የተከፈተ ክብ ቅንፍ `(` በትክክል መዘጋቱን `)` ያረጋግጡ።"
    ),
    "cannot implicitly convert type": (
        "የዳታ አይነት አለመጣጣም (Type Mismatch)፦ የተሳሳተ የዳታ አይነት ለመመደብ ሞክረዋል።"
    ),
    "index was outside the bounds": (
        "የዝርዝር ወሰን አልፏል፦ በዝርዝሩ (Array) ውስጥ የሌለን ቦታ ለማግኘት ሞክረዋል።"
    ),
}


def _get_friendly_csharp_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_CSHARP_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_CSHARP_ERRORS_AM[pattern]
    return (
        f"C# Error:\n{raw_err}",
        f"የC# ስህተት፦\n{raw_err}",
    )


def wrap_student_csharp_code(user_code: str) -> str:
    """If student wrote a snippet without class/Main wrapper, wrap it automatically."""
    stripped = user_code.strip()
    if "class " in stripped and "Main(" in stripped:
        return stripped

    return f"""using System;
using System.Collections.Generic;

public class Program {{
    public static void Main() {{
{user_code}
    }}
}}
"""


def run_student_csharp_code(code_str: str) -> ExecutionResult:
    """Compile and execute student C# code safely using csc.exe."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty C# code",
            friendly_explanation_en="Please write some C# code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የC# ኮድ ይጻፉ!",
        )

    # Check for forbidden security tokens
    for token in FORBIDDEN_CSHARP_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    full_source = wrap_student_csharp_code(raw)

    with tempfile.TemporaryDirectory() as td:
        cs_file = os.path.join(td, "Program.cs")
        exe_file = os.path.join(td, "Program.exe")

        try:
            with open(cs_file, "w", encoding="utf-8") as f:
                f.write(full_source)

            # Compile with csc.exe
            compile_proc = subprocess.run(
                [CSC_PATH, "/nologo", f"/out:{exe_file}", cs_file],
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                encoding="utf-8",
                errors="replace",
            )

            if compile_proc.returncode != 0:
                raw_err = compile_proc.stdout.strip() or compile_proc.stderr.strip()
                # Clean up file paths from error text
                raw_err = re.sub(r"[A-Za-z]:\\[^\n]+\.cs", "Program.cs", raw_err)
                en_expl, am_expl = _get_friendly_csharp_error(raw_err)
                return ExecutionResult(
                    success=False,
                    output="",
                    error_message=raw_err,
                    friendly_explanation_en=en_expl,
                    friendly_explanation_am=am_expl,
                )

            # Run compiled executable
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

            if run_proc.returncode != 0 and stderr:
                en_expl, am_expl = _get_friendly_csharp_error(stderr)
                return ExecutionResult(
                    success=False,
                    output="",
                    error_message=stderr,
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
                friendly_explanation_en="Your C# program took too long to run. Did you create an infinite loop (`while (true)`)?",
                friendly_explanation_am="የC# ፕሮግራምዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ (`while (true)`) ፈጥረው ይሆን?",
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error_message=str(e),
                friendly_explanation_en=f"Execution error: {e}",
                friendly_explanation_am=f"የማስኬጃ ስህተት፦ {e}",
            )
