"""Safe, in-memory SQLite sandbox runner for beginner SQL exercises."""

from __future__ import annotations

import re
import sqlite3
from typing import Dict, List, Optional, Tuple
from bot.codelab.sandbox import ExecutionResult


# Prohibited words that shouldn't be executed in a lightweight student sandbox
PROHIBITED_SQL = {
    "ATTACH",
    "DETACH",
    "PRAGMA",
    "LOAD_EXTENSION",
    "VACUUM",
}

FRIENDLY_SQL_ERRORS_EN = {
    "syntax error": (
        "SQL Syntax Error: Check your keywords and spelling. Did you forget a comma `,` or write a keyword wrong?"
    ),
    "no such table": (
        "Table Not Found: The table you referenced does not exist in this database. Double check table names like `students` or `products`."
    ),
    "no such column": (
        "Column Not Found: One of the column names you typed does not exist. Check your spelling."
    ),
    "ambiguous column name": (
        "Ambiguous Column: That column exists in multiple tables. Prefix it with the table name (e.g. `students.id`)."
    ),
    "incomplete input": (
        "Incomplete Query: Your SQL command is missing something at the end. Check for matching quotes or brackets."
    ),
    "unrecognized token": (
        "Unrecognized Symbol: There is an unexpected character in your SQL query."
    ),
}

FRIENDLY_SQL_ERRORS_AM = {
    "syntax error": (
        "የSQL የሰዋሰው ስህተት (Syntax Error)፦ ቃላቶችን በትክክል መጻፍዎን እና ኮማ `,` አለመርሳትዎን ያረጋግጡ።"
    ),
    "no such table": (
        "ሰንጠረዡ አልተገኘም (No such table)፦ የጠቀሱት የዳታቤዝ ሰንጠረዥ የለም። የሰንጠረዡን ስም ደግመው ያረጋግጡ (ለምሳሌ፦ `students` ወይም `products`)።"
    ),
    "no such column": (
        "አምድ አልተገኘም (No such column)፦ የጻፉት የአምድ ስም በሰንጠረዡ ውስጥ የለም። ፊደላቱን ያረጋግጡ።"
    ),
    "ambiguous column name": (
        "የተምታታ የአምድ ስም፦ ይህ አምድ በሁለቱም ሰንጠረዦች ውስጥ አለ። የሰንጠረዡን ስም አስቀድመው ይጥቀሱ (ለምሳሌ፦ `students.id`)።"
    ),
    "incomplete input": (
        "ያልተሟላ ትዕዛዝ፦ የSQL ትዕዛዝዎ መጨረሻ ላይ የሆነ ነገር ጎድሎታል።"
    ),
    "unrecognized token": (
        "ያልታወቀ ምልክት፦ በትዕዛዝዎ ውስጥ ያልተለመደ ወይም የተሳሳተ ምልክት አለ።"
    ),
}


def _get_friendly_sql_error(raw_err: str) -> Tuple[str, str]:
    err_lower = raw_err.lower()
    for pattern, en_msg in FRIENDLY_SQL_ERRORS_EN.items():
        if pattern in err_lower:
            return en_msg, FRIENDLY_SQL_ERRORS_AM[pattern]
    return (
        f"SQL Error: {raw_err}",
        f"የSQL ስህተት፦ {raw_err}",
    )


def format_sql_table(headers: List[str], rows: List[Tuple]) -> str:
    """Format tabular query results into clean monospace text for Telegram."""
    if not headers:
        return "(Empty table / ምንም አምድ የለም)"

    # Convert all cells to string
    str_rows = [[str(val) if val is not None else "NULL" for val in row] for row in rows]

    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in str_rows:
        for idx, val in enumerate(row):
            if idx < len(col_widths):
                col_widths[idx] = max(col_widths[idx], len(val))

    # Header row
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    separator_line = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    lines = [header_line, separator_line]

    if not str_rows:
        lines.append("(0 rows returned / ምንም መረጃ አልተገኘም)")
    else:
        for row in str_rows[:15]:  # limit to top 15 rows for display
            row_line = " | ".join(val.ljust(col_widths[i]) for i, val in enumerate(row))
            lines.append(row_line)
        if len(str_rows) > 15:
            lines.append(f"... and {len(str_rows) - 15} more rows")

    return "\n".join(lines)


def run_student_sql_code(
    query_str: str,
    setup_script: Optional[str] = None,
) -> ExecutionResult:
    """Execute student SQL query in a safe, isolated in-memory SQLite database."""
    raw = query_str.strip()
    if not raw:
        return ExecutionResult(
            success=False,
            output="",
            error_message="Empty query submitted",
            friendly_explanation_en="Please write a SQL query before submitting!",
            friendly_explanation_am="እባክዎ ከመላክዎ በፊት የSQL ትዕዛዝ ይጻፉ!",
        )

    # Check prohibited keywords
    tokens = re.findall(r"\b[A-Za-z_]+\b", raw.upper())
    for t in tokens:
        if t in PROHIBITED_SQL:
            return ExecutionResult(
                success=False,
                output="",
                error_message=f"Command '{t}' is restricted.",
                friendly_explanation_en=f"For security reasons, `{t}` is not permitted in CodeBuddy exercises.",
                friendly_explanation_am=f"ለደህንነት ሲባል `{t}` በኮድበዲ ልምምዶች ውስጥ አልተፈቀደም።",
            )

    # Execute in an isolated in-memory database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    try:
        # Run optional setup script (e.g. creating seed tables)
        if setup_script:
            cursor.executescript(setup_script)

        # Run student statement(s)
        # We split by semicolon to allow multi-statements (e.g. INSERT then SELECT)
        statements = [s.strip() for s in raw.split(";") if s.strip()]

        last_headers: List[str] = []
        last_rows: List[Tuple] = []
        is_select = False
        total_changes = 0

        for stmt in statements:
            cursor.execute(stmt)
            if cursor.description:
                # It returned tabular rows (e.g. SELECT)
                is_select = True
                last_headers = [col[0] for col in cursor.description]
                last_rows = cursor.fetchall()
            else:
                total_changes += cursor.rowcount

        conn.commit()

        if is_select:
            table_display = format_sql_table(last_headers, last_rows)
            row_count_str = f"({len(last_rows)} row{'s' if len(last_rows) != 1 else ''})"
            output = f"📊 Query Result {row_count_str}:\n```text\n{table_display}\n```"
        else:
            output = f"✅ Query executed successfully! Rows affected: {max(0, total_changes)}"

        return ExecutionResult(
            success=True,
            output=output,
        )

    except sqlite3.Error as e:
        err_msg = str(e)
        en_expl, am_expl = _get_friendly_sql_error(err_msg)
        return ExecutionResult(
            success=False,
            output="",
            error_message=err_msg,
            friendly_explanation_en=en_expl,
            friendly_explanation_am=am_expl,
        )
    finally:
        conn.close()
