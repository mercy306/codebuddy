"""Safe sandboxed Express.js runner using Node.js, Express, and ephemeral local ports."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

FORBIDDEN_EXPRESS_PATTERNS = [
    r"\brequire\s*\(\s*['\"](?!express\b)",
    r"\bchild_process\b",
    r"\bfs\b",
    r"\bnet\b",
    r"\bhttp\b",
    r"\bhttps\b",
    r"\beval\s*\(",
    r"\bFunction\s*\(",
    r"\b__proto__\b",
]

FRIENDLY_EXPRESS_ERRORS_EN = {
    "cannot set headers after they are sent": (
        "Cannot Set Headers: You attempted to send multiple responses for the same request (e.g., calling `res.send()` or `res.json()` twice)."
    ),
    "is not a function": (
        "Type Error: Verify your route handler or middleware is a function like `(req, res) => { ... }` or `(req, res, next) => { ... }`."
    ),
    "cannot read properties of undefined": (
        "Undefined Property: Ensure you enabled `app.use(express.json())` for `req.body`, or check property names on `req.params` or `req.query`."
    ),
    "unexpected token": (
        "Syntax Error: Check your JavaScript syntax, commas, brackets, or arrow function definitions `=>`."
    ),
    "identifier 'app' has already been declared": (
        "Duplicate Identifier: `app` was declared multiple times. Only declare `const app = express();` once."
    ),
}

FRIENDLY_EXPRESS_ERRORS_AM = {
    "cannot set headers after they are sent": (
        "መልስ ከተላከ በኋላ ራስጌዎችን መቀየር አይቻልም፦ ለአንድ ጥያቄ ከአንድ በላይ ምላሽ ለመላክ ሞክረዋል (ለምሳሌ `res.send()` ወይም `res.json()` ሁለት ጊዜ መጥራት)።"
    ),
    "is not a function": (
        "የፈንክሽን ስህተት፦ የራውተር ተቆጣጣሪው ትክክለኛ ፈንክሽን መሆኑን ያረጋግጡ፤ ለምሳሌ `(req, res) => { ... }`።"
    ),
    "cannot read properties of undefined": (
        "ያልተገኘ ባህሪ፦ ለ `req.body` የ `app.use(express.json())` መመሪያን ማንቃትዎን፣ ወይም `req.params` እና `req.query`ን ያረጋግጡ።"
    ),
    "unexpected token": (
        "የአገባብ (Syntax) ስህተት፦ የኮድዎን አጻጻፍ፣ ቅንፎችን ወይም የቀስት ፈንክሽን `=>` ምልክቶችን ያረጋግጡ።"
    ),
    "identifier 'app' has already been declared": (
        "የተደገመ ስም፦ `app` ከአንድ ጊዜ በላይ ተሰይሟል። `const app = express();`ን አንዴ ብቻ ይጠቀሙ።"
    ),
}

HARNESS_EXPRESS_TEMPLATE = """
const express = require('express');

// Monkey patch application.listen so student calls to app.listen() don't block
const dummyServer = {
    close: (cb) => { if (cb) cb(); },
    on: () => {},
    address: () => ({ port: 3000 })
};
express.application.listen = function(...args) {
    const cb = args.find(a => typeof a === 'function');
    if (cb) {
        try { cb(); } catch (e) {}
    }
    return dummyServer;
};

(async function() {
    try {
        let app;
        %s

        if (typeof app === 'undefined' || !app) {
            console.error("No Express app defined.");
            process.exit(1);
        }

        const stack = (app.router || app._router)?.stack || [];
        const routeLayers = stack.filter(l => l.route);

        if (routeLayers.length === 0) {
            process.exit(0);
        }

        // Determine target route to test
        let chosenLayer = routeLayers.find(l => l.route.path === '/api/profile')
            || routeLayers.find(l => l.route.path === '/items')
            || routeLayers.find(l => l.route.path === '/search')
            || routeLayers.find(l => l.route.path.startsWith('/user'))
            || routeLayers.find(l => l.route.path.includes('status'))
            || routeLayers[0];

        const routePath = chosenLayer.route.path;
        const method = Object.keys(chosenLayer.route.methods)[0].toUpperCase();

        let reqPath = routePath;
        if (reqPath.includes(':')) {
            reqPath = reqPath.replace(/:[a-zA-Z0-9_]+/g, '42');
        } else if (reqPath === '/search') {
            reqPath = '/search?q=nodejs';
        }

        // Restore original listen to bind ephemeral port
        const realServer = require('http').createServer(app);
        realServer.listen(0, '127.0.0.1', async () => {
            try {
                const port = realServer.address().port;
                const fetchOptions = { method: method };
                if (method === 'POST') {
                    fetchOptions.headers = { 'Content-Type': 'application/json' };
                    fetchOptions.body = JSON.stringify({ title: 'Express Mastery', name: 'Express' });
                }

                const res = await fetch(`http://127.0.0.1:${port}${reqPath}`, fetchOptions);
                const text = await res.text();
                realServer.close(() => {
                    process.stdout.write(text.trim());
                    process.exit(0);
                });
            } catch (err) {
                realServer.close(() => {
                    console.error(err.message || String(err));
                    process.exit(1);
                });
            }
        });
    } catch (err) {
        console.error(err.message || String(err));
        process.exit(1);
    }
})();
"""


def check_express_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan Express code for unauthorized operations."""
    for pattern in FORBIDDEN_EXPRESS_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "").replace(r"\s*", "").replace("\\", "")
            err_en = f"Security Notice: `{clean_word}` is restricted in beginner Express.js exercises."
            err_am = f"የደህንነት ቁጥጥር፦ በጀማሪ የኤክስፕረስ ልምምዶች ላይ `{clean_word}` መጠቀም አልተፈቀደም።"
            return False, err_en, err_am
    return True, None, None


def _get_friendly_express_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_EXPRESS_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_EXPRESS_ERRORS_AM[pattern]
    return (
        f"Express Error:\n{raw_err}",
        f"የኤክስፕረስ ስህተት፦\n{raw_err}",
    )


def run_student_express_code(code_str: str) -> ExecutionResult:
    """Execute and test student Express.js server code safely."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Express code",
            friendly_explanation_en="Please write some Express.js server code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የኤክስፕረስ (Express.js) ሰርቨር ኮድ ይጻፉ!",
        )

    is_safe, err_en, err_am = check_express_safety(raw)
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

    # Normalize student code:
    # If student used `const app = express();`, ensure `app` variable assignment doesn't conflict
    prepared_code = raw
    if re.search(r"\b(const|let|var)\s+app\s*=", prepared_code):
        prepared_code = re.sub(r"\b(const|let|var)\s+app\s*=", "app =", prepared_code, count=1)
    else:
        prepared_code = "app = express();\n" + prepared_code

    harness_code = HARNESS_EXPRESS_TEMPLATE % prepared_code

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
            en_msg, am_msg = _get_friendly_express_error(err_msg)
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
            error_message="Express server execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! Verify that your route handler sends a response with `res.send()` or `res.json()`.",
            friendly_explanation_am="የማስኬጃ ጊዜ አልቋል! የራውተር ተቆጣጣሪው በ `res.send()` ወይም `res.json()` ምላሽ መመለሱን ያረጋግጡ።",
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
