"""Safe sandboxed React Native mobile code runner using Node.js, sucrase, and mobile component mocks."""

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

FORBIDDEN_RN_PATTERNS = [
    r"\brequire\s*\(",
    r"\bimport\s+.*from\s+['\"](?!react\b|react-native\b)",
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

FRIENDLY_RN_ERRORS_EN = {
    "text strings must be rendered within a <text> component": (
        "Mobile Constraint: In React Native, text strings cannot sit directly inside a `<View>`. You must wrap all text inside a `<Text>` component!"
    ),
    "html tags are not supported in react native": (
        "No HTML on Mobile: In React Native, HTML tags like `<div>` or `<p>` do not exist on phones! Use `<View>` for containers and `<Text>` for words."
    ),
    "expected corresponding jsx closing tag": (
        "Unclosed Tag: Make sure every `<View>` is closed with `</View>` and every `<Text>` is closed with `</Text>`."
    ),
    "adjacent jsx elements must be wrapped": (
        "Multiple Root Elements: In React Native, wrap multiple sibling elements in a parent `<View>...</View>`."
    ),
    "is not defined": (
        "Undefined Component or Variable: Make sure you import or spell mobile components like `<View>` and `<Text>` correctly."
    ),
}

FRIENDLY_RN_ERRORS_AM = {
    "text strings must be rendered within a <text> component": (
        "የሞባይል ህግ፦ በሪያክት ኔቲቭ ውስጥ ጽሁፍ በ `<View>` ውስጥ ብቻውን ሊቀመጥ አይችልም። ማንኛውም ጽሁፍ በ `<Text>` ታግ ውስጥ መሆን አለበት!"
    ),
    "html tags are not supported in react native": (
        "በሞባይል ላይ የ HTML ታጎች የሉም፦ በሪያክት ኔቲቭ ውስጥ እንደ `<div>` ወይም `<p>` ያሉ ታጎች አይሰሩም! በ `<div>` ፈንታ `<View>`፣ በ `<p>` ፈንታ `<Text>` ይጠቀሙ።"
    ),
    "expected corresponding jsx closing tag": (
        "ያልተዘጋ ታግ፦ እያንዳንዱ `<View>` በ `</View>` እንዲሁም `<Text>` በ `</Text>` መዘጋቱን ያረጋግጡ።"
    ),
    "adjacent jsx elements must be wrapped": (
        "የኮምፖነንት ማቀፊያ ስህተት፦ በርካታ የሞባይል ኤለመንቶችን በአንድ ዋና `<View>...</View>` ውስጥ ማቀፍ አለብዎት።"
    ),
    "is not defined": (
        "ኮምፖነንቱ አልታወቀም፦ እንደ `<View>` እና `<Text>` ያሉ የሞባይል ክፍሎች ፊደላት አጻጻፍ በትክክል መሆኑን ያረጋግጡ።"
    ),
}

HARNESS_RN_TEMPLATE = """
const { transform } = require('sucrase');
const React = require('react');
const ReactDOMServer = require('react-dom/server');

const View = ({ children, style, ...rest }) => {
    React.Children.forEach(children, child => {
        if (typeof child === 'string' && child.trim().length > 0) {
            throw new Error("Text strings must be rendered within a <Text> component.");
        }
    });
    return React.createElement('div', { className: 'rn-view', style, ...rest }, children);
};

const Text = ({ children, style, ...rest }) => {
    return React.createElement('span', { className: 'rn-text', style, ...rest }, children);
};

const TouchableOpacity = ({ children, style, ...rest }) => {
    return React.createElement('button', { className: 'rn-touchable', style, ...rest }, children);
};

const Button = ({ title, onPress, color, style, ...rest }) => {
    return React.createElement('button', { className: 'rn-button', style, ...rest }, title || 'Button');
};

const ScrollView = ({ children, style, ...rest }) => {
    return React.createElement('section', { className: 'rn-scrollview', style, ...rest }, children);
};

const SafeAreaView = ({ children, style, ...rest }) => {
    return React.createElement('main', { className: 'rn-safeareaview', style, ...rest }, children);
};

const Image = ({ source, style, ...rest }) => {
    return React.createElement('img', { className: 'rn-image', src: (source && source.uri) || '', style, ...rest });
};

const StyleSheet = {
    create: (styles) => styles,
};

const studentCode = %s;

try {
    let codeToTransform = studentCode.trim();

    // Catch beginner usage of HTML tags in React Native
    const htmlRegex = /<(?:div|p|span|h1|h2|h3|h4|h5|h6|ul|li|button|section|article)\\b/i;
    if (htmlRegex.test(codeToTransform)) {
        throw new Error("HTML tags are not supported in React Native. Use <View> and <Text> instead!");
    }

    // Auto-wrap raw JSX snippet if needed
    const hasFunction = /\\bfunction\\s+([A-Za-z0-9_]+)/.test(codeToTransform) ||
                        /\\bconst\\s+([A-Za-z0-9_]+)\\s*=/.test(codeToTransform);

    let targetComponentName = null;

    if (!hasFunction && codeToTransform.startsWith('<')) {
        codeToTransform = `function App() { return ( ${codeToTransform} ); }`;
        targetComponentName = 'App';
    } else {
        const matchFunc = codeToTransform.match(/\\bfunction\\s+([A-Z][A-Za-z0-9_]*)/);
        const matchConst = codeToTransform.match(/\\b(?:const|let|var)\\s+([A-Z][A-Za-z0-9_]*)\\s*=/);
        if (matchFunc) {
            targetComponentName = matchFunc[1];
        } else if (matchConst) {
            targetComponentName = matchConst[1];
        } else {
            const anyFunc = codeToTransform.match(/\\bfunction\\s+([a-zA-Z0-9_]+)/);
            if (anyFunc) targetComponentName = anyFunc[1];
        }
    }

    const transformed = transform(codeToTransform, {
        transforms: ['jsx', 'imports'],
        jsxRuntime: 'automatic'
    }).code;

    const execution = new Function(
        'React', 'ReactDOMServer', 'require',
        'View', 'Text', 'TouchableOpacity', 'Button', 'ScrollView', 'SafeAreaView', 'Image', 'StyleSheet',
        `
        ${transformed}
        if (typeof ${targetComponentName} !== 'undefined') {
            try {
                const el = React.createElement(${targetComponentName}, {
                    name: 'Sara',
                    role: 'Mobile Engineer',
                    phone: '+251 91 123 4567',
                    online: true
                });
                return ReactDOMServer.renderToStaticMarkup(el);
            } catch(e) {
                return 'Render Error: ' + e.message;
            }
        }
        return '';
    `);

    const htmlOutput = execution(
        React, ReactDOMServer, require,
        View, Text, TouchableOpacity, Button, ScrollView, SafeAreaView, Image, StyleSheet
    );

    if (htmlOutput) {
        // Format output into clean native mobile tags for student display
        let cleanNative = htmlOutput
            .replace(/<div class="rn-view"(?: style="([^"]*)")?>/g, (match, st) => st ? `<View style="${st}">` : '<View>')
            .replace(/<\\/div>/g, '</View>')
            .replace(/<span class="rn-text"(?: style="([^"]*)")?>/g, (match, st) => st ? `<Text style="${st}">` : '<Text>')
            .replace(/<\\/span>/g, '</Text>')
            .replace(/<button class="rn-touchable"(?: style="([^"]*)")?>/g, (match, st) => st ? `<TouchableOpacity style="${st}">` : '<TouchableOpacity>')
            .replace(/<button class="rn-button"[^>]*>([^<]*)<\\/button>/g, '<Button title="$1" />')
            .replace(/<\\/button>/g, '</TouchableOpacity>')
            .replace(/<section class="rn-scrollview"[^>]*>/g, '<ScrollView>')
            .replace(/<\\/section>/g, '</ScrollView>')
            .replace(/<main class="rn-safeareaview"[^>]*>/g, '<SafeAreaView>')
            .replace(/<\\/main>/g, '</SafeAreaView>');

        console.log(cleanNative);
    }
} catch (err) {
    console.error(err.message || String(err));
    process.exit(1);
}
"""


def check_rn_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan React Native code for forbidden patterns."""
    for pattern in FORBIDDEN_RN_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "").replace(r"\s*", "").replace("\\", "")
            err_en = f"Security Notice: `{clean_word}` is restricted in beginner React Native exercises."
            err_am = f"የደህንነት ቁጥጥር፦ በጀማሪ የሪያክት ኔቲቭ ልምምዶች ላይ `{clean_word}` መጠቀም አልተፈቀደም።"
            return False, err_en, err_am
    return True, None, None


def _get_friendly_rn_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_RN_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_RN_ERRORS_AM[pattern]
    return (
        f"React Native Error:\n{raw_err}",
        f"የሪያክት ኔቲቭ ስህተት፦\n{raw_err}",
    )


def run_student_react_native_code(code_str: str) -> ExecutionResult:
    """Execute and render student React Native code safely."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty React Native code",
            friendly_explanation_en="Please write some React Native code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የሪያክት ኔቲቭ (React Native) ኮድ ይጻፉ!",
        )

    is_safe, err_en, err_am = check_rn_safety(raw)
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
    harness_code = HARNESS_RN_TEMPLATE % json.dumps(raw)

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

        if result.returncode != 0 or "Render Error:" in stdout:
            err_msg = stderr or stdout
            en_msg, am_msg = _get_friendly_rn_error(err_msg)
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
            error_message="React Native execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! Check that your component returns promptly.",
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
