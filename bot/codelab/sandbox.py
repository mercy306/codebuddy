"""Safe sandboxed Python code executor for beginner coding challenges."""

from __future__ import annotations

import ast
import io
import sys
from dataclasses import dataclass
from typing import Optional, Tuple

FORBIDDEN_NAMES = {
    "open",
    "exec",
    "eval",
    "__import__",
    "compile",
    "globals",
    "locals",
    "getattr",
    "setattr",
    "delattr",
    "input",
}

FORBIDDEN_MODULES = {
    "os",
    "sys",
    "subprocess",
    "shutil",
    "socket",
    "urllib",
    "requests",
    "pathlib",
}


@dataclass(frozen=True)
class ExecutionResult:
    """Represents the output of running student code."""

    success: bool
    output: str
    error_message: Optional[str] = None
    friendly_explanation_en: Optional[str] = None
    friendly_explanation_am: Optional[str] = None


def check_code_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Inspect AST to prevent imports, file operations, and dangerous builtins."""
    try:
        tree = ast.parse(code_str)
    except SyntaxError as e:
        err_en, err_am = get_friendly_error(e)
        return False, err_en, err_am

    for node in ast.walk(tree):
        # Disallow imports
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return (
                False,
                "Importing external modules is disabled in beginner exercises.",
                "ለጀማሪ መልመጃዎች ሞጁሎችን መጫን (import ማድረግ) አይፈቀድም።",
            )
        # Disallow calls to forbidden functions
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_NAMES:
                return (
                    False,
                    f"Use of `{node.func.id}()` is not allowed in beginner challenges.",
                    f"`{node.func.id}()`ን መጠቀም በዚህ መልመጃ ውስጥ አይፈቀድም።",
                )
            if isinstance(node.func, ast.Attribute) and node.func.attr in FORBIDDEN_NAMES:
                return (
                    False,
                    "Access to dangerous attributes is restricted.",
                    "ይህንን ባህሪ መጠቀም የተከለከለ ነው።",
                )
        # Prevent access to private/dunder attributes like __class__, __subclasses__
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            return (
                False,
                "Access to special internal attributes is not allowed.",
                "ውስጣዊ ባህሪያትን መጠቀም አይፈቀድም።",
            )

    return True, None, None


def get_friendly_error(exc: Exception) -> Tuple[str, str]:
    """Translate common Python exceptions into beginner-friendly explanations."""
    if isinstance(exc, SyntaxError):
        msg = str(exc.msg).lower()
        if "unterminated string" in msg:
            return (
                "You opened a quotation mark `\"` or `'` for text but forgot to close it!",
                "ለጽሁፍ የጥቅስ ምልክት `\"` ከፍተው ሳይዘጉ ቀርተዋል!",
            )
        if "was never closed" in msg:
            return (
                "You opened parentheses `(` but forgot to close them with `)`!",
                "ቅንፍ `(` ከፍተው በ `)` ሳይዘጉ ቀርተዋል!",
            )
        return (
            "Check your spelling, quotes, and parentheses.",
            "ፊደላትን፣ የጥቅስ ምልክቶችን እና ቅንፎችን በትክክል መጻፍዎን ያረጋግጡ።",
        )
    if isinstance(exc, NameError):
        name = getattr(exc, "name", "variable")
        return (
            f"Python doesn't know what `{name}` is. If it's a word, did you forget quotes `\"{name}\"`?",
            f"ፓይተን `{name}` ምን እንደሆነ አላወቀም። ጽሁፍ ከሆነ በጥቅስ ምልክት `\"{name}\"` መጻፍዎን ያረጋግጡ።",
        )
    if isinstance(exc, TypeError):
        return (
            "You tried to combine incompatible types (like adding numbers to plain text without converting).",
            "የማይጣጣሙ የመረጃ አይነቶችን ለማጣመር ሞክረዋል (ለምሳሌ ቁጥርን እና ጽሁፍን ያለ ልወጣ መደመር)።",
        )
    if isinstance(exc, ZeroDivisionError):
        return (
            "In math and code, you cannot divide a number by zero!",
            "በሂሳብም ሆነ በኮዲንግ ማንኛውንም ቁጥር ለዜሮ ማካፈል አይቻልም!",
        )

    return (
        f"An error occurred: {exc}",
        f"ስህተት ተከስቷል፦ {exc}",
    )


def run_student_code(code_str: str) -> ExecutionResult:
    """Safely execute Python code and capture standard output."""
    # 1. Safety verification
    is_safe, err_en, err_am = check_code_safety(code_str)
    if not is_safe:
        return ExecutionResult(
            success=False,
            output="",
            error_message=err_en,
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )

    # 2. Redirect stdout
    captured_stdout = io.StringIO()
    safe_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "sum": sum,
            "max": max,
            "min": min,
        }
    }
    local_scope = {}

    old_stdout = sys.stdout
    sys.stdout = captured_stdout

    try:
        # Compile and execute
        compiled = compile(code_str, "<student_code>", "exec")
        exec(compiled, safe_globals, local_scope)
        sys.stdout = old_stdout
        output = captured_stdout.getvalue()
        return ExecutionResult(
            success=True,
            output=output,
        )
    except Exception as exc:
        sys.stdout = old_stdout
        err_en, err_am = get_friendly_error(exc)
        return ExecutionResult(
            success=False,
            output=captured_stdout.getvalue(),
            error_message=str(exc),
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )
    finally:
        sys.stdout = old_stdout
