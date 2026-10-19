"""Localized strings for CodeBuddy bot in English and Amharic."""

from __future__ import annotations
from typing import Dict

# Language codes supported
LANG_EN = "en"
LANG_AM = "am"
SUPPORTED_LANGUAGES = (LANG_EN, LANG_AM)
DEFAULT_LANGUAGE = LANG_EN

STRINGS: Dict[str, Dict[str, str]] = {
    # Greetings & Onboarding
    "welcome": {
        LANG_EN: (
            "👋 Welcome to *CodeBuddy*!\n\n"
            "I'm here to teach you programming from absolute zero in simple, "
            "beginner-friendly steps.\n\n"
            "Please select your preferred language / እባክዎ ቋንቋ ይምረጡ:"
        ),
        LANG_AM: (
            "👋 ወደ *ኮድበዲ (CodeBuddy)* እንኳን በደህና መጡ!\n\n"
            "ፕሮግራሚንግን ከመሰረቱ ጀምሮ በቀላል ደረጃዎች እንማማራለን።\n\n"
            "እባክዎ የሚፈልጉትን ቋንቋ ይምረጡ / Please select your preferred language:"
        ),
    },
    "choose_language": {
        LANG_EN: "🌐 Please select your preferred language:",
        LANG_AM: "🌐 እባክዎ የሚመርጡትን ቋንቋ ይምረጡ፦",
    },
    "language_selected": {
        LANG_EN: "✅ Language set to *English*! Welcome to your coding journey.",
        LANG_AM: "✅ ቋንቋው ወደ *አማርኛ* ተቀይሯል! እንኳን ወደ ኮዲንግ ጉዞዎ በደህና መጡ።",
    },
    # Main Navigation Menu
    "main_menu_title": {
        LANG_EN: "What would you like to explore today? Choose an option below:",
        LANG_AM: "ዛሬ ምን ማሰስ ይፈልጋሉ? ከዚህ በታች ካሉት አንዱን ይምረጡ፦",
    },
    "btn_learn": {
        LANG_EN: "📚 Learn",
        LANG_AM: "📚 ተማር",
    },
    "btn_practice": {
        LANG_EN: "💻 Practice",
        LANG_AM: "💻 ልምምድ",
    },
    "btn_progress": {
        LANG_EN: "📊 My Progress",
        LANG_AM: "📊 የእኔ እድገት",
    },
    "btn_settings": {
        LANG_EN: "⚙️ Settings",
        LANG_AM: "⚙️ ቅንብሮች",
    },
    "btn_change_language": {
        LANG_EN: "🌐 Change Language",
        LANG_AM: "🌐 ቋንቋ ቀይር",
    },
    "btn_reset_progress": {
        LANG_EN: "🔄 Reset / Start from Beginning",
        LANG_AM: "🔄 እድገት አድስ / ከመጀመሪያ ጀምር",
    },
    "btn_start_first_lesson": {
        LANG_EN: "🚀 Start Lesson 1.1",
        LANG_AM: "🚀 የመጀመሪያውን ትምህርት ጀምር",
    },
    "reset_success_alert": {
        LANG_EN: "🔄 Progress reset! You are starting completely from the beginning.",
        LANG_AM: "🔄 እድገትዎ ታድሷል! ከመጀመሪያ ጀምረዋል።",
    },
    # Learning Navigation Strings
    "learn_modules_title": {
        LANG_EN: "📚 *Programming Curriculum*\n\nSelect a module below to start learning:",
        LANG_AM: "📚 *የፕሮግራሚንግ ማውጫ*\n\nመማር ለመጀመር ከዚህ በታች ካሉት ምዕራፎች አንዱን ይምረጡ፦",
    },
    "lessons_list_title": {
        LANG_EN: "📖 *Lessons in {module_title}:*\n\nChoose a lesson to begin:",
        LANG_AM: "📖 *በ{module_title} ውስጥ ያሉ ትምህርቶች፦*\n\nለመጀመር አንድ ትምህርት ይምረጡ፦",
    },
    "btn_complete_lesson": {
        LANG_EN: "✅ Mark as Completed",
        LANG_AM: "✅ እንደተጠናቀቀ ምልክት አድርግ",
    },
    "btn_lesson_completed": {
        LANG_EN: "🎉 Completed!",
        LANG_AM: "🎉 ተጠናቋል!",
    },
    "btn_next_lesson": {
        LANG_EN: "Next ▶",
        LANG_AM: "ቀጣይ ▶",
    },
    "btn_prev_lesson": {
        LANG_EN: "◀ Prev",
        LANG_AM: "◀ ቀዳሚ",
    },
    "btn_back_to_lessons": {
        LANG_EN: "📋 Lessons List",
        LANG_AM: "📋 የትምህርቶች ዝርዝር",
    },
    "btn_back_to_modules": {
        LANG_EN: "📚 All Modules",
        LANG_AM: "📚 ሁሉም ምዕራፎች",
    },
    "lesson_completed_alert": {
        LANG_EN: "🎉 Great job! Lesson marked as completed.",
        LANG_AM: "🎉 በጣም ጎበዝ! ትምህርቱን በተሳካ ሁኔታ አጠናቀዋል።",
    },
    # Practice Navigation Strings
    "practice_hub_title": {
        LANG_EN: (
            "💻 *Practice Arena*\n\n"
            "Sharpen your coding skills with interactive quizzes and code prediction challenges!\n\n"
            "Choose an option below to test what you've learned:"
        ),
        LANG_AM: (
            "💻 *የልምምድ ሜዳ*\n\n"
            "በቀላል ጥያቄዎች እና የኮድ ውጤት መገመቻ ፈተናዎች እውቀትዎን ያዳብሩ!\n\n"
            "የተማሩትን ለመፈተሽ ከዚህ በታች ይምረጡ፦"
        ),
    },
    # Section contents
    "learn_content": {
        LANG_EN: (
            "📚 *Learn Programming*\n\n"
            "We will guide you step-by-step through:\n"
            "• *What is Code?* - Giving instructions to computers\n"
            "• *Variables* - Storing information like numbers and words\n"
            "• *Conditions* - Making decisions with `if` and `else`\n"
            "• *Loops* - Repeating actions without repeating yourself\n\n"
            "Tap a module below to begin your lessons!"
        ),
        LANG_AM: (
            "📚 *ፕሮግራሚንግ መማር*\n\n"
            "ደረጃ በደረጃ የምንማራቸው ዋና ዋና ክፍሎች፦\n"
            "• *ኮዲንግ ምንድን ነው?* - ለኮምፒውተር ትዕዛዝ መስጠት\n"
            "• *ቫሪያብል (Variables)* - መረጃዎችን እና ቁጥሮችን መያዝ\n"
            "• *ሁኔታዎች (Conditions)* - በ `if` እና `else` ውሳኔዎችን መስጠት\n"
            "• *ድግግሞሾች (Loops)* - ስራዎችን ደጋግሞ ማከናወን\n\n"
            "ትምህርቶችን ለመጀመር ከታች ካሉት ምዕራፎች አንዱን ይጫኑ!"
        ),
    },
    "practice_content": {
        LANG_EN: (
            "💻 *Practice Arena*\n\n"
            "Practice makes permanent! Here you will test your knowledge with:\n"
            "• Quick bite-sized quizzes\n"
            "• Code prediction puzzles\n"
            "• Hands-on coding exercises\n\n"
            "Choose a challenge below to start practicing!"
        ),
        LANG_AM: (
            "💻 *የልምምድ ሜዳ*\n\n"
            "ልምምድ እውቀትን ያጠነክራል! እዚህ ያወቁትን ይፈትሻሉ፦\n"
            "• አጫጭር እና ቀላል ጥያቄዎች\n"
            "• የኮድ ውጤት መገመት\n"
            "• ተግባራዊ የኮዲንግ ልምምዶች\n\n"
            "መለማመድ ለመጀመር ከታች ካሉት ፈተናዎች አንዱን ይምረጡ!"
        ),
    },
    "progress_content": {
        LANG_EN: (
            "📊 *My Learning Progress*\n\n"
            "👤 *Status:* Beginner\n"
            "📖 *Completed Lessons:* 0\n"
            "🎯 *Solved Exercises:* 0\n"
            "🔥 *Current Streak:* 1 Day\n\n"
            "Keep showing up every day! Consistency is key to learning code."
        ),
        LANG_AM: (
            "📊 *የእኔ የመማር እድገት*\n\n"
            "👤 *ደረጃ፦* ጀማሪ\n"
            "📖 *የተጠናቀቁ ትምህርቶች፦* 0\n"
            "🎯 *የተፈቱ ልምምዶች፦* 0\n"
            "🔥 *የቀናት ተከታታይነት፦* 1 ቀን\n\n"
            "በየቀኑ መለማመድዎን ይቀጥሉ! የኮዲንግ ሚስጥር ተከታታይነት ነው።"
        ),
    },
    "settings_content": {
        LANG_EN: (
            "⚙️ *Settings*\n\n"
            "You can update your language preference or customize your experience below:"
        ),
        LANG_AM: (
            "⚙️ *ቅንብሮች*\n\n"
            "ከዚህ በታች የመረጡትን ቋንቋ መቀየር ይችላሉ፦"
        ),
    },
    # Help command
    "help": {
        LANG_EN: (
            "ℹ️ *CodeBuddy Help Guide*\n\n"
            "CodeBuddy teaches programming to complete beginners in plain English and Amharic.\n\n"
            "*Available Commands:*\n"
            "• /start - Welcome screen and language selection\n"
            "• /menu - Open the main menu\n"
            "• /tutor - Interactive conversational tutor (step-by-step dialogue)\n"
            "• /codelab - Write and run real Python code\n"
            "• /learn - Browse programming modules & lessons\n"
            "• /practice - Open the practice quizzes arena\n"
            "• /help - Show this guide\n"
            "• /settings - Change language and preferences\n\n"
            "💡 *Tip:* Use the buttons at the bottom of your screen to navigate quickly!"
        ),
        LANG_AM: (
            "ℹ️ *የኮድበዲ አጋዥ መመሪያ*\n\n"
            "ኮድበዲ ለጀማሪዎች ፕሮግራሚንግን በቀላል አማርኛ እና እንግሊዝኛ ያስተምራል።\n\n"
            "*ጠቃሚ ትዕዛዞች:*\n"
            "• /start - ቦቱን እንደገና ለማስጀመር እና ቋንቋ ለመምረጥ\n"
            "• /menu - ዋናውን ማውጫ ለመክፈት\n"
            "• /tutor - በደረጃ የሚያስተምር የግል አስተማሪ (ውይይት)\n"
            "• /codelab - እውነተኛ የፓይተን ኮድ መጻፍ እና መሞከር\n"
            "• /learn - የትምህርት ምዕራፎችን ለማሰስ\n"
            "• /practice - የልምምድ ጥያቄዎችን ለመጀመር\n"
            "• /help - ይህን መመሪያ ለማየት\n"
            "• /settings - ቋንቋ እና ሌሎች ቅንብሮችን ለመቀየር\n\n"
            "💡 *ምክር፦* በቀላሉ ለመጠቀም በማያ ገጽዎ ግርጌ ያሉትን ቁልፎች ይጠቀሙ!"
        ),
    },
    # Fallback / Unknown messages
    "unknown_message": {
        LANG_EN: (
            "🤖 I didn't recognize that message.\n\n"
            "Please use the menu buttons below or send /help to see what I can do!"
        ),
        LANG_AM: (
            "🤖 ይቅርታ፣ የላኩት መልእክት አልገባኝም።\n\n"
            "እባክዎ ከታች ያሉትን ቁልፎች ይጠቀሙ ወይም /help ብለው ይጻፉ!"
        ),
    },
}


def get_string(key: str, lang: str = DEFAULT_LANGUAGE) -> str:
    """Retrieve localized string by key and language code with safe fallback."""
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE

    key_dict = STRINGS.get(key)
    if not key_dict:
        return f"[{key}]"

    return key_dict.get(lang) or key_dict.get(DEFAULT_LANGUAGE, f"[{key}]")


def build_progress_card(
    completed_count: int,
    total_count: int,
    solved_quizzes: int = 0,
    total_quizzes: int = 0,
    lang: str = DEFAULT_LANGUAGE,
) -> str:
    """Build a visual progress message with a percentage bar and quiz score."""
    total_items = total_count + total_quizzes
    completed_items = completed_count + solved_quizzes

    if total_items <= 0:
        percent = 0
    else:
        percent = int((completed_items / total_items) * 100)

    # Visual 10-block bar: e.g. [████░░░░░░]
    filled_blocks = min(10, max(0, percent // 10))
    empty_blocks = 10 - filled_blocks
    progress_bar = f"[{'█' * filled_blocks}{'░' * empty_blocks}] {percent}%"

    if percent >= 100:
        level_en = "Champion Coder 🏆"
        level_am = "የኮዲንግ ሻምፒዮን 🏆"
    elif percent >= 50:
        level_en = "Intermediate Explorer 🚀"
        level_am = "አሳሽ ተማሪ 🚀"
    else:
        level_en = "Beginning Explorer 🌱"
        level_am = "ጀማሪ አሳሽ 🌱"

    if lang == LANG_AM:
        return (
            "📊 *የእኔ የመማር እድገት*\n\n"
            f"👤 *ደረጃ፦* {level_am}\n"
            f"📈 *አጠቃላይ እድገት፦* {progress_bar}\n"
            f"📖 *የተጠናቀቁ ትምህርቶች፦* {completed_count} ከ {total_count}\n"
            f"🎯 *የተፈቱ ፈተናዎች፦* {solved_quizzes} ከ {total_quizzes}\n"
            "🔥 *የቀናት ተከታታይነት፦* 1 ቀን\n\n"
            "በየቀኑ መለማመድዎን ይቀጥሉ! የኮዲንግ ሚስጥር ተከታታይነት ነው።"
        )

    return (
        "📊 *My Learning Progress*\n\n"
        f"👤 *Level:* {level_en}\n"
        f"📈 *Overall Progress:* {progress_bar}\n"
        f"📖 *Completed Lessons:* {completed_count} of {total_count}\n"
        f"🎯 *Solved Quizzes:* {solved_quizzes} of {total_quizzes}\n"
        "🔥 *Current Streak:* 1 Day\n\n"
        "Keep showing up every day! Consistency is key to learning code."
    )
