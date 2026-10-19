"""Unit and integration tests for Express.js runner and interactive tutor curriculum."""

import pytest
from bot.codelab.express_sandbox import run_student_express_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_express import EXPRESS_TUTOR_CHAPTERS


def test_express_hello_server():
    code = """
    const express = require('express');
    const app = express();

    app.get('/', (req, res) => {
      res.send('Hello Express!');
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == "Hello Express!"


def test_express_json_response():
    code = """
    const express = require('express');
    const app = express();

    app.get('/api/status', (req, res) => {
      res.json({ status: 'online', users: 100 });
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == '{"status":"online","users":100}'


def test_express_route_params():
    code = """
    const express = require('express');
    const app = express();

    app.get('/users/:id', (req, res) => {
      res.send(`User ID: ${req.params.id}`);
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == "User ID: 42"


def test_express_query_string():
    code = """
    const express = require('express');
    const app = express();

    app.get('/search', (req, res) => {
      res.send(`Search results for: ${req.query.q}`);
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == "Search results for: nodejs"


def test_express_middleware():
    code = """
    const express = require('express');
    const app = express();

    app.use((req, res, next) => {
      req.role = 'Admin';
      next();
    });

    app.get('/api/user', (req, res) => {
      res.send(`Welcome ${req.role}!`);
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == "Welcome Admin!"


def test_express_post_json():
    code = """
    const express = require('express');
    const app = express();

    app.use(express.json());

    app.post('/items', (req, res) => {
      res.json({ created: req.body.title });
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == '{"created":"Express Mastery"}'


def test_express_capstone_microservice():
    code = """
    const express = require('express');
    const app = express();

    app.use(express.json());

    app.get('/api/profile', (req, res) => {
      res.json({
        developer: 'Liya',
        stack: 'Node + Express',
        role: 'Backend Engineer'
      });
    });
    """
    res = run_student_express_code(code)
    assert res.success is True
    assert res.output == '{"developer":"Liya","stack":"Node + Express","role":"Backend Engineer"}'


def test_express_safety_blocks():
    dangerous_code = """
    const express = require('express');
    const fs = require('fs');
    const app = express();
    """
    res = run_student_express_code(dangerous_code)
    assert res.success is False
    assert "restricted" in res.error_message.lower() or "security" in res.error_message.lower()


def test_express_syntax_error():
    broken_code = """
    const express = require('express');
    const app = express();
    app.get('/broken' (req, res) => {
    """
    res = run_student_express_code(broken_code)
    assert res.success is False
    assert res.friendly_explanation_en is not None


def test_express_curriculum_structure():
    chapters = get_all_tutor_chapters("express")
    assert len(chapters) == 7
    assert chapters[0].id == "express_ch1"
    assert chapters[6].id == "express_ch7"

    ch1 = get_tutor_chapter("express_ch1")
    assert ch1 is not None
    assert "Express" in ch1.title_en
    assert "ኤክስፕረስ" in ch1.title_am

    # Check next chapter progression
    assert get_next_tutor_chapter_id("express_ch1") == "express_ch2"
    assert get_next_tutor_chapter_id("express_ch6") == "express_ch7"
    assert get_next_tutor_chapter_id("express_ch7") is None
