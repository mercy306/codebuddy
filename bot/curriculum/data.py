"""Curriculum data definitions and helper query functions."""

from __future__ import annotations
from typing import List, Optional, Tuple
from bot.curriculum.models import Module, Lesson

MODULES: List[Module] = [
    Module(
        id="m1",
        order=1,
        title_en="Module 1: What is Programming?",
        title_am="ምዕራፍ 1፦ ፕሮግራሚንግ ምንድን ነው?",
        description_en="Learn how humans talk to computers and run your very first command.",
        description_am="ሰዎች ከኮምፒውተር ጋር እንዴት እንደሚግባቡ ይማሩ እና የመጀመሪያውን ትዕዛዝ ያሂዱ።",
        lessons=[
            Lesson(
                id="m1_l1",
                module_id="m1",
                order=1,
                title_en="1.1 Giving Instructions to Computers",
                title_am="1.1 ለኮምፒውተር ትዕዛዝ መስጠት",
                content_en=(
                    "📖 *Lesson 1.1: Giving Instructions to Computers*\n\n"
                    "Think of programming like writing a cooking recipe! 🍳\n\n"
                    "A computer is super fast, but it only does exactly what we tell it to do, step-by-step.\n\n"
                    "In Python, when we want the computer to display words on the screen, we use the `print()` command:\n\n"
                    "```python\n"
                    'print("Hello, CodeBuddy!")\n'
                    "```\n\n"
                    "💡 *Key Takeaway:*\n"
                    "Whatever text you put inside quotes `\" \"` inside `print(...)` is shown to the user on the screen."
                ),
                content_am=(
                    "📖 *ትምህርት 1.1፦ ለኮምፒውተር ትዕዛዝ መስጠት*\n\n"
                    "ፕሮግራሚንግ ልክ እንደ ምግብ ማብሰያ መመሪያ (Recipe) ነው! 🍳\n\n"
                    "ኮምፒውተር እጅግ ፈጣን ነው፣ ነገር ግን እኛ ደረጃ በደረጃ የነገርነውን ብቻ በትክክል ይፈጽማል።\n\n"
                    "በፓይተን (Python) ኮምፒውተሩ በማያ ገጹ ላይ ጽሁፍ እንዲያሳይ ስንፈልግ `print()` የሚለውን ትዕዛዝ እንጠቀማለን፦\n\n"
                    "```python\n"
                    'print("ሰላም፣ ኮድበዲ!")\n'
                    "```\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "በጥቅስ ምልክት `\" \"` ውስጥ ያደረጉትን ማንኛውንም ጽሁፍ ኮምፒውተሩ በማያ ገጹ ላይ ያሳያል።"
                ),
            ),
            Lesson(
                id="m1_l2",
                module_id="m1",
                order=2,
                title_en="1.2 Working with Numbers",
                title_am="1.2 ከቁጥሮች ጋር መስራት",
                content_en=(
                    "📖 *Lesson 1.2: Working with Numbers*\n\n"
                    "Computers love math! 🧮 Unlike text, numbers don't need quotation marks `\" \"`.\n\n"
                    "Look at this code:\n\n"
                    "```python\n"
                    "print(10 + 5)\n"
                    "print(20 * 2)\n"
                    "```\n\n"
                    "Output:\n"
                    "```text\n"
                    "15\n"
                    "40\n"
                    "```\n\n"
                    "💡 *Key Takeaway:*\n"
                    "Text requires quotes `\"hello\"`, but numbers `10` are written directly so the computer can calculate them."
                ),
                content_am=(
                    "📖 *ትምህርት 1.2፦ ከቁጥሮች ጋር መስራት*\n\n"
                    "ኮምፒውተሮች ሂሳብ መስራት በጣም ይወዳሉ! 🧮 ከቃላት በተለየ ቁጥሮች የጥቅስ ምልክት `\" \"` አያስፈልጋቸውም።\n\n"
                    "ይህንን ኮድ ይመልከቱ፦\n\n"
                    "```python\n"
                    "print(10 + 5)\n"
                    "print(20 * 2)\n"
                    "```\n\n"
                    "ውጤት፦\n"
                    "```text\n"
                    "15\n"
                    "40\n"
                    "```\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "ጽሁፍ በጥቅስ ምልክት `\"ሰላም\"` ይቀመጣል፤ ቁጥሮች ግን ኮምፒውተሩ በቀጥታ እንዲያሰላቸው ያለ ጥቅስ ምልክት ይጻፋሉ።"
                ),
            ),
        ],
    ),
    Module(
        id="m2",
        order=2,
        title_en="Module 2: Variables & Storing Data",
        title_am="ምዕራፍ 2፦ ቫሪያብሎች እና መረጃ መያዝ",
        description_en="Learn how to store names, scores, and numbers using labeled boxes called variables.",
        description_am="ስሞችን፣ ውጤቶችን እና ቁጥሮችን ቫሪያብል (Variables) በሚባሉ ሳጥኖች ውስጥ እንዴት ማስቀመጥ እንደሚቻል ይማሩ።",
        lessons=[
            Lesson(
                id="m2_l1",
                module_id="m2",
                order=1,
                title_en="2.1 What is a Variable?",
                title_am="2.1 ቫሪያብል ምንድን ነው?",
                content_en=(
                    "📖 *Lesson 2.1: What is a Variable?*\n\n"
                    "Imagine a storage box with a label on it 📦. In programming, that box is called a *Variable*.\n\n"
                    "You give the box a name, and store any value inside it:\n\n"
                    "```python\n"
                    'student_name = "Almaz"\n'
                    "user_age = 20\n\n"
                    'print("Student:", student_name)\n'
                    'print("Age:", user_age)\n'
                    "```\n\n"
                    "💡 *Key Takeaway:*\n"
                    "The `=` symbol doesn't mean equal in math here—it means *store* the value on the right into the box on the left!"
                ),
                content_am=(
                    "📖 *ትምህርት 2.1፦ ቫሪያብል ምንድን ነው?*\n\n"
                    "ስም የተለጠፈበት የእቃ መያዣ ሳጥን በዓይነ-ህሊናዎ ይሳሉ 📦። በኮዲንግ ይህ ሳጥን *ቫሪያብል (Variable)* ይባላል።\n\n"
                    "ለሳጥኑ ስም ትሰጡታላችሁ፣ ከዚያም የፈለጋችሁትን መረጃ ውስጡ ታስቀምጣላችሁ፦\n\n"
                    "```python\n"
                    'student_name = "አልማዝ"\n'
                    "user_age = 20\n\n"
                    'print("ተማሪ፦", student_name)\n'
                    'print("ዕድሜ፦", user_age)\n'
                    "```\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "እዚህ ላይ የ `=` ምልክት በቀኝ በኩል ያለውን መረጃ በግራ በኩል ወዳለው ሳጥን *አስቀምጥ* ማለት ነው።"
                ),
            ),
            Lesson(
                id="m2_l2",
                module_id="m2",
                order=2,
                title_en="2.2 Updating Variables",
                title_am="2.2 ቫሪያብሎችን መቀየር",
                content_en=(
                    "📖 *Lesson 2.2: Updating Variables*\n\n"
                    "The word *variable* comes from 'vary' (it can change!) 🔄\n\n"
                    "In a game, your score changes as you play:\n\n"
                    "```python\n"
                    "score = 0\n"
                    "score = score + 10\n"
                    "print(score)\n"
                    "```\n\n"
                    "The computer evaluates `0 + 10` and places `10` back into `score`.\n\n"
                    "💡 *Key Takeaway:*\n"
                    "Variables can be updated anytime as your program runs."
                ),
                content_am=(
                    "📖 *ትምህርት 2.2፦ ቫሪያብሎችን መቀየር*\n\n"
                    "*ቫሪያብል* ማለት ተለዋዋጭ ማለት ነው 🔄\n\n"
                    "በአንድ ጨዋታ ውስጥ ውጤትዎ እየተጫወቱ ሲሄዱ እንደሚቀየረው ሁሉ፦\n\n"
                    "```python\n"
                    "score = 0\n"
                    "score = score + 10\n"
                    "print(score)\n"
                    "```\n\n"
                    "ኮምፒውተሩ `0 + 10`ን ያሰላና `10`ን ወደ `score` መልሶ ያስቀምጣል።\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "ፕሮግራሙ በሚሰራበት ጊዜ የቫሪያብል እሴት በማንኛውም ሰዓት ሊቀየር ይችላል።"
                ),
            ),
        ],
    ),
    Module(
        id="m3",
        order=3,
        title_en="Module 3: Making Decisions with Conditions",
        title_am="ምዕራፍ 3፦ በኮድ ውሳኔዎችን መስጠት",
        description_en="Teach your programs how to think and choose actions using if and else.",
        description_am="ፕሮግራሞችዎ በ `if` እና `else` ተጠቅመው እንዴት ማሰብ እና መወሰን እንደሚችሉ ይማሩ።",
        lessons=[
            Lesson(
                id="m3_l1",
                module_id="m3",
                order=1,
                title_en="3.1 If Statements",
                title_am="3.1 የ If ውሳኔዎች",
                content_en=(
                    "📖 *Lesson 3.1: If Statements*\n\n"
                    "In real life: *If it rains, take an umbrella.* ☔\n\n"
                    "In Python, we use `if` to check conditions:\n\n"
                    "```python\n"
                    "battery = 15\n\n"
                    "if battery < 20:\n"
                    '    print("⚠️ Low battery! Please plug in charger.")\n'
                    "```\n\n"
                    "Notice the 4 spaces indent before `print`. That tells Python this action belongs inside the `if`!"
                ),
                content_am=(
                    "📖 *ትምህርት 3.1፦ የ If ውሳኔዎች*\n\n"
                    "በእውነተኛ ህይወት፦ *ዝናብ ከዘነበ፣ ጃንጥላ ያዙ።* ☔\n\n"
                    "በፓይተን ሁኔታዎችን ለመፈተሽ `if`ን እንጠቀማለን፦\n\n"
                    "```python\n"
                    "battery = 15\n\n"
                    "if battery < 20:\n"
                    '    print("⚠️ ባትሪው አነስተኛ ነው! ቻርጀር ይሰኩ።")\n'
                    "```\n\n"
                    "ከ `print` በፊት ያለውን የ 4 ክፍተቶች (Indentation) ልብ ይበሉ። ይህ ፓይተን ድርጊቱ የ `if` አካል መሆኑን እንዲያውቅ ያደርጋል!"
                ),
            ),
            Lesson(
                id="m3_l2",
                module_id="m3",
                order=2,
                title_en="3.2 Adding Else",
                title_am="3.2 Else (ካልሆነ) መጨመር",
                content_en=(
                    "📖 *Lesson 3.2: Adding Else*\n\n"
                    "What happens when the condition is NOT true? That's what `else` is for! 🔀\n\n"
                    "```python\n"
                    "score = 75\n\n"
                    "if score >= 50:\n"
                    '    print("🎉 Congratulations, you passed!")\n'
                    "else:\n"
                    '    print("💪 Keep practicing, you can do it!")\n'
                    "```\n\n"
                    "💡 *Key Takeaway:*\n"
                    "Only one branch runs: if the condition is True, the `if` block runs; otherwise, the `else` block runs."
                ),
                content_am=(
                    "📖 *ትምህርት 3.2፦ Else (ካልሆነ) መጨመር*\n\n"
                    "ሁኔታው እውነት ካልሆነ ምን ይደረግ? ለዚህ ነው `else` የሚያስፈልገው! 🔀\n\n"
                    "```python\n"
                    "score = 75\n\n"
                    "if score >= 50:\n"
                    '    print("🎉 እንኳን ደስ አለዎት፣ አልፈዋል!")\n'
                    "else:\n"
                    '    print("💪 ልምምድዎን ይቀጥሉ፣ ይችላሉ!")\n'
                    "```\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "ከሁለቱ አንዱ ብቻ ይከናወናል፦ ሁኔታው እውነት ከሆነ የ `if` ክፍል፣ ካልሆነ ግን የ `else` ክፍል ይሰራል።"
                ),
            ),
        ],
    ),
    Module(
        id="m4",
        order=4,
        title_en="Module 4: Loops & Repetition",
        title_am="ምዕራፍ 4፦ ድግግሞሾች (Loops)",
        description_en="Learn how to repeat actions effortlessly without writing the same line twice.",
        description_am="አንድ አይነት የኮድ መስመር ደጋግመው ሳይጽፉ ስራዎችን በራስ-ሰር እንዴት መድገም እንደሚቻል ይማሩ።",
        lessons=[
            Lesson(
                id="m4_l1",
                module_id="m4",
                order=1,
                title_en="4.1 The Power of Loops",
                title_am="4.1 የድግግሞሽ (Loop) ኃይል",
                content_en=(
                    "📖 *Lesson 4.1: The Power of Loops*\n\n"
                    "Imagine having to say 'Good morning' 100 times! 😴\n\n"
                    "Instead of typing 100 lines, a `for` loop does it in just 2 lines:\n\n"
                    "```python\n"
                    "for i in range(5):\n"
                    '    print("Good morning! ☀️")\n'
                    "```\n\n"
                    "💡 *Key Takeaway:*\n"
                    "`range(5)` tells the computer to repeat 5 times: 0, 1, 2, 3, 4."
                ),
                content_am=(
                    "📖 *ትምህርት 4.1፦ የድግግሞሽ (Loop) ኃይል*\n\n"
                    "'እንደምን አደሩ' የሚለውን 100 ጊዜ መጻፍ እንዳለብዎት ያስቡ! 😴\n\n"
                    "100 መስመር ከመጻፍ ይልቅ `for` loop በ 2 መስመር ብቻ ያከናውነዋል፦\n\n"
                    "```python\n"
                    "for i in range(5):\n"
                    '    print("እንደምን አደሩ! ☀️")\n'
                    "```\n\n"
                    "💡 *ዋና ነጥብ፦*\n"
                    "`range(5)` ለኮምፒውተሩ ስራውን 5 ጊዜ እንዲደግመው ይነግረዋል (0, 1, 2, 3, 4)።"
                ),
            ),
            Lesson(
                id="m4_l2",
                module_id="m4",
                order=2,
                title_en="4.2 Looping Over Lists",
                title_am="4.2 ዝርዝሮችን በድግግሞሽ ማሰስ",
                content_en=(
                    "📖 *Lesson 4.2: Looping Over Lists*\n\n"
                    "You can loop through a list of items one by one:\n\n"
                    "```python\n"
                    'fruits = ["Apple 🍎", "Banana 🍌", "Orange 🍊"]\n\n'
                    "for fruit in fruits:\n"
                    '    print("I like", fruit)\n'
                    "```\n\n"
                    "🎉 *Congratulations!* You have completed the foundational beginner modules!"
                ),
                content_am=(
                    "📖 *ትምህርት 4.2፦ ዝርዝሮችን በድግግሞሽ ማሰስ*\n\n"
                    "የተዘረዘሩ እቃዎችን አንድ በአንድ በ loop ማሰስ ይችላሉ፦\n\n"
                    "```python\n"
                    'fruits = ["ፖም 🍎", "ሙዝ 🍌", "ብርቱካን 🍊"]\n\n'
                    "for fruit in fruits:\n"
                    '    print("እወዳለሁ፦", fruit)\n'
                    "```\n\n"
                    "🎉 *እንኳን ደስ አለዎት!* መሰረታዊ የጀማሪ ምዕራፎችን አጠናቀዋል!"
                ),
            ),
        ],
    ),
]


def get_all_modules() -> List[Module]:
    """Return all curriculum modules ordered."""
    return sorted(MODULES, key=lambda m: m.order)


def get_module(module_id: str) -> Optional[Module]:
    """Retrieve module by its identifier."""
    for mod in MODULES:
        if mod.id == module_id:
            return mod
    return None


def get_lesson(lesson_id: str) -> Tuple[Optional[Module], Optional[Lesson]]:
    """Retrieve parent module and lesson by lesson_id."""
    for mod in MODULES:
        for les in mod.lessons:
            if les.id == lesson_id:
                return mod, les
    return None, None


def get_adjacent_lessons(lesson_id: str) -> Tuple[Optional[str], Optional[str]]:
    """Return previous and next lesson IDs across the entire curriculum."""
    all_lessons: List[Lesson] = []
    for mod in get_all_modules():
        all_lessons.extend(mod.lessons)

    for idx, les in enumerate(all_lessons):
        if les.id == lesson_id:
            prev_id = all_lessons[idx - 1].id if idx > 0 else None
            next_id = all_lessons[idx + 1].id if idx + 1 < len(all_lessons) else None
            return prev_id, next_id

    return None, None


def get_total_lessons_count() -> int:
    """Return total number of lessons across all modules."""
    return sum(len(m.lessons) for m in MODULES)
