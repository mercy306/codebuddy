"""Safe HTML code validator and preview generator for beginner exercises."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from typing import List, Tuple, Optional
from bot.codelab.sandbox import ExecutionResult


class BeginnerHTMLParser(HTMLParser):
    """Simple parser to validate tags, nesting, and build a text preview."""

    def __init__(self) -> None:
        super().__init__()
        self.tags_stack: List[str] = []
        self.preview_parts: List[str] = []
        self.has_error: bool = False
        self.error_tag: Optional[str] = None
        self.parsed_tags: List[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        self.parsed_tags.append(tag.lower())
        # Self-closing void tags
        if tag.lower() in ("img", "br", "hr", "input", "meta", "link"):
            if tag.lower() == "img":
                alt = dict(attrs).get("alt", "Image")
                self.preview_parts.append(f" [Image: {alt}] ")
            elif tag.lower() == "input":
                val = dict(attrs).get("placeholder", "Input box")
                self.preview_parts.append(f" [Input: {val}] ")
            return

        self.tags_stack.append(tag.lower())
        if tag.lower() == "h1":
            self.preview_parts.append("\n# ")
        elif tag.lower() == "h2":
            self.preview_parts.append("\n## ")
        elif tag.lower() == "h3":
            self.preview_parts.append("\n### ")
        elif tag.lower() == "p":
            self.preview_parts.append("\n")
        elif tag.lower() == "li":
            self.preview_parts.append("\n• ")
        elif tag.lower() == "button":
            self.preview_parts.append(" [Button: ")

    def handle_endtag(self, tag: str) -> None:
        tag_lower = tag.lower()
        if tag_lower in ("img", "br", "hr", "input", "meta", "link"):
            return

        if not self.tags_stack:
            self.has_error = True
            self.error_tag = tag_lower
            return

        expected = self.tags_stack.pop()
        if expected != tag_lower:
            self.has_error = True
            self.error_tag = tag_lower

        if tag_lower == "button":
            self.preview_parts.append(" ] ")

    def handle_data(self, data: str) -> None:
        cleaned = data.strip()
        if cleaned:
            self.preview_parts.append(cleaned)


def run_student_html_code(code_str: str) -> ExecutionResult:
    """Validate student HTML snippet and render a simulated browser preview."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty HTML submitted",
            friendly_explanation_en="Please type some HTML code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የHTML ኮድ ይጻፉ!",
        )

    # Basic tag existence check
    if not re.search(r"<[a-zA-Z0-9]+.*?>", raw):
        return ExecutionResult(
            success=False,
            output="",
            error_message="No HTML tags found",
            friendly_explanation_en="HTML requires tags enclosed in `<` and `>` brackets (e.g. `<h1>...</h1>`).",
            friendly_explanation_am="HTML በ `<` እና `>` ቅንፎች ውስጥ የሚጻፉ ታጎችን ይፈልጋል (ለምሳሌ፦ `<h1>...</h1>`)።",
        )

    parser = BeginnerHTMLParser()
    try:
        parser.feed(raw)
    except Exception as exc:
        return ExecutionResult(
            success=False,
            output="",
            error_message=str(exc),
            friendly_explanation_en=f"HTML Syntax Error: Check your open and closing `<>` brackets: {exc}",
            friendly_explanation_am=f"የHTML ስህተት፦ የመክፈቻ እና የመዝጊያ `<>` ቅንፎችዎን ያረጋግጡ፦ {exc}",
        )

    if parser.has_error:
        tag = parser.error_tag or "tag"
        return ExecutionResult(
            success=False,
            output="",
            error_message=f"Mismatched closing tag </{tag}>",
            friendly_explanation_en=f"Tag Mismatch: Found `</{tag}>` without a matching opening tag! Every open tag `<tag>` needs `</tag>`.",
            friendly_explanation_am=f"የታግ ስህተት፦ የተዘጋበት `</{tag}>` መክፈቻ ታግ የለውም! እያንዳንዱ `<tag>` የሚዘጋበት `</tag>` ያስፈልገዋል።",
        )

    if parser.tags_stack:
        unclosed = parser.tags_stack[-1]
        return ExecutionResult(
            success=False,
            output="",
            error_message=f"Unclosed tag <{unclosed}>",
            friendly_explanation_en=f"Unclosed Tag: You opened `<{unclosed}>` but forgot to close it with `</{unclosed}>`!",
            friendly_explanation_am=f"ያልተዘጋ ታግ፦ `<{unclosed}>`ን ከፍተው በ `</{unclosed}>` መዝጋት ረስተዋል!",
        )

    preview_text = "".join(parser.preview_parts).strip()
    if not preview_text:
        preview_text = "HTML page rendered successfully!"

    return ExecutionResult(
        success=True,
        output=preview_text,
    )
