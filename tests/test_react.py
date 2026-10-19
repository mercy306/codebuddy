"""Unit and integration tests for the React / JSX sandbox runner and curriculum."""

import pytest
from bot.codelab.react_sandbox import run_student_react_code
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_react import REACT_TUTOR_CHAPTERS


def test_react_raw_jsx():
    res = run_student_react_code("<h1>Hello React!</h1>")
    assert res.success is True
    assert res.output == "<h1>Hello React!</h1>"


def test_react_functional_component():
    code = """
    function Welcome() {
        return <h2>Welcome to CodeBuddy!</h2>;
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == "<h2>Welcome to CodeBuddy!</h2>"


def test_react_curly_brace_expressions():
    code = """
    function Greeting() {
        const name = "Sara";
        return <h3>Hello, {name}!</h3>;
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == "<h3>Hello, Sara!</h3>"


def test_react_props():
    code = """
    function UserBadge(props) {
        return <p>User: {props.name}</p>;
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == "<p>User: Abebe</p>"


def test_react_conditional_rendering():
    code = """
    function Status(props) {
        return <span>{props.online ? "Online" : "Offline"}</span>;
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == "<span>Online</span>"


def test_react_list_mapping():
    code = """
    function TechList() {
        const skills = ["HTML", "CSS", "React"];
        return (
            <ul>
                {skills.map(s => <li key={s}>{s}</li>)}
            </ul>
        );
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == "<ul><li>HTML</li><li>CSS</li><li>React</li></ul>"


def test_react_profile_card_capstone():
    code = """
    function ProfileCard() {
        const user = { name: "Liya", role: "Developer" };
        return (
            <div className="card">
                <h2>{user.name}</h2>
                <p>{user.role}</p>
            </div>
        );
    }
    """
    res = run_student_react_code(code)
    assert res.success is True
    assert res.output == '<div class="card"><h2>Liya</h2><p>Developer</p></div>'


def test_react_syntax_error_handling():
    code = "<div><span>Unclosed"  # missing closing tags
    res = run_student_react_code(code)
    assert res.success is False
    assert "Unclosed JSX Tag" in res.friendly_explanation_en
    assert "ያልተዘጋ የጄኤስኤክስ" in res.friendly_explanation_am


def test_react_curriculum_chapters():
    chapters = get_all_tutor_chapters("react")
    assert len(chapters) == 7
    assert chapters[0].id == "react_ch1"
    assert chapters[6].id == "react_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("react_ch1")
    assert ch1 is not None
    assert ch1.track == "react"

    next_id = get_next_tutor_chapter_id("react_ch1")
    assert next_id == "react_ch2"

    last_next = get_next_tutor_chapter_id("react_ch7")
    assert last_next is None
