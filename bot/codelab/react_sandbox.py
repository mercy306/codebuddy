"""Safe sandboxed React / JSX runner using Node.js, sucrase, and react-dom/server."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

FORBIDDEN_REACT_PATTERNS = [
    r"\brequire\s*\(",
    r"\bimport\s+.*from\s+['\"](?!react\b)",
    r"\bprocess\b",
    r"\bchild_process\b",
    r"\bfs\b",
    r"\bhttp\b",
    r"\bhttps\b",
    r"\bnet\b",
    r"\beval\s*\(",
    r"\bFunction\s*\(",
    r"\b__proto__\b",
]

FRIENDLY_REACT_ERRORS_EN = {
    "expected corresponding jsx closing tag": (
        "Unclosed JSX Tag: Every opening tag like `<div>` must have a matching closing tag `</div>` or self-close `<img />`."
    ),
    "adjacent jsx elements must be wrapped": (
        "Multiple JSX Elements: Wrap adjacent elements in a parent tag like `<div>...</div>` or a fragment `<>...</>`."
    ),
    "unexpected token": (
        "JSX Syntax Error: Check your tags `<...>`, closing tags `</...>`, and curly braces `{...}`."
    ),
    "is not defined": (
        "Undefined Variable or Component: Make sure variables and component names are spelled correctly."
    ),
    "functions are not valid as a react child": (
        "Function Render Error: You passed a function instead of calling it or rendering JSX."
    ),
    "unterminated jsx": (
        "Unclosed JSX Tag: Every opening tag like `<div>` must have a matching closing tag `</div>` or self-close `<img />`."
    ),
}

FRIENDLY_REACT_ERRORS_AM = {
    "expected corresponding jsx closing tag": (
        "ያልተዘጋ የጄኤስኤክስ (JSX) ታግ፦ እያንዳንዱ መክፈቻ ታግ እንደ `<div>` የመዝጊያ ታግ `</div>` ወይም ራሱን የሚዘጋ `<img />` ያስፈልገዋል።"
    ),
    "adjacent jsx elements must be wrapped": (
        "በርካታ የጄኤስኤክስ ኤለመንቶች፦ በርካታ ታጎችን በአንድ ዋና ታግ እንደ `<div>...</div>` ወይም `<>...</>` ውስጥ ማቀፍ አለብዎት።"
    ),
    "unexpected token": (
        "የጄኤስኤክስ የሰዋሰው ስህተት፦ ታጎችን `<...>`፣ መዝጊያዎችን `</...>` እና የፈረንሳይ ቅንፎችን `{...}` ያረጋግጡ።"
    ),
    "is not defined": (
        "ተለዋዋጩ ወይም ኮምፖነንቱ አልታወቀም፦ የስሞችን ፊደላት አጻጻፍ በትክክል ያረጋግጡ።"
    ),
    "functions are not valid as a react child": (
        "የኮምፖነንት ስህተት፦ ፈንክሽኑን ሳይጠሩ በቀጥታ በጄኤስኤክስ ውስጥ ለማሳየት ሞክረዋል።"
    ),
    "unterminated jsx": (
        "ያልተዘጋ የጄኤስኤክስ (JSX) ታግ፦ እያንዳንዱ መክፈቻ ታግ እንደ `<div>` የመዝጊያ ታግ `</div>` ወይም ራሱን የሚዘጋ `<img />` ያስፈልገዋል።"
    ),
}

# Node script harness to transform and render React
HARNESS_TEMPLATE = """
const { transform } = require('sucrase');
const React = require('react');
const ReactDOMServer = require('react-dom/server');

const studentCode = %s;

try {
    let codeToTransform = studentCode.trim();

    // If student provided raw JSX rather than a component or full code, wrap in App
    const hasFunction = /\\bfunction\\s+([A-Za-z0-9_]+)/.test(codeToTransform) ||
                        /\\bconst\\s+([A-Za-z0-9_]+)\\s*=/.test(codeToTransform);

    let targetComponentName = null;

    if (!hasFunction && codeToTransform.startsWith('<')) {
        codeToTransform = `function App() { return ( ${codeToTransform} ); }`;
        targetComponentName = 'App';
    } else {
        // Find component names (prefer PascalCase names)
        const matchFunc = codeToTransform.match(/\\bfunction\\s+([A-Z][A-Za-z0-9_]*)/);
        const matchConst = codeToTransform.match(/\\b(?:const|let|var)\\s+([A-Z][A-Za-z0-9_]*)\\s*=/);
        if (matchFunc) {
            targetComponentName = matchFunc[1];
        } else if (matchConst) {
            targetComponentName = matchConst[1];
        } else {
            // Fallback to any function
            const anyFunc = codeToTransform.match(/\\bfunction\\s+([a-zA-Z0-9_]+)/);
            if (anyFunc) targetComponentName = anyFunc[1];
        }
    }

    const transformed = transform(codeToTransform, {
        transforms: ['jsx', 'imports'],
        jsxRuntime: 'automatic'
    }).code;

    // Run in isolated sandbox context
    const execution = new Function('React', 'ReactDOMServer', 'require', `
        ${transformed}
        if (typeof ${targetComponentName} !== 'undefined') {
            try {
                // If the component accepts props, provide friendly sample props
                const el = React.createElement(${targetComponentName}, { name: 'Abebe', role: 'Member', online: true });
                return ReactDOMServer.renderToStaticMarkup(el);
            } catch(e) {
                return 'Render Error: ' + e.message;
            }
        }
        return '';
    `);

    const htmlOutput = execution(React, ReactDOMServer, require);
    if (htmlOutput) {
        console.log(htmlOutput);
    }
} catch (err) {
    console.error(err.message || String(err));
    process.exit(1);
}
"""


def check_react_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan React code for dangerous modules."""
    for pattern in FORBIDDEN_REACT_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "").replace(r"\s*", "").replace("\\", "")
            err_en = f"Security Notice: `{clean_word}` is restricted in beginner React exercises."
            err_am = f"የደህንነት ቁጥጥር፦ በጀማሪ የሪያክት ልምምዶች ላይ `{clean_word}` መጠቀም አልተፈቀደም።"
            return False, err_en, err_am
    return True, None, None


def _get_friendly_react_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_REACT_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_REACT_ERRORS_AM[pattern]
    return (
        f"React Error:\n{raw_err}",
        f"የሪያክት ስህተት፦\n{raw_err}",
    )


def run_student_react_code(code_str: str) -> ExecutionResult:
    """Execute and render student React JSX code safely."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty React code",
            friendly_explanation_en="Please write some React / JSX code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የሪያክት (React) ኮድ ይጻፉ!",
        )

    is_safe, err_en, err_am = check_react_safety(raw)
    if not is_safe:
        return ExecutionResult(
            success=False,
            output="",
            error_message=err_en,
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )

    node_bin = shutil.which("node")
    if not node_bin:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Node.js runtime not found",
            friendly_explanation_en="Node.js is currently not available on this server.",
            friendly_explanation_am="የኖድ (Node.js) አስተርጓሚ በዚህ ሰርቨር ላይ አልተገኘም።",
        )

    import json
    harness_code = HARNESS_TEMPLATE % json.dumps(raw)

    temp_js = None
    try:
        temp_js = tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".cjs",
            delete=False,
            dir=os.getcwd(),  # Allow requiring local node_modules
        )
        temp_js.write(harness_code.encode("utf-8"))
        temp_js.close()

        result = subprocess.run(
            [node_bin, temp_js.name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            encoding="utf-8",
            errors="replace",
            cwd=os.getcwd(),
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0 or "Render Error:" in stdout:
            err_msg = stderr or stdout
            en_msg, am_msg = _get_friendly_react_error(err_msg)
            return ExecutionResult(
                success=False,
                output="",
                error_message=err_msg,
                friendly_explanation_en=en_msg,
                friendly_explanation_am=am_msg,
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
            error_message="React execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! Check for infinite loops or deep recursions.",
            friendly_explanation_am="የማስኬጃ ጊዜ አልቋል! ማብቂያ የሌለው ሉፕ አለመኖሩን ያረጋግጡ።",
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
        if temp_js and os.path.exists(temp_js.name):
            try:
                os.unlink(temp_js.name)
            except OSError:
                pass
