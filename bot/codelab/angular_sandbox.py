"""Safe sandboxed Angular component evaluator with friendly bilingual error translations."""

from __future__ import annotations

import re
import ast
from typing import Tuple, Optional, Any, Dict
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 3
MAX_OUTPUT_CHARS = 2000

FRIENDLY_ANGULAR_ERRORS_EN = {
    "unclosed_interpolation": (
        "Unclosed Interpolation: Angular template interpolation requires closing double curly braces `}}`."
    ),
    "missing_component_decorator": (
        "Missing Decorator: Angular components require the `@Component({ selector: '...', template: '...' })` decorator."
    ),
    "missing_class": (
        "Missing Component Class: Remember to export your component class (e.g. `export class WelcomeComponent { ... }`)."
    ),
    "jsx_used": (
        "Angular uses HTML templates, not JSX! Place your HTML inside the `template: \\`...\\`` property of `@Component`."
    ),
}

FRIENDLY_ANGULAR_ERRORS_AM = {
    "unclosed_interpolation": (
        "ያልተዘጋ የኢንተርፖሌሽን ምልክት፦ የአንጉላር የጽሁፍ ማሳያ በድርብ የፈረንሳይ ቅንፍ `}}` መዘጋት አለበት።"
    ),
    "missing_component_decorator": (
        "ዴኮሬተር ጎድሏል፦ የአንጉላር ኮምፖነንቶች `@Component({ selector: '...', template: '...' })` ዴኮሬተር ያስፈልጋቸዋል።"
    ),
    "missing_class": (
        "የኮምፖነንት ክላስ ጎድሏል፦ የኮምፖነንት ክላሱን (ለምሳሌ፦ `export class WelcomeComponent { ... }`) ማስቀመጥዎን ያረጋግጡ።"
    ),
    "jsx_used": (
        "አንጉላር JSX አይጠቀምም! የ HTML ታጎችዎን በ `@Component` ውስጥ በ `template: \\`...\\`` ውስጥ ይጻፉ።"
    ),
}


def parse_angular_properties(class_body: str) -> Dict[str, Any]:
    """Extract property values from TypeScript class body."""
    props: Dict[str, Any] = {}

    # Match lines like: name = 'Angular'; or count: number = 42; or isDisabled = true;
    prop_pattern = re.compile(
        r"(?:public\s+|private\s+)?([a-zA-Z0-9_]+)(?:\s*:\s*[^=;]+)?\s*=\s*([^;]+);?"
    )

    for match in prop_pattern.finditer(class_body):
        key = match.group(1).strip()
        raw_val = match.group(2).strip()

        # Parse literals safely
        if raw_val.lower() == "true":
            props[key] = True
        elif raw_val.lower() == "false":
            props[key] = False
        elif raw_val.lower() == "null":
            props[key] = None
        elif (raw_val.startswith("'") and raw_val.endswith("'")) or (raw_val.startswith('"') and raw_val.endswith('"')):
            props[key] = raw_val[1:-1]
        elif (raw_val.startswith("`") and raw_val.endswith("`")):
            props[key] = raw_val[1:-1]
        elif raw_val.startswith("[") and raw_val.endswith("]"):
            try:
                # Parse list safely using AST
                props[key] = ast.literal_eval(raw_val)
            except Exception:
                # Fallback to string items split
                items = [x.strip().strip("'\"`") for x in raw_val[1:-1].split(",") if x.strip()]
                props[key] = items
        else:
            try:
                if "." in raw_val:
                    props[key] = float(raw_val)
                else:
                    props[key] = int(raw_val)
            except ValueError:
                props[key] = raw_val

    return props


def render_angular_template(template: str, props: Dict[str, Any]) -> str:
    """Evaluate and render an Angular template against class properties."""
    html = template.strip()

    # 1. Handle *ngFor directives: e.g. <li *ngFor="let s of skills">{{ s }}</li>
    ng_for_regex = re.compile(
        r"<([a-zA-Z0-9_-]+)\s+[^>]*\*ngFor\s*=\s*[\"']let\s+([a-zA-Z0-9_]+)\s+of\s+([a-zA-Z0-9_]+)[\"'][^>]*>(.*?)<\/\1>",
        re.DOTALL
    )

    def replace_ng_for(match: re.Match) -> str:
        tag = match.group(1)
        item_var = match.group(2)
        list_var = match.group(3)
        inner_content = match.group(4)

        list_val = props.get(list_var, [])
        if not isinstance(list_val, (list, tuple)):
            return ""

        rendered_items = []
        for item in list_val:
            item_rendered = re.sub(
                r"\{\{\s*" + re.escape(item_var) + r"\s*\}\}",
                str(item),
                inner_content
            )
            rendered_items.append(f"<{tag}>{item_rendered}</{tag}>")

        return "".join(rendered_items)

    html = ng_for_regex.sub(replace_ng_for, html)

    # 2. Handle *ngIf directives: e.g. <p *ngIf="isLoggedIn">Welcome</p>
    ng_if_regex = re.compile(
        r"<([a-zA-Z0-9_-]+)\s+[^>]*\*ngIf\s*=\s*[\"']([a-zA-Z0-9_]+)[\"'][^>]*>(.*?)<\/\1>",
        re.DOTALL
    )

    def replace_ng_if(match: re.Match) -> str:
        tag = match.group(1)
        cond_var = match.group(2)
        inner_content = match.group(3)

        cond_val = props.get(cond_var, False)
        if cond_val:
            return f"<{tag}>{inner_content}</{tag}>"
        return ""

    html = ng_if_regex.sub(replace_ng_if, html)

    # 3. Handle property bindings: e.g. [disabled]="isDisabled"
    prop_bind_regex = re.compile(
        r'\[([a-zA-Z0-9_-]+)\]\s*=\s*["\']([a-zA-Z0-9_]+)["\']'
    )

    def replace_prop_bind(match: re.Match) -> str:
        attr = match.group(1)
        var_name = match.group(2)
        val = props.get(var_name)
        if attr == "disabled":
            return "disabled" if val else ""
        if val is None or val is False:
            return ""
        return f'{attr}="{val}"'

    html = prop_bind_regex.sub(replace_prop_bind, html)

    # 4. Clean up event bindings: (click)="increment()" -> (click)="increment()"
    # 5. Handle template interpolation: {{ property }} or {{ 2 + 2 }}
    def replace_interpolation(match: re.Match) -> str:
        expr = match.group(1).strip()
        if expr in props:
            return str(props[expr])
        # Try evaluating math expression
        try:
            return str(eval(expr, {"__builtins__": {}}, props))
        except Exception:
            return expr

    html = re.sub(r"\{\{\s*(.*?)\s*\}\}", replace_interpolation, html)

    # Clean redundant whitespaces inside tags
    html = re.sub(r"\s+>", ">", html)
    html = re.sub(r">\s+<", "><", html)

    return html.strip()


def run_student_angular_code(code_str: str) -> ExecutionResult:
    """Parse, validate, and render student Angular component code."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Angular code",
            friendly_explanation_en="Please write some Angular component code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የአንጉላር (Angular) ኮድ ይጻፉ!",
        )

    # Check for unclosed interpolation
    if "{{" in raw and "}}" not in raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Unclosed interpolation {{ ... }}",
            friendly_explanation_en=FRIENDLY_ANGULAR_ERRORS_EN["unclosed_interpolation"],
            friendly_explanation_am=FRIENDLY_ANGULAR_ERRORS_AM["unclosed_interpolation"],
        )

    # Check for JSX elements improperly used in Angular
    if "<View>" in raw or "<Text>" in raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="React Native tags used in Angular",
            friendly_explanation_en="Mobile <View> and <Text> belong to React Native! Angular uses standard HTML tags.",
            friendly_explanation_am="<View> እና <Text> የሪያክት ኔቲቭ ናቸው! አንጉላር መደበኛ የ HTML ታጎችን ይጠቀማል።",
        )

    # Extract template
    template_match = re.search(
        r"template\s*:\s*(?:`([\s\S]*?)`|'([\s\S]*?)'|\"([\s\S]*?)\")",
        raw
    )

    if not template_match:
        # If student just wrote raw HTML template directly, allow it
        if raw.startswith("<") and not "@Component" in raw:
            template = raw
            class_body = ""
        else:
            return ExecutionResult(
                success=False,
                output="",
                error_message="Missing template property in @Component",
                friendly_explanation_en="Every Angular `@Component` must define a `template: \\`...\\`` property.",
                friendly_explanation_am="እያንዳንዱ የአንጉላር `@Component` የ `template: \\`...\\`` ንብረት ሊኖረው ይገባል።",
            )
    else:
        template = template_match.group(1) or template_match.group(2) or template_match.group(3) or ""
        # Extract class body
        class_match = re.search(r"class\s+[a-zA-Z0-9_]+\s*\{([\s\S]*)\}", raw)
        class_body = class_match.group(1) if class_match else ""

    props = parse_angular_properties(class_body)
    rendered_html = render_angular_template(template, props)

    if len(rendered_html) > MAX_OUTPUT_CHARS:
        rendered_html = rendered_html[:MAX_OUTPUT_CHARS] + "\n...[Output truncated]"

    return ExecutionResult(
        success=True,
        output=rendered_html,
        error_message=None,
    )
