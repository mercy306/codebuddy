"""Safe sandboxed JavaScript code executor using Node.js."""

from __future__ import annotations

import subprocess
import shutil
import re
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult


FORBIDDEN_JS_PATTERNS = [
    r"\brequire\b",
    r"\bimport\b",
    r"\bprocess\b",
    r"\bchild_process\b",
    r"\bfs\b",
    r"\bhttp\b",
    r"\bhttps\b",
    r"\bnet\b",
    r"\beval\b",
    r"\bFunction\b",
    r"\bglobal\b",
    r"\bglobalThis\b",
    r"\bWebAssembly\b",
    r"\b__proto__\b",
    r"\bprototype\b",
]


def check_js_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan JavaScript code for dangerous modules and prototypes."""
    for pattern in FORBIDDEN_JS_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "")
            err_en = (
                f"🛡️ Safety Check: Using `{clean_word}` is forbidden for security in beginner exercises."
            )
            err_am = (
                f"🛡️ የደህንነት ቁጥጥር፦ በጀማሪ ልምምዶች ላይ `{clean_word}` መጠቀም ለደህንነት ሲባል አይፈቀድም።"
            )
            return False, err_en, err_am
    return True, None, None


def get_friendly_js_error(error_text: str) -> Tuple[str, str]:
    """Translate JavaScript errors into friendly beginner explanations."""
    err_lower = error_text.lower()

    if "syntaxerror" in err_lower:
        if "missing )" in err_lower:
            return (
                "Syntax Error: You forgot a closing parenthesis `)`. Make sure every `(` has a matching `)`!",
                "የአገባብ ስህተት (Syntax Error)፦ የመዝጊያ ቅንፍ `)` ረስተዋል። እያንዳንዱ `(` የሚዘጋበት `)` እንዳለው ያረጋግጡ!",
            )
        if "unexpected token" in err_lower:
            return (
                "Syntax Error: Check your quotation marks `\" \"`, curly braces `{ }`, and semicolons `;`.",
                "የአገባብ ስህተት (Syntax Error)፦ የጥቅስ ምልክቶችን `\" \"` እና የፈረንሳይ ቅንፎችን `{ }` በትክክል መዝጋትዎን ያረጋግጡ።",
            )
        return (
            "Syntax Error: Python and JavaScript need exact punctuation. Check quotes and brackets!",
            "የአገባብ ስህተት (Syntax Error)፦ ጃቫስክሪፕት ጥንቃቄ የተሞላበት ስርአተ-ነጥብ ይፈልጋል። ጥቅሶችን እና ቅንፎችን ያረጋግጡ!",
        )

    if "referenceerror" in err_lower:
        match = re.search(r"(\w+) is not defined", error_text)
        var_name = match.group(1) if match else "A variable"
        return (
            f"Reference Error: `{var_name}` is not defined. Did you declare it with `let {var_name}` first, or misspell it?",
            f"የማጣቀሻ ስህተት (Reference Error)፦ `{var_name}` አልታወቀም። መጀመሪያ በ `let {var_name}` ፈጥረውታል ወይስ የፊደል ግድፈት አለ?",
        )

    if "typeerror" in err_lower:
        return (
            "Type Error: You tried to perform an action on the wrong data type.",
            "የአይነት ስህተት (Type Error)፦ ተገቢ ባልሆነ የመረጃ አይነት ላይ ትዕዛዝ ለመስጠት ሞክረዋል።",
        )

    # General fallback
    first_line = error_text.strip().split("\n")[0] if error_text else "Error"
    return (
        f"JavaScript Error: {first_line}",
        f"የጃቫስክሪፕት ስህተት፦ {first_line}",
    )


def run_student_js_code(code_str: str, timeout_seconds: float = 2.0) -> ExecutionResult:
    """Execute student JavaScript code in a sandboxed Node.js subprocess."""
    node_bin = shutil.which("node")
    if not node_bin:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Node.js is not available on this server.",
            friendly_explanation_en="Node.js runtime is currently unavailable.",
            friendly_explanation_am="የNode.js ማሄጃ በአሁኑ ሰዓት አልተገኘም።",
        )

    # Safety check
    is_safe, err_en, err_am = check_js_safety(code_str)
    if not is_safe:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Security restriction triggered",
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )

    try:
        proc = subprocess.run(
            [node_bin, "--disallow-code-generation-from-strings", "-e", code_str],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            encoding="utf-8",
            errors="replace",
        )

        if proc.returncode == 0:
            return ExecutionResult(
                success=True,
                output=proc.stdout,
            )

        # Non-zero return code (Error thrown)
        raw_error = proc.stderr.strip()
        err_en, err_am = get_friendly_js_error(raw_error)
        return ExecutionResult(
            success=False,
            output=proc.stdout,
            error_message=raw_error,
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )

    except subprocess.TimeoutExpired:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Execution timed out",
            friendly_explanation_en="⏰ Timeout: Your code took too long to run. Check for infinite loops!",
            friendly_explanation_am="⏰ ጊዜው አልቋል፦ ኮድዎ ረጅም ጊዜ ወስዷል። የማያልቅ ሉፕ (Infinite loop) እንዳይኖር ያረጋግጡ!",
        )
    except Exception as exc:
        return ExecutionResult(
            success=False,
            output="",
            error_message=str(exc),
            friendly_explanation_en=f"Runtime error: {exc}",
            friendly_explanation_am=f"የስራ ሰዓት ስህተት፦ {exc}",
        )
