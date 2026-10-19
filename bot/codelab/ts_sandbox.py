"""Safe TypeScript sandbox runner using Node.js native TypeScript engine."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 3
MAX_OUTPUT_CHARS = 2000

# Security tokens blocked
FORBIDDEN_TS_TOKENS = {
    "child_process",
    "require('fs')",
    'require("fs")',
    "require('child_process')",
    'require("child_process")',
    "process.exit",
    "process.env",
    "process.kill",
    "globalThis.process",
    "eval(",
    "Function(",
    "import('fs')",
    'import("fs")',
    "import('child_process')",
    'import("child_process")',
}

FRIENDLY_TS_ERRORS_EN = {
    "is not defined": (
        "TypeScript cannot find that variable. Check your spelling or ensure you declared it with `let` or `const`."
    ),
    "syntaxerror": (
        "Syntax Error: Check your brackets `{}`, quotes, colons `:`, or commas `,`."
    ),
    "unexpected token": (
        "Syntax Error: Check your brackets `{}`, quotes, colons `:`, or commas `,`."
    ),
    "missing ) after argument list": (
        "Missing Closing Parenthesis: You forgot to close a `)` at the end of `console.log(...)`."
    ),
    "type annotation": (
        "Type Error: TypeScript found an invalid type annotation. Check your `: string`, `: number`, or `: boolean` syntax."
    ),
}

FRIENDLY_TS_ERRORS_AM = {
    "is not defined": (
        "ያልታወቀ ተለዋዋጭ፦ የተየቡትን ቃል ፊደላት ያረጋግጡ፤ እንዲሁም ተለዋዋጩን በ `let` ወይም `const` ማስጀመርዎን ያረጋግጡ።"
    ),
    "syntaxerror": (
        "የሰዋሰው ስህተት (Syntax Error)፦ ቅንፎችን `{}`, ጥቅሶችን, ኮለን `:`, ወይም ኮማ `,` በትክክል መጻፍዎን ያረጋግጡ።"
    ),
    "unexpected token": (
        "የሰዋሰው ስህተት (Syntax Error)፦ ቅንፎችን `{}`, ጥቅሶችን, ኮለን `:`, ወይም ኮማ `,` በትክክል መጻፍዎን ያረጋግጡ።"
    ),
    "missing ) after argument list": (
        "ያልተዘጋ ቅንፍ፦ የ `console.log(...)` መዝጊያ ቅንፍ `)` መርሳትዎን ያረጋግጡ።"
    ),
    "type annotation": (
        "የዳታ አይነት ስህተት፦ የታይፕ አጻጻፍዎን ያረጋግጡ (ለምሳሌ፦ `: string`, `: number`, ወይም `: boolean`)።"
    ),
}



def _get_friendly_ts_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_TS_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_TS_ERRORS_AM[pattern]
    return (
        f"TypeScript Error:\n{raw_err}",
        f"የታይፕስክሪፕት ስህተት፦\n{raw_err}",
    )


def run_student_ts_code(code_str: str) -> ExecutionResult:
    """Execute student TypeScript code safely using Node's native strip-types engine."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty TypeScript code",
            friendly_explanation_en="Please write some TypeScript code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የታይፕስክሪፕት ኮድ ይጻፉ!",
        )

    for token in FORBIDDEN_TS_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    temp_file = None
    try:
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".ts",
            delete=False,
            encoding="utf-8",
        )
        temp_file.write(raw)
        temp_file.close()

        result = subprocess.run(
            [
                "node",
                "--experimental-strip-types",
                "--disallow-code-generation-from-strings",
                temp_file.name,
            ],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0 or (stderr and not stdout):
            clean_err = stderr or "TypeScript execution failed."
            # Remove full temp paths
            clean_err = re.sub(r"[A-Za-z]:\\[^\n]+\.ts", "exercise.ts", clean_err)
            en_expl, am_expl = _get_friendly_ts_error(clean_err)
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
            friendly_explanation_en="Your TypeScript program took too long to run. Did you create an infinite loop?",
            friendly_explanation_am="ፕሮግራምዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ ፈጥረው ይሆን?",
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
        if temp_file and os.path.exists(temp_file.name):
            try:
                os.unlink(temp_file.name)
            except OSError:
                pass
