"""C# curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

CSHARP_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="cs_ch1",
        order=1,
        title_en="C# Ch 1: Welcome to C# & Console.WriteLine",
        title_am="ሲ ሻርፕ ምዕራፍ 1፦ ከC# ጋር መተዋወቅ እና Console.WriteLine",
        description_en="Discover Microsoft C#, the language behind Unity game engine and enterprise software.",
        description_am="የዩኒቲ (Unity) ጌም ኢንጂን እና የቢዝነስ አፕሊኬሽኖች ቋንቋ የሆነውን ማይክሮሶፍት C# ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *Welcome to C# (C-Sharp)!* 🎮\n\n"
                    "Developed by Microsoft, **C#** is one of the most beloved programming languages in the world.\n\n"
                    "It is the #1 language used to create **video games in Unity** (like Pokemon GO, Among Us, and Hollow Knight), "
                    "as well as desktop software and massive enterprise cloud servers!\n\n"
                    "In C#, to print text to the screen, we tell the console:\n"
                    "`Console.WriteLine(\"Your Text\");`\n\n"
                    "⚠️ *Rule*: Like Java, every C# statement must end with a semicolon `;`!"
                ),
                message_am=(
                    "⚡ *እንኳን ወደ C# (ሲ-ሻርፕ) በደህና መጡ!* 🎮\n\n"
                    "በማይክሮሶፍት የተሰራው **C#** በዓለም ላይ እጅግ ተወዳጅ ከሆኑት የኮምፒውተር ቋንቋዎች አንዱ ነው።\n\n"
                    "በተለይም በ**ዩኒቲ (Unity) ጌም ማበልጸጊያ** ውስጥ የቪዲዮ ጨዋታዎችን ለመስራት (እንደ Among Us, Pokemon GO ያሉ) "
                    "እንዲሁም ግዙፍ የክላውድ ሲስተሞችን ለመገንባት ዋነኛው ቋንቋ ነው!\n\n"
                    "በC# ውስጥ ጽሁፍ በስክሪኑ ላይ ለማውጣት የምንጠቀመው ትዕዛዝ፦\n"
                    "`Console.WriteLine(\"ጽሁፍ እዚህ\");`\n\n"
                    "⚠️ *ህግ*፦ በC# ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን `;` መዘጋት አለበት!"
                ),
            ),
            TutorStep(
                id="cs_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first words in C#!\n\n"
                    "👇 *Type this line in the chat and send:*\n"
                    '```csharp\nConsole.WriteLine("Hello C#");\n```'
                ),
                message_am=(
                    "በC# የመጀመሪያውን ጽሁፍ እናሳትም!\n\n"
                    "👇 *ይህንን መስመር ጽፈው ይላኩ፦*\n"
                    '```csharp\nConsole.WriteLine("Hello C#");\n```'
                ),
                expected_code_output="Hello C#",
                hint_en='Write `Console.WriteLine("Hello C#");` with capital C and W and a semicolon `;`.',
                hint_am='በካፒታል C እና W እንዲሁም መጨረሻው ላይ ሴሚኮለን `;` በማድረግ `Console.WriteLine("Hello C#");` ብለው ይጻፉ።',
                success_message_en=(
                    "🎉 *BOOM!* You just compiled and executed real Microsoft C# code!"
                ),
                success_message_am=(
                    "🎉 *ድንቅ!* እውነተኛ የC# ኮድ አሁን በተሳካ ሁኔታ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="cs_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which command displays text on the screen in C#?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ በማያ ገጹ ላይ ጽሁፍ እንዲታይ የሚያደርገው ትዕዛዝ የትኛው ነው?"
                ),
                options_en=[
                    "Console.WriteLine()",
                    "print()",
                    "System.out.println()",
                    "echo()",
                ],
                options_am=[
                    "Console.WriteLine()",
                    "print()",
                    "System.out.println()",
                    "echo()",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `Console.WriteLine()` is C#'s standard output command!",
                success_message_am="🌟 ትክክል! `Console.WriteLine()` በC# ውስጥ ጽሁፍ ለማሳየት የሚያገለግል ትዕዛዝ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="cs_ch2",
        order=2,
        title_en="C# Ch 2: Variables & Combining Text",
        title_am="ሲ ሻርፕ ምዕራፍ 2፦ ተለዋዋጮች እና ጽሁፍን ማጣመር",
        description_en="Learn typed variables and combining text with the + operator.",
        description_am="ተለዋዋጮችን እና በ+ ምልክት ጽሁፍንና ተለዋዋጭን በአንድ ላይ ማጣመር ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *C# Variables: Numbers and Text*\n\n"
                    "In C#, variables have clear types:\n"
                    "- `int score = 50;` (Numbers)\n"
                    "- `string player = \"Yared\";` (Text)\n\n"
                    "To combine text and variables when printing, we use the `+` operator:\n"
                    "```csharp\nstring hero = \"Yared\";\nConsole.WriteLine(\"Player: \" + hero);\n```\n\n"
                    "This glues the words and the variable together!"
                ),
                message_am=(
                    "📦 *የC# ተለዋዋጮች፦ ቁጥሮች እና ጽሁፎች*\n\n"
                    "በC# ውስጥ ተለዋዋጮች የዳታ አይነት አላቸው፦\n"
                    "- `int score = 50;` (ቁጥሮች)\n"
                    "- `string player = \"Yared\";` (ጽሁፎች)\n\n"
                    "ጽሁፍን እና ተለዋዋጭን አጣምሮ ለማሳየት የ `+` ምልክት እንጠቀማለን፦\n"
                    "```csharp\nstring hero = \"Yared\";\nConsole.WriteLine(\"Player: \" + hero);\n```\n\n"
                    "ይህ ቃላቱን እና የተለዋዋጩን ዋጋ አንድ ላይ ያጣብቃቸዋል!"
                ),
            ),
            TutorStep(
                id="cs_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare `int level = 5;` and print `Level: 5` using the `+` operator!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```csharp\nint level = 5;\nConsole.WriteLine("Level: " + level);\n```'
                ),
                message_am=(
                    "`int level = 5;` ፈጥረው በ `\"Level: \" + level` ያትሙት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```csharp\nint level = 5;\nConsole.WriteLine("Level: " + level);\n```'
                ),
                expected_code_output="Level: 5",
                hint_en='Write `int level = 5;` then `Console.WriteLine("Level: " + level);`.',
                hint_am='`int level = 5;` ጽፈው በሁለተኛው መስመር `Console.WriteLine("Level: " + level);` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Smooth concatenation!* You mastered combining text and variables in C#!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* የC# ጽሁፍ እና ተለዋዋጭ ማጣመርን በሚገባ ተምረዋል!"
                ),
            ),
            TutorStep(
                id="cs_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which operator is used to join text and variables together in C#?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ ጽሁፍን እና ተለዋዋጭን በአንድ ላይ ለማጣመር የምንጠቀመው ምልክት የቱ ነው?"
                ),
                options_en=[
                    "+",
                    "&",
                    ",",
                    "->",
                ],
                options_am=[
                    "+",
                    "&",
                    ",",
                    "->",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! The `+` operator joins strings and variables!",
                success_message_am="🌟 ትክክል! የ `+` ምልክት ጽሁፎችን እና ተለዋዋጮችን ያጣምራል!",
            ),
        ],
    ),
    TutorChapter(

        id="cs_ch3",
        order=3,
        title_en="C# Ch 3: Game Decisions with if/else",
        title_am="ሲ ሻርፕ ምዕራፍ 3፦ የጨዋታ ውሳኔዎች (if / else)",
        description_en="Learn how game characters check health and trigger Game Over.",
        description_am="የጨዋታ ገጸ-ባህሪያት ጤናቸውን (HP) እንዴት እንደሚፈትሹ እና Game Over እንደሚሉ ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "👾 *Game Logic: Checking Health*\n\n"
                    "In Unity games, every character checks their health points (`hp`).\n\n"
                    "If `hp <= 0`, the character is defeated:\n\n"
                    "```csharp\nint hp = 0;\nif (hp <= 0) {\n    Console.WriteLine(\"Game Over\");\n} else {\n    Console.WriteLine(\"Alive!\");\n}\n```"
                ),
                message_am=(
                    "👾 *የጨዋታ ሎጂክ፦ የጤና መጠንን (HP) መፈተሽ*\n\n"
                    "በዩኒቲ ጌሞች ውስጥ እያንዳንዱ ገጸ-ባህሪ የህይወት መጠኑን (`hp`) ይፈትሻል።\n\n"
                    "የህይወት መጠኑ 0 ወይም ከዚያ በታች ከሆነ ጨዋታው ያበቃል፦\n\n"
                    "```csharp\nint hp = 0;\nif (hp <= 0) {\n    Console.WriteLine(\"Game Over\");\n} else {\n    Console.WriteLine(\"Alive!\");\n}\n```"
                ),
            ),
            TutorStep(
                id="cs_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Check if character is alive when `hp = 75`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```csharp\nint hp = 75;\nif (hp > 0) {\n    Console.WriteLine("Alive");\n}\n```'
                ),
                message_am=(
                    "የተጫዋቹ ህይወት `hp = 75` ሲሆን በህይወት መኖሩን (Alive) አትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```csharp\nint hp = 75;\nif (hp > 0) {\n    Console.WriteLine("Alive");\n}\n```'
                ),
                expected_code_output="Alive",
                hint_en='Write the if condition checking `hp > 0` and print "Alive".',
                hint_am='`hp > 0` መሆኑን በif መርምረው "Alive" ብለው ያትሙ።',
                success_message_en=(
                    "🎉 *Character is Alive!* You just wrote your first real video game conditional logic!"
                ),
                success_message_am=(
                    "🎉 *ተጫዋቹ በህይወት አለ!* የመጀመሪያውን የቪዲዮ ጌም ሎጂክ ኮድ በC# ጽፈዋል!"
                ),
            ),
            TutorStep(
                id="cs_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In C#, which block runs if the `if` condition evaluates to false?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ የ `if` መስፈርት ሳይሳካ ሲቀር (ሐሰት ሲሆን) የትኛው ክፍል ይሰራል?"
                ),
                options_en=[
                    "else",
                    "then",
                    "stop",
                    "otherwise",
                ],
                options_am=[
                    "else",
                    "then",
                    "stop",
                    "otherwise",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! The `else` block executes when the condition is false!",
                success_message_am="🌟 ትክክል! መስፈርቱ ሳይሟላ ሲቀር የ `else` ክፍል ይሰራል!",
            ),
        ],
    ),
    TutorChapter(
        id="cs_ch4",
        order=4,
        title_en="C# Ch 4: Loops & Countdown Timers",
        title_am="ሲ ሻርፕ ምዕራፍ 4፦ ሉፖች እና የቁልቁለት ቆጣሪዎች (Countdowns)",
        description_en="Learn how for loops power countdown timers and enemy spawners.",
        description_am="የ for ሉፖች የጨዋታ ቆጣሪዎችን እና ተደጋጋሚ ድርጊቶችን እንዴት እንደሚያንቀሳቅሱ ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⏳ *Countdowns with for Loops*\n\n"
                    "In video games, timers count down: 3... 2... 1... START!\n\n"
                    "To count down backwards, we start at 3 and use `i--` (decrease by 1):\n\n"
                    "```csharp\nfor (int i = 3; i >= 1; i--) {\n    Console.WriteLine(i);\n}\n```"
                ),
                message_am=(
                    "⏳ *የቁልቁለት ቆጣሪዎች በ for ሉፕ*\n\n"
                    "በጨዋታዎች ውስጥ ቆጣሪዎች ወደ ኋላ ይቆጥራሉ፦ 3... 2... 1... ጀምር!\n\n"
                    "ወደ ኋላ ለመቁጠር ከ3 ጀምረን `i--` (በየዙሩ 1 ቀንስ) እንጠቀማለን፦\n\n"
                    "```csharp\nfor (int i = 3; i >= 1; i--) {\n    Console.WriteLine(i);\n}\n```"
                ),
            ),
            TutorStep(
                id="cs_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Run a countdown from 3 to 1!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```csharp\nfor (int i = 3; i >= 1; i--) {\n    Console.WriteLine(i);\n}\n```"
                ),
                message_am=(
                    "ከ 3 እስከ 1 የሚቆጥር የቁልቁለት ቆጣሪ እናስኬድ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```csharp\nfor (int i = 3; i >= 1; i--) {\n    Console.WriteLine(i);\n}\n```"
                ),
                expected_code_output="3\n2\n1",
                hint_en="Write the backwards for loop using `i--` and print `i`.",
                hint_am="የ for ሉፑን በ `i--` ወደ ኋላ እንዲቆጥር አድርገው ጽፈው ይላኩ።",
                success_message_en=(
                    "🚀 *3... 2... 1... BLAST OFF!* Your countdown loop completed perfectly!"
                ),
                success_message_am=(
                    "🚀 *3... 2... 1... ተጀመረ!* የቁልቁለት ቆጣሪው በሚገባ ሰርቷል!"
                ),
            ),
            TutorStep(
                id="cs_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In C#, which operator decreases a variable by 1?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ የአንድን ተለዋዋጭ ዋጋ በ1 ለመቀነስ የምንጠቀመው የቱ ነው?"
                ),
                options_en=[
                    "i--",
                    "i++",
                    "i - 0",
                    "i**",
                ],
                options_am=[
                    "i--",
                    "i++",
                    "i - 0",
                    "i**",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `i--` is shortcut for decreasing by 1!",
                success_message_am="🌟 በትክክል! `i--` ማለት ከቁጥሩ ላይ 1 ቀንስ ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="cs_ch5",
        order=5,
        title_en="C# Ch 5: Game Inventories with Arrays",
        title_am="ሲ ሻርፕ ምዕራፍ 5፦ የጨዋታ እቃዎች ዝርዝር (Game Inventory)",
        description_en="Learn how game characters store weapons and items in arrays.",
        description_am="የጨዋታ ገጸ-ባህሪያት መሳሪያዎችን እና እቃዎችን በአሬይ ውስጥ እንዴት እንደሚያስቀምጡ ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎒 *Game Inventory: Storing Weapons in Arrays*\n\n"
                    "Every hero in an RPG has an inventory of items (Sword, Shield, Potion).\n\n"
                    "In C#, we store strings in an array like this:\n"
                    "```csharp\nstring[] inventory = {\"Sword\", \"Shield\", \"Potion\"};\n```\n\n"
                    "Accessing `inventory[0]` gets the first item: `\"Sword\"`!"
                ),
                message_am=(
                    "🎒 *የጨዋታ እቃዎች ማከማቻ (Inventory)*\n\n"
                    "በጀብዱ ጨዋታዎች ውስጥ ተጫዋቾች የእቃዎች ቦርሳ አላቸው (ጎራዴ፣ ጋሻ፣ መድሀኒት)።\n\n"
                    "በC# ውስጥ እነዚህን በአሬይ ውስጥ እንዲህ እናስቀምጣቸዋለን፦\n"
                    "```csharp\nstring[] inventory = {\"Sword\", \"Shield\", \"Potion\"};\n```\n\n"
                    "`inventory[0]` የመጀመሪያውን እቃ (Sword) ያወጣል!"
                ),
            ),
            TutorStep(
                id="cs_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Equip your first weapon by printing `inventory[0]`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```csharp\nstring[] inventory = {"Sword", "Shield"};\nConsole.WriteLine(inventory[0]);\n```'
                ),
                message_am=(
                    "በቦርሳዎ ውስጥ ያለውን የመጀመሪያውን መሳሪያ `inventory[0]` አትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```csharp\nstring[] inventory = {"Sword", "Shield"};\nConsole.WriteLine(inventory[0]);\n```'
                ),
                expected_code_output="Sword",
                hint_en='Write `string[] inventory = {"Sword", "Shield"};` then print index 0.',
                hint_am='አሬዩን ፈጥረው በሁለተኛው መስመር `Console.WriteLine(inventory[0]);` ብለው ይላኩ።',
                success_message_en=(
                    "⚔️ *Weapon Equipped!* Sword is in your hand ready for battle!"
                ),
                success_message_am=(
                    "⚔️ *መሳሪያውን ታጥቀዋል!* ጎራዴው ዝግጁ ሆኗል!"
                ),
            ),
            TutorStep(
                id="cs_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In C#, what index holds the second element of an array?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ የአንድ አሬይ ሁለተኛው እቃ የሚገኝበት ኢንዴክስ ስንት ነው?"
                ),
                options_en=[
                    "1",
                    "2",
                    "0",
                    "-1",
                ],
                options_am=[
                    "1",
                    "2",
                    "0",
                    "-1",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Since arrays start at 0, the second item is at index 1!",
                success_message_am="🌟 ትክክል! ቆጠራ ከ0 ስለሚጀምር ሁለተኛው እቃ የሚገኘው በ1 ላይ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="cs_ch6",
        order=6,
        title_en="C# Ch 6: Methods & Calculations",
        title_am="ሲ ሻርፕ ምዕራፍ 6፦ ሜተዶች እና የሂሳብ ቀመሮች",
        description_en="Learn how methods bundle reusable game mechanics.",
        description_am="ሜተዶች የጨዋታ ህጎችን እና ቀመሮችን እንዴት እንደሚያጠቃልሉ ይማሩ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "💥 *Game Mechanics: Attack Power Calculation*\n\n"
                    "When a player attacks an enemy, damage is calculated by multiplying base attack by a critical hit multiplier:\n\n"
                    "```csharp\nstatic int Attack(int power) {\n    return power * 2;\n}\n```\n\n"
                    "C# built-in `Math.Min` and `Math.Max` can also cap damage so enemies don't get negative health!"
                ),
                message_am=(
                    "💥 *የጨዋታ ቀመሮች፦ የጥቃት ሀይል (Damage) ስሌት*\n\n"
                    "አንድ ተጫዋች ጠላትን ሲመታ፣ የሚደርሰው ጉዳት በመሰረታዊ ጥቃት እና በወሳኝ ምት (Critical hit) ብዜት ይሰላል፦\n\n"
                    "```csharp\nstatic int Attack(int power) {\n    return power * 2;\n}\n```\n\n"
                    "በተጨማሪም የC# `Math.Max` እና `Math.Min` ጠላት ከ0 በታች ህይወት እንዳይኖረው ለመቆጣጠር ይጠቅማሉ!"
                ),
            ),
            TutorStep(
                id="cs_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Use `Math.Max(0, 100 - 120)` to ensure health never drops below 0!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```csharp\nint safeHp = Math.Max(0, -20);\nConsole.WriteLine(safeHp);\n```"
                ),
                message_am=(
                    "ህይወት ከ 0 በታች እንዳይወርድ በ `Math.Max(0, -20)` እንከላከል!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```csharp\nint safeHp = Math.Max(0, -20);\nConsole.WriteLine(safeHp);\n```"
                ),
                expected_code_output="0",
                hint_en="Write `int safeHp = Math.Max(0, -20);` then `Console.WriteLine(safeHp);`.",
                hint_am="`int safeHp = Math.Max(0, -20);` ጽፈው በሁለተኛው መስመር `Console.WriteLine(safeHp);` ብለው ይላኩ።",
                success_message_en=(
                    "🛡️ *Damage Capped!* Health was protected and safely stayed at 0!"
                ),
                success_message_am=(
                    "🛡️ *ጉዳቱ ተቆጥጥሯል!* የህይወት መጠኑ ከ0 በታች እንዳይወርድ ተደርጓል!"
                ),
            ),
            TutorStep(
                id="cs_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What does `Math.Max(10, 50)` return in C#?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በC# ውስጥ `Math.Max(10, 50)` የሚመልሰው ዋጋ ስንት ነው?"
                ),
                options_en=[
                    "50",
                    "10",
                    "60",
                    "40",
                ],
                options_am=[
                    "50",
                    "10",
                    "60",
                    "40",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `Math.Max` returns the larger of two values (50)!",
                success_message_am="🌟 ትክክል! `Math.Max` ከሁለቱ ትልቁን (50) ይመልሳል!",
            ),
        ],
    ),
    TutorChapter(
        id="cs_ch7",
        order=7,
        title_en="C# Ch 7: Capstone Project: RPG Combat Battle Arena",
        title_am="ሲ ሻርፕ ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የRPG ጦርነት አሬና ጌም",
        description_en="Combine variables, health math, conditions, and string interpolation into a real battle round.",
        description_am="ተለዋዋጮችን፣ የህይወት ቀመሮችን፣ ሁኔታዎችን እና String Interpolation በማጣመር የጦርነት ዙር ጨዋታ ይገንቡ።",
        track="csharp",
        steps=[
            TutorStep(
                id="cs_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚔️ *C# Capstone Project: The RPG Battle Round!* 🐉\n\n"
                    "You now know:\n"
                    "1. `Console.WriteLine` to display game narrative\n"
                    "2. Typed variables (`int bossHp = 100;`)\n"
                    "3. String interpolation (`$\"...\"`)\n"
                    "4. `if / else` decision branches\n"
                    "5. Health bounds protection\n\n"
                    "In this capstone, you will program a battle round where the Hero strikes a Boss for 45 damage:\n"
                    "- Start: `int bossHp = 100;`\n"
                    "- Damage: `int damage = 45;`\n"
                    "- Calculate remaining: `bossHp -= damage;`\n"
                    "- Print: `Boss HP: 55`"
                ),
                message_am=(
                    "⚔️ *የC# ማጠቃለያ ፕሮጀክት፦ የRPG ጦርነት ዙር!* 🐉\n\n"
                    "እስካሁን የተማርናቸው፦\n"
                    "1. `Console.WriteLine` የታሪኩን ጽሁፍ ለማሳየት\n"
                    "2. ተለዋዋጮች (`int bossHp = 100;`)\n"
                    "3. String interpolation (`$\"...\"`)\n"
                    "4. የ `if / else` የውሳኔ ቅርንጫፎች\n"
                    "5. የህይወት መጠን ስሌት\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት ጀግናው ጭራቁን (Boss) 45 ጉዳት የሚያደርስበትን የጦርነት ዙር እናዘጋጃለን፦\n"
                    "- የመጀመሪያ ህይወት፦ `int bossHp = 100;`\n"
                    "- ጉዳት፦ `int damage = 45;`\n"
                    "- ቀሪ ህይወት፦ `bossHp -= damage;`\n"
                    "- ማሳወቅ፦ `Boss HP: 55`"
                ),
            ),
            TutorStep(
                id="cs_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete RPG combat strike!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```csharp\nint bossHp = 100;\nint damage = 45;\nbossHp = bossHp - damage;\nConsole.WriteLine("Boss HP: " + bossHp);\n```'
                ),
                message_am=(
                    "ሙሉውን የጦርነት ምት ኮድ ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```csharp\nint bossHp = 100;\nint damage = 45;\nbossHp = bossHp - damage;\nConsole.WriteLine("Boss HP: " + bossHp);\n```'
                ),
                expected_code_output="Boss HP: 55",
                hint_en='Write the damage calculation with `Console.WriteLine("Boss HP: " + bossHp);`.',
                hint_am='`Console.WriteLine("Boss HP: " + bossHp);` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *CRITICAL STRIKE!* ⚔️🐉\n\n"
                    "You just programmed a real video game combat mechanic in C#!\n\n"
                    "Boss HP dropped from 100 to 55! You are ready to create games with C#!"
                ),

                success_message_am=(
                    "🎉 *አስደናቂ ምት!* ⚔️🐉\n\n"
                    "እውነተኛ የቪዲዮ ጨዋታ የውጊያ ሎጂክ በC# ገንብተዋል!\n\n"
                    "የጭራቁ ህይወት ከ100 ወደ 55 ወርዷል! አሁን በC# ጌሞችን ለመስራት ዝግጁ ነዎት!"
                ),
            ),
            TutorStep(
                id="cs_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final C# Master Question:*\n\n"
                    "Which game engine is world-famous for using C# as its primary programming language?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የC# ማጠቃለያ ጥያቄ፦*\n\n"
                    "C#ን እንደ ዋነኛ የኮዲንግ ቋንቋው በመጠቀም በዓለም ዙሪያ ዝነኛ የሆነው የጌም ኢንጂን የትኛው ነው?"
                ),
                options_en=[
                    "Unity",
                    "Unreal (C++)",
                    "Godot (GDScript)",
                    "Pygame",
                ],
                options_am=[
                    "Unity",
                    "Unreal (C++)",
                    "Godot (GDScript)",
                    "Pygame",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! Unity is the world's most popular game engine powered by C#!",
                success_message_am="🏆 እጅግ ድንቅ! ዩኒቲ (Unity) በC# የሚሰራ በዓለም ላይ እጅግ ታዋቂው የጌም ኢንጂን ነው!",
            ),
        ],
    ),
]
