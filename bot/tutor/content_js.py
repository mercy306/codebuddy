"""JavaScript curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

JS_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="js_ch1",
        order=1,
        title_en="JS Ch 1: Meet JavaScript & First Web Code",
        title_am="ጄኤስ ምዕራፍ 1፦ ከጃቫስክሪፕት ጋር መተዋወቅ እና የመጀመሪያ ኮድ",
        description_en="Learn how the language of the Internet displays words and calculates numbers.",
        description_am="የኢንተርኔት እና የድህረ-ገጾች ቋንቋ የሆነው ጃቫስክሪፕት ጽሁፎችን እና ቁጥሮችን እንዴት እንደሚያሳይ ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌐 *Welcome to JavaScript (JS)!* 🚀\n\n"
                    "If HTML is the skeleton of a website and CSS is the clothing, "
                    "**JavaScript is the living brain!**\n\n"
                    "Every button click, popup, like button, and interactive animation on the web "
                    "runs on JavaScript.\n\n"
                    "Ready to send your first message to the JavaScript engine?"
                ),
                message_am=(
                    "🌐 *እንኳን ወደ ጃቫስክሪፕት (JavaScript) በደህና መጡ!* 🚀\n\n"
                    "ድህረ-ገጾችን (Websites) እንደ ሰው ብናስብ፣ HTML አጥንቱ፣ CSS ልብሱ ሲሆን፣ "
                    "**ጃቫስክሪፕት ህያው አእምሮው ነው!**\n\n"
                    "በኢንተርኔት ላይ የሚጫኗቸው አዝራሮች፣ አኒሜሽኖች እና ቻቶች በሙሉ በጃቫስክሪፕት ይሰራሉ።\n\n"
                    "የመጀመሪያውን የጃቫስክሪፕት ትዕዛዝ ለመስጠት ዝግጁ ነዎት?"
                ),
            ),
            TutorStep(
                id="js_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "In JavaScript, we tell the computer to display text using `console.log()`.\n\n"
                    "Text goes inside quotation marks `\" \"`:\n\n"
                    "👇 *Type this exact code in the chat right now:*\n"
                    '```javascript\nconsole.log("Hello Web!");\n```'
                ),
                message_am=(
                    "በጃቫስክሪፕት ውስጥ ጽሁፍ በስክሪኑ ላይ እንዲወጣ `console.log()` የሚለውን ትዕዛዝ እንጠቀማለን።\n\n"
                    "ጽሁፉ በጥቅስ ምልክት `\" \"` ውስጥ ይቀመጣል፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```javascript\nconsole.log("Hello Web!");\n```'
                ),
                expected_code_output="Hello Web!",
                hint_en='Write `console.log("Hello Web!");` with quotes and parentheses!',
                hint_am='በጥቅስ እና በቅንፍ `console.log("Hello Web!");` ብለው ይጻፉ!',
                success_message_en=(
                    "🎉 *Look at that!* You just ran real JavaScript in the engine and printed `Hello Web!`!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* እውነተኛ የጃቫስክሪፕት ኮድ በማስኬድ `Hello Web!` ብለው አሳይተዋል!"
                ),
            ),
            TutorStep(
                id="js_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "Quick question: In Python we used `print()`. What do we use in JavaScript?"
                ),
                message_am=(
                    "ፈጣን ጥያቄ፦ በፓይተን `print()` ስንጠቀም፣ በጃቫስክሪፕት ውስጥ የምንጠቀመው የትኛውን ነው?"
                ),
                options_en=[
                    "console.log() 🖥️",
                    "display.now()",
                    "show_text()",
                ],
                options_am=[
                    "console.log() 🖥️",
                    "display.now()",
                    "show_text()",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* `console.log()` is the universally used command in JS to inspect and display data.",
                success_message_am="🎯 *ትክክል ነው!* በጃቫስክሪፕት ውስጥ ውጤትን ለማሳየት `console.log()`ን እንጠቀማለን።",
            ),
            TutorStep(
                id="js_ch1_s4",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Just like in math, numbers don't need quotation marks!\n\n"
                    "👇 *Type this calculation in the chat:*\n"
                    "```javascript\nconsole.log(20 + 30);\n```"
                ),
                message_am=(
                    "እንደ ማንኛውም የሂሳብ ስሌት፣ ቁጥሮች የጥቅስ ምልክት አያስፈልጋቸውም!\n\n"
                    "👇 *ይህንን ስሌት ጽፈው ይላኩ፦*\n"
                    "```javascript\nconsole.log(20 + 30);\n```"
                ),
                expected_code_output="50",
                hint_en="Write `console.log(20 + 30);` without quotes!",
                hint_am="ያለ ጥቅስ ምልክት `console.log(20 + 30);` ብለው ይጻፉ!",
                success_message_en="⚡ *50!* JavaScript computed the math instantly!",
                success_message_am="⚡ *ውጤቱ፦ 50!* ጃቫስክሪፕት በቅጽበት ደምሮ አሳይቷል!",
            ),
            TutorStep(
                id="js_ch1_s5",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You completed JavaScript Chapter 1!* 🎓\n\n"
                    "You learned:\n"
                    "1. JavaScript powers the entire interactive web.\n"
                    "2. We display output using `console.log()`.\n"
                    "3. Numbers compute math without quotes.\n\n"
                    "Ready to learn how JavaScript stores memory with `let` in Chapter 2?"
                ),
                message_am=(
                    "🏆 *የጃቫስክሪፕት ምዕራፍ 1ን አጠናቀዋል!* 🎓\n\n"
                    "ምን ተማሩ?፦\n"
                    "1. ጃቫስክሪፕት የድህረ-ገጾች ዋነኛ አንቀሳቃሽ ነው።\n"
                    "2. ውጤት ለማሳየት `console.log()` እንጠቀማለን።\n"
                    "3. ቁጥሮች ያለ ጥቅስ ምልክት ይሰላሉ።\n\n"
                    "በምዕራፍ 2 በ `let` መረጃዎችን በቫሪያብል ማስታወስ ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch2",
        order=2,
        title_en="JS Ch 2: Memory & Variables (let & const)",
        title_am="ጄኤስ ምዕራፍ 2፦ ማህደረ-ትውስታ እና ቫሪያብሎች (let)",
        description_en="Learn how let and const store names, user scores, and items in JavaScript.",
        description_am="በጃቫስክሪፕት ውስጥ `let` እና `const` ስሞችን እና መረጃዎችን እንዴት እንደሚያስቀምጡ ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Variables in JavaScript: `let`*\n\n"
                    "In modern JavaScript, when we create a new storage box, we declare it with **`let`**:\n"
                    "```javascript\nlet city = \"Nairobi\";\n```\n"
                    "This tells the browser: *\"Reserve memory for a box named `city`, and put 'Nairobi' inside!\"*"
                ),
                message_am=(
                    "📦 *ቫሪያብሎች በጃቫስክሪፕት፦ `let`*\n\n"
                    "በዘመናዊ ጃቫስክሪፕት አዲስ የማስቀመጫ ሳጥን ስንፈጥር **`let`** የሚለውን ቃል እናስቀድማለን፦\n"
                    "```javascript\nlet city = \"Nairobi\";\n```\n"
                    "ይህ ማለት፦ *\"`city` የሚባል ሳጥን አዘጋጅተህ 'Nairobi' የሚለውን አስቀምጥ!\"* ማለት ነው።"
                ),
            ),
            TutorStep(
                id="js_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create a variable with `let` and print it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nlet score = 100;\nconsole.log(score);\n```"
                ),
                message_am=(
                    "በ `let` ቫሪያብል ፈጥረን እናሳየው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nlet score = 100;\nconsole.log(score);\n```"
                ),
                expected_code_output="100",
                hint_en='Line 1: `let score = 100;`\nLine 2: `console.log(score);`',
                hint_am='መስመር 1፦ `let score = 100;`\nመስመር 2፦ `console.log(score);`',
                success_message_en=(
                    "🎉 *BULLSEYE!* `score` remembered 100 and displayed it!"
                ),
                success_message_am=(
                    "🎉 *በትክክል ሰርቷል!* `score` 100 የሚለውን ቁጥር ይዞ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="js_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "In JavaScript, what keyword do we use when creating a variable whose value can change?"
                ),
                message_am=(
                    "በጃቫስክሪፕት ውስጥ ወደፊት እሴቱ ሊለወጥ የሚችል አዲስ ቫሪያብል ለመፍጠር የትኛውን ቁልፍ ቃል እንጠቀማለን?"
                ),
                options_en=[
                    "let 📦",
                    "make",
                    "box",
                ],
                options_am=[
                    "let 📦",
                    "make",
                    "box",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Exact!* `let` is the standard keyword for creating variables in modern JavaScript.",
                success_message_am="🎯 *ትክክል!* `let` በዘመናዊ ጃቫስክሪፕት ውስጥ አዲስ ቫሪያብል ለመፍጠር የሚያገለግል ቃል ነው።",
            ),
            TutorStep(
                id="js_ch2_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered JavaScript Variables!* 🎓\n\n"
                    "You know how websites remember your username, shopping cart items, and score.\n\n"
                    "Ready to teach JavaScript how to make smart decisions with `if/else` in Chapter 3?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 2ን (ቫሪያብሎችን) አጠናቀዋል!* 🎓\n\n"
                    "ድህረ-ገጾች የተጠቃሚ ስምን እና ውጤትን እንዴት እንደሚያስታውሱ አውቀዋል።\n\n"
                    "በምዕራፍ 3 ጃቫስክሪፕት በ `if/else` ውሳኔ እንዲወስን ለማስተማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch3",
        order=3,
        title_en="JS Ch 3: Decisions & Logic (if and else)",
        title_am="ጄኤስ ምዕራፍ 3፦ ውሳኔዎች እና አመክንዮ (if/else)",
        description_en="Learn how parentheses and curly braces {} let JavaScript make choices.",
        description_am="በጃቫስክሪፕት ውስጥ የፈረንሳይ ቅንፎች {} እና `if/else` ውሳኔዎችን እንዴት እንደሚሰጡ ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🧠 *Decisions in JavaScript*\n\n"
                    "In JavaScript, conditions go inside parentheses `()` and the action goes inside "
                    "curly braces `{}`:\n"
                    "```javascript\nif (score >= 50) {\n  console.log(\"Pass!\");\n}\n```\n"
                    "Think of `{ }` like a fenced room that only opens when the condition is TRUE!"
                ),
                message_am=(
                    "🧠 *ውሳኔዎች በጃቫስክሪፕት*\n\n"
                    "በጃቫስክሪፕት ውስጥ ሁኔታው በክብ ቅንፍ `()` ውስጥ ሲቀመጥ፣ የሚተገበረው ስራ ደግሞ "
                    "በፈረንሳይ ቅንፍ `{}` ውስጥ ይጻፋል፦\n"
                    "```javascript\nif (score >= 50) {\n  console.log(\"Pass!\");\n}\n```\n"
                    "`{ }` ልክ እንደታጠረ ግቢ ሲሆን የሚከፈተው ሁኔታው እውነት (True) ሲሆን ብቻ ነው!"
                ),
            ),
            TutorStep(
                id="js_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's test an `if...else` decision in JavaScript!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nlet age = 15;\nif (age >= 18) {\n  console.log(\"Allowed\");\n} else {\n  console.log(\"Too young\");\n}\n```"
                ),
                message_am=(
                    "የ `if...else` ውሳኔን በጃቫስክሪፕት እንሞክረው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nlet age = 15;\nif (age >= 18) {\n  console.log(\"Allowed\");\n} else {\n  console.log(\"Too young\");\n}\n```"
                ),
                expected_code_output="Too young",
                hint_en='Remember curly braces: `if (age >= 18) { ... } else { ... }`',
                hint_am='የፈረንሳይ ቅንፎችን ያስታውሱ፦ `if (age >= 18) { ... } else { ... }`',
                success_message_en=(
                    "🌟 *PERFECT!* 15 is under 18, so JavaScript jumped directly to the `else` block and printed `Too young`!"
                ),
                success_message_am=(
                    "🌟 *በጣም ድንቅ!* 15 ከ 18 ስለሚያንስ፣ ጃቫስክሪፕት በቀጥታ ወደ `else` በመዝለል `Too young` ብሎ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="js_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "In JavaScript, what brackets contain the code to execute inside an `if` block?"
                ),
                message_am=(
                    "በጃቫስክሪፕት ውስጥ በ `if` ውስጥ የሚተገበረው ኮድ በየትኞቹ ቅንፎች ውስጥ ይቀመጣል?"
                ),
                options_en=[
                    "Curly braces { } 🔒",
                    "Angle brackets < >",
                    "Quotes \" \"",
                ],
                options_am=[
                    "የፈረንሳይ ቅንፎች { } 🔒",
                    "የማዕዘን ቅንፎች < >",
                    "የጥቅስ ምልክት \" \"",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* `{ }` bundles blocks of code in JavaScript, C, Java, and many other languages.",
                success_message_am="🎯 *ትክክል ነው!* የፈረንሳይ ቅንፎች `{ }` በጃቫስክሪፕት ውስጥ የኮድ ብሎክን ለመያዝ ያገለግላሉ።",
            ),
            TutorStep(
                id="js_ch3_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered JavaScript Decisions!* 🎓\n\n"
                    "You know how web applications check passwords and validate credit cards.\n\n"
                    "Ready to supercharge your code with Loops in Chapter 4?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 3ን (ውሳኔዎችን) አጠናቀዋል!* 🎓\n\n"
                    "የይለፍ ቃላት እና መረጃዎች በድህረ-ገጾች ላይ እንዴት እንደሚፈተሹ አውቀዋል።\n\n"
                    "በምዕራፍ 4 ሉፖችን (Loops) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch4",
        order=4,
        title_en="JS Ch 4: Loops & Automation in JavaScript",
        title_am="ጄኤስ ምዕራፍ 4፦ ድግግሞሽ እና ሉፖች በጃቫስክሪፕት",
        description_en="Learn how for loops repeat actions in the classic JavaScript style.",
        description_am="በክላሲክ የጃቫስክሪፕት ስልት `for` ሉፖች ስራን እንዴት ደጋግመው እንደሚያከናውኑ ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *The Classic `for` Loop in JavaScript*\n\n"
                    "JavaScript uses a 3-part formula to count:\n"
                    "1. Start: `let i = 0`\n"
                    "2. Condition: `i < 3`\n"
                    "3. Step: `i++` (adds 1 each turn)\n\n"
                    "```javascript\nfor (let i = 0; i < 3; i++) {\n  console.log(\"Hello!\");\n}\n```"
                ),
                message_am=(
                    "⚡ *ክላሲክ የ `for` ሉፕ በጃቫስክሪፕት*\n\n"
                    "ጃቫስክሪፕት ሉፕ ለማስኬድ ባለ 3 ክፍል ቀመር ይጠቀማል፦\n"
                    "1. መነሻ፦ `let i = 0`\n"
                    "2. መቆሚያ፦ `i < 3`\n"
                    "3. ጭማሪ፦ `i++` (በእያንዳንዱ ዙር 1 ይደምራል)\n\n"
                    "```javascript\nfor (let i = 0; i < 3; i++) {\n  console.log(\"Hello!\");\n}\n```"
                ),
            ),
            TutorStep(
                id="js_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's count from 1 to 3 with a JavaScript loop!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nfor (let i = 1; i <= 3; i++) {\n  console.log(i);\n}\n```"
                ),
                message_am=(
                    "በጃቫስክሪፕት ሉፕ ከ 1 እስከ 3 እንቁጠር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nfor (let i = 1; i <= 3; i++) {\n  console.log(i);\n}\n```"
                ),
                expected_code_output="1\n2\n3",
                hint_en='Line 1: `for (let i = 1; i <= 3; i++) {`\nLine 2: `  console.log(i);`\nLine 3: `}`',
                hint_am='መስመር 1፦ `for (let i = 1; i <= 3; i++) {`\nመስመር 2፦ `  console.log(i);`\nመስመር 3፦ `}`',
                success_message_en=(
                    "🎉 *Look at that automated counting!* `1`, `2`, `3`!"
                ),
                success_message_am=(
                    "🎉 *አውቶማቲክ ቆጣሪ ሰርቷል!* `1`፣ `2`፣ `3`!"
                ),
            ),
            TutorStep(
                id="js_ch4_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered JavaScript Loops!* 🎓\n\n"
                    "You can now process lists of 10,000 products, animate elements, and automate code.\n\n"
                    "Ready to learn how JavaScript handles collections with Arrays in Chapter 5?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 4ን (ሉፖችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን በሺዎች የሚቆጠሩ መረጃዎችን በቅጽበት ማከናወን ይችላሉ።\n\n"
                    "በምዕራፍ 5 አሬዮችን (Arrays) በጃቫስክሪፕት ለማየት ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch5",
        order=5,
        title_en="JS Ch 5: JavaScript Arrays (Lists)",
        title_am="ጄኤስ ምዕራፍ 5፦ የጃቫስክሪፕት አሬይ (Arrays)",
        description_en="Learn how arrays store multiple items like shopping carts and chat messages.",
        description_am="አሬዮች (Arrays) በርካታ መረጃዎችን በቅንፍ [] ውስጥ እንዴት እንደሚያስቀምጡ ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎒 *Arrays in JavaScript*\n\n"
                    "Just like in Python, JavaScript uses square brackets `[]` called **Arrays**:\n"
                    "```javascript\nlet tech = [\"HTML\", \"CSS\", \"JavaScript\"];\n```\n"
                    "And counting starts at index **0**!"
                ),
                message_am=(
                    "🎒 *አሬይ (Arrays) በጃቫስክሪፕት*\n\n"
                    "እንደ ፓይተን ሁሉ፣ በጃቫስክሪፕትም በካሬ ቅንፍ `[]` የሚሰሩ ስብስቦች **አሬይ (Array)** ይባላሉ፦\n"
                    "```javascript\nlet tech = [\"HTML\", \"CSS\", \"JavaScript\"];\n```\n"
                    "ቆጠራም የሚጀምረው ከ **0** ነው!"
                ),
            ),
            TutorStep(
                id="js_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's retrieve the first web language from our array!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nlet tech = [\"HTML\", \"CSS\", \"JS\"];\nconsole.log(tech[0]);\n```"
                ),
                message_am=(
                    "የመጀመሪያውን የቴክኖሎጂ ስም ከአሬዩ አውጥተን እናሳይ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nlet tech = [\"HTML\", \"CSS\", \"JS\"];\nconsole.log(tech[0]);\n```"
                ),
                expected_code_output="HTML",
                hint_en='Line 1: `let tech = ["HTML", "CSS", "JS"];`\nLine 2: `console.log(tech[0]);`',
                hint_am='መስመር 1፦ `let tech = ["HTML", "CSS", "JS"];`\nመስመር 2፦ `console.log(tech[0]);`',
                success_message_en=(
                    "🌟 *Retrieved: HTML!* You mastered index zero!"
                ),
                success_message_am=(
                    "🌟 *ውጤት፦ HTML!* የመጀመሪያውን ቦታ (Index 0) በሚገባ ተረድተዋል!"
                ),
            ),
            TutorStep(
                id="js_ch5_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered JavaScript Arrays!* 🎓\n\n"
                    "Every web feed, post list, and image gallery is an Array.\n\n"
                    "Ready to build custom reusable machines with Functions in Chapter 6?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 5ን (አሬዮችን) አጠናቀዋል!* 🎓\n\n"
                    "በድህረ-ገጾች ላይ የምናያቸው የፖስቶች እና የፎቶዎች ዝርዝር በሙሉ አሬይ ናቸው።\n\n"
                    "በምዕራፍ 6 በጃቫስክሪፕት ፋንክሽኖችን (Functions) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch6",
        order=6,
        title_en="JS Ch 6: Functions in JavaScript",
        title_am="ጄኤስ ምዕራፍ 6፦ ፋንክሽኖች በጃቫስክሪፕት (Functions)",
        description_en="Learn how the function keyword builds reusable commands for websites.",
        description_am="`function` የሚለውን ቁልፍ ቃል በመጠቀም ለድህረ-ገጾች ተደጋጋሚ ትዕዛዞችን እንዴት መገንባት እንደሚቻል ይማሩ።",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🛠️ *Functions in JavaScript*\n\n"
                    "While Python uses `def`, JavaScript uses the full word **`function`**:\n"
                    "```javascript\nfunction sayHello() {\n  console.log(\"Hello from JS!\");\n}\n\nsayHello();\n```"
                ),
                message_am=(
                    "🛠️ *ፋንክሽኖች በጃቫስክሪፕት*\n\n"
                    "ፓይተን `def` ሲጠቀም፣ ጃቫስክሪፕት ሙሉውን **`function`** የሚለውን ቃል ይጠቀማል፦\n"
                    "```javascript\nfunction sayHello() {\n  console.log(\"Hello from JS!\");\n}\n\nsayHello();\n```"
                ),
            ),
            TutorStep(
                id="js_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create a function that multiplies numbers by 3:\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nfunction triple(num) {\n  console.log(num * 3);\n}\n\ntriple(10);\n```"
                ),
                message_am=(
                    "የተሰጠውን ቁጥር በ 3 የሚያባዛ ፋንክሽን እንስራ፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nfunction triple(num) {\n  console.log(num * 3);\n}\n\ntriple(10);\n```"
                ),
                expected_code_output="30",
                hint_en='Line 1: `function triple(num) {`\nLine 2: `  console.log(num * 3);`\nLine 3: `}`\nLine 4: `triple(10);`',
                hint_am='`function triple(num) { ... }` ጽፈው በመጨረሻ `triple(10);` ይጥሩ!',
                success_message_en=(
                    "🔥 *RESULT: 30!* Your custom function calculated `10 * 3 = 30`!"
                ),
                success_message_am=(
                    "🔥 *ውጤት፦ 30!* የፈጠሩት ፋንክሽን `10 * 3 = 30` ብሎ አሰልቷል!"
                ),
            ),
            TutorStep(
                id="js_ch6_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered JavaScript Functions!* 🎓\n\n"
                    "Now you are ready for the grand finale: Chapter 7 Capstone Game Project!"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 6ን (ፋንክሽኖችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን ለመጨረሻው ፕሮጀክት ዝግጁ ነዎት፦ ምዕራፍ 7 Capstone Game Project!"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="js_ch7",
        order=7,
        title_en="JS Ch 7: Capstone Project — Web Dice Game",
        title_am="ጄኤስ ምዕራፍ 7፦ የመጨረሻ ፕሮጀክት — የዳይስ ጨዋታ",
        description_en="Combine Variables, Logic, and Functions into a playable JavaScript game!",
        description_am="ቫሪያብሎችን፣ ውሳኔዎችን እና ፋንክሽኖችን በማጣመር የሚሰራ የጃቫስክሪፕት ጨዋታ ይገንቡ!",
        track="javascript",
        steps=[
            TutorStep(
                id="js_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎲 *Welcome to your JavaScript Capstone!* 🏆\n\n"
                    "We are going to build a **Lucky Roll Dice Game** in JavaScript!\n\n"
                    "If the roll is 6, the player hits the jackpot!\n"
                    "Let's write the complete game function."
                ),
                message_am=(
                    "🎲 *እንኳን ወደ ጃቫስክሪፕት የመጨረሻ ፕሮጀክት በደህና መጡ!* 🏆\n\n"
                    "የዳይስ መወርወሪያ ጨዋታ (Lucky Roll Game) እንገነባለን!\n\n"
                    "የወደቀው ቁጥር 6 ከሆነ ተጫዋቹ ጃክፖት ያሸንፋል!\n"
                    "ሙሉውን የጨዋታ ፋንክሽን እንስራ።"
                ),
            ),
            TutorStep(
                id="js_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Build the complete dice game function and test roll 6:\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```javascript\nfunction roll(dice) {\n  if (dice === 6) {\n    console.log(\"Jackpot!\");\n  } else {\n    console.log(\"Try again!\");\n  }\n}\n\nroll(6);\n```"
                ),
                message_am=(
                    "ሙሉውን የዳይስ ጨዋታ ጽፈው በ 6 ይሞክሩት፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nfunction roll(dice) {\n  if (dice === 6) {\n    console.log(\"Jackpot!\");\n  } else {\n    console.log(\"Try again!\");\n  }\n}\n\nroll(6);\n```"
                ),
                expected_code_output="Jackpot!",
                hint_en='Notice triple equals `===` for strict comparison in JavaScript!',
                hint_am='በጃቫስክሪፕት ውስጥ እኩል መሆናቸውን ለማረጋገጥ ሦስት እኩል ይሆናል `===` እንጠቀማለን!',
                success_message_en=(
                    "🎉🎊 *JACKPOT! YOU BUILT A COMPLETE JAVASCRIPT GAME!* 🎮✨"
                ),
                success_message_am=(
                    "🎉🎊 *ጃክፖት! ሙሉ የጃቫስክሪፕት ጨዋታ በተሳካ ሁኔታ ሰርተዋል!* 🎮✨"
                ),
            ),
            TutorStep(
                id="js_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌟🎓 **CONGRATULATIONS, JAVASCRIPT GRADUATE!** 🎓🌟\n\n"
                    "You have officially mastered the foundations of JavaScript:\n"
                    "1. 🌐 Displaying web console output (`console.log()`)\n"
                    "2. 📦 Memory & Variables with `let`\n"
                    "3. 🧠 Smart logic with `if/else` and `{}`\n"
                    "4. ⚡ Automation with `for` loops\n"
                    "5. 🎒 Collections with Arrays `[]`\n"
                    "6. 🛠️ Custom reusable tools with `function`\n"
                    "7. 🎲 Building interactive web game logic!\n\n"
                    "You now know both **Python AND JavaScript**! 🚀🔥"
                ),
                message_am=(
                    "🌟🎓 **እንኳን ደስ አለዎት! የጃቫስክሪፕት ተመራቂ ሆነዋል!** 🎓🌟\n\n"
                    "የጃቫስክሪፕት መሰረታዊ እውቀቶችን በሙሉ ጨርሰዋል፦\n"
                    "1. 🌐 የድህረ-ገጽ ውጤት ማሳየት (`console.log()`)\n"
                    "2. 📦 ማህደረ-ትውስታ እና ቫሪያብሎች በ `let`\n"
                    "3. 🧠 ብልህ ውሳኔዎች በ `if/else` እና `{}`\n"
                    "4. ⚡ አውቶሜሽን በ `for` ሉፖች\n"
                    "5. 🎒 የመረጃ ስብስቦች በ Arrays `[]`\n"
                    "6. 🛠️ የራስ መሳሪያዎችን በ `function` መገንባት\n"
                    "7. 🎲 በይነተገናኝ የጨዋታ አመክንዮ መገንባት!\n\n"
                    "አሁን **ፓይተንንም ጃቫስክሪፕትንም** በሚገባ ያውቃሉ! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_js_chapters() -> List[TutorChapter]:
    """Return all JavaScript tutor chapters ordered."""
    return sorted(JS_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_js_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve JavaScript tutor chapter by ID."""
    for ch in JS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_js_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next JavaScript chapter ID."""
    chapters = get_all_js_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
