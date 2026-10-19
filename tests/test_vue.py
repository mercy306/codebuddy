"""Unit and integration tests for Vue.js 3 sandbox runner and interactive tutor curriculum."""

import pytest
from bot.codelab.vue_sandbox import run_student_vue_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_vue import VUE_TUTOR_CHAPTERS


def test_vue_interpolation():
    code = """{
      template: `<h1>Hello {{ name }}!</h1>`,
      data() {
        return { name: 'Vue.js' };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<h1>Hello Vue.js!</h1>"


def test_vue_reactive_count():
    code = """{
      template: `<h2>Likes: {{ count }}</h2>`,
      data() {
        return { count: 42 };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<h2>Likes: 42</h2>"


def test_vue_attribute_binding():
    code = """{
      template: `<button :disabled="isDisabled">Submit</button>`,
      data() {
        return { isDisabled: true };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<button disabled>Submit</button>"


def test_vue_event_binding():
    code = """{
      template: `<button @click="count++">Clicks: {{ count }}</button>`,
      data() {
        return { count: 7 };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<button>Clicks: 7</button>"


def test_vue_v_if_directive():
    code = """{
      template: `<p v-if="isAwesome">Vue is Awesome!</p>`,
      data() {
        return { isAwesome: true };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<p>Vue is Awesome!</p>"


def test_vue_v_for_directive():
    code = """{
      template: `<ul><li v-for="item in items" :key="item">{{ item }}</li></ul>`,
      data() {
        return { items: ['Vue', 'Vite', 'Pinia'] };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == "<ul><li>Vue</li><li>Vite</li><li>Pinia</li></ul>"


def test_vue_capstone_card():
    code = """{
      template: `<div class="card"><h2>{{ user.name }}</h2><p>Role: {{ user.role }}</p></div>`,
      data() {
        return {
          user: { name: 'Liya', role: 'Vue Architect' }
        };
      }
    }"""
    res = run_student_vue_code(code)
    assert res.success is True
    assert res.output == '<div class="card"><h2>Liya</h2><p>Role: Vue Architect</p></div>'


def test_vue_safety_blocks():
    dangerous_code = """{
      template: `<div>Hack</div>`,
      data() {
        const fs = require('fs');
        return {};
      }
    }"""
    res = run_student_vue_code(dangerous_code)
    assert res.success is False
    assert "restricted" in res.error_message.lower() or "security" in res.error_message.lower()


def test_vue_unclosed_interpolation():
    broken_code = """{
      template: `<h1>Hello {{ name</h1>`,
      data() { return { name: 'Vue' }; }
    }"""
    res = run_student_vue_code(broken_code)
    assert res.success is False
    assert "interpolation" in (res.friendly_explanation_en or "").lower()


def test_vue_curriculum_structure():
    chapters = get_all_tutor_chapters("vue")
    assert len(chapters) == 7
    assert chapters[0].id == "vue_ch1"
    assert chapters[6].id == "vue_ch7"

    ch1 = get_tutor_chapter("vue_ch1")
    assert ch1 is not None
    assert "Interpolation" in ch1.title_en
    assert "ኢንተርፖሌሽን" in ch1.title_am or "Interpolation" in ch1.title_am

    # Check next chapter progression
    assert get_next_tutor_chapter_id("vue_ch1") == "vue_ch2"
    assert get_next_tutor_chapter_id("vue_ch6") == "vue_ch7"
    assert get_next_tutor_chapter_id("vue_ch7") is None
