"""Safe CSS code validator and preview generator for beginner exercises."""

from __future__ import annotations

import re
from typing import Dict, Optional, Tuple
from bot.codelab.sandbox import ExecutionResult


KNOWN_CSS_PROPERTIES = {
    "color",
    "background",
    "background-color",
    "font-size",
    "font-family",
    "font-weight",
    "text-align",
    "padding",
    "margin",
    "border",
    "border-radius",
    "display",
    "width",
    "height",
    "justify-content",
    "align-items",
    "cursor",
    "box-shadow",
    "opacity",
}


def run_student_css_code(code_str: str) -> ExecutionResult:
    """Validate student CSS rule and output a simulated style card."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty CSS submitted",
            friendly_explanation_en="Please write some CSS rules before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የCSS ህግጋትን ይጻፉ!",
        )

    # Check for matching curly braces
    open_braces = raw.count("{")
    close_braces = raw.count("}")

    if open_braces == 0:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Missing opening brace {",
            friendly_explanation_en="CSS rules require curly braces `{ }` around styles (e.g. `h1 { color: blue; }`).",
            friendly_explanation_am="የCSS ህግጋት በፈረንሳይ ቅንፎች `{ }` ውስጥ መጻፍ አለባቸው (ለምሳሌ፦ `h1 { color: blue; }`)።",
        )

    if open_braces > close_braces:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Unclosed curly brace {",
            friendly_explanation_en="Unclosed Brace: You opened a `{` but forgot to close it with `}`!",
            friendly_explanation_am="ያልተዘጋ ቅንፍ፦ `{` ከፍተው በ `}` መዝጋት ረስተዋል!",
        )

    if close_braces > open_braces:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Extra closing brace }",
            friendly_explanation_en="Extra Brace: Found `}` without a matching opening `{`.",
            friendly_explanation_am="ተጨማሪ ቅንፍ፦ ያለ መክፈቻ የተዘጋ `}` ተገኝቷል።",
        )

    # Extract selector and declarations
    match = re.match(r"^([^{]+)\{(.+)\}$", raw, re.DOTALL)
    if not match:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Invalid CSS rule format",
            friendly_explanation_en="CSS format should be: `selector { property: value; }`",
            friendly_explanation_am="የCSS አጻጻፍ ቅርጽ፦ `selector { property: value; }` መሆን አለበት።",
        )

    selector = match.group(1).strip()
    declarations_raw = match.group(2).strip()

    if not declarations_raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty CSS declaration block",
            friendly_explanation_en="Your CSS block is empty! Add at least one style like `color: blue;` inside `{ }`.",
            friendly_explanation_am="የCSS ብሎክዎ ባዶ ነው! በ `{ }` ውስጥ እንደ `color: blue;` ያለ ስታይል ያስገቡ።",
        )

    # Parse declarations: property: value;
    declarations: Dict[str, str] = {}
    lines = [d.strip() for d in declarations_raw.split(";") if d.strip()]

    for line in lines:
        if ":" not in line:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Missing colon in '{line}'",
                friendly_explanation_en=f"Syntax Error: In CSS, properties and values must be separated by a colon `:` (e.g. `color: red;`). Look at `{line}`.",
                friendly_explanation_am=f"የአገባብ ስህተት፦ በCSS ውስጥ ባህሪ እና እሴት በሁለት ነጥብ `:` መለየት አለባቸው (ለምሳሌ፦ `color: red;`)። `{line}`ን ይመልከቱ።",
            )
        prop, val = line.split(":", 1)
        declarations[prop.strip().lower()] = val.strip()

    # Build stylized preview
    preview_lines = [f"Style applied to <{selector}>:"]
    for prop, val in declarations.items():
        preview_lines.append(f"  - {prop}: {val}")

    return ExecutionResult(
        success=True,
        output="\n".join(preview_lines),
    )
