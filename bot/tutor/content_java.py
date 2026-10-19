"""Java curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

JAVA_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="java_ch1",
        order=1,
        title_en="Java Ch 1: Your First Java Code",
        title_am="ጃቫ ምዕራፍ 1፦ የመጀመሪያው የጃቫ ኮድ",
        description_en="Learn how Java powers billions of devices and write your first System.out.println statement.",
        description_am="ጃቫ በቢሊዮኖች የሚቆጠሩ መሳሪያዎችን እንዴት እንደሚያንቀሳቅስ ይማሩ እና የመጀመሪያውን የSystem.out.println ኮድ ይጻፉ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "☕ *Welcome to Java!* 🚀\n\n"
                    "Java is one of the most powerful and widely-used programming languages in human history.\n\n"
                    "It runs on over **3 billion devices** worldwide — from Android apps, Minecraft, and ATM banking systems, to NASA space missions!\n\n"
                    "In Java, to display words on the screen, we tell the system:\n"
                    "`System.out.println(\"Your Text\");`\n\n"
                    "⚠️ *Rule*: In Java, every statement must end with a semicolon `;`!"
                ),
                message_am=(
                    "☕ *እንኳን ወደ ጃቫ (Java) በደህና መጡ!* 🚀\n\n"
                    "ጃቫ በዓለም ታሪክ ውስጥ እጅግ ጠንካራ እና በስፋት ጥቅም ላይ ከዋሉ የኮምፒውተር ቋንቋዎች አንዱ ነው።\n\n"
                    "በዓለም ላይ ከ**3 ቢሊዮን በላይ መሳሪያዎች** ላይ ይሰራል — ከአንድሮይድ አፖች፣ ማይንክራፍት (Minecraft) ጨዋታ፣ የባንክ ኤቲኤም (ATM) ሲስተሞች፣ እስከ ናሳ (NASA) ድረስ!\n\n"
                    "በጃቫ ውስጥ ጽሁፍ በስክሪኑ ላይ ለማውጣት የምንጠቀመው ትዕዛዝ፦\n"
                    "`System.out.println(\"ጽሁፍ እዚህ\");`\n\n"
                    "⚠️ *ህግ*፦ በጃቫ ውስጥ እያንዳንዱ የኮድ መስመር በሴሚኮለን `;` መዘጋት አለበት!"
                ),
            ),
            TutorStep(
                id="java_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first words in Java!\n\n"
                    "👇 *Type this line in the chat and send:*\n"
                    '```java\nSystem.out.println("Hello Java");\n```'
                ),
                message_am=(
                    "በጃቫ የመጀመሪያውን ጽሁፍ እናሳትም!\n\n"
                    "👇 *ይህንን መስመር ጽፈው ይላኩ፦*\n"
                    '```java\nSystem.out.println("Hello Java");\n```'
                ),
                expected_code_output="Hello Java",
                hint_en='Write `System.out.println("Hello Java");` with capital S and a semicolon `;` at the end.',
                hint_am='በካፒታል S እና መጨረሻው ላይ ሴሚኮለን `;` በማድረግ `System.out.println("Hello Java");` ብለው ይጻፉ።',
                success_message_en=(
                    "🎉 *BOOM!* You just compiled and ran real Java code on OpenJDK 21!"
                ),
                success_message_am=(
                    "🎉 *ድንቅ!* እውነተኛ የጃቫ ኮድ አሁን በስክሪኑ ላይ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="java_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What must you put at the end of every statement in Java?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በጃቫ ውስጥ በእያንዳንዱ የኮድ መስመር መጨረሻ ላይ ምን መደረግ አለበት?"
                ),
                options_en=[
                    "A semicolon `;`",
                    "A period `.`",
                    "A colon `:`",
                    "Nothing",
                ],
                options_am=[
                    "ሴሚኮለን `;`",
                    "ነጥብ `.`",
                    "ኮለን `:`",
                    "ምንም",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Every single Java statement ends with a semicolon `;`!",
                success_message_am="🌟 በትክክል! በጃቫ ውስጥ እያንዳንዱ መስመር በሴሚኮለን `;` ይዘጋል!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch2",
        order=2,
        title_en="Java Ch 2: Variables & Data Types",
        title_am="ጃቫ ምዕራፍ 2፦ ተለዋዋጮች እና የዳታ አይነቶች (Data Types)",
        description_en="Learn strict typing with int, double, and String.",
        description_am="የዳታ አይነቶችን (int, double, እና String) በጃቫ ውስጥ እንዴት እንደምንጠቀም ይማሩ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Strict Types: Giving Boxes a Specific Job*\n\n"
                    "In Python, you can put anything into a variable. But **Java is strictly typed** — it requires you to declare the exact type of data beforehand!\n\n"
                    "- **`int`**: Whole numbers (e.g. `int age = 20;`)\n"
                    "- **`double`**: Decimals (e.g. `double price = 9.99;`)\n"
                    "- **`String`**: Text wrapped in quotes (e.g. `String name = \"Sara\";`)\n\n"
                    "This prevents bugs before your code even runs!"
                ),
                message_am=(
                    "📦 *የዳታ አይነቶች፦ ለእያንዳንዱ ሳጥን የተወሰነ ስራ መስጠት*\n\n"
                    "በፓይተን ውስጥ ማንኛውንም ዳታ በተለዋዋጭ ውስጥ ማስቀመጥ ይቻላል። ነገር ግን **ጃቫ ጥብቅ ነው** — አስቀድመው የዳታውን አይነት (Data Type) መግለጽ አለብዎት!\n\n"
                    "- **`int`**፦ ሙሉ ቁጥሮች (ለምሳሌ፦ `int age = 20;`)\n"
                    "- **`double`**፦ ነጥብ ያላቸው ቁጥሮች (ለምሳሌ፦ `double price = 9.99;`)\n"
                    "- **`String`**፦ ጽሁፎች (ለምሳሌ፦ `String name = \"Sara\";`)\n\n"
                    "ይህ ጥብቅነት ፕሮግራሙ ከመሰራቱ በፊት ስህተቶች እንዳይፈጠሩ አስቀድሞ ይከላከላል!"
                ),
            ),
            TutorStep(
                id="java_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare an integer variable `int score = 100;` and print it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nint score = 100;\nSystem.out.println(score);\n```"
                ),
                message_am=(
                    "የሙሉ ቁጥር ተለዋዋጭ `int score = 100;` ፈጥረው በSystem.out.println ያትሙት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nint score = 100;\nSystem.out.println(score);\n```"
                ),
                expected_code_output="100",
                hint_en="Write `int score = 100;` on the first line and `System.out.println(score);` on the second line.",
                hint_am="በመጀመሪያው መስመር `int score = 100;` በሁለተኛው መስመር `System.out.println(score);` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *Variables mastered!* You created a strongly typed integer variable in Java!"
                ),
                success_message_am=(
                    "🎉 *ጎበዝ!* የመጀመሪያውን የጃቫ ተለዋዋጭ በትክክል ፈጥረዋል!"
                ),
            ),
            TutorStep(
                id="java_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which data type in Java is used to store whole numbers without decimals?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በጃቫ ውስጥ ነጥብ የሌላቸውን ሙሉ ቁጥሮች ለማስቀመጥ የትኛውን የዳታ አይነት እንጠቀማለን?"
                ),
                options_en=[
                    "int",
                    "String",
                    "double",
                    "char",
                ],
                options_am=[
                    "int",
                    "String",
                    "double",
                    "char",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `int` is short for integer!",
                success_message_am="🌟 ትክክል! `int` ማለት integer (ሙሉ ቁጥር) ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch3",
        order=3,
        title_en="Java Ch 3: Making Decisions with if/else",
        title_am="ጃቫ ምዕራፍ 3፦ ውሳኔዎችን መወሰን (if / else)",
        description_en="Learn how programs make choices using conditional logic.",
        description_am="ፕሮግራሞች በ if እና else አማካኝነት ምርጫዎችን እንዴት እንደሚወስኑ ይማሩ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Making Decisions with if / else*\n\n"
                    "Computers become intelligent when they can make choices.\n\n"
                    "In Java, conditions are enclosed in parentheses `( )`, and the actions to take are inside curly braces `{ }`:\n\n"
                    "```java\nint battery = 15;\nif (battery < 20) {\n    System.out.println(\"Low Battery!\");\n}\n```"
                ),
                message_am=(
                    "🚦 *ውሳኔዎችን በ if / else መወሰን*\n\n"
                    "ኮምፒውተሮች ብልህ የሚሆኑት በሁኔታዎች ላይ ተመስርተው ውሳኔ ሲወስኑ ነው።\n\n"
                    "በጃቫ ውስጥ መስፈርቱን በቅንፍ `( )` ውስጥ እናስቀምጣለን፤ የሚፈጸመውን ተግባር ደግሞ በፈረንሳይ ቅንፍ `{ }` ውስጥ እናስገባለን፦\n\n"
                    "```java\nint battery = 15;\nif (battery < 20) {\n    System.out.println(\"Low Battery!\");\n}\n```"
                ),
            ),
            TutorStep(
                id="java_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Check if a student passed their exam!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nint score = 85;\nif (score >= 50) {\n    System.out.println(\"Pass\");\n}\n```"
                ),
                message_am=(
                    "ተማሪው ፈተናውን ማለፉን እንመርምር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nint score = 85;\nif (score >= 50) {\n    System.out.println(\"Pass\");\n}\n```"
                ),
                expected_code_output="Pass",
                hint_en='Write the if condition with `System.out.println("Pass");` inside curly braces.',
                hint_am='`System.out.println("Pass");` በቅንፍ ውስጥ በማስገባት ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *Decision made!* The condition was true, so Java printed 'Pass'!"
                ),
                success_message_am=(
                    "🎉 *ውሳኔው ተላለፈ!* ውጤቱ ከ50 በላይ ስለሆነ ጃቫ 'Pass' የሚለውን አትሟል!"
                ),
            ),
            TutorStep(
                id="java_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Where do you place the condition of an `if` statement in Java?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በጃቫ ውስጥ የ `if` መስፈርት በምን ምልክት ውስጥ ይቀመጣል?"
                ),
                options_en=[
                    "Inside parentheses `( )`",
                    "Inside square brackets `[ ]`",
                    "Inside double quotes `\" \"`",
                    "Without any brackets",
                ],
                options_am=[
                    "በክብ ቅንፍ `( )` ውስጥ",
                    "በካሬ ቅንፍ `[ ]` ውስጥ",
                    "በጥቅስ ምልክት `\" \"` ውስጥ",
                    "ምንም ቅንፍ ሳያስፈልገው",
                ],
                correct_option_index=0,
                success_message_en="🌟 Correct! Conditions in Java always go inside parentheses `( )`!",
                success_message_am="🌟 ትክክል! በጃቫ ውስጥ መስፈርቶች ሁልጊዜም በክብ ቅንፍ `( )` ውስጥ ይቀመጣሉ!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch4",
        order=4,
        title_en="Java Ch 4: Repeating Actions with Loops",
        title_am="ጃቫ ምዕራፍ 4፦ ድርጊቶችን በሉፕ (Loops) መድገም",
        description_en="Learn how for loops eliminate repetitive code.",
        description_am="የ for ሉፕ አሰልቺ ድግግሞሾችን እንዴት እንደሚያስቀር ይማሩ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *The Classic for Loop in Java*\n\n"
                    "If you want to count from 1 to 5, you don't copy-paste `println` 5 times.\n\n"
                    "Java uses the famous 3-part `for` loop:\n"
                    "```java\nfor (int i = 1; i <= 3; i++) {\n    System.out.println(i);\n}\n```\n\n"
                    "1. `int i = 1;` -> Start at 1\n"
                    "2. `i <= 3;` -> Keep running while i <= 3\n"
                    "3. `i++` -> Add 1 each time"
                ),
                message_am=(
                    "🔄 *የታወቀው የጃቫ for ሉፕ*\n\n"
                    "ከ 1 እስከ 5 ለመቁጠር `println`ን 5 ጊዜ አንገለብጥም።\n\n"
                    "ጃቫ 3 ክፍሎች ያሉት ዝነኛ `for` ሉፕ ይጠቀማል፦\n"
                    "```java\nfor (int i = 1; i <= 3; i++) {\n    System.out.println(i);\n}\n```\n\n"
                    "1. `int i = 1;` -> ከ 1 ጀምር\n"
                    "2. `i <= 3;` -> i ከ 3 እስኪያንስ ድረስ ቀጥል\n"
                    "3. `i++` -> በእያንዳንዱ ዙር 1 ጨምር"
                ),
            ),
            TutorStep(
                id="java_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's count from 1 to 3 with a loop!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nfor (int i = 1; i <= 3; i++) {\n    System.out.println(i);\n}\n```"
                ),
                message_am=(
                    "በሉፕ በመጠቀም ከ 1 እስከ 3 እንቁጠር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nfor (int i = 1; i <= 3; i++) {\n    System.out.println(i);\n}\n```"
                ),
                expected_code_output="1\n2\n3",
                hint_en="Write the exact for loop with `System.out.println(i);` inside.",
                hint_am="የ for ሉፑን በትክክል ጽፈው ይላኩ።",
                success_message_en=(
                    "🎉 *Look at that loop spin!* 1, 2, 3 printed automatically!"
                ),
                success_message_am=(
                    "🎉 *ሉፑ ሰርቷል!* 1, 2, 3 በራሱ ተቆጥሮ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="java_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Java, what does `i++` mean in a loop?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በጃቫ ውስጥ በሉፕ ጊዜ `i++` ማለት ምን ማለት ነው?"
                ),
                options_en=[
                    "Increase the value of i by 1",
                    "Multiply i by 2",
                    "Stop the loop immediately",
                    "Print the variable i",
                ],
                options_am=[
                    "የ iን ዋጋ በ1 ጨምር",
                    "iን በ2 አባዛ",
                    "ሉፑን ወዲያውኑ አቁም",
                    "ተለዋዋጩን i አትም",
                ],
                correct_option_index=0,
                success_message_en="🌟 Exactly right! `i++` is shortcut for `i = i + 1`!",
                success_message_am="🌟 በትክክል! `i++` ማለት በእያንዳንዱ ዙር 1 ጨምር ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch5",
        order=5,
        title_en="Java Ch 5: Storing Collections with Arrays",
        title_am="ጃቫ ምዕራፍ 5፦ መረጃዎችን በዝርዝር (Arrays) ማከማቸት",
        description_en="Learn how to store multiple items inside a single array.",
        description_am="ብዙ መረጃዎችን በአንድ ዝርዝር (Array) ውስጥ እንዴት እንደምናስቀምጥ ይማሩ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📚 *Storing Multiple Items: Arrays*\n\n"
                    "Imagine you have 100 students. Creating `student1`, `student2`, ... would be exhausting!\n\n"
                    "An **Array** stores multiple values inside square brackets `[ ]`:\n\n"
                    "```java\nint[] scores = {90, 85, 95};\n```\n\n"
                    "⚠️ *Rule*: Like in Python & JS, computers start counting items at index **0**!\n"
                    "`scores[0]` is 90."
                ),
                message_am=(
                    "📚 *ብዙ መረጃዎችን ማከማቸት፦ አሬይ (Arrays)*\n\n"
                    "100 ተማሪዎች አሉዎት እንበል፤ ለእያንዳንዳቸው `student1`, `student2` እያሉ ተለዋዋጭ መፍጠር አሰልቺ ነው!\n\n"
                    "**አሬይ (Array)** ብዙ መረጃዎችን በአንድ ላይ በካሬ ቅንፍ `[ ]` እንዲያስቀምጡ ያስችልዎታል፦\n\n"
                    "```java\nint[] scores = {90, 85, 95};\n```\n\n"
                    "⚠️ *ህግ*፦ እንደ ፓይተን እና ጃቫስክሪፕት ሁሉ፣ ኮምፒውተሮች መቁጠር የሚጀምሩት ከ **0** ነው!\n"
                    "`scores[0]` የመጀመሪያው (90) ነው።"
                ),
            ),
            TutorStep(
                id="java_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create an array of numbers and print the first element at index 0!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nint[] numbers = {10, 20, 30};\nSystem.out.println(numbers[0]);\n```"
                ),
                message_am=(
                    "የቁጥሮች አሬይ ፈጥረው በመጀመሪያው ቦታ (ኢንዴክስ 0) ላይ ያለውን ቁጥር ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nint[] numbers = {10, 20, 30};\nSystem.out.println(numbers[0]);\n```"
                ),
                expected_code_output="10",
                hint_en="Write `int[] numbers = {10, 20, 30};` then `System.out.println(numbers[0]);`.",
                hint_am="`int[] numbers = {10, 20, 30};` ጽፈው በሁለተኛው መስመር `System.out.println(numbers[0]);` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *First element fetched!* Java arrays give you fast indexed access!"
                ),
                success_message_am=(
                    "🎉 *የመጀመሪያው ቁጥር መጣ!* የአሬይ ኢንዴክስ 0 የመጀመሪያውን እሴት ያመጣል!"
                ),
            ),
            TutorStep(
                id="java_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Java, what is the index of the first element in an array?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በጃቫ ውስጥ የአንድ አሬይ የመጀመሪያው እቃ ኢንዴክስ (መለያ ቁጥር) ስንት ነው?"
                ),
                options_en=[
                    "0",
                    "1",
                    "-1",
                    "10",
                ],
                options_am=[
                    "0",
                    "1",
                    "-1",
                    "10",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Arrays are zero-indexed in Java!",
                success_message_am="🌟 ትክክል! በጃቫ ውስጥ አሬይ መቆጠር የሚጀምረው ከ0 ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch6",
        order=6,
        title_en="Java Ch 6: Methods (Functions in Java)",
        title_am="ጃቫ ምዕራፍ 6፦ ሜተዶች (በጃቫ ውስጥ ያሉ ፈንክሽኖች)",
        description_en="Learn how methods bundle reusable logic.",
        description_am="ሜተዶች እንደገና ጥቅም ላይ ሊውል የሚችልን ኮድ እንዴት እንደሚያጠቃልሉ ይማሩ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚙️ *Reusable Actions: Methods in Java*\n\n"
                    "In Python, we call reusable code blocks `def` functions. In Java, they are called **Methods**.\n\n"
                    "A method specifies:\n"
                    "1. Return type (e.g. `int` or `void` if it returns nothing)\n"
                    "2. Name (e.g. `add`)\n"
                    "3. Parameters inside `(int a, int b)`\n\n"
                    "```java\nstatic int doubleNumber(int x) {\n    return x * 2;\n}\n```"
                ),
                message_am=(
                    "⚙️ *እንደገና ጥቅም ላይ የሚውሉ ተግባራት፦ ሜተዶች (Methods)*\n\n"
                    "በፓይተን ውስጥ 'functions' የምንላቸውን በጃቫ ውስጥ **ሜተዶች (Methods)** ብለን እንጠራቸዋለን።\n\n"
                    "አንድ ሜተር የሚከተሉትን ይገልጻል፦\n"
                    "1. የመመለሻ አይነት (ለምሳሌ `int` ወይም ምንም የማይመልስ ከሆነ `void`)\n"
                    "2. ስሙ (ለምሳሌ `add`)\n"
                    "3. የሚቀበላቸው ዋጋዎች `(int a, int b)`\n\n"
                    "```java\nstatic int doubleNumber(int x) {\n    return x * 2;\n}\n```"
                ),
            ),
            TutorStep(
                id="java_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Call a method that calculates `Math.max(45, 90)` and prints the larger number!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nint result = Math.max(45, 90);\nSystem.out.println(result);\n```"
                ),
                message_am=(
                    "የትልቁን ቁጥር ዋጋ የሚያወጣውን የጃቫ ሜተር `Math.max(45, 90)` እንጥራ እና እናትመው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nint result = Math.max(45, 90);\nSystem.out.println(result);\n```"
                ),
                expected_code_output="90",
                hint_en="Write `int result = Math.max(45, 90);` then `System.out.println(result);`.",
                hint_am="`int result = Math.max(45, 90);` ጽፈው በሁለተኛው መስመር `System.out.println(result);` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Method executed!* `Math.max` evaluated the numbers and returned 90!"
                ),
                success_message_am=(
                    "🎉 *ሜተዱ ሰርቷል!* ጃቫ ሁለቱን ቁጥሮች አወዳድሮ ትልቁን (90) መልሷል!"
                ),
            ),
            TutorStep(
                id="java_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What keyword is used for a Java method that does NOT return any value?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "ምንም አይነት እሴት ለማይመልስ የጃቫ ሜተር የምንጠቀመው ቃል የቱ ነው?"
                ),
                options_en=[
                    "void",
                    "empty",
                    "null",
                    "none",
                ],
                options_am=[
                    "void",
                    "empty",
                    "null",
                    "none",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `void` indicates the method performs an action without returning data!",
                success_message_am="🌟 ትክክል! `void` ማለት ምንም ዳታ አይመልስም ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="java_ch7",
        order=7,
        title_en="Java Ch 7: Capstone Project: Bank ATM System",
        title_am="ጃቫ ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የባንክ ኤቲኤም (ATM) ሲስተም",
        description_en="Combine variables, conditions, and calculations to build an ATM withdrawal system.",
        description_am="ተለዋዋጮችን፣ ሁኔታዎችን እና ሂሳብን በማጣመር የባንክ ኤቲኤም ሲስተም ይገንቡ።",
        track="java",
        steps=[
            TutorStep(
                id="java_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏦 *Java Capstone Project: The ATM Banking System!* 💳\n\n"
                    "Java powers the vast majority of financial institutions and ATM networks worldwide.\n\n"
                    "In this capstone, you will build an automated ATM withdrawal check:\n"
                    "1. Store starting balance (`int balance = 500;`)\n"
                    "2. Requested withdrawal amount (`int withdraw = 200;`)\n"
                    "3. If balance >= withdraw:\n"
                    "   - Deduct money: `balance = balance - withdraw;`\n"
                    "   - Print new remaining balance!\n"
                    "4. If not enough balance: Print 'Insufficient Funds'!"
                ),
                message_am=(
                    "🏦 *የጃቫ ማጠቃለያ ፕሮጀክት፦ የባንክ ኤቲኤም (ATM) ሲስተም!* 💳\n\n"
                    "በዓለም ላይ ያሉ አብዛኛዎቹ የፋይናንስ ተቋማት እና የኤቲኤም ኔትወርኮች በጃቫ ነው የሚሰሩት።\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት ውስጥ እውነተኛ የኤቲኤም የገንዘብ ማውጫ ሲስተም እንሰራለን፦\n"
                    "1. የመጀመሪያውን ሂሳብ ማስቀመጥ (`int balance = 500;`)\n"
                    "2. የሚወጣው ገንዘብ (`int withdraw = 200;`)\n"
                    "3. በቂ ገንዘብ ካለ (balance >= withdraw)፦\n"
                    "   - ገንዘቡን መቀነስ `balance = balance - withdraw;`\n"
                    "   - ቀሪውን ገንዘብ ማሳወቅ!\n"
                    "4. በቂ ካልሆነ 'Insufficient Funds' ብሎ ማሳወቅ!"
                ),
            ),
            TutorStep(
                id="java_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete ATM withdrawal transaction code!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```java\nint balance = 500;\nint withdraw = 200;\nbalance = balance - withdraw;\nSystem.out.println(\"Remaining: \" + balance);\n```"
                ),
                message_am=(
                    "ሙሉውን የኤቲኤም ገንዘብ ማውጫ ኮድ ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```java\nint balance = 500;\nint withdraw = 200;\nbalance = balance - withdraw;\nSystem.out.println(\"Remaining: \" + balance);\n```"
                ),
                expected_code_output="Remaining: 300",
                hint_en='Write the ATM balance deduction with `System.out.println("Remaining: " + balance);`.',
                hint_am='`System.out.println("Remaining: " + balance);` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *TRANSACTION SUCCESSFUL!* 🏦💳\n\n"
                    "You just programmed an automated banking logic in Java!\n\n"
                    "Balance was 500, withdrew 200, remaining balance is 300!"
                ),
                success_message_am=(
                    "🎉 *ገንዘቡ በተሳካ ሁኔታ ወጥቷል!* 🏦💳\n\n"
                    "እውነተኛ የባንክ ኤቲኤም ሲስተም በጃቫ ገንብተዋል!\n\n"
                    "ሂሳቡ 500 ነበር፣ 200 ወጥቷል፣ ቀሪው 300 መሆኑን አረጋግጧል!"
                ),
            ),
            TutorStep(
                id="java_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final Java Master Question:*\n\n"
                    "Which line correctly combines text and a variable in Java printing?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የጃቫ ማጠቃለያ ጥያቄ፦*\n\n"
                    "በጃቫ ጽሁፍን እና ተለዋዋጭን በአንድ ላይ አጣምሮ ለማሳየት ትክክለኛው የትኛው ነው?"
                ),
                options_en=[
                    'System.out.println("Remaining: " + balance);',
                    'System.out.println("Remaining: ", balance);',
                    'System.out.println("Remaining: " & balance);',
                    'System.out.println("Remaining: " . balance);',
                ],
                options_am=[
                    'System.out.println("Remaining: " + balance);',
                    'System.out.println("Remaining: ", balance);',
                    'System.out.println("Remaining: " & balance);',
                    'System.out.println("Remaining: " . balance);',
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! The `+` operator concatenates strings and variables in Java!",
                success_message_am="🏆 ድንቅ ስራ! በጃቫ የ `+` ምልክት ጽሁፍን እና ተለዋዋጭን ለማጣመር ያገለግላል!",
            ),
        ],
    ),
]
