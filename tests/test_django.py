"""Unit and integration tests for Django sandbox runner and interactive tutor curriculum."""

import pytest
from bot.codelab.django_sandbox import run_student_django_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_django import DJANGO_TUTOR_CHAPTERS


def test_django_http_response():
    code = """
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello Django!")
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == "Hello Django!"


def test_django_json_response():
    code = """
from django.http import JsonResponse

def status_view(request):
    return JsonResponse({"status": "online", "framework": "Django"})
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == '{"status": "online", "framework": "Django"}'


def test_django_template_context():
    code = """
from django.template import Template, Context

template = Template("<h1>Welcome to {{ site_name }}!</h1>")
context = Context({"site_name": "CodeBuddy"})
output = template.render(context)
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == "<h1>Welcome to CodeBuddy!</h1>"


def test_django_url_routing():
    code = """
from django.urls import path
from django.http import HttpResponse

def about_view(request):
    return HttpResponse("About CodeBuddy Learning Platform")

urlpatterns = [
    path("about/", about_view),
]
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == "About CodeBuddy Learning Platform"


def test_django_path_converter():
    code = """
from django.http import HttpResponse

def user_profile(request, user_id):
    return HttpResponse(f"Profile of User #{user_id}")
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == "Profile of User #42"


def test_django_orm_model():
    code = """
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.students} enrolled)"

    class Meta:
        app_label = "learn"
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == "Django Web Development (250 enrolled)"


def test_django_capstone():
    code = """
from django.http import JsonResponse

def developer_profile(request):
    return JsonResponse({
        "developer": "Liya",
        "framework": "Django",
        "role": "Full-Stack Python Engineer"
    })
"""
    res = run_student_django_code(code)
    assert res.success is True
    assert res.output == '{"developer": "Liya", "framework": "Django", "role": "Full-Stack Python Engineer"}'


def test_django_safety_blocks():
    dangerous_code = """
import os
from django.http import HttpResponse

def hack(request):
    return HttpResponse("hacked")
"""
    res = run_student_django_code(dangerous_code)
    assert res.success is False
    assert "restricted" in res.error_message.lower() or "security" in res.error_message.lower()


def test_django_syntax_error():
    broken_code = """
from django.http import HttpResponse
def broken(request)
    return HttpResponse("no colon")
"""
    res = run_student_django_code(broken_code)
    assert res.success is False
    assert res.friendly_explanation_en is not None


def test_django_curriculum_structure():
    chapters = get_all_tutor_chapters("django")
    assert len(chapters) == 7
    assert chapters[0].id == "django_ch1"
    assert chapters[6].id == "django_ch7"

    ch1 = get_tutor_chapter("django_ch1")
    assert ch1 is not None
    assert "Django" in ch1.title_en
    assert "ዲጃንጎ" in ch1.title_am

    # Check next chapter progression
    assert get_next_tutor_chapter_id("django_ch1") == "django_ch2"
    assert get_next_tutor_chapter_id("django_ch6") == "django_ch7"
    assert get_next_tutor_chapter_id("django_ch7") is None
