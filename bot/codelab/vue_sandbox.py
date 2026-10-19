"""Safe sandboxed Vue.js 3 runner using Node.js, vue, and vue/server-renderer."""

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

FORBIDDEN_VUE_PATTERNS = [
    r"\brequire\s*\(",
    r"\bimport\s+.*from\s+['\"](?!vue\b)",
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

FRIENDLY_VUE_ERRORS_EN = {
    "unclosed interpolation": (
        "Unclosed Interpolation: Vue template expressions require closing double curly braces `}}`."
    ),
    "compiler error": (
        "Vue Template Error: Check your tags `<...>`, closing tags `</...>`, or directive syntax (`:bind`, `@click`, `v-if`)."
    ),
    "is not defined on instance": (
        "Undefined Property: Make sure all variables used in your template are returned in `data() { return { ... } }`."
    ),
    "tag has no matching end tag": (
        "Unclosed HTML Tag: Every opening HTML tag in a Vue template must have a matching closing tag."
    ),
}

FRIENDLY_VUE_ERRORS_AM = {
    "unclosed interpolation": (
        "ያልተዘጋ የኢንተርፖሌሽን ምልክት፦ የቪው የጽሁፍ ማሳያ በድርብ የፈረንሳይ ቅንፍ `}}` መዘጋት አለበት።"
    ),
    "compiler error": (
        "የቪው ቴምፕሌት ስህተት፦ ታጎችን `<...>`፣ መዝጊያዎችን `</...>` ወይም የመመሪያ አጻጻፍን (`:bind`, `@click`, `v-if`) ያረጋግጡ።"
    ),
    "is not defined on instance": (
        "ተለዋዋጩ አልታወቀም፦ በቴምፕሌት ውስጥ የተጠቀሟቸው ተለዋዋጮች በ `data()` ውስጥ መመለሳቸውን ያረጋግጡ።"
    ),
    "tag has no matching end tag": (
        "ያልተዘጋ ታግ፦ በቪው ቴምፕሌት ውስጥ እያንዳንዱ መክፈቻ ታግ የሚዘጋበት ታግ ሊኖረው ይገባል።"
    ),
}

HARNESS_VUE_TEMPLATE = """
const { createSSRApp } = require('vue');
const { renderToString } = require('vue/server-renderer');

const studentCode = %s;

(async function() {
    try {
        let raw = studentCode.trim();

        if (raw.startsWith('export default')) {
            raw = raw.replace(/^export\\s+default\\s+/, '');
        }

        let compObj = null;
        if (raw.startsWith('{') && raw.endsWith('}')) {
            compObj = eval('(' + raw + ')');
        } else if (raw.startsWith('<')) {
            compObj = {
                template: raw,
                data() {
                    return {
                        name: 'Vue.js',
                        message: 'Welcome to Vue!',
                        count: 42,
                        isAwesome: true,
                        isDisabled: true,
                        items: ['Vue', 'Vite', 'Pinia'],
                        user: { name: 'Liya', role: 'Vue Architect' }
                    };
                }
            };
        } else {
            compObj = eval('(' + raw + ')');
        }

        const app = createSSRApp(compObj);
        let html = await renderToString(app);

        // Strip Vue SSR comment artifacts <!--[--> and <!--]-->
        html = html.replace(/<!--\\[-->/g, '').replace(/<!--\\]-->/g, '').replace(/<!--.*?-->/g, '').trim();

        console.log(html);
    } catch (err) {
        console.error(err.message || String(err));
        process.exit(1);
    }
})();
"""


def check_vue_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan Vue code for dangerous modules."""
    for pattern in FORBIDDEN_VUE_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "").replace(r"\s*", "").replace("\\", "")
            err_en = f"Security Notice: `{clean_word}` is restricted in beginner Vue exercises."
            err_am = f"የደህንነት ቁጥጥር፦ በጀማሪ የቪው ልምምዶች ላይ `{clean_word}` መጠቀም አልተፈቀደም።"
            return False, err_en, err_am
    return True, None, None


def _get_friendly_vue_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_VUE_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_VUE_ERRORS_AM[pattern]
    return (
        f"Vue Error:\n{raw_err}",
        f"የቪው ስህተት፦\n{raw_err}",
    )


def run_student_vue_code(code_str: str) -> ExecutionResult:
    """Execute and render student Vue.js component code safely."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Vue code",
            friendly_explanation_en="Please write some Vue component code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የቪው (Vue.js) ኮድ ይጻፉ!",
        )

    # Check unclosed interpolation
    if "{{" in raw and "}}" not in raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Unclosed interpolation {{ ... }}",
            friendly_explanation_en=FRIENDLY_VUE_ERRORS_EN["unclosed interpolation"],
            friendly_explanation_am=FRIENDLY_VUE_ERRORS_AM["unclosed interpolation"],
        )

    is_safe, err_en, err_am = check_vue_safety(raw)
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
            friendly_explanation_en="Node.js runtime is currently not available on this server.",
            friendly_explanation_am="የኖድ (Node.js) አስተርጓሚ በዚህ ሰርቨር ላይ አልተገኘም።",
        )

    import json
    harness_code = HARNESS_VUE_TEMPLATE % json.dumps(raw)

    temp_js = None
    try:
        temp_js = tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".cjs",
            delete=False,
            dir=os.getcwd(),
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

        if result.returncode != 0:
            err_msg = stderr or stdout
            en_msg, am_msg = _get_friendly_vue_error(err_msg)
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
            error_message="Vue execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! Check that your component terminates.",
            friendly_explanation_am="የማስኬጃ ጊዜ አልቋል! ኮምፖነንቱ ማብቂያ እንዳለው ያረጋግጡ።",
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
