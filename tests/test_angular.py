"""Unit and integration tests for the Angular enterprise sandbox runner and curriculum."""

import pytest
from bot.codelab.angular_sandbox import run_student_angular_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_angular import ANGULAR_TUTOR_CHAPTERS


def test_angular_interpolation():
    code = """
    @Component({
      selector: 'app-welcome',
      template: '<h1>Hello {{ name }}!</h1>'
    })
    export class WelcomeComponent {
      name = 'Angular';
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == "<h1>Hello Angular!</h1>"


def test_angular_stats_count():
    code = """
    @Component({
      selector: 'app-stats',
      template: '<h2>Active Users: {{ count }}</h2>'
    })
    export class StatsComponent {
      count = 100;
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == "<h2>Active Users: 100</h2>"


def test_angular_property_binding():
    code = """
    @Component({
      selector: 'app-btn',
      template: '<button [disabled]="isDisabled">Submit</button>'
    })
    export class BtnComponent {
      isDisabled = true;
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == "<button disabled>Submit</button>"


def test_angular_event_binding():
    code = """
    @Component({
      selector: 'app-counter',
      template: '<button (click)="increment()">Clicks: {{ count }}</button>'
    })
    export class CounterComponent {
      count = 5;
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == '<button (click)="increment()">Clicks: 5</button>'


def test_angular_ng_if_directive():
    code = """
    @Component({
      selector: 'app-auth',
      template: '<p *ngIf="isLoggedIn">Welcome Back!</p>'
    })
    export class AuthComponent {
      isLoggedIn = true;
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == "<p>Welcome Back!</p>"


def test_angular_ng_for_directive():
    code = """
    @Component({
      selector: 'app-skills',
      template: '<ul><li *ngFor="let s of skills">{{ s }}</li></ul>'
    })
    export class SkillsComponent {
      skills = ['TypeScript', 'Angular', 'RxJS'];
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == "<ul><li>TypeScript</li><li>Angular</li><li>RxJS</li></ul>"


def test_angular_dashboard_card_capstone():
    code = """
    @Component({
      selector: 'app-user-card',
      template: '<div class="card"><h2>{{ name }}</h2><p>Role: {{ role }}</p></div>'
    })
    export class UserCardComponent {
      name = 'Liya';
      role = 'Lead Architect';
    }
    """
    res = run_student_angular_code(code)
    assert res.success is True
    assert res.output == '<div class="card"><h2>Liya</h2><p>Role: Lead Architect</p></div>'


def test_angular_unclosed_interpolation_error():
    code = "<h1>Hello {{ name</h1>"
    res = run_student_angular_code(code)
    assert res.success is False
    assert "Unclosed Interpolation" in res.friendly_explanation_en
    assert "ያልተዘጋ የኢንተርፖሌሽን" in res.friendly_explanation_am


def test_angular_curriculum_chapters():
    chapters = get_all_tutor_chapters("angular")
    assert len(chapters) == 7
    assert chapters[0].id == "ng_ch1"
    assert chapters[6].id == "ng_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("ng_ch1")
    assert ch1 is not None
    assert ch1.track == "angular"

    next_id = get_next_tutor_chapter_id("ng_ch1")
    assert next_id == "ng_ch2"

    last_next = get_next_tutor_chapter_id("ng_ch7")
    assert last_next is None
