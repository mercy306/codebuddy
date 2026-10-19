"""Curriculum content for the interactive conversational tutor."""

from __future__ import annotations
from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="ch1",
        order=1,
        title_en="Chapter 1: Your First Conversation with Code",
        title_am="ምዕራፍ 1፦ ከኮድ ጋር የመጀመሪያው ንግግር",
        description_en="Learn how to instruct a computer to display text and calculate math.",
        description_am="ኮምፒውተር ጽሁፎችን እንዲያሳይ እና ሂሳብ እንዲያሰላ እንዴት ማዘዝ እንደሚቻል ይማሩ።",
        steps=[
            TutorStep(
                id="ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "👨‍🏫 *Hey there! I am CodeBuddy, your personal coding teacher.* 🤝\n\n"
                    "Today, we are starting from absolute zero. You do not need any math or computer background.\n\n"
                    "Think of a computer like a super-fast robot. It doesn't understand everyday English or Amharic, "
                    "so we talk to it using a simple language called **Python**.\n\n"
                    "Ready to teach your computer its very first word?"
                ),
                message_am=(
                    "👨‍🏫 *ሰላም! እኔ ኮድበዲ (CodeBuddy) ነኝ፤ የግል የኮዲንግ አስተማሪዎ።* 🤝\n\n"
                    "ዛሬ የምንጀምረው ከዜሮ ነው፤ ምንም አይነት የሂሳብ ወይም የኮምፒውተር እውቀት አያስፈልግዎትም።\n\n"
                    "ኮምፒውተርን እጅግ ፈጣን ሮቦት እንደሆነ አድርገው ያስቡ። እኛ በምንነጋገረው ቋንቋ ሳይሆን "
                    "**ፓይተን (Python)** በሚባል ቀላል የኮምፒውተር ቋንቋ እንግባባለን።\n\n"
                    "ለኮምፒውተርዎ የመጀመሪያ ቃሉን ለማስተማር ዝግጁ ነዎት?"
                ),
            ),
            TutorStep(
                id="ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "To make the computer display words on the screen, we use the `print()` command.\n\n"
                    "Because words are human text, we wrap them in quotation marks `\" \"`.\n\n"
                    "👇 *Your turn! Type this exact code in the chat right now:*\n"
                    '```python\nprint("Hello")\n```'
                ),
                message_am=(
                    "ኮምፒውተሩ በማያ ገጹ ላይ ጽሁፍ እንዲያሳይ ስንፈልግ `print()` የሚለውን ትዕዛዝ እንጠቀማለን።\n\n"
                    "ጽሁፎች የሰው ቃላት ስለሆኑ በጥቅስ ምልክት `\" \"` ውስጥ እናስቀምጣቸዋለን።\n\n"
                    "👇 *የእርስዎ ተራ ነው! የሚከተለውን ኮድ በቻቱ ላይ ጽፈው ይላኩ፦*\n"
                    '```python\nprint("Hello")\n```'
                ),
                expected_code_output="Hello",
                hint_en='Write `print("Hello")` with quotes and parentheses!',
                hint_am='በጥቅስ እና በቅንፍ `print("Hello")` ብለው ይጻፉ!',
                success_message_en=(
                    "🎉 *BOOM! You did it!* Look at that—the computer received your command and displayed `Hello`!\n\n"
                    "You just wrote and executed real computer code!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ! ሰርቷል!* ኮምፒውተሩ የሰጡትን ትዕዛዝ ተቀብሎ `Hello` ብሎ አሳይቷል!\n\n"
                    "እውነተኛ የኮምፒውተር ኮድ በተሳካ ሁኔታ ጽፈዋል!"
                ),
            ),
            TutorStep(
                id="ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "Quick question to see if you caught the secret: 🕵️\n\n"
                    "Why did we wrap `\"Hello\"` inside quotation marks `\" \"`?"
                ),
                message_am=(
                    "ሚስጥሩን በሚገባ መረዳትዎን እንፈትሽ፦ 🕵️\n\n"
                    "`\"Hello\"`ን በጥቅስ ምልክት `\" \"` ውስጥ ያስገባነው ለምንድን ነው?"
                ),
                options_en=[
                    "Because it is text/words 📝",
                    "Because it is a number 🔢",
                    "Just for decoration ✨",
                ],
                options_am=[
                    "ጽሁፍ/ቃል ስለሆነ 📝",
                    "ቁጥር ስለሆነ 🔢",
                    "ለጌጥ ብቻ ✨",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* Words and text must always have quotation marks in Python.",
                success_message_am="🎯 *ትክክል ነው!* በፓይተን ውስጥ ቃላት እና ጽሁፎች ሁልጊዜ በጥቅስ ምልክት ውስጥ መቀመጥ አለባቸው።",
            ),
            TutorStep(
                id="ch1_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "Now, what about numbers? 🧮\n\n"
                    "Unlike words, numbers **do not need quotation marks**.\n\n"
                    "When you write numbers without quotes, Python acts like a calculator and solves the math automatically!"
                ),
                message_am=(
                    "ስለ ቁጥሮችስ? 🧮\n\n"
                    "ከቃላት በተለየ፣ ቁጥሮች **የጥቅስ ምልክት አያስፈልጋቸውም**።\n\n"
                    "ቁጥሮችን ያለ ጥቅስ ምልክት ሲጽፉ፣ ፓይተን እንደ ካልኩሌተር ያሰላቸዋል!"
                ),
            ),
            TutorStep(
                id="ch1_s5",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's test Python's math power! ⚡\n\n"
                    "👇 *Type this code in the chat and send it:*\n"
                    "```python\nprint(15 + 25)\n```"
                ),
                message_am=(
                    "የፓይተንን የሂሳብ አቅም እንፈትሸው! ⚡\n\n"
                    "👇 *የሚከተለውን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nprint(15 + 25)\n```"
                ),
                expected_code_output="40",
                hint_en="Write `print(15 + 25)` without quotes!",
                hint_am="ያለ ጥቅስ ምልክት `print(15 + 25)` ብለው ይጻፉ!",
                success_message_en="🎯 *Result: 40!* Python added the numbers together instantly because there were no quotes!",
                success_message_am="🎯 *ውጤቱ፦ 40!* ምንም አይነት የጥቅስ ምልክት ስላልነበረ ፓይተን ቁጥሮቹን በቀጥታ ደምሮ ውጤቱን አሳይቷል!",
            ),
            TutorStep(
                id="ch1_s6",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *Congratulations! You graduated Chapter 1!* 🎓\n\n"
                    "You learned:\n"
                    "1. How to give instructions with `print()`\n"
                    "2. Text needs quotes `\"Hello\"`\n"
                    "3. Numbers don't need quotes `print(10 + 5)`\n\n"
                    "Ready to give the computer a memory in Chapter 2?"
                ),
                message_am=(
                    "🏆 *እንኳን ደስ አለዎት! ምዕራፍ 1ን በተሳካ ሁኔታ አጠናቀዋል!* 🎓\n\n"
                    "ምን ተማሩ?፦\n"
                    "1. በ `print()` ትዕዛዝ መስጠት\n"
                    "2. ጽሁፍ የጥቅስ ምልክት እንደሚያስፈልገው `\"Hello\"`\n"
                    "3. ቁጥሮች የጥቅስ ምልክት እንደማያስፈልጋቸው `print(10 + 5)`\n\n"
                    "በምዕራፍ 2 ለኮምፒውተሩ ማስታወሻ (Memory) ለመስጠት ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch2",
        order=2,
        title_en="Chapter 2: Giving the Computer a Memory",
        title_am="ምዕራፍ 2፦ ለኮምፒውተሩ ማስታወሻ መስጠት",
        description_en="Learn how variables store names, numbers, and scores in labeled boxes.",
        description_am="ቫሪያብሎች (Variables) ስሞችን እና ውጤቶችን በሳጥኖች ውስጥ እንዴት እንደሚያስቀምጡ ይማሩ።",
        steps=[
            TutorStep(
                id="ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Imagine a labeled storage box!*\n\n"
                    "In programming, that box is called a **Variable**.\n\n"
                    "You give the box a name, and store whatever you want inside it:\n"
                    '```python\nname = "Almaz"\n```\n'
                    "Now, whenever you say `name`, the computer remembers `\"Almaz\"`!"
                ),
                message_am=(
                    "📦 *ስም የተለጠፈበትን የማስቀመጫ ሳጥን ያስቡ!*\n\n"
                    "በኮዲንግ ይህ ሳጥን **ቫሪያብል (Variable)** ይባላል።\n\n"
                    "ለሳጥኑ ስም ትሰጣላችሁ፣ ከዚያም የፈለጋችሁትን መረጃ ውስጡ ታስቀምጣላችሁ፦\n"
                    '```python\nname = "አልማዝ"\n```\n'
                    "አሁን `name` ባላችሁ ቁጥር፣ ኮምፒውተሩ `\"አልማዝ\"`ን ያስታውሳል!"
                ),
            ),
            TutorStep(
                id="ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's store a city name and print it!\n\n"
                    "👇 *Type both lines in one message and send:*\n"
                    '```python\ncity = "Hawassa"\nprint(city)\n```'
                ),
                message_am=(
                    "የከተማ ስም በቫሪያብል ውስጥ አስቀምጠን እናሳይ!\n\n"
                    "👇 *ሁለቱንም መስመሮች በአንድ መልእክት ጽፈው ይላኩ፦*\n"
                    '```python\ncity = "Hawassa"\nprint(city)\n```'
                ),
                expected_code_output="Hawassa",
                hint_en='Line 1: `city = "Hawassa"`\nLine 2: `print(city)`',
                hint_am='መስመር 1፦ `city = "Hawassa"`\nመስመር 2፦ `print(city)`',
                success_message_en=(
                    "🎉 *Look at that!* You stored `\"Hawassa\"` in the `city` box, "
                    "and the computer retrieved it and printed it!"
                ),
                success_message_am=(
                    "🎉 *አዩት አይደል!* `\"Hawassa\"`ን በ `city` ሳጥን ውስጥ አስቀመጡ፣ "
                    "ኮምፒውተሩም መልሶ አወጣውና አሳየው!"
                ),
            ),
            TutorStep(
                id="ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "Notice that in `print(city)`, we did NOT put quotes around `city`! Why?"
                ),
                message_am=(
                    "በ `print(city)` ላይ በ `city` ዙሪያ የጥቅስ ምልክት አላደረግንም! ለምን ይመስልዎታል?"
                ),
                options_en=[
                    "Because city is a variable name, not plain text 📦",
                    "We forgot the quotes 😅",
                    "Quotes are forbidden in Python ❌",
                ],
                options_am=[
                    "city የቫሪያብል ስም እንጂ ተራ ቃል ስላልሆነ 📦",
                    "ስለረሳነው ነው 😅",
                    "ጥቅስ መጠቀም ስለማይቻል ❌",
                ],
                correct_option_index=0,
                success_message_en="🌟 *Brilliant!* If we wrote `print(\"city\")`, it would print the literal word 'city'. But `print(city)` prints the value inside the box!",
                success_message_am="🌟 *በጣም አሪፍ ማስተዋል!* `print(\"city\")` ብለን ብንጽፍ 'city' የሚለውን ቃል ያሳያል፤ ያለ ጥቅስ `print(city)` ሲሆን ግን በሳጥኑ ውስጥ ያለውን እሴት ያሳያል!",
            ),
            TutorStep(
                id="ch2_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Chapter 2: Variables!* 🎓\n\n"
                    "You now know how programs remember data like player scores, usernames, and messages.\n\n"
                    "Ready to teach the computer how to think and make decisions?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 2ን (ቫሪያብሎችን) በሚገባ አጠናቀዋል!* 🎓\n\n"
                    "ፕሮግራሞች የተጠቃሚን ስም፣ ውጤት እና መልዕክት እንዴት እንደሚያስታውሱ አውቀዋል።\n\n"
                    "በቀጣይ ኮምፒውተሩ እንዲያስብ እና እንዲወስን ለማስተማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch3",
        order=3,
        title_en="Chapter 3: Teaching Code to Make Decisions",
        title_am="ምዕራፍ 3፦ ኮምፒውተር እንዲወስን ማስተማር",
        description_en="Learn how if and else give your program a brain to make choices.",
        description_am="`if` እና `else` ኮምፒውተሩ ሁኔታዎችን አይቶ እንዲወስን እንዴት እንደሚያደርጉት ይማሩ።",
        steps=[
            TutorStep(
                id="ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🧠 *How do humans make decisions?*\n\n"
                    "We use conditions every day: *\"If it rains, take an umbrella.\"*\n\n"
                    "In Python, we teach the computer to do the exact same thing using the **`if`** statement:\n"
                    "```python\nif score >= 50:\n    print(\"You passed!\")\n```\n"
                    "Notice the colon `:` at the end and the indented 4 spaces before `print`!"
                ),
                message_am=(
                    "🧠 *ሰዎች እንዴት ይወስናሉ?*\n\n"
                    "በዕለት ተዕለት ህይወታችን ሁኔታዎችን እናያለን፦ *\"ዝናብ ከዘነበ፣ ጃንጥላ ያዝ።\"*\n\n"
                    "በፓይተን ውስጥም ኮምፒውተሩ ልክ እንደዚህ እንዲወስን **`if`** የሚለውን ቃል እንጠቀማለን፦\n"
                    "```python\nif score >= 50:\n    print(\"አልፈዋል!\")\n```\n"
                    "በመስመሩ መጨረሻ ያለውን ሁለት ነጥብ `:` እና ከስሩ ያሉትን 4 ክፍተቶች (Indent) ልብ ይበሉ!"
                ),
            ),
            TutorStep(
                id="ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's test an `if` statement! Check if an age allows entry:\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nage = 20\nif age >= 18:\n    print(\"Welcome!\")\n```"
                ),
                message_am=(
                    "የ `if` ውሳኔን እንሞክረው! እድሜ ከ18 በላይ ከሆነ መግባት ይቻላል፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nage = 20\nif age >= 18:\n    print(\"Welcome!\")\n```"
                ),
                expected_code_output="Welcome!",
                hint_en='Line 1: `age = 20`\nLine 2: `if age >= 18:`\nLine 3: `    print("Welcome!")`',
                hint_am='መስመር 1፦ `age = 20`\nመስመር 2፦ `if age >= 18:`\nመስመር 3፦ `    print("Welcome!")`',
                success_message_en=(
                    "🎉 *YES!* The computer checked `age >= 18`, saw that 20 is greater than 18, "
                    "and displayed `Welcome!`"
                ),
                success_message_am=(
                    "🎉 *በትክክል!* ኮምፒውተሩ `age >= 18` መሆኑን አረጋገጠ፤ 20 ከ 18 ስለሚበልጥ "
                    "`Welcome!` ብሎ አሳየ!"
                ),
            ),
            TutorStep(
                id="ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "Quick brain check: 🧠\n\n"
                    "What would happen if `age` was set to `12` instead of `20`?"
                ),
                message_am=(
                    "ፈጣን የፈተና ጥያቄ፦ 🧠\n\n"
                    "የ `age` ዋጋ ከ 20 ይልቅ `12` ቢሆን ኖሮ ምን ይፈጠር ነበር?"
                ),
                options_en=[
                    "Nothing would print because the condition is False 🛑",
                    "It would still print 'Welcome!' 🟢",
                    "The computer would show a crash error 💥",
                ],
                options_am=[
                    "ሁኔታው ስላልተሟላ ምንም ነገር አይታይም ነበር 🛑",
                    "አሁንም 'Welcome!' ብሎ ያሳያል 🟢",
                    "ኮምፒውተሩ የስህተት መልእክት ያሳያል 💥",
                ],
                correct_option_index=0,
                success_message_en="🎯 *100% correct!* Because 12 is less than 18, Python simply skips the indented line without crashing.",
                success_message_am="🎯 *ሙሉ በሙሉ ትክክል!* 12 ከ 18 ስለሚያንስ፣ ፓይተን ከስር ያለውን መስመር ዝም ብሎ ያልፈዋል።",
            ),
            TutorStep(
                id="ch3_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "Now, what if the condition is False and we want a backup plan?\n\n"
                    "We use **`else:`**! 💡\n\n"
                    "```python\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Try again\")\n```\n"
                    "If the `if` test passes, it runs the first block. Otherwise, it runs the `else` block!"
                ),
                message_am=(
                    "ሁኔታው ካልተሟላስ ሌላ አማራጭ እንዴት እናሳያለን?\n\n"
                    "**`else:`** የተባለውን ቃል እንጠቀማለን! 💡\n\n"
                    "```python\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Try again\")\n```\n"
                    "ውጤቱ 50 ወይም ከዚያ በላይ ከሆነ የመጀመሪያው ይተገበራል፤ ካልሆነ ግን ሁለተኛው (else) ይተገበራል!"
                ),
            ),
            TutorStep(
                id="ch3_s5",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's test an `if...else` in action!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nscore = 35\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Try again\")\n```"
                ),
                message_am=(
                    "የ `if...else`ን በተግባር እንሞክረው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nscore = 35\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Try again\")\n```"
                ),
                expected_code_output="Try again",
                hint_en='Line 1: `score = 35`\nLine 2: `if score >= 50:`\nLine 3: `    print("Pass")`\nLine 4: `else:`\nLine 5: `    print("Try again")`',
                hint_am='መስመር 1፦ `score = 35`\nመስመር 2፦ `if score >= 50:`\nመስመር 3፦ `    print("Pass")`\nመስመር 4፦ `else:`\nመስመር 5፦ `    print("Try again")`',
                success_message_en=(
                    "🌟 *Outstanding!* The computer saw 35 is less than 50, skipped the first line, "
                    "and executed the `else` branch to print `Try again`!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ነው!* ኮምፒውተሩ 35 ከ 50 እንደሚያንስ ተመልክቶ፣ የመጀመሪያውን ዘሎ `else`ን "
                    "በማስኬድ `Try again` ብሎ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="ch3_s6",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Chapter 3: Making Decisions!* 🎓\n\n"
                    "You now know how login screens check passwords, how games decide game over, "
                    "and how apps react to user input.\n\n"
                    "Ready to unlock the power of Loops & Automation in Chapter 4?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 3ን (ውሳኔዎችን) በብቃት አጠናቀዋል!* 🎓\n\n"
                    "የይለፍ ቃላት እንዴት እንደሚፈተሹ፣ ጌሞች እንዴት አሸናፊ እና ተሸናፊን እንደሚለዩ አውቀዋል።\n\n"
                    "በምዕራፍ 4 አውቶሜሽን እና ድግግሞሽን (Loops) ለማየት ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch4",
        order=4,
        title_en="Chapter 4: The Power of Loops & Automation",
        title_am="ምዕራፍ 4፦ ድግግሞሽ እና አውቶሜሽን (Loops)",
        description_en="Learn how loops repeat tasks hundreds of times in a fraction of a second.",
        description_am="ሉፖች (Loops) በአይን ጥቅሻ ውስጥ ስራዎችን በመቶዎች ጊዜ እንዴት እንደሚደግሙ ይማሩ።",
        steps=[
            TutorStep(
                id="ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *Why do we use computers?*\n\n"
                    "If a human has to write \"I love coding\" 100 times, their hands get tired.\n\n"
                    "Computers never get tired! In Python, a **loop** lets you repeat anything as many times as you want:\n"
                    "```python\nfor i in range(3):\n    print(\"Hello!\")\n```\n"
                    "The computer will run `print(\"Hello!\")` 3 times in a row automatically!"
                ),
                message_am=(
                    "⚡ *ኮምፒውተርን ለምን እንጠቀማለን?*\n\n"
                    "አንድ ሰው \"ኮዲንግ እወዳለሁ\" የሚለውን 100 ጊዜ እንዲጽፍ ቢጠየቅ እጁ ይዝላል።\n\n"
                    "ኮምፒውተሮች ግን በፍጹም አይደክሙም! በፓይተን ውስጥ **ሉፕ (Loop)** የተባለው መሳሪያ ማንኛውንም ስራ "
                    "በፈለጉት መጠን እንዲደጋገም ያደርጋል፦\n"
                    "```python\nfor i in range(3):\n    print(\"Hello!\")\n```\n"
                    "ኮምፒውተሩ `print(\"Hello!\")`ን 3 ጊዜ በተከታታይ ያሳያል!"
                ),
            ),
            TutorStep(
                id="ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's see this superpower with your own eyes!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nfor i in range(3):\n    print(\"Go!\")\n```"
                ),
                message_am=(
                    "ይህንን አስደናቂ ሀይል በገዛ እጅዎ ይሞክሩት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfor i in range(3):\n    print(\"Go!\")\n```"
                ),
                expected_code_output="Go!\nGo!\nGo!",
                hint_en='Line 1: `for i in range(3):`\nLine 2: `    print("Go!")` (with 4 spaces indentation!)',
                hint_am='መስመር 1፦ `for i in range(3):`\nመስመር 2፦ `    print("Go!")` (ከስሩ 4 ክፍተት በማድረግ!)',
                success_message_en=(
                    "🔥 *BOOM! 3 times in less than a millisecond!* Look at that:\n"
                    "`Go!`\n`Go!`\n`Go!`\n\n"
                    "You just automated repetition with your first loop!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ነው! በቅጽበት 3 ጊዜ ተደጋግሟል!*፦\n"
                    "`Go!`\n`Go!`\n`Go!`\n\n"
                    "የመጀመሪያውን ሉፕ በተሳካ ሁኔታ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "Imagine you changed `range(3)` to `range(500)`.\n\n"
                    "How many times would the computer repeat the line?"
                ),
                message_am=(
                    "በ `range(3)` ፈንታ `range(500)` ብለው ቢቀይሩትስ?\n\n"
                    "ኮምፒውተሩ ስራውን ስንት ጊዜ ይደግመዋል?"
                ),
                options_en=[
                    "Exactly 500 times in the blink of an eye ⚡",
                    "Only 3 times",
                    "It will get tired and stop halfway 😴",
                ],
                options_am=[
                    "በትክክል 500 ጊዜ በአይን ጥቅሻ ውስጥ ⚡",
                    "3 ጊዜ ብቻ",
                    "ይደክመውና ግማሽ ላይ ያቆማል 😴",
                ],
                correct_option_index=0,
                success_message_en="🚀 *Spot on!* A loop can repeat 500, 5,000, or 50,000 times without ever making a mistake or getting tired.",
                success_message_am="🚀 *ትክክል ነው!* ሉፕ 500፣ 5000፣ ወይም 50,000 ጊዜ ቢሆንም ያለምንም ስህተት እና ድካም ያከናውናል።",
            ),
            TutorStep(
                id="ch4_s4",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Did you know `i` is actually a counting variable that tracks the number?\n\n"
                    "Let's count from 1 to 3! 👇 *Type this code in the chat:*\n"
                    "```python\nfor i in range(1, 4):\n    print(i)\n```"
                ),
                message_am=(
                    "`i` የሚለው ፊደል ቁጥሮቹን የሚቆጥር ቫሪያብል መሆኑን ያውቃሉ?\n\n"
                    "ከ 1 እስከ 3 እንቁጠር! 👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfor i in range(1, 4):\n    print(i)\n```"
                ),
                expected_code_output="1\n2\n3",
                hint_en='Line 1: `for i in range(1, 4):`\nLine 2: `    print(i)`',
                hint_am='መስመር 1፦ `for i in range(1, 4):`\nመስመር 2፦ `    print(i)`',
                success_message_en=(
                    "🎉 *Look at that automated counter!* `1`, `2`, `3`.\n\n"
                    "Each turn through the loop, `i` held the next number!"
                ),
                success_message_am=(
                    "🎉 *አውቶማቲክ ቆጣሪ ሰርቷል!* `1`፣ `2`፣ `3`።\n\n"
                    "በእያንዳንዱ ዙር ላይ `i` የሚቀጥለውን ቁጥር በመያዝ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="ch4_s5",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *INCREDIBLE MILESTONE ACHIEVED!* 🎓🚀\n\n"
                    "You have now mastered the 4 Core Pillars of ALL programming:\n"
                    "1. 🗣️ **Output & Math** (`print()`, arithmetic)\n"
                    "2. 📦 **Memory** (Variables)\n"
                    "3. 🧠 **Logic** (`if...else` decisions)\n"
                    "4. ⚡ **Automation** (`for` loops)\n\n"
                    "Ready to unlock Chapter 5 and learn how to store collections of data?"
                ),
                message_am=(
                    "🏆 *ትልቅ እና አስደናቂ ደረጃ ላይ ደርሰዋል!* 🎓🚀\n\n"
                    "የማንኛውም ፕሮግራሚንግ 4ቱን ዋና ምሰሶዎች አውቀዋል፦\n"
                    "1. 🗣️ **ውጤት እና ሂሳብ** (`print()` እና ስሌት)\n"
                    "2. 📦 **ማህደረ-ትውስታ** (Variables)\n"
                    "3. 🧠 **ውሳኔ እና አመክንዮ** (`if...else`)\n"
                    "4. ⚡ **አውቶሜሽን** (`for` loops)\n\n"
                    "በምዕራፍ 5 በርካታ መረጃዎችን በአንድ ላይ ማደራጀት (Lists) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch5",
        order=5,
        title_en="Chapter 5: Lists & Data Collections",
        title_am="ምዕራፍ 5፦ ዝርዝሮች እና የመረጃ ስብስቦች (Lists)",
        description_en="Learn how to store multiple items in a single list using square brackets [].",
        description_am="በርካታ መረጃዎችን በቅንፍ [] ውስጥ በአንድ ዝርዝር እንዴት እንደሚያስቀምጡ ይማሩ።",
        steps=[
            TutorStep(
                id="ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎒 *The Shopping Backpack (Lists)*\n\n"
                    "What if you have 50 items? Creating `item1`, `item2`, `item3`... would take forever.\n\n"
                    "Instead, Python gives us a **List** using square brackets `[]`:\n"
                    "```python\nfruits = [\"Apple\", \"Banana\", \"Mango\"]\n```\n"
                    "Now all 3 fruits are neatly packed inside one single variable!"
                ),
                message_am=(
                    "🎒 *የግዢ ቦርሳ (Lists)*\n\n"
                    "50 እቃዎች ቢኖሩዎትስ? `item1`፣ `item2` እያሉ 50 ቫሪያብል መፍጠር አድካሚ ነው!\n\n"
                    "በዚህ ፈንታ፣ ፓይተን በካሬ ቅንፍ `[]` የሚሰራ **ዝርዝር (List)** ይሰጠናል፦\n"
                    "```python\nfruits = [\"Apple\", \"Banana\", \"Mango\"]\n```\n"
                    "አሁን ሦስቱም ፍራፍሬዎች በአንድ ቫሪያብል ውስጥ ተቀምጠዋል!"
                ),
            ),
            TutorStep(
                id="ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's grab the very first item from the list!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nfruits = [\"Apple\", \"Banana\", \"Mango\"]\nprint(fruits[0])\n```"
                ),
                message_am=(
                    "የመጀመሪያውን ፍሬ ከዝርዝሩ ውስጥ አውጥተን እናሳይ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfruits = [\"Apple\", \"Banana\", \"Mango\"]\nprint(fruits[0])\n```"
                ),
                expected_code_output="Apple",
                hint_en='Line 1: `fruits = ["Apple", "Banana", "Mango"]`\nLine 2: `print(fruits[0])`',
                hint_am='መስመር 1፦ `fruits = ["Apple", "Banana", "Mango"]`\nመስመር 2፦ `print(fruits[0])`',
                success_message_en=(
                    "🎉 *YES!* `Apple` was retrieved! In programming, counting always starts at **0**!"
                ),
                success_message_am=(
                    "🎉 *በትክክል!* `Apple` ወጥቷል! በኮዲንግ ውስጥ ቆጠራ ሁልጊዜ የሚጀምረው ከ **0** ነው!"
                ),
            ),
            TutorStep(
                id="ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "If `fruits[0]` is \"Apple\", which index gets \"Banana\"?"
                ),
                message_am=(
                    "`fruits[0]` \"Apple\" ከሆነ፣ \"Banana\"ን ለማግኘት ስንት ቁጥር እንጠቀማለን?"
                ),
                options_en=[
                    "fruits[1] 🍌",
                    "fruits[2]",
                    "fruits[10]",
                ],
                options_am=[
                    "fruits[1] 🍌",
                    "fruits[2]",
                    "fruits[10]",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* Position 0 is 1st, position 1 is 2nd, and position 2 is 3rd.",
                success_message_am="🎯 *ትክክል ነው!* ቦታ 0 የመጀመሪያው፣ ቦታ 1 ሁለተኛው፣ ቦታ 2 ደግሞ ሦስተኛው ነው።",
            ),
            TutorStep(
                id="ch5_s4",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Now, let's combine Lists with Loops! Loop through every item:\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\ncolors = [\"Red\", \"Green\"]\nfor c in colors:\n    print(c)\n```"
                ),
                message_am=(
                    "አሁን ዝርዝርን ከሉፕ ጋር እናጣምረው! እያንዳንዱን ከለር በተራ ያሳያል፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\ncolors = [\"Red\", \"Green\"]\nfor c in colors:\n    print(c)\n```"
                ),
                expected_code_output="Red\nGreen",
                hint_en='Line 1: `colors = ["Red", "Green"]`\nLine 2: `for c in colors:`\nLine 3: `    print(c)`',
                hint_am='መስመር 1፦ `colors = ["Red", "Green"]`\nመስመር 2፦ `for c in colors:`\nመስመር 3፦ `    print(c)`',
                success_message_en=(
                    "🌟 *Pure elegance!* The loop automatically visited every item in the list and printed it!"
                ),
                success_message_am=(
                    "🌟 *በጣም ድንቅ ስራ!* ሉፑ በዝርዝሩ ውስጥ ያሉትን እቃዎች አንድ በአንድ አውጥቶ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="ch5_s5",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Chapter 5: Lists!* 🎓\n\n"
                    "Now you can manage playlists, high scores, student rosters, and inventories.\n\n"
                    "Ready to learn how to build your own custom tools in Chapter 6: Functions?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 5ን (ዝርዝሮችን) በሚገባ አጠናቀዋል!* 🎓\n\n"
                    "አሁን የተማሪዎችን ስም፣ ውጤቶችን እና የዕቃ ዝርዝሮችን ማስተዳደር ይችላሉ።\n\n"
                    "በምዕራፍ 6 የራስዎን አጋዥ መሳሪያዎች (Functions) መፍጠር ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch6",
        order=6,
        title_en="Chapter 6: Custom Functions & Reusable Code",
        title_am="ምዕራፍ 6፦ ፋንክሽኖች እና ተደጋጋሚ ኮድ (Functions)",
        description_en="Learn how to create your own reusable commands and machines using def.",
        description_am="`def`ን በመጠቀም እንደገና ጥቅም ላይ ሊውሉ የሚችሉ የራስዎን ትዕዛዞች እንዴት እንደሚፈጥሩ ይማሩ።",
        steps=[
            TutorStep(
                id="ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "☕ *The Coffee Machine Analogy*\n\n"
                    "You don't rebuild a coffee machine every morning—you just press the button!\n\n"
                    "In Python, a **Function** is a machine you build once using **`def`** (define), "
                    "and then call it whenever you need it:\n"
                    "```python\ndef say_hi():\n    print(\"Hi there!\")\n\nsay_hi() # Runs it!\n```"
                ),
                message_am=(
                    "☕ *የቡና ማሽን ምሳሌ*\n\n"
                    "በየማለዳው አዲስ የቡና ማሽን አትሰሩም፤ ያለውን ቁልፍ ብቻ ትጫናላችሁ!\n\n"
                    "በፓይተን ውስጥም **ፋንክሽን (Function)** ማለት አንድ ጊዜ በ **`def`** የምትሰሩት "
                    "እና በፈለጋችሁ ጊዜ ስሙን ጠርታችሁ የምታሰሩት ማሽን ነው፦\n"
                    "```python\ndef say_hi():\n    print(\"Hi there!\")\n\nsay_hi() # ያሰረዋል!\n```"
                ),
            ),
            TutorStep(
                id="ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create your very first function and run it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\ndef greet():\n    print(\"Hello, Coder!\")\n\ngreet()\n```"
                ),
                message_am=(
                    "የመጀመሪያውን ፋንክሽን ሰርተው ያሰሩት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\ndef greet():\n    print(\"Hello, Coder!\")\n\ngreet()\n```"
                ),
                expected_code_output="Hello, Coder!",
                hint_en='Line 1: `def greet():`\nLine 2: `    print("Hello, Coder!")`\nLine 3: (empty)\nLine 4: `greet()`',
                hint_am='መስመር 1፦ `def greet():`\nመስመር 2፦ `    print("Hello, Coder!")`\nመስመር 3፦ `greet()`',
                success_message_en=(
                    "🎉 *BRAVO!* You defined `greet()` and called it! "
                    "You can call `greet()` 100 times anywhere in your program!"
                ),
                success_message_am=(
                    "🎉 *አስደናቂ ነው!* `greet()`ን ፈጥረው አስኬዱት! "
                    "አሁን በፕሮግራምዎ ውስጥ በፈለጉት ቦታ `greet()` በማለት መጠቀም ይችላሉ!"
                ),
            ),
            TutorStep(
                id="ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "What does the word `def` tell Python?"
                ),
                message_am=(
                    "`def` የሚለው ቃል ለፓይተን ምን ይነግረዋል?"
                ),
                options_en=[
                    "\"I am defining a new custom function!\" 🛠️",
                    "\"Delete everything on the computer!\" 💥",
                    "\"Download an update!\" 🌐",
                ],
                options_am=[
                    "\"አዲስ ፋንክሽን እየፈጠርኩ ነው!\" 🛠️",
                    "\"ሁሉንም ነገር አጥፋ!\" 💥",
                    "\"አፕዴት አድርግ!\" 🌐",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Exact!* `def` is the magic keyword that defines a new tool for Python to remember.",
                success_message_am="🎯 *ትክክል!* `def` አዲስ መሳሪያ ለፓይተን ለማስተማር የምንጠቀምበት ቁልፍ ቃል ነው።",
            ),
            TutorStep(
                id="ch6_s4",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Functions can also take inputs (parameters)! Let's multiply any number by 2:\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\ndef double(num):\n    print(num * 2)\n\ndouble(25)\n```"
                ),
                message_am=(
                    "ፋንክሽኖች መረጃዎችን ተቀብለው መስራት ይችላሉ! የተሰጠውን ቁጥር በ 2 የሚያባዛ እንስራ፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\ndef double(num):\n    print(num * 2)\n\ndouble(25)\n```"
                ),
                expected_code_output="50",
                hint_en='Line 1: `def double(num):`\nLine 2: `    print(num * 2)`\nLine 3: `double(25)`',
                hint_am='መስመር 1፦ `def double(num):`\nመስመር 2፦ `    print(num * 2)`\nመስመር 3፦ `double(25)`',
                success_message_en=(
                    "🔥 *RESULT: 50!* You passed `25` into `double()`, and it calculated `25 * 2 = 50`!"
                ),
                success_message_am=(
                    "🔥 *ውጤት፦ 50!* `25`ን ለ `double()` ሰጡት፣ እሱም `25 * 2 = 50` ብሎ አሰላው!"
                ),
            ),
            TutorStep(
                id="ch6_s5",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Chapter 6: Functions!* 🎓\n\n"
                    "You write clean, reusable, professional-grade code now.\n\n"
                    "Are you ready for the ultimate test: Chapter 7 Capstone Project — Building a real game?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 6ን (ፋንክሽኖችን) በከፍተኛ ብቃት አጠናቀዋል!* 🎓\n\n"
                    "አሁን ንጹህ እና እንደገና ጥቅም ላይ ሊውል የሚችል ፕሮፌሽናል ኮድ መጻፍ ይችላሉ።\n\n"
                    "ለመጨረሻው ፈተና ዝግጁ ነዎት? ምዕራፍ 7፦ እውነተኛ የቁጥር መገመቻ ጨዋታ (Capstone Project)!"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="ch7",
        order=7,
        title_en="Chapter 7: Capstone Project — Secret Number Game",
        title_am="ምዕራፍ 7፦ የመጨረሻ ፕሮጀክት — ሚስጥራዊ ቁጥር መገመቻ ጌም",
        description_en="Combine Variables, If/Else, Loops, and Functions into a real playable game!",
        description_am="ቫሪያብሎችን፣ ውሳኔዎችን፣ ሉፖችን እና ፋንክሽኖችን በማጣመር እውነተኛ ጨዋታ ይስሩ!",
        steps=[
            TutorStep(
                id="ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎮 *Welcome to your Capstone Project!* 🏆\n\n"
                    "Professional developers don't memorize textbooks—they build projects.\n\n"
                    "In this chapter, we will build a **Secret Number Guessing Game** from scratch "
                    "using everything you've learned:\n"
                    "• Variables (to hold secret number and guesses)\n"
                    "• Conditionals (`if`, `elif`, `else` to check win/lose)\n"
                    "• Loops (to test multiple guesses)\n\n"
                    "Let's start building step 1!"
                ),
                message_am=(
                    "🎮 *እንኳን ወደ መጨረሻው ፕሮጀክት በደህና መጡ!* 🏆\n\n"
                    "እውነተኛ ፕሮግራመሮች የሚለኩት በሰሯቸው ፕሮጀክቶች ነው!\n\n"
                    "በዚህ ምዕራፍ የተማሩትን ሁሉ በመጠቀም **ሚስጥራዊ ቁጥር መገመቻ ጨዋታ** እንሰራለን፦\n"
                    "• ቫሪያብሎች (ሚስጥራዊ ቁጥሩን እና ግምቶችን ለመያዝ)\n"
                    "• ውሳኔዎች (`if`, `elif`, `else` አሸናፊ እና ተሸናፊን ለመለየት)\n"
                    "• ሉፖች (ግምቶችን ለመፈተሽ)\n\n"
                    "ደረጃ 1ን አብረን እንጀምር!"
                ),
            ),
            TutorStep(
                id="ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Step 1: Set the secret number to `7`, set the player's guess to `7`, and check if they win!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nsecret = 7\nguess = 7\nif guess == secret:\n    print(\"Winner!\")\n```"
                ),
                message_am=(
                    "ደረጃ 1፦ ሚስጥራዊ ቁጥሩን `7`፣ የተገመተውን ቁጥር `7` አድርገን አሸናፊ መሆናቸውን እንፈትሽ፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nsecret = 7\nguess = 7\nif guess == secret:\n    print(\"Winner!\")\n```"
                ),
                expected_code_output="Winner!",
                hint_en='Line 1: `secret = 7`\nLine 2: `guess = 7`\nLine 3: `if guess == secret:`\nLine 4: `    print("Winner!")`',
                hint_am='መስመር 1፦ `secret = 7`\nመስመር 2፦ `guess = 7`\nመስመር 3፦ `if guess == secret:`\nመስመር 4፦ `    print("Winner!")`',
                success_message_en=(
                    "🎯 *WINNER!* Notice the double equals `==`! In Python, `==` means 'are these two equal?'"
                ),
                success_message_am=(
                    "🎯 *አሸናፊ!* ድርብ እኩል ይሆናል `==` ምልክትን ልብ ይበሉ! በፓይተን ውስጥ `==` ማለት 'እኩል ናቸው ወይ?' ብሎ ለመጠየቅ ያገለግላል።"
                ),
            ),
            TutorStep(
                id="ch7_s3",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Step 2: Add hints! If the guess is too low, tell them \"Too low!\"\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```python\nsecret = 7\nguess = 3\nif guess == secret:\n    print(\"Winner!\")\nelif guess < secret:\n    print(\"Too low!\")\n```"
                ),
                message_am=(
                    "ደረጃ 2፦ አጋዥ ፍንጭ እንጨምር! ግምቱ ካነሰ \"Too low!\" ይበል፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nsecret = 7\nguess = 3\nif guess == secret:\n    print(\"Winner!\")\nelif guess < secret:\n    print(\"Too low!\")\n```"
                ),
                expected_code_output="Too low!",
                hint_en='Line 1: `secret = 7`\nLine 2: `guess = 3`\nLine 3: `if guess == secret:`\nLine 4: `    print("Winner!")`\nLine 5: `elif guess < secret:`\nLine 6: `    print("Too low!")`',
                hint_am='`elif guess < secret:` ከስሩ `print("Too low!")` ያድርጉ።',
                success_message_en=(
                    "💡 *Awesome!* The game gave a helpful hint: `Too low!`"
                ),
                success_message_am=(
                    "💡 *ድንቅ ነው!* ጨዋታው `Too low!` በማለት ፍንጭ ሰጥቷል!"
                ),
            ),
            TutorStep(
                id="ch7_s4",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Final Step: Wrap the game inside a reusable function `play()` with multiple guesses!\n\n"
                    "👇 *Type this complete game in the chat and send:*\n"
                    "```python\ndef play(guess):\n    secret = 5\n    if guess == secret:\n        print(\"You won!\")\n    else:\n        print(\"Try again!\")\n\nplay(5)\n```"
                ),
                message_am=(
                    "የመጨረሻ ደረጃ፦ ጨዋታውን በሙሉ በ `play()` ፋንክሽን ውስጥ እናጠቃልለው፦\n\n"
                    "👇 *ይህንን ሙሉ ጨዋታ ጽፈው ይላኩ፦*\n"
                    "```python\ndef play(guess):\n    secret = 5\n    if guess == secret:\n        print(\"You won!\")\n    else:\n        print(\"Try again!\")\n\nplay(5)\n```"
                ),
                expected_code_output="You won!",
                hint_en='Define `def play(guess):`, check `if guess == secret:` and call `play(5)`!',
                hint_am='`def play(guess):` ብለው ይጀምሩ እና በመጨረሻው `play(5)` ብለው ይጠሩት!',
                success_message_en=(
                    "🎊 *YOU BUILT A COMPLETE PLAYABLE GAME!* 🎮✨\n\n"
                    "Look at what you created: A function, a secret variable, conditional logic, and output!"
                ),
                success_message_am=(
                    "🎊 *ሙሉ በሙሉ የሚሰራ ጨዋታ ሰርተዋል!* 🎮✨\n\n"
                    "የሰሩትን ይመልከቱ፦ ፋንክሽን፣ ቫሪያብል፣ የውሳኔ አመክንዮ እና ውጤት አጣምረው ተጠቅመዋል!"
                ),
            ),
            TutorStep(
                id="ch7_s5",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌟🎓 **CONGRATULATIONS, PYTHON GRADUATE!** 🎓🌟\n\n"
                    "You have officially completed all 7 chapters of CodeBuddy!\n\n"
                    "📜 **What You Now Truly Understand:**\n"
                    "1. 🗣️ How computers interpret code (`print`, types)\n"
                    "2. 📦 How memory stores information (Variables)\n"
                    "3. 🧠 How programs make smart decisions (`if/elif/else`)\n"
                    "4. ⚡ How computers automate repetitive work (`for` loops)\n"
                    "5. 🎒 How to store and manipulate collections (`lists`)\n"
                    "6. 🛠️ How to build custom modular tools (`functions`)\n"
                    "7. 🎮 How to architect and build a real game project!\n\n"
                    "You are now ready to write real Python programs, solve challenges in CodeLab, "
                    "and build whatever you imagine! 🚀🔥"
                ),
                message_am=(
                    "🌟🎓 **እንኳን ደስ አለዎት! የፓይተን ተመራቂ ሆነዋል!** 🎓🌟\n\n"
                    "ሁሉንም 7 የኮድበዲ ምዕራፎች በስኬት አጠናቀዋል!\n\n"
                    "📜 **በጥልቀት የተረዱት እውቀት፦**\n"
                    "1. 🗣️ ኮምፒውተሮች ኮድን እንዴት እንደሚረዱ (`print` እና አይነቶች)\n"
                    "2. 📦 መረጃ በማህደረ-ትውስታ ውስጥ እንዴት እንደሚቀመጥ (Variables)\n"
                    "3. 🧠 ፕሮግራሞች እንዴት ብልህ ውሳኔ እንደሚወስኑ (`if/elif/else`)\n"
                    "4. ⚡ ኮምፒውተሮች ድካም አልባ አውቶሜሽን እንዴት እንደሚሰሩ (`for` loops)\n"
                    "5. 🎒 በርካታ መረጃዎችን በአንድ ላይ ማደራጀት (`lists`)\n"
                    "6. 🛠️ እንደገና ጥቅም ላይ ሊውሉ የሚችሉ የራስ መሳሪያዎችን መስራት (`functions`)\n"
                    "7. 🎮 እውነተኛ የጨዋታ ፕሮጀክት መገንባት!\n\n"
                    "አሁን እውነተኛ የፓይተን ፕሮግራሞችን ለመጻፍ እና በኮድላብ ፈተናዎችን ለመፍታት ሙሉ በሙሉ ዝግጁ ነዎት! 🚀🔥"
                ),
            ),
        ],
    ),
]


from bot.tutor.content_js import JS_TUTOR_CHAPTERS
from bot.tutor.content_html import HTML_TUTOR_CHAPTERS
from bot.tutor.content_css import CSS_TUTOR_CHAPTERS
from bot.tutor.content_sql import SQL_TUTOR_CHAPTERS
from bot.tutor.content_java import JAVA_TUTOR_CHAPTERS
from bot.tutor.content_csharp import CSHARP_TUTOR_CHAPTERS
from bot.tutor.content_ts import TYPESCRIPT_TUTOR_CHAPTERS
from bot.tutor.content_bash import BASH_TUTOR_CHAPTERS
from bot.tutor.content_vb import VB_TUTOR_CHAPTERS
from bot.tutor.content_perl import PERL_TUTOR_CHAPTERS
from bot.tutor.content_php import PHP_TUTOR_CHAPTERS
from bot.tutor.content_c import C_TUTOR_CHAPTERS
from bot.tutor.content_react import REACT_TUTOR_CHAPTERS
from bot.tutor.content_rn import RN_TUTOR_CHAPTERS
from bot.tutor.content_angular import ANGULAR_TUTOR_CHAPTERS
from bot.tutor.content_vue import VUE_TUTOR_CHAPTERS
from bot.tutor.content_express import EXPRESS_TUTOR_CHAPTERS
from bot.tutor.content_django import DJANGO_TUTOR_CHAPTERS


def get_all_tutor_chapters(track: str = "python") -> List[TutorChapter]:
    """Return all chapters ordered for the specified track."""
    if track == "django":
        return sorted(DJANGO_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "express":
        return sorted(EXPRESS_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "vue":
        return sorted(VUE_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "angular":
        return sorted(ANGULAR_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "react_native":
        return sorted(RN_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "react":
        return sorted(REACT_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "c":
        return sorted(C_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "php":
        return sorted(PHP_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "javascript":
        return sorted(JS_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "html":
        return sorted(HTML_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "css":
        return sorted(CSS_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "sql":
        return sorted(SQL_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "java":
        return sorted(JAVA_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "csharp":
        return sorted(CSHARP_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "typescript":
        return sorted(TYPESCRIPT_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "bash":
        return sorted(BASH_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "vb":
        return sorted(VB_TUTOR_CHAPTERS, key=lambda c: c.order)
    if track == "perl":
        return sorted(PERL_TUTOR_CHAPTERS, key=lambda c: c.order)
    return sorted(TUTOR_CHAPTERS, key=lambda c: c.order)


def get_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve tutor chapter by ID from any track."""
    for ch in TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in JS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in HTML_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in CSS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in SQL_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in JAVA_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in CSHARP_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in TYPESCRIPT_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in BASH_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in VB_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in PERL_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in PHP_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in C_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in REACT_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in RN_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in ANGULAR_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in VUE_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in EXPRESS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    for ch in DJANGO_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return the next chapter ID within its track."""
    if current_id.startswith("django_"):
        chapters = get_all_tutor_chapters("django")
    elif current_id.startswith("express_"):
        chapters = get_all_tutor_chapters("express")
    elif current_id.startswith("vue_"):
        chapters = get_all_tutor_chapters("vue")
    elif current_id.startswith("ng_"):
        chapters = get_all_tutor_chapters("angular")
    elif current_id.startswith("rn_"):
        chapters = get_all_tutor_chapters("react_native")
    elif current_id.startswith("react_"):
        chapters = get_all_tutor_chapters("react")
    elif current_id.startswith("c_"):
        chapters = get_all_tutor_chapters("c")
    elif current_id.startswith("php_"):
        chapters = get_all_tutor_chapters("php")
    elif current_id.startswith("perl_"):
        chapters = get_all_tutor_chapters("perl")
    elif current_id.startswith("vb_"):
        chapters = get_all_tutor_chapters("vb")
    elif current_id.startswith("bash_"):
        chapters = get_all_tutor_chapters("bash")
    elif current_id.startswith("ts_"):
        chapters = get_all_tutor_chapters("typescript")
    elif current_id.startswith("cs_"):
        chapters = get_all_tutor_chapters("csharp")
    elif current_id.startswith("java_"):
        chapters = get_all_tutor_chapters("java")
    elif current_id.startswith("sql_"):
        chapters = get_all_tutor_chapters("sql")
    elif current_id.startswith("css_"):
        chapters = get_all_tutor_chapters("css")
    elif current_id.startswith("html_"):
        chapters = get_all_tutor_chapters("html")
    elif current_id.startswith("js_"):
        chapters = get_all_tutor_chapters("javascript")
    else:
        chapters = get_all_tutor_chapters("python")

    for idx, ch in enumerate(chapters):





        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id

            return None
    return None

