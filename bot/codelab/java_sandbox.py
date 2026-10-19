"""Safe Java sandbox runner executing user code using OpenJDK 21."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import Tuple
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

# Prohibit malicious Java system APIs
FORBIDDEN_JAVA_TOKENS = {
    "ProcessBuilder",
    "Runtime.getRuntime",
    "System.exit",
    "java.io.File",
    "FileInputStream",
    "FileOutputStream",
    "Files.write",
    "Files.delete",
    "Socket",
    "ServerSocket",
    "URL",
    "HttpURLConnection",
}

FRIENDLY_JAVA_ERRORS_EN = {
    "cannot find symbol": (
        "Java cannot find a variable or method you typed. Check your spelling and ensure the variable was declared."
    ),
    "';' expected": (
        "Missing Semicolon: In Java, every statement must end with a semicolon `;`."
    ),
    "; expected": (
        "Missing Semicolon: In Java, every statement must end with a semicolon `;`."
    ),

    "reached end of file while parsing": (
        "Missing Closing Bracket: Check that every opening brace `{` or parenthesis `(` has a matching closing `}` or `)`."
    ),
    "incompatible types": (
        "Type Mismatch: You tried to assign a value of one type to a variable of a different type (e.g. text into an int)."
    ),
    "bad operand types": (
        "Type Error: The operator cannot be applied to these types."
    ),
    "arrayindexoutofboundsexception": (
        "Index Out of Bounds: You tried to access an item position that does not exist in the array."
    ),
}

FRIENDLY_JAVA_ERRORS_AM = {
    "cannot find symbol": (
        "ያልታወቀ ስም ወይም ተለዋዋጭ፦ የተየቡትን ቃል ፊደላት ያረጋግጡ፤ እንዲሁም ተለዋዋጩ አስቀድሞ መፈጠሩን ያረጋግጡ።"
    ),
    "';' expected": (
        "ሴሚኮለን `;` ጎድሏል፦ በጃቫ ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን `;` መጨረስ አለበት።"
    ),
    "; expected": (
        "ሴሚኮለን `;` ጎድሏል፦ በጃቫ ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን `;` መጨረስ አለበት።"
    ),

    "reached end of file while parsing": (
        "ያልተዘጋ ቅንፍ፦ እያንዳንዱ የተከፈተ ቅንፍ `{` ወይም `(` በትክክል መዘጋቱን `}` ወይም `)` ያረጋግጡ።"
    ),
    "incompatible types": (
        "የዳታ አይነት አለመጣጣም (Type Mismatch)፦ የተሳሳተ የዳታ አይነት ለመመደብ ሞክረዋል (ለምሳሌ ጽሁፍን በint ውስጥ)።"
    ),
    "bad operand types": (
        "የአይነት ስህተት፦ ይህ ምልክት ከተጠቀሱት የዳታ አይነቶች ጋር አብሮ አይሰራም።"
    ),
    "arrayindexoutofboundsexception": (
        "የዝርዝር ወሰን አልፏል፦ በዝርዝሩ (Array) ውስጥ የሌለን ቦታ ለማግኘት ሞክረዋል።"
    ),
}


def _get_friendly_java_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_JAVA_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_JAVA_ERRORS_AM[pattern]
    return (
        f"Java Error:\n{raw_err}",
        f"የጃቫ ስህተት፦\n{raw_err}",
    )


def wrap_student_java_code(user_code: str) -> str:
    """If student wrote a snippet without class/main wrapper, wrap it automatically."""
    stripped = user_code.strip()
    if "class " in stripped and "main(" in stripped:
        return stripped

    # Wrap snippet inside standard Main class
    return f"""public class Main {{
    public static void main(String[] args) {{
{user_code}
    }}
}}
"""


def run_student_java_code(code_str: str) -> ExecutionResult:
    """Execute student Java code safely using OpenJDK 21 single-file launcher."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Java code",
            friendly_explanation_en="Please write some Java code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የጃቫ ኮድ ይጻፉ!",
        )

    # Check for forbidden security tokens
    for token in FORBIDDEN_JAVA_TOKENS:
        if token in raw:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Usage of '{token}' is prohibited.",
                friendly_explanation_en=f"For security reasons, `{token}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{token}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    full_source = wrap_student_java_code(raw)

    temp_file = None
    try:
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".java",
            delete=False,
            encoding="utf-8",
        )
        temp_file.write(full_source)
        temp_file.close()

        # Run with java single-file launcher (available in Java 11+)
        result = subprocess.run(
            ["java", temp_file.name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0 or (stderr and not stdout):
            clean_err = stderr or "Java execution failed."
            # Remove full disk path from error traces for cleaner output
            clean_err = re.sub(r"[A-Za-z]:\\[^\n]+\.java", "Main.java", clean_err)
            en_expl, am_expl = _get_friendly_java_error(clean_err)
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
            friendly_explanation_en="Your program took too long to run. Did you create an infinite loop (`while (true)`)?",
            friendly_explanation_am="ፕሮግራምዎ ረጅም ሰዓት ወስዷል። ማለቂያ የሌለው ሉፕ (`while (true)`) ፈጥረው ይሆን?",
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
