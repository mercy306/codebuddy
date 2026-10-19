# CodeBuddy 🤖🇪🇹🇬🇧

**CodeBuddy** is a beginner-friendly Telegram bot designed to teach programming fundamentals from absolute zero using simple, accessible language in both **English** and **Amharic (አማርኛ)**.

---

## 🌟 Implemented Features

### Milestone 1: Bot Foundation & Bilingual Interface
- **aiogram 3 Framework:** Asynchronous Telegram bot built with aiogram 3.
- **Bilingual Interface:** Full localization support for English and Amharic.
- **Language Selection (`/start`):** Welcoming message with inline buttons to switch between English and Amharic.
- **Persistent Preferences:** User language preference is stored in a local SQLite database (`data/codebuddy.db`).
- **Main Navigation Menu:** Interactive keyboard featuring:
  - 📚 **Learn** (*ተማር*)
  - 💻 **Practice** (*ልምምድ*)
  - 📊 **My Progress** (*የእኔ እድገት*)
  - ⚙️ **Settings** (*ቅንብሮች*)
- **Help Command (`/help`):** Localized beginner guide explaining commands and navigation.
- **Friendly Fallback:** Helpful responses when users send unexpected inputs.
- **Secure Configuration:** Bot tokens are loaded via `python-dotenv` from `.env`, masked in logs, and excluded from version control.

### Milestone 2: Interactive "Learn" Curriculum Engine
- **Structured Beginner Modules:**
  - **Module 1**: What is Programming? (*ምዕራፍ 1፦ ፕሮግራሚንግ ምንድን ነው?*)
  - **Module 2**: Variables & Storing Data (*ምዕራፍ 2፦ ቫሪያብሎች እና መረጃ መያዝ*)
  - **Module 3**: Making Decisions with `if` / `else` (*ምዕራፍ 3፦ በኮድ ውሳኔዎችን መስጠት*)
  - **Module 4**: Loops & Repetition (*ምዕራፍ 4፦ ድግግሞሾች - Loops*)
- **Interactive Lesson Reader:**
  - Bite-sized cards with explanations and formatted Python code blocks.
  - Interactive pagination buttons (`[◀ Prev]`, `[Next ▶]`, `[📋 Lessons List]`).
  - Interactive `[✅ Mark as Completed]` action that records progress directly into SQLite.

### Milestone 3: Interactive Practice Arena & Quizzes
- **Interactive Quizzes & Challenges:**
  - Conceptual and code prediction questions mapped to Modules 1–4.
  - Multiple-choice options with instant evaluation.
  - Clear explanations in English and Amharic explaining *why* the answer is correct or incorrect.
  - Sequential progression with `[Next Challenge ▶]` and `[🔄 Try Again]` buttons.

### Milestone 4: Hands-On CodeLab (Writing Real Code)
- **Safe Sandboxed Code Execution:**
  - Real Python code execution with AST-based safety checks (restricts imports, file access, and dangerous builtins).
  - Captures `stdout` output in real time.
  - Generates beginner-friendly error diagnostics for common pitfalls (unclosed quotes, missing parentheses, undefined variables).
- **Direct Chat Code Writing (`/codelab`):**
  - Prompt: Student is given a coding challenge.
  - Action: Student types real Python code directly into Telegram chat!
  - Immediate Evaluation: Bot runs the code, checks the printed output, and either celebrates success or points out where to adjust.
- **Progress Tracking in SQLite:**
  - Records completed code writing exercises in `user_code_challenges` table.
- **Automated Test Suite:** 39 comprehensive tests with `pytest` and `pytest-asyncio`.

---

## 📁 Project Structure

```text
codebuddy/
│
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules for Python, .env, DB, and caches
├── README.md                 # Project documentation and setup guide
├── requirements.txt          # Production and testing dependencies
├── pytest.ini                # Pytest configuration
│
├── bot/
│   ├── __init__.py           # Package initializer
│   ├── config.py             # Secure configuration loader and token masking
│   ├── database.py           # SQLite database manager (async with aiosqlite)
│   ├── strings.py            # Localized strings dictionary (English & Amharic)
│   │
│   ├── curriculum/           # Course content & lesson models
│   │   ├── __init__.py
│   │   ├── models.py         # Module and Lesson dataclasses
│   │   └── data.py           # Bilingual lessons and query helpers
│   │
│   ├── practice/             # Quizzes and interactive challenges
│   │   ├── __init__.py
│   │   ├── models.py         # QuizQuestion dataclass
│   │   └── data.py           # Practice questions and evaluation helpers
│   │
│   ├── codelab/              # Hands-on code writing sandbox
│   │   ├── __init__.py
│   │   ├── sandbox.py        # Safe execution engine & friendly error parser
│   │   └── challenges.py     # Real code writing challenge prompts & solutions
│   │
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── language.py       # Inline keyboard for English / Amharic selection
│   │   ├── learn.py          # Module list, lesson list, and navigation keyboards
│   │   ├── practice.py       # Quiz question, options, and challenge result keyboards
│   │   ├── codelab.py        # CodeLab challenge view, hint, and result keyboards
│   │   └── menu.py           # Reply & inline keyboards for main menu & settings
│   │
│   ├── handlers/
│   │   ├── __init__.py       # Handler registration in priority order
│   │   ├── start.py          # /start command & language callback query handlers
│   │   ├── help.py           # /help localized command handler
│   │   ├── learn.py          # Interactive curriculum, lessons & completion
│   │   ├── practice.py       # Practice arena, quiz questions & instant feedback
│   │   ├── codelab.py        # Real code writing submission and evaluation
│   │   ├── menu.py           # Handlers for Learn, Practice, Progress, Settings
│   │   └── fallback.py       # Polite handler for unrecognized messages
│   │
│   └── main.py               # Application entry point & error logging setup
│
└── tests/
    ├── __init__.py
    ├── conftest.py           # Mock fixtures for Telegram messages & test SQLite DB
    ├── test_codelab.py       # Tests for sandbox, code safety, and real coding challenges
    ├── test_config.py        # Tests for configuration validation & token masking
    ├── test_curriculum.py    # Tests for module models, content & adjacent traversal
    ├── test_database.py      # Tests for SQLite user settings & lesson completion
    ├── test_handlers.py      # Automated tests for start, language callbacks & menus
    ├── test_learn_handlers.py# Tests for curriculum pagination & progress cards
    ├── test_practice.py      # Tests for quizzes, answers, scoring & arena flow
    └── test_strings.py       # Localization parity tests between English & Amharic
```

---

## 🐍 Python Version & Compatibility Notice

> [!IMPORTANT]
> **Recommended Python Version:** **Python 3.12** (or 3.10 / 3.11).
> 
> **Why?** Python 3.15 is currently an unreleased/experimental version for which pre-compiled binary wheels (wheels for packages like `aiohttp` and `pydantic-core`) are not yet available on PyPI for Windows AMD64. Attempting to install them under Python 3.15 requires Microsoft Visual C++ Build Tools and a full Rust (`cargo`) toolchain. Under Python 3.12, pre-compiled wheels install instantly without any compilation dependencies.

---

## 🚀 Windows PowerShell Setup Guide

Follow these steps in **Windows PowerShell** to set up and run CodeBuddy:

### 1. Open PowerShell and Navigate to the Project

```powershell
cd c:\Users\bsd\codebuddy
```

### 2. Set Up the Virtual Environment with Python 3.12

If using Python 3.12 installed via `uv` or the Python Launcher (`py`):

```powershell
# Using uv (fastest)
uv venv --python 3.12 .venv

# Or using standard py launcher
py -3.12 -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

*(If PowerShell script execution is restricted, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first).*

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env.example` file to create your local `.env`:

```powershell
Copy-Item .env.example .env
```

Open `.env` in your editor and insert your Telegram bot token from [@BotFather](https://t.me/BotFather):

```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ_your_token_here
DATABASE_PATH=data/codebuddy.db
LOG_LEVEL=INFO
```

> [!WARNING]
> Never commit your `.env` file to version control. It is already included in `.gitignore`.

### 5. Run the Bot

Launch the bot polling process:

```powershell
python -m bot.main
```

You should see log output similar to:
```text
2026-10-19 12:30:28,445 | INFO     | codebuddy | Starting CodeBuddy bot...
2026-10-19 12:30:28,445 | INFO     | codebuddy | Bot token loaded successfully (8628...c8yc)
2026-10-19 12:30:28,449 | INFO     | bot.database | Database initialized successfully at data\codebuddy.db
2026-10-19 12:30:28,468 | INFO     | codebuddy | Routers registered. Starting long polling...
```

Open Telegram, find your bot, and send `/start`!

---

## 🧪 Running Automated Tests

Run the complete test suite using `pytest`:

```powershell
pytest -v
```

All 39 unit and integration tests will execute against an isolated temporary SQLite database and mock Telegram events.
