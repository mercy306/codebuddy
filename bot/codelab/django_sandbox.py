"""Safe sandboxed Django runner using in-memory settings and RequestFactory."""

from __future__ import annotations

import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Tuple, Optional
from bot.codelab.sandbox import ExecutionResult

TIMEOUT_SECONDS = 4
MAX_OUTPUT_CHARS = 2000

FORBIDDEN_DJANGO_PATTERNS = [
    r"\bimport\s+os\b",
    r"\bfrom\s+os\b",
    r"\bimport\s+sys\b",
    r"\bfrom\s+sys\b",
    r"\bimport\s+subprocess\b",
    r"\bfrom\s+subprocess\b",
    r"\bimport\s+shutil\b",
    r"\bfrom\s+shutil\b",
    r"\bimport\s+socket\b",
    r"\bfrom\s+socket\b",
    r"\beval\s*\(",
    r"\bexec\s*\(",
    r"\b__import__\b",
    r"\bopen\s*\(",
]

FRIENDLY_DJANGO_ERRORS_EN = {
    "improperlyconfigured": (
        "Django Configuration Error: Check your Django settings or template backend setup."
    ),
    "typeerror": (
        "Type Error: Verify your view function signature accepts `request` or correct arguments."
    ),
    "syntaxerror": (
        "Syntax Error: Check Python indentation, colons `:`, and quotes in your Django code."
    ),
    "nameerror": (
        "Name Error: Make sure all required Django imports (e.g., `HttpResponse`, `JsonResponse`, `models`) are imported."
    ),
    "attributeerror": (
        "Attribute Error: Check property names on your models, views, or template contexts."
    ),
}

FRIENDLY_DJANGO_ERRORS_AM = {
    "improperlyconfigured": (
        "የዲጃንጎ ቅንብር ስህተት፦ የዲጃንጎ ቴምፕሌት ወይም ሴቲንግስ በትክክል መዋቀራቸውን ያረጋግጡ።"
    ),
    "typeerror": (
        "የአይነት (Type) ስህተት፦ የቪው ፈንክሽኑ `request` ወይም ትክክለኛ መለኪያዎችን መቀበሉን ያረጋግጡ።"
    ),
    "syntaxerror": (
        "የአገባብ (Syntax) ስህተት፦ የኮድዎን አጻጻፍ፣ ክፍተቶች (Indentation) እና የኮለን `:` ምልክቶችን ያረጋግጡ።"
    ),
    "nameerror": (
        "ያልታወቀ ስም፦ አስፈላጊ የዲጃንጎ ክፍሎች (ለምሳሌ `HttpResponse`, `JsonResponse`, `models`) ማስመጣትዎን ያረጋግጡ።"
    ),
    "attributeerror": (
        "የባህሪ ስህተት፦ በሞዴሎች፣ ቪው ወይም ቴምፕሌት ውስጥ የተጠቀሟቸውን ባህሪያት ያረጋግጡ።"
    ),
}

HARNESS_DJANGO_TEMPLATE = """
import io
import inspect
import sys
import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="codebuddy-secret-key",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": False,
            }
        ],
    )
django.setup()

from django.test import RequestFactory
from django.db import models
from django.http import HttpResponse, JsonResponse

rf = RequestFactory()

# Capture any stdout prints
stdout_capture = io.StringIO()
old_stdout = sys.stdout
sys.stdout = stdout_capture

student_scope = {}
student_code = %r

try:
    exec(student_code, student_scope)
    
    sys.stdout = old_stdout
    printed = stdout_capture.getvalue().strip()
    
    output = None
    if "output" in student_scope:
        output = str(student_scope["output"]).strip()
    elif "urlpatterns" in student_scope and student_scope["urlpatterns"]:
        cb = student_scope["urlpatterns"][0].callback
        res = cb(rf.get("/"))
        output = res.content.decode("utf-8").strip()
    else:
        # Check for model subclass
        user_models = [
            v for k, v in student_scope.items()
            if inspect.isclass(v) and issubclass(v, models.Model) and v is not models.Model
        ]
        if user_models:
            m_cls = user_models[0]
            try:
                m_inst = m_cls(title="Django Web Development", students=250)
                output = str(m_inst).strip()
            except Exception:
                try:
                    m_inst = m_cls()
                    output = str(m_inst).strip()
                except Exception:
                    output = printed
        else:
            # Check for user view functions
            views = [
                v for k, v in student_scope.items()
                if inspect.isfunction(v) and not k.startswith("_")
            ]
            if views:
                v = views[0]
                sig = inspect.signature(v)
                if len(sig.parameters) == 2:
                    res = v(rf.get("/users/42/"), 42)
                else:
                    res = v(rf.get("/"))
                if hasattr(res, "content"):
                    output = res.content.decode("utf-8").strip()
                else:
                    output = str(res).strip()
    
    if output is None:
        output = printed

    sys.stdout.write(output or printed)
except Exception as e:
    sys.stdout = old_stdout
    sys.stderr.write(f"{type(e).__name__}: {e}\\n")
    sys.exit(1)
"""


def check_django_safety(code_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
    """Scan student Django code for disallowed system modules."""
    for pattern in FORBIDDEN_DJANGO_PATTERNS:
        if re.search(pattern, code_str):
            clean_word = pattern.replace(r"\b", "").replace(r"\s+", " ").replace("\\", "")
            err_en = f"Security Notice: `{clean_word}` is restricted in beginner Django exercises."
            err_am = f"የደህንነት ቁጥጥር፦ በጀማሪ የዲጃንጎ ልምምዶች ላይ `{clean_word}` መጠቀም አልተፈቀደም።"
            return False, err_en, err_am
    return True, None, None


def _get_friendly_django_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_DJANGO_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_DJANGO_ERRORS_AM[pattern]
    return (
        f"Django Error:\n{raw_err}",
        f"የዲጃንጎ ስህተት፦\n{raw_err}",
    )


def run_student_django_code(code_str: str) -> ExecutionResult:
    """Execute student Django code safely in a dedicated subprocess."""
    raw = code_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty Django code",
            friendly_explanation_en="Please write some Django code before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የዲጃንጎ (Django) ኮድ ይጻፉ!",
        )

    is_safe, err_en, err_am = check_django_safety(raw)
    if not is_safe:
        return ExecutionResult(
            success=False,
            output="",
            error_message=err_en,
            friendly_explanation_en=err_en,
            friendly_explanation_am=err_am,
        )

    python_bin = sys.executable

    harness_code = HARNESS_DJANGO_TEMPLATE % raw

    temp_py = None
    try:
        temp_py = tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".py",
            delete=False,
            dir=os.getcwd(),
        )
        temp_py.write(harness_code.encode("utf-8"))
        temp_py.close()

        result = subprocess.run(
            [python_bin, temp_py.name],
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
            en_msg, am_msg = _get_friendly_django_error(err_msg)
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
            error_message="Django execution timed out (>4s)",
            friendly_explanation_en="Execution timed out! Verify that your code terminates cleanly.",
            friendly_explanation_am="የማስኬጃ ጊዜ አልቋል! ኮድዎ ማብቂያ እንዳለው ያረጋግጡ።",
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
        if temp_py and os.path.exists(temp_py.name):
            try:
                os.unlink(temp_py.name)
            except OSError:
                pass
