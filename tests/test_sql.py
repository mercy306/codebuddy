"""Unit and integration tests for the SQL sandbox runner and curriculum."""

import pytest
from bot.codelab.sql_checker import run_student_sql_code, format_sql_table
from bot.tutor.content import get_all_tutor_chapters, get_tutor_chapter, get_next_tutor_chapter_id
from bot.tutor.content_sql import SQL_SEED_SCRIPT, SQL_TUTOR_CHAPTERS


def test_sql_format_table():
    headers = ["id", "name", "score"]
    rows = [(1, "Abebe", 88), (2, "Sara", 95)]
    output = format_sql_table(headers, rows)
    assert "id" in output
    assert "Abebe" in output
    assert "Sara" in output


def test_sql_basic_select():
    res = run_student_sql_code("SELECT 1 + 1 AS sum;")
    assert res.success is True
    assert "sum" in res.output
    assert "2" in res.output


def test_sql_with_seed_database():
    res = run_student_sql_code("SELECT name, score FROM students WHERE score >= 90;", setup_script=SQL_SEED_SCRIPT)
    assert res.success is True
    assert "Sara" in res.output
    assert "Tigist" in res.output
    assert "Abebe" not in res.output  # score is 88, so filtered out


def test_sql_order_by():
    res = run_student_sql_code("SELECT name, score FROM students ORDER BY score DESC;", setup_script=SQL_SEED_SCRIPT)
    assert res.success is True
    assert "Sara" in res.output
    # Sara (95) should appear before Tigist (91)
    assert res.output.index("Sara") < res.output.index("Tigist")


def test_sql_insert_and_update():
    query = """
    INSERT INTO students (id, name, age, city, score) VALUES (5, 'Marta', 22, 'Addis', 99);
    UPDATE students SET score = 100 WHERE id = 5;
    SELECT name, score FROM students WHERE id = 5;
    """
    res = run_student_sql_code(query, setup_script=SQL_SEED_SCRIPT)
    assert res.success is True
    assert "Marta" in res.output
    assert "100" in res.output


def test_sql_syntax_error_friendly():
    res = run_student_sql_code("SELEC * FROM students;", setup_script=SQL_SEED_SCRIPT)
    assert res.success is False
    assert "Syntax Error" in res.friendly_explanation_en
    assert "የሰዋሰው ስህተት" in res.friendly_explanation_am


def test_sql_prohibited_command():
    res = run_student_sql_code("ATTACH DATABASE 'danger.db' AS d;")
    assert res.success is False
    assert "restricted" in res.error_message


def test_sql_curriculum_chapters():
    chapters = get_all_tutor_chapters("sql")
    assert len(chapters) == 7
    assert chapters[0].id == "sql_ch1"
    assert chapters[6].id == "sql_ch7"

    # Verify lookups and navigation
    ch1 = get_tutor_chapter("sql_ch1")
    assert ch1 is not None
    assert ch1.track == "sql"

    next_id = get_next_tutor_chapter_id("sql_ch1")
    assert next_id == "sql_ch2"

    last_next = get_next_tutor_chapter_id("sql_ch7")
    assert last_next is None
