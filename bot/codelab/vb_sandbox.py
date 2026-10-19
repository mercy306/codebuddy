"""Safe Visual Basic (.NET) sandbox runner using Microsoft vbc.exe compiler."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

VBC_PATH = "C:/Windows/Microsoft.NET/Framework64/v4.0.30319/vbc.exe"
TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

# Prohibit malicious calls
FORBIDDEN_VB_TOKENS = {
    "Process.Start",
    "Environment.Exit",
    "File.Delete",
    "Directory.Delete",
    "Socket",
    "TcpClient",
    "WebClient",
    "Registry",
    "DllImport",
}

FRIENDLY_VB_ERRORS_EN = {
    "is not declared": (
        "Variable Not Declared: In Visual Basic, variables must be declared using `Dim name As Type` (e.g. `Dim age As Integer = 20`)."
    ),
    "expected 'end if'": (
        "Missing End If: In Visual Basic, every `If` block must be closed with `End If`."
    ),
    "expected 'next'": (
        "Missing Next: In Visual Basic, every `For` loop must end with `Next`."
    ),
    "type mismatch": (
        "Type Mismatch: You attempted to assign a value of the wrong data type."
    ),
}

FRIENDLY_VB_ERRORS_AM = {
    "is not declared": (
        "ተለዋዋጩ አልታወቀም፦ በቪዥዋል ቤዚክ ውስጥ ተለዋዋጮች በ `Dim` መፈጠር አለባቸው (ለምሳሌ፦ `Dim age As Integer = 20`)።"
    ),
    "expected 'end if'": (
        "ያልተዘጋ የIf ትዕዛዝ፦ በቪዥዋል ቤዚክ ውስጥ እያንዳንዱ `If` በ `End If` መዘጋት አለበት።"
    ),
    "expected 'next'": (
        "ያልተዘጋ ሉፕ፦ በቪዥዋል ቤዚክ ውስጥ እያንዳንዱ የ `For` ሉፕ በ `Next` ይጠናቀቃል።"
    ),
    "type mismatch": (
        "የዳታ አይነት አለመጣጣም፦ የተሳሳተ የዳታ አይነት ለመመደብ ሞክረዋል።"
    ),
}


def _get_friendly_vb_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_VB_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_VB_ERRORS_AM[pattern]
    return (
        f"Visual Basic Error:\n{raw_err}",
        f"የቪዥዋል ቤዚክ ስህተት፦\n{raw_err}",
    )


def wrap_student_vb_code(user_code: str) -> str:
    """If student wrote a snippet without Module/Sub Main, wrap it automatically."""
    stripped = user_code.strip()
    if "Module " in stripped and "Sub Main" in stripped:
        return stripped

    return f"""Imports System
Imports System.Collections.Generic

Module Program
    Sub Main()
{user_code}
    End Sub
End Module
"""


def run_student_vb_code(code_str: str) -> ExecutionResult:
    """Compile and execute student Visual Basic code safely using vbc.exe."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Visual Basic code",
            friendly_explanation_en="Please write some Visual Basic code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የቪዥዋል ቤዚክ ኮድ ይጻፉ!",
        )

    for token in FORBIDDEN_VB_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    full_source = wrap_student_vb_code(raw)

    with tempfile.TemporaryDirectory() as td:
        vb_file = os.path.join(td, "Program.vb")
        exe_file = os.path.join(td, "Program.exe")

        try:
            with open(vb_file, "w", encoding="utf-8") as f:
                f.write(full_source)

            # Compile with vbc.exe
            compile_proc = subprocess.run(
                [VBC_PATH, "/nologo", f"/out:{exe_file}", vb_file],
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                encoding="utf-8",
                errors="replace",
            )

            if compile_proc.returncode != 0:
                raw_err = compile_proc.stdout.strip() or compile_proc.stderr.strip()
                raw_err = re.sub(r"[A-Za-z]:\\[^\n]+\.vb", "Program.vb", raw_err)
                en_expl, am_expl = _get_friendly_vb_error(raw_err)
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
                en_expl, am_expl = _get_friendly_vb_error(stderr)
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
                friendly_explanation_en="Your Visual Basic program took too long to run. Did you create an infinite loop?",
                friendly_explanation_am="የቪዥዋል ቤዚክ ፕሮግራምዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ ፈጥረው ይሆን?",
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error_message=str(e),
                friendly_explanation_en=f"Execution error: {e}",
                friendly_explanation_am=f"የማስኬጃ ስህተት፦ {e}",
            )
