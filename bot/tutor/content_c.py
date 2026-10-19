"""C curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

C_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="c_ch1",
        order=1,
        title_en="C Ch 1: The Mother of Modern Code & printf",
        title_am="ሲ ምዕራፍ 1፦ የዘመናዊ ቋንቋዎች እናት እና printf",
        description_en="Discover the foundational language that built Linux, Windows, and modern computing.",
        description_am="ሊኑክስን፣ ዊንዶውስን እና መላው የኮምፒውተር አለምን ያቆመውን የሲ (C) ቋንቋ ይማሩ።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🇨 *Welcome to the C Language!* 🏛️⚡\n\n"
                    "Created by Dennis Ritchie at Bell Labs, **C is the mother of all modern programming**!\n\n"
                    "- The **Linux Kernel**, **Windows Kernel**, and **macOS** are written in C.\n"
                    "- Python, JavaScript engines, and databases (MySQL, SQLite) are all built with C.\n"
                    "- Rockets, cars, airplanes, and medical devices run on C because of its lightning speed and direct hardware control.\n\n"
                    "In C, to print text to the screen, we use `printf()`:\n\n"
                    "```c\nprintf(\"Hello C!\\n\");\n```\n\n"
                    "- Text is placed inside double quotes `\"...\"`\n"
                    "- Every C statement ends with a semicolon `;`\n"
                    "- `\\n` creates a fresh new line!"
                ),
                message_am=(
                    "🇨 *እንኳን ወደ ሲ (C) ቋንቋ በደህና መጡ!* 🏛️⚡\n\n"
                    "በዴኒስ ሪቺ የተፈጠረው ሲ (C) **የዘመናዊ ኮዲንግ አለም እናት** በመባል ይታወቃል!\n\n"
                    "- **የሊኑክስ፣ የዊንዶውስ እና የማክ (macOS)** የኮምፒውተር አንጎል (Kernel) የተገነቡት በ C ነው።\n"
                    "- ፓይተን፣ የጃቫስክሪፕት ሞተሮች እና ዳታቤዞች የተሰሩት በ C ነው።\n"
                    "- ሮኬቶች፣ አውሮፕላኖች እና የህክምና መሳሪያዎች በከፍተኛ ፍጥነቱ ምክንያት በ C ይሰራሉ።\n\n"
                    "በ C ውስጥ ጽሁፍ ለማሳየት `printf()` የሚለውን ትዕዛዝ እንጠቀማለን፦\n\n"
                    "```c\nprintf(\"Hello C!\\n\");\n```\n\n"
                    "- ጽሁፍ በጥቅስ ምልክት `\"...\"` ውስጥ ይቀመጣል\n"
                    "- እያንዳንዱ መስመር በሴሚኮለን `;` ይዘጋል\n"
                    "- `\\n` አዲስ መስመር ይፈጥራል!"
                ),
            ),
            TutorStep(
                id="c_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first message in C!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```c\nprintf("Hello C!\\n");\n```'
                ),
                message_am=(
                    "በ C ቋንቋ የመጀመሪያውን ጽሁፍ እናውጣ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nprintf("Hello C!\\n");\n```'
                ),
                expected_code_output="Hello C!",
                hint_en='Write `printf("Hello C!\\n");` with quotes, parenthesis, and a semicolon `;`.',
                hint_am='በጥቅስ እና በሴሚኮለን `printf("Hello C!\\n");` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *BRAVO!* You just compiled and executed real C code directly on hardware!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* እውነተኛ የሲ (C) ኮድ ኮምፓይል ተደርጎ በማሽኑ ላይ ሰርቷል!"
                ),
            ),
            TutorStep(
                id="c_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which standard function is used in C to print formatted text to the screen?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ C ቋንቋ ውስጥ ጽሁፎችን ለማሳየት የትኛው መሰረታዊ ፈንክሽን ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "printf()",
                    "echo()",
                    "System.out()",
                    "print_line()",
                ],
                options_am=[
                    "printf()",
                    "echo()",
                    "System.out()",
                    "print_line()",
                ],
                correct_option_index=0,
                hint_en="Dennis Ritchie named it `printf` for 'print formatted'!",
                hint_am="ፈጣሪው ዴኒስ ሪቺ 'print formatted' በሚል `printf` ብሎ ሰየመው!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch2",
        order=2,
        title_en="C Ch 2: Typed Variables & Format Specifiers",
        title_am="ሲ ምዕራፍ 2፦ ተለዋዋጮች እና የፎርማት ምልክቶች",
        description_en="Store integers, decimals, and print them with format placeholders.",
        description_am="ሙሉ ቁጥሮችን እና አስርዮሾችን በማህደረ-ትውስታ ውስጥ ማስቀመጥ እና በፎርማት ማሳየት።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Data Types & Memory in C* 🧠\n\n"
                    "C is a strongly typed language. The computer allocates exact bytes in RAM based on the type you declare:\n\n"
                    "- `int`: Whole numbers like `10`, `500`\n"
                    "- `float` / `double`: Decimal numbers like `3.14`\n"
                    "- `char`: Single letters like `'A'`\n\n"
                    "To print a variable with `printf()`, we use **Format Specifiers** (placeholders):\n"
                    "- `%d` for integers (`int`)\n"
                    "- `%f` for decimals (`float`)\n\n"
                    "```c\nint score = 95;\nprintf(\"Score: %d\\n\", score);\n```"
                ),
                message_am=(
                    "📦 *የዳታ አይነቶች እና ሜሞሪ በ C* 🧠\n\n"
                    "የሲ (C) ቋንቋ አይነቶችን በጥብቅ ይወስናል። ኮምፒውተሩ በማህደረ-ትውስታው (RAM) ውስጥ እንደ አይነቱ ቦታ ይመድባል፦\n\n"
                    "- `int`፦ ሙሉ ቁጥሮች (እንደ `10`, `500`)\n"
                    "- `float` / `double`፦ የአስርዮሽ ቁጥሮች (እንደ `3.14`)\n"
                    "- `char`፦ ነጠላ ፊደላት (እንደ `'A'`)\n\n"
                    "በ `printf()` ውስጥ ተለዋዋጭን ለማሳየት **የፎርማት ምልክቶችን** እንጠቀማለን፦\n"
                    "- `%d` ለሙሉ ቁጥር (`int`)\n"
                    "- `%f` ለአስርዮሽ (`float`)\n\n"
                    "```c\nint score = 95;\nprintf(\"Score: %d\\n\", score);\n```"
                ),
            ),
            TutorStep(
                id="c_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare an integer `int score = 95;` and print it using `%d`!\n\n"
                    "👇 *Type and send this code:*\n"
                    '```c\nint score = 95;\nprintf("Score: %d\\n", score);\n```'
                ),
                message_am=(
                    "የ `int score = 95;` ተለዋዋጭ ፈጥረው በ `%d` አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nint score = 95;\nprintf("Score: %d\\n", score);\n```'
                ),
                expected_code_output="Score: 95",
                hint_en='Write `int score = 95; printf("Score: %d\\n", score);`',
                hint_am='`int score = 95; printf("Score: %d\\n", score);` ብለው ይላኩ።',
                success_message_en=(
                    "🌟 *PERFECT!* You stored 95 in high-speed hardware memory and printed it with `%d`!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* 95 ቁጥርን በማህደረ-ትውስታ አስቀምጠው በ `%d` አሳይተዋል!"
                ),
            ),
            TutorStep(
                id="c_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Which format specifier is used in `printf()` to display an integer (`int`)?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ `printf()` ውስጥ ሙሉ ቁጥርን (`int`) ለማሳየት የትኛው የፎርማት ምልክት ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "%d (decimal integer)",
                    "%s (string)",
                    "%c (single char)",
                    "%p (pointer)",
                ],
                options_am=[
                    "%d (ሙሉ ቁጥር)",
                    "%s (ጽሁፍ)",
                    "%c (ነጠላ ፊደል)",
                    "%p (ፖይንተር)",
                ],
                correct_option_index=0,
                hint_en="`%d` stands for decimal integer!",
                hint_am="`%d` ለሙሉ ቁጥሮች (decimal integer) ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch3",
        order=3,
        title_en="C Ch 3: Numbers & Hardware Arithmetic",
        title_am="ሲ ምዕራፍ 3፦ ቁጥሮች እና የማሽን ሂሳብ",
        description_en="Harness the raw CPU speed of C for mathematical calculations.",
        description_am="የኮምፒውተር ፕሮሰሰርን ፈጣን የሂሳብ ስሌት በ C መምራት።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔢 *Math at Silicon Speed!* ⚡\n\n"
                    "Because C translates directly into machine assembly instructions, calculations execute in nanoseconds!\n\n"
                    "Operators:\n"
                    "- Addition: `+`\n"
                    "- Subtraction: `-`\n"
                    "- Multiplication: `*`\n"
                    "- Division: `/`\n"
                    "- Modulo (remainder): `%`\n\n"
                    "```c\nint a = 20;\nint b = 30;\nprintf(\"%d\\n\", a + b); // 50\n```"
                ),
                message_am=(
                    "🔢 *ፈጣን የሂሳብ ስሌት በማሽን ፍጥነት!* ⚡\n\n"
                    "የሲ (C) ቋንቋ በቀጥታ ወደ ማሽን ትዕዛዝ ስለሚቀየር ስሌቶችን በናኖሰከንድ ያከናውናል!\n\n"
                    "የሂሳብ ምልክቶች፦\n"
                    "- መደመር፦ `+`\n"
                    "- መቀነስ፦ `-`\n"
                    "- ማባዛት፦ `*`\n"
                    "- ማካፈል፦ `/`\n"
                    "- ቀሪ ማግኛ (Modulo)፦ `%`\n\n"
                    "```c\nint a = 20;\nint b = 30;\nprintf(\"%d\\n\", a + b); // 50 ያወጣል\n```"
                ),
            ),
            TutorStep(
                id="c_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Add two integers: `int a = 45; int b = 55;` and print their sum with `%d`!\n\n"
                    "👇 *Type and send this code:*\n"
                    '```c\nint a = 45;\nint b = 55;\nprintf("%d\\n", a + b);\n```'
                ),
                message_am=(
                    "ሁለት ሙሉ ቁጥሮችን ደምረው በ `%d` አውጡ፦ `int a = 45; int b = 55;`!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nint a = 45;\nint b = 55;\nprintf("%d\\n", a + b);\n```'
                ),
                expected_code_output="100",
                hint_en='Write `int a = 45; int b = 55; printf("%d\\n", a + b);`',
                hint_am='`int a = 45; int b = 55; printf("%d\\n", a + b);` ብለው ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* The CPU executed the addition and printed `100`!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ፕሮሰሰሩ ስሌቱን በቅጽበት አከናውኖ `100` አሳይቷል!"
                ),
            ),
            TutorStep(
                id="c_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "In C, what is the result of integer division: `printf(\"%d\", 7 / 2);`?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ C ውስጥ ሙሉ ቁጥር ለሙሉ ቁጥር ሲካፈል `printf(\"%d\", 7 / 2);` ምን ያወጣል?"
                ),
                options_en=[
                    "3 (the decimal is truncated in integer math)",
                    "3.5",
                    "4",
                    "Error",
                ],
                options_am=[
                    "3 (ሙሉ ቁጥር ስለሆነ አስርዮሹ ይጣላል)",
                    "3.5",
                    "4",
                    "ስህተት",
                ],
                correct_option_index=0,
                hint_en="In C, dividing two `int`s produces an `int`, dropping the fractional part!",
                hint_am="በ C ውስጥ ሙሉ ቁጥር ለሙሉ ቁጥር ሲካፈል ውጤቱ ሙሉ ቁጥር ብቻ ነው (አስርዮሹ ይጣላል)!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch4",
        order=4,
        title_en="C Ch 4: Making Decisions with if / else",
        title_am="ሲ ምዕራፍ 4፦ ውሳኔዎች በ if / else",
        description_en="Control execution paths based on sensor limits, conditions, and thresholds.",
        description_am="እንደ ሴንሰር ገደቦች እና መስፈርቶች ያሉ ሁኔታዎችን በ if/else መቆጣጠር።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Making Decisions with `if` and `else`* 🧠\n\n"
                    "C allows microcontrollers and operating systems to make split-second decisions:\n\n"
                    "```c\nif (temp > 100) {\n    printf(\"Warning! Overheating!\\n\");\n} else {\n    printf(\"Normal Temp\\n\");\n}\n```\n\n"
                    "- The condition is wrapped in parentheses `( )`\n"
                    "- The code block is wrapped in curly braces `{ }`\n"
                    "- In C, non-zero means TRUE, and `0` means FALSE!"
                ),
                message_am=(
                    "🚦 *በ `if` እና `else` ውሳኔዎችን መወሰን* 🧠\n\n"
                    "በ C ቋንቋ ማሽኖች እና ኦፕሬቲንግ ሲስተሞች ሁኔታዎችን አይተው ይወስናሉ፦\n\n"
                    "```c\nif (temp > 100) {\n    printf(\"Warning! Overheating!\\n\");\n} else {\n    printf(\"Normal Temp\\n\");\n}\n```\n\n"
                    "- መስፈርቱ በቅንፍ `( )` ውስጥ ይቀመጣል\n"
                    "- የሚሰራው ኮድ በፈረንሳይ ቅንፍ `{ }` ውስጥ ይጻፋል\n"
                    "- በ C ውስጥ ከዜሮ ውጪ ያለ ማንኛውም ቁጥር እውነት (TRUE) ሲሆን `0` ሀሰት (FALSE) ነው!"
                ),
            ),
            TutorStep(
                id="c_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write an `if` condition to check if `temp = 30` is greater than `25`!\n\n"
                    "👇 *Type and send:*\n"
                    '```c\nint temp = 30;\nif (temp > 25) {\n    printf("Warm\\n");\n}\n```'
                ),
                message_am=(
                    "የ `temp = 30` ሙቀት ከ `25` በላይ መሆኑን በ `if` ይፈትሹ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nint temp = 30;\nif (temp > 25) {\n    printf("Warm\\n");\n}\n```'
                ),
                expected_code_output="Warm",
                hint_en='Write `int temp = 30; if (temp > 25) { printf("Warm\\n"); }`',
                hint_am='`int temp = 30; if (temp > 25) { printf("Warm\\n"); }` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *EXCELLENT!* The CPU branch evaluated to TRUE and printed `Warm`!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* መስፈርቱ እውነት ሆኖ ተገኝቶ `Warm` ብሎ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="c_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In C, which numeric value represents FALSE?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ C ቋንቋ ውስጥ ሀሰትን (FALSE) የሚወክለው የትኛው ቁጥር ነው?"
                ),
                options_en=[
                    "0",
                    "1",
                    "-1",
                    "100",
                ],
                options_am=[
                    "0",
                    "1",
                    "-1",
                    "100",
                ],
                correct_option_index=0,
                hint_en="In C, `0` is FALSE, and any non-zero value is TRUE!",
                hint_am="በ C ውስጥ `0` ሀሰት (FALSE) ሲሆን ማንኛውም ከ 0 ውጪ የሆነ ቁጥር እውነት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch5",
        order=5,
        title_en="C Ch 5: Repeating with Loops",
        title_am="ሲ ምዕራፍ 5፦ ዑደቶች በ for እና while",
        description_en="Harness automated repetition with blazing fast for loops.",
        description_am="ፈጣን የ `for` ሉፕ በመጠቀም ስራዎችን በራስ-ሰር ማከናወን።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *The Classic C `for` Loop* ⚡\n\n"
                    "The `for` loop syntax invented in C is so famous that JavaScript, Java, C#, PHP, and TypeScript all copied it!\n\n"
                    "```c\nfor (int i = 1; i <= 3; i++) {\n    printf(\"%d \", i);\n}\n```\n\n"
                    "1. `int i = 1;` initializes the counter variable\n"
                    "2. `i <= 3;` loop test condition\n"
                    "3. `i++` increments counter by 1 each step"
                ),
                message_am=(
                    "🔄 *ታዋቂው የሲ (C) `for` ሉፕ* ⚡\n\n"
                    "በ C የተፈጠረውን የ `for` ሉፕ አጻጻፍ ጃቫስክሪፕት፣ ጃቫ፣ ሲሻርፕ፣ ፒኤችፒ እና ታይፕስክሪፕት በሙሉ ቀድተወታል!\n\n"
                    "```c\nfor (int i = 1; i <= 3; i++) {\n    printf(\"%d \", i);\n}\n```\n\n"
                    "1. `int i = 1;` ቆጣሪውን በ 1 ያስጀምራል\n"
                    "2. `i <= 3;` የሉፑ ማብቂያ መስፈርት\n"
                    "3. `i++` በእያንዳንዱ ዙር 1 ይጨምራል"
                ),
            ),
            TutorStep(
                id="c_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write a loop counting from 1 to 3 with spaces!\n\n"
                    "👇 *Type and send:*\n"
                    '```c\nfor (int i = 1; i <= 3; i++) {\n    printf("%d ", i);\n}\n```'
                ),
                message_am=(
                    "ከ 1 እስከ 3 የሚቆጥር የ `for` ሉፕ እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nfor (int i = 1; i <= 3; i++) {\n    printf("%d ", i);\n}\n```'
                ),
                expected_code_output="1 2 3",
                hint_en='Write `for (int i = 1; i <= 3; i++) { printf("%d ", i); }`',
                hint_am='`for (int i = 1; i <= 3; i++) { printf("%d ", i); }` ብለው ይላኩ።',
                success_message_en=(
                    "🔥 *OUTSTANDING!* You just ran a high-speed compiled C loop!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* እጅግ ፈጣን የ C ቋንቋ ሉፕ በተሳካ ሁኔታ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="c_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Which loop header correctly loops 5 times starting from 0?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "ከ 0 ጀምሮ 5 ጊዜ በትክክል የሚዞረው የትኛው ነው?"
                ),
                options_en=[
                    "for (int i = 0; i < 5; i++)",
                    "for (int i = 0; i > 5; i++)",
                    "for (i = 5; i = 0; i--)",
                    "for loop(5)",
                ],
                options_am=[
                    "for (int i = 0; i < 5; i++)",
                    "for (int i = 0; i > 5; i++)",
                    "for (i = 5; i = 0; i--)",
                    "for loop(5)",
                ],
                correct_option_index=0,
                hint_en="0, 1, 2, 3, 4 gives 5 iterations when `i < 5`!",
                hint_am="ከ 0 ጀምሮ `i < 5` እስኪሆን ድረስ (0, 1, 2, 3, 4) በትክክል 5 ጊዜ ይዞራል!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch6",
        order=6,
        title_en="C Ch 6: Arrays in C",
        title_am="ሲ ምዕራፍ 6፦ አሬይ (Arrays) በ C",
        description_en="Store continuous blocks of memory and access values by index.",
        description_am="ተከታታይ የሜሞሪ ክፍሎችን በአሬይ ማስቀመጥ እና በኢንዴክስ መጥራት።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📋 *Contiguous Memory: Arrays in C* 🧱\n\n"
                    "In C, an array is a sequence of elements stored back-to-back in RAM.\n\n"
                    "```c\nint scores[3] = {85, 92, 78};\n```\n\n"
                    "- The index starts at `0`: `scores[0]` is `85`\n"
                    "- The second item is `scores[1]`: `92`\n"
                    "- C arrays are fixed size and blazingly fast!"
                ),
                message_am=(
                    "📋 *ተከታታይ ሜሞሪ፦ አሬይ (Arrays) በ C* 🧱\n\n"
                    "በ C ውስጥ አሬይ ማለት በማህደረ-ትውስታ ውስጥ ተከታትለው የተቀመጡ መረጃዎች ስብስብ ነው፦\n\n"
                    "```c\nint scores[3] = {85, 92, 78};\n```\n\n"
                    "- ቆጠራው ከ `0` ይጀምራል፦ `scores[0]` ዋጋው `85` ነው\n"
                    "- ሁለተኛው `scores[1]` ዋጋው `92` ነው\n"
                    "- በ C ውስጥ አሬይ ቋሚ መጠን ያለው እና እጅግ ፈጣን ነው!"
                ),
            ),
            TutorStep(
                id="c_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create an array `int nums[3] = {10, 20, 30};` and print the second element (`nums[1]`) with `%d`!\n\n"
                    "👇 *Type and send:*\n"
                    '```c\nint nums[3] = {10, 20, 30};\nprintf("%d\\n", nums[1]);\n```'
                ),
                message_am=(
                    "የ `int nums[3] = {10, 20, 30};` አሬይ ፈጥረው ሁለተኛውን እሴት (`nums[1]`) አውጡ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\nint nums[3] = {10, 20, 30};\nprintf("%d\\n", nums[1]);\n```'
                ),
                expected_code_output="20",
                hint_en='Write `int nums[3] = {10, 20, 30}; printf("%d\\n", nums[1]);`',
                hint_am='`int nums[3] = {10, 20, 30}; printf("%d\\n", nums[1]);` ብለው ይላኩ።',
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You accessed an element from raw memory via index `1`!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* በኢንዴክስ `1` አማካኝነት ከሜሞሪ ሁለተኛውን እሴት አውጥተዋል!"
                ),
            ),
            TutorStep(
                id="c_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "If an array has 4 items: `int vals[4] = {1, 2, 3, 4};`, what is the index of the very first element?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "አንድ አሬይ 4 መረጃዎች ቢኖሩት `int vals[4] = {1, 2, 3, 4};`፣ የመጀመሪያው መረጃ ኢንዴክስ ስንት ነው?"
                ),
                options_en=[
                    "0",
                    "1",
                    "-1",
                    "4",
                ],
                options_am=[
                    "0",
                    "1",
                    "-1",
                    "4",
                ],
                correct_option_index=0,
                hint_en="In C, array indexing always starts at 0!",
                hint_am="በ C ውስጥ የአሬይ ቆጠራ ሁልጊዜ ከ 0 ነው የሚጀምረው!",
            ),
        ],
    ),
    TutorChapter(
        id="c_ch7",
        order=7,
        title_en="C Ch 7: Functions & Hardware Capstone Project",
        title_am="ሲ ምዕራፍ 7፦ ፈንክሽኖች እና የማሽን መቆጣጠሪያ ፕሮጀክት",
        description_en="Write modular functions and construct a hardware sensor monitor.",
        description_am="እንደገና ጥቅም ላይ የሚውሉ ፈንክሽኖችን በመገንባት የሴንሰር መቆጣጠሪያ ፕሮጀክት መስራት።",
        track="c",
        steps=[
            TutorStep(
                id="c_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *Functions in C* 🛠️\n\n"
                    "A function in C specifies its return type and the types of its parameters:\n\n"
                    "```c\nint addBonus(int score) {\n    return score + 10;\n}\n```\n\n"
                    "- `int` at the start means it returns an integer\n"
                    "- `(int score)` means it receives an integer\n"
                    "- `return` passes back the calculated answer!\n\n"
                    "Now let's build our grand capstone: A Score Bonus Calculator!"
                ),
                message_am=(
                    "🏗️ *ፈንክሽኖች (Functions) በ C* 🛠️\n\n"
                    "በ C ውስጥ ፈንክሽን የሚመልሰውን አይነትና የሚቀበለውን ፓራሜትር አስቀድሞ ይገልጻል፦\n\n"
                    "```c\nint addBonus(int score) {\n    return score + 10;\n}\n```\n\n"
                    "- መጀመሪያ ላይ ያለው `int` የሚመልሰውን አይነት ያሳያል\n"
                    "- `(int score)` የሚቀበለውን አይነት ያመለክታል\n"
                    "- `return` ውጤቱን ይመልሳል!\n\n"
                    "አሁን የመጨረሻውን ታላቅ ፕሮጀክት እንገንባ፦ የነጥብ ጭማሪ አስሊ (Score Bonus Calculator)!"
                ),
            ),
            TutorStep(
                id="c_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a complete C program with `addBonus(int score)` that returns `score + 10`, and print the result for `90` in `main()`!\n\n"
                    "👇 *Type and send:*\n"
                    '```c\n#include <stdio.h>\n\nint addBonus(int score) {\n    return score + 10;\n}\n\nint main(void) {\n    printf("Final: %d\\n", addBonus(90));\n    return 0;\n}\n```'
                ),
                message_am=(
                    "የ `addBonus(int score)` ፈንክሽን ጽፈው `score + 10` እንዲመልስ ያድርጉና በ `main()` ውስጥ ለ `90` አውጥተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```c\n#include <stdio.h>\n\nint addBonus(int score) {\n    return score + 10;\n}\n\nint main(void) {\n    printf("Final: %d\\n", addBonus(90));\n    return 0;\n}\n```'
                ),
                expected_code_output="Final: 100",
                hint_en='Write the full program with `addBonus` and `main`, printing `"Final: %d\\n"` for `addBonus(90)`.',
                hint_am='ሙሉውን ፕሮግራም በ `addBonus` እና `main` ጽፈው `Final: %d` በማለት ለ `addBonus(90)` አሳይተው ይላኩ።',
                success_message_en=(
                    "🏆 *MASTER OF SYSTEMS!* You have officially written, compiled, and linked a complete native C program!"
                ),
                success_message_am=(
                    "🏆 *የስርዓት ፕሮግራሚንግ አዋቂ!* እውነተኛ እና የተሟላ የሲ (C) ፕሮግራም ጽፈው ኮምፓይል በማድረግ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="c_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! C GRADUATE!** 🌟🎓\n\n"
                    "You have conquered the most respected foundational language in computer science:\n"
                    "1. 🏛️ Direct native execution with `printf()` and `\\n`\n"
                    "2. 📦 High-speed typed variables with `%d`, `%f`\n"
                    "3. 🔢 Nanosecond CPU arithmetic and modulo `%`\n"
                    "4. 🚦 Conditional logic and hardware branching with `if` / `else`\n"
                    "5. 🔄 The classic `for` loop that defined modern programming\n"
                    "6. 📋 Contiguous memory arrays and zero-based indexing\n"
                    "7. 🛠️ Modular functions and full native compilation!\n\n"
                    "You now hold the keys to operating systems, embedded hardware, and high-performance engineering! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የሲ (C) ቋንቋ ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "በኮምፒውተር ሳይንስ አለም ውስጥ እጅግ የተከበረውን መሰረታዊ ቋንቋ ተምረው ጨርሰዋል፦\n"
                    "1. 🏛️ ፈጣን የማሽን አሰራር በ `printf()` እና `\\n`\n"
                    "2. 📦 የሜሞሪ ተለዋዋጮች በ `%d` እና `%f`\n"
                    "3. 🔢 ፈጣን የሲፒዩ (CPU) ሂሳብ እና ስሌቶች\n"
                    "4. 🚦 ብልህ ውሳኔዎች በ `if` እና `else`\n"
                    "5. 🔄 ዘመናዊ ፕሮግራሚንግን የመሰረተው ታዋቂው `for` ሉፕ\n"
                    "6. 📋 ተከታታይ የሜሞሪ አሬይ በዜሮ ቆጠራ\n"
                    "7. 🛠️ ፈንክሽኖች እና የተሟላ የሲ (C) ፕሮግራም ማቀናበር!\n\n"
                    "አሁን ኦፕሬቲንግ ሲስተሞችን፣ ማሽኖችን እና ከፍተኛ ፍጥነት ያላቸውን ፕሮግራሞች ለመገንባት ቁልፉ በእጅዎ ነው! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_c_chapters() -> List[TutorChapter]:
    """Return all C tutor chapters ordered."""
    return sorted(C_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_c_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve C tutor chapter by ID."""
    for ch in C_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_c_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next C chapter ID."""
    chapters = get_all_c_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
