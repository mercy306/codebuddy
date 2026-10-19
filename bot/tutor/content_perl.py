"""Perl 5 curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

PERL_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="perl_ch1",
        order=1,
        title_en="Perl Ch 1: Welcome to Perl 5 & print",
        title_am="ፐርል ምዕራፍ 1፦ ከፐርል 5 ጋር መተዋወቅ እና print",
        description_en="Discover the Swiss Army Knife of the internet and text processing.",
        description_am="የኢንተርኔት እና የጽሁፍ ማቀናበሪያው ሁለገብ ቋንቋ የሆነውን ፐርል (Perl 5) ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🐪 *Welcome to Perl 5!* 📜\n\n"
                    "Known affectionately as **'The Duct Tape of the Internet'**, Perl powers major parts of Amazon, DuckDuckGo, "
                    "bioinformatics DNA sequencing, and massive log parsing pipelines!\n\n"
                    "In Perl, to output text, we use the `print` command:\n\n"
                    "```perl\nprint(\"Hello Perl\\n\");\n```\n\n"
                    "- In Perl, strings can use double quotes `\"...\"`\n"
                    "- Every statement ends with a semicolon `;`\n"
                    "- `\\n` creates a clean new line!"
                ),
                message_am=(
                    "🐪 *እንኳን ወደ ፐርል 5 (Perl) በደህና መጡ!* 📜\n\n"
                    "በአለም ዙሪያ **'የኢንተርኔቱ ሁለገብ ማጣበቂያ'** ተብሎ የሚታወቀው ፐርል እንደ Amazon፣ DuckDuckGo ባሉ ድረ-ገጾች፣ "
                    "በዲኤንኤ (DNA) ምርምር እና በትልልቅ የዳታ ማጣሪያዎች ውስጥ ዋነኛ መሪ ነው!\n\n"
                    "በፐርል ውስጥ ጽሁፍ ለማሳየት `print` የሚለውን ትዕዛዝ እንጠቀማለን፦\n\n"
                    "```perl\nprint(\"Hello Perl\\n\");\n```\n\n"
                    "- ጽሁፎች በጥቅስ `\"...\"` ውስጥ ይቀመጣሉ\n"
                    "- እያንዳንዱ መስመር በሴሚኮለን `;` ይዘጋል\n"
                    "- `\\n` አዲስ መስመር ይፈጥራል!"
                ),
            ),
            TutorStep(
                id="perl_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first words in Perl!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nprint("Hello Perl");\n```'
                ),
                message_am=(
                    "በፐርል የመጀመሪያውን ጽሁፍ እናሳትም!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nprint("Hello Perl");\n```'
                ),
                expected_code_output="Hello Perl",
                hint_en='Write `print("Hello Perl");` with a semicolon `;` at the end.',
                hint_am='`print("Hello Perl");` ብለው በሴሚኮለን በመዝጋት ይላኩ።',
                success_message_en=(
                    "🎉 *EXECUTED!* You just ran real Perl 5 on the system!"
                ),
                success_message_am=(
                    "🎉 *ተፈጽሟል!* እውነተኛ የፐርል 5 ኮድ አሁን በተሳካ ሁኔታ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="perl_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which command displays text on the screen in Perl?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ በማያ ገጹ ላይ ጽሁፍ እንዲታይ የሚያደርገው ትዕዛዝ የትኛው ነው?"
                ),
                options_en=[
                    "print",
                    "echo",
                    "show",
                    "write",
                ],
                options_am=[
                    "print",
                    "echo",
                    "show",
                    "write",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `print` is Perl's core output function!",
                success_message_am="🌟 በትክክል! `print` በፐርል ውስጥ ጽሁፍ ማሳያ ትዕዛዝ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch2",
        order=2,
        title_en="Perl Ch 2: Scalars (Variables with $)",
        title_am="ፐርል ምዕራፍ 2፦ ስካላርስ (ተለዋዋጮች በ $)",
        description_en="Learn how Perl manages single values using the dollar sign $.",
        description_am="ፐርል ነጠላ መረጃዎችን በዶላር ምልክት $ አማካኝነት እንዴት እንደሚያስተዳድር ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "💲 *Scalars: Single Items Start with `$`*\n\n"
                    "In Perl, variables that hold a single item (a number or a string) are called **Scalars**.\n\n"
                    "They always start with the **`$`** sign (think `$` looks like an **S** for **S**calar!):\n\n"
                    "```perl\nmy $name = \"Abebe\";\nmy $score = 100;\n```\n\n"
                    "- `my` creates a clean, safe local variable!"
                ),
                message_am=(
                    "💲 *ስካላርስ፦ ነጠላ መረጃዎች በ `$` ይጀምራሉ*\n\n"
                    "በፐርል ውስጥ ነጠላ መረጃ (ቁጥር ወይም ጽሁፍ) የሚይዙ ተለዋዋጮች **ስካላርስ (Scalars)** ይባላሉ።\n\n"
                    "ሁልጊዜም በ**`$`** ምልክት ይጀምራሉ (`$` ፊደሉ **S** ይመስላል ለ **S**calar!)፦\n\n"
                    "```perl\nmy $name = \"Abebe\";\nmy $score = 100;\n```\n\n"
                    "- `my` ንጹህ እና አስተማማኝ ተለዋዋጭ ይፈጥራል!"
                ),
            ),
            TutorStep(
                id="perl_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare `my $score = 80;` and print `$score + 20`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```perl\nmy $score = 80;\nprint($score + 20);\n```"
                ),
                message_am=(
                    "`my $score = 80;` ፈጥረው የ `$score + 20`ን ድምር ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```perl\nmy $score = 80;\nprint($score + 20);\n```"
                ),
                expected_code_output="100",
                hint_en="Write `my $score = 80;` then `print($score + 20);` with semicolons.",
                hint_am="`my $score = 80;` ጽፈው በሁለተኛው መስመር `print($score + 20);` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Scalar calculated!* 80 + 20 = 100 printed cleanly!"
                ),
                success_message_am=(
                    "🎉 *ስካላሩ ሰርቷል!* 80 + 20 = 100 በተሳካ ሁኔታ ተሰልቷል!"
                ),
            ),
            TutorStep(
                id="perl_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Perl, which prefix indicates a scalar variable (single number or string)?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ ነጠላ እሴትን (ቁጥር ወይም ጽሁፍ) የሚያመለክተው መለያ ምልክት የቱ ነው?"
                ),
                options_en=[
                    "$ (Dollar)",
                    "@ (At)",
                    "% (Percent)",
                    "& (Ampersand)",
                ],
                options_am=[
                    "$ (የዶላር ምልክት)",
                    "@ (የአት ምልክት)",
                    "% (የፐርሰንት ምልክት)",
                    "& (የአምፐርሳንድ ምልክት)",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `$` denotes scalars in Perl!",
                success_message_am="🌟 በትክክል! `$` ለስካላር (ነጠላ መረጃ) የሚያገለግል ምልክት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch3",
        order=3,
        title_en="Perl Ch 3: Decisions with if / else",
        title_am="ፐርል ምዕራፍ 3፦ ውሳኔዎች በ if / else",
        description_en="Learn conditional branching in Perl.",
        description_am="በፐርል ውስጥ በ if እና else አማካኝነት ውሳኔዎችን መወሰን ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Making Decisions: if / else in Perl*\n\n"
                    "In Perl, conditions go inside parentheses `( )`, and the actions are enclosed in curly braces `{ }`:\n\n"
                    "```perl\nmy $score = 85;\nif ($score >= 50) {\n    print(\"Pass\");\n} else {\n    print(\"Fail\");\n}\n```\n\n"
                    "Notice: Curly braces `{ }` are **always required** in Perl `if` statements!"
                ),
                message_am=(
                    "🚦 *ውሳኔዎችን መወሰን፦ if እና else በፐርል*\n\n"
                    "በፐርል ውስጥ መስፈርቱ በክብ ቅንፍ `( )` ውስጥ ይቀመጣል፤ የሚፈጸመው ድርጊት ደግሞ በፈረንሳይ ቅንፍ `{ }` ውስጥ ይገባል፦\n\n"
                    "```perl\nmy $score = 85;\nif ($score >= 50) {\n    print(\"Pass\");\n} else {\n    print(\"Fail\");\n}\n```\n\n"
                    "ልብ ይበሉ፦ በፐርል ውስጥ የፈረንሳይ ቅንፍ `{ }` **ሁልጊዜም ግዴታ ነው**!"
                ),
            ),
            TutorStep(
                id="perl_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Check if `$score >= 50` and print `Pass`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nmy $score = 85;\nif ($score >= 50) {\n    print("Pass");\n}\n```'
                ),
                message_am=(
                    "ውጤቱ `$score >= 50` መሆኑን መርምረው `Pass` የሚል ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nmy $score = 85;\nif ($score >= 50) {\n    print("Pass");\n}\n```'
                ),
                expected_code_output="Pass",
                hint_en='Write `my $score = 85;` then `if ($score >= 50) { print("Pass"); }`.',
                hint_am='`my $score = 85;` ጽፈው በ if ውስጥ `print("Pass");` በማስገባት ይላኩ።',
                success_message_en=(
                    "🎉 *Decision made!* Score was 85, so 'Pass' was printed!"
                ),
                success_message_am=(
                    "🎉 *ውሳኔው ተላለፈ!* ውጤቱ 85 ስለሆነ 'Pass' የሚለው ታትሟል!"
                ),
            ),
            TutorStep(
                id="perl_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Perl, are curly braces `{ }` mandatory for `if` statements?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ ለ `if` ትዕዛዞች የፈረንሳይ ቅንፎች `{ }` መጠቀም ግዴታ ነው?"
                ),
                options_en=[
                    "Yes, curly braces are always mandatory in Perl if blocks",
                    "No, they are optional",
                    "Only on Windows",
                    "Only for numbers",
                ],
                options_am=[
                    "አዎ፣ በፐርል ውስጥ የፈረንሳይ ቅንፎች ሁልጊዜም ግዴታ ናቸው",
                    "አይ፣ አማራጭ ናቸው",
                    "በዊንዶውስ ላይ ብቻ",
                    "ለቁጥሮች ብቻ",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Perl requires braces around all control blocks!",
                success_message_am="🌟 በትክክል! ፐርል ለሁሉም የውሳኔ ክፍሎች የፈረንሳይ ቅንፍ ማስገባት ግዴታ ያደርጋል!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch4",
        order=4,
        title_en="Perl Ch 4: Counting with for Loops",
        title_am="ፐርል ምዕራፍ 4፦ በ for ሉፖች መቁጠር",
        description_en="Learn how for loops eliminate manual repetition.",
        description_am="የ for ሉፖች አሰልቺ ድግግሞሾችን እንዴት እንደሚያስቀሩ ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *The Clean Perl Range Loop: `(1..3)`*\n\n"
                    "Perl has one of the most expressive range syntaxes in the world: `(1..3)`!\n\n"
                    "```perl\nfor my $i (1..3) {\n    print(\"$i\\n\");\n}\n```\n\n"
                    "`(1..3)` creates a list from 1 to 3 automatically!"
                ),
                message_am=(
                    "🔄 *ግልጹ የፐርል የቁጥር ወሰን ሉፕ፦ `(1..3)`*\n\n"
                    "ፐርል በአለም ላይ እጅግ ማራኪ ከሆኑት የቁጥር ወሰን መግለጫዎች አንዱ አለው፦ `(1..3)`!\n\n"
                    "```perl\nfor my $i (1..3) {\n    print(\"$i\\n\");\n}\n```\n\n"
                    "`(1..3)` ከ 1 እስከ 3 ያሉትን ቁጥሮች በራሱ ያዘጋጃል!"
                ),
            ),
            TutorStep(
                id="perl_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Count from 1 to 3 using `for my $i (1..3)`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nfor my $i (1..3) {\n    print("$i\\n");\n}\n```'
                ),
                message_am=(
                    "በ `for my $i (1..3)` በመጠቀም ከ 1 እስከ 3 እንቁጠር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nfor my $i (1..3) {\n    print("$i\\n");\n}\n```'
                ),
                expected_code_output="1\n2\n3",
                hint_en='Write `for my $i (1..3) { print("$i\\n"); }`.',
                hint_am='`for my $i (1..3) { print("$i\\n"); }` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *Loop complete!* 1, 2, 3 printed automatically!"
                ),
                success_message_am=(
                    "🎉 *ሉፑ ሰርቷል!* 1, 2, 3 በራሱ ተቆጥሮ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="perl_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Perl, what does the range operator `(1..5)` represent?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ `(1..5)` የሚለው ምልክት ምንን ያመለክታል?"
                ),
                options_en=[
                    "A list of numbers from 1 to 5",
                    "1 divided by 5",
                    "A decimal number 1.5",
                    "A file named 1..5",
                ],
                options_am=[
                    "ከ 1 እስከ 5 ያሉ የቁጥሮች ዝርዝር",
                    "1 ሲካፈል ለ 5",
                    "ነጥብ ያለው ቁጥር 1.5",
                    "1..5 የተባለ ፋይል",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `..` is the range operator in Perl!",
                success_message_am="🌟 በትክክል! `..` በፐርል ውስጥ የቁጥሮች ወሰን መግለጫ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch5",
        order=5,
        title_en="Perl Ch 5: Lists & Arrays (Variables with @)",
        title_am="ፐርል ምዕራፍ 5፦ አሬዮች (ተለዋዋጮች በ @)",
        description_en="Learn how arrays start with @ and access items with $arr[0].",
        description_am="አሬይ በ@ ምልክት እንደሚጀምር እና እቃዎችን በ$arr[0] እንደምናወጣ ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📚 *Arrays in Perl Start with `@`*\n\n"
                    "While a single item is a Scalar (`$`), a whole list/array starts with **`@`** (think **`@`** for **A**rray!):\n\n"
                    "```perl\nmy @items = (\"Sword\", \"Shield\");\n```\n\n"
                    "⚠️ *Rule*: When you fetch a single element, it becomes a scalar, so you use **`$`**:\n"
                    "`print($items[0]);` prints `Sword`!"
                ),
                message_am=(
                    "📚 *በፐርል ውስጥ አሬዮች በ `@` ይጀምራሉ*\n\n"
                    "ነጠላ መረጃ ስካላር (`$`) ሲሆን፣ ሙሉ ዝርዝር/አሬይ ደግሞ በ**`@`** ይጀምራል (`@` ለ **A**rray!)፦\n\n"
                    "```perl\nmy @items = (\"Sword\", \"Shield\");\n```\n\n"
                    "⚠️ *ህግ*፦ ከዝርዝሩ ውስጥ አንዱን ነጠላ እቃ ስታወጡ ስካላር ስለሚሆን በ **`$`** ትጠሩታላችሁ፦\n"
                    "`print($items[0]);` 'Sword' ብሎ ያትማል!"
                ),
            ),
            TutorStep(
                id="perl_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create an array `@items = (\"Sword\", \"Shield\");` and print index 0!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nmy @items = ("Sword", "Shield");\nprint($items[0]);\n```'
                ),
                message_am=(
                    "`my @items = (\"Sword\", \"Shield\");` ፈጥረው በመጀመሪያው ቦታ ያለውን ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nmy @items = ("Sword", "Shield");\nprint($items[0]);\n```'
                ),
                expected_code_output="Sword",
                hint_en='Write `my @items = ("Sword", "Shield");` then `print($items[0]);`.',
                hint_am='`my @items = ("Sword", "Shield");` ጽፈው በሁለተኛው መስመር `print($items[0]);` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Array item fetched!* Sword retrieved from index 0!"
                ),
                success_message_am=(
                    "🎉 *የአሬይ እቃው መጥቷል!* 'Sword' ከኢንዴክስ 0 በተሳካ ሁኔታ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="perl_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Perl, which symbol is prefixed when declaring an entire array?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ ሙሉ አሬይ (ዝርዝር) ለመፍጠር ከስሙ ፊት የምናስቀምጠው ምልክት የቱ ነው?"
                ),
                options_en=[
                    "@ (At sign)",
                    "$ (Dollar)",
                    "% (Percent)",
                    "* (Asterisk)",
                ],
                options_am=[
                    "@ (የአት ምልክት)",
                    "$ (የዶላር ምልክት)",
                    "% (የፐርሰንት ምልክት)",
                    "* (የኮከብ ምልክት)",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `@` represents arrays/lists in Perl!",
                success_message_am="🌟 በትክክል! `@` በፐርል ውስጥ አሬይን ያመለክታል!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch6",
        order=6,
        title_en="Perl Ch 6: Subroutines (Functions)",
        title_am="ፐርል ምዕራፍ 6፦ ሰብሩቲንስ (Subroutines / Functions)",
        description_en="Learn how subroutines bundle reusable logic in Perl.",
        description_am="በፐርል ውስጥ እንደገና ጥቅም ላይ ሊውል የሚችልን ኮድ በ subroutines እንዴት እንደምናጠቃልል ይማሩ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚙️ *Subroutines: Functions in Perl*\n\n"
                    "In Perl, functions are called **Subroutines**, declared using the keyword `sub`:\n\n"
                    "```perl\nsub greet {\n    print(\"Welcome to Perl!\");\n}\n```\n\n"
                    "To call it, simply type: `greet();`!"
                ),
                message_am=(
                    "⚙️ *ሰብሩቲንስ፦ ፈንክሽኖች በፐርል*\n\n"
                    "በፐርል ውስጥ ፈንክሽኖች **ሰብሩቲንስ (Subroutines)** ይባላሉ፤ የሚፈጠሩትም በ `sub` አማካኝነት ነው፦\n\n"
                    "```perl\nsub greet {\n    print(\"Welcome to Perl!\");\n}\n```\n\n"
                    "ለመጥራት በቀላሉ `greet();` ብሎ መጻፍ በቂ ነው!"
                ),
            ),
            TutorStep(
                id="perl_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a subroutine `greet` and call it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nsub greet {\n    print("Welcome to Perl!");\n}\ngreet();\n```'
                ),
                message_am=(
                    "`greet` የተባለ ሰብሩቲን ሰርተው ጥሩት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nsub greet {\n    print("Welcome to Perl!");\n}\ngreet();\n```'
                ),
                expected_code_output="Welcome to Perl!",
                hint_en='Define `sub greet { print("Welcome to Perl!"); }` then call `greet();`.',
                hint_am='ሰብሩቲኑን ከፈጠሩ በኋላ በሁለተኛው መስመር `greet();` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Subroutine called!* Your reusable Perl logic executed perfectly!"
                ),
                success_message_am=(
                    "🎉 *ሰብሩቲኑ ሰርቷል!* የፈጠሩት ፈንክሽን በትክክል ተጠርቶ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="perl_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword is used to define a function in Perl?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ ፈንክሽን (Subroutine) ለመፍጠር የምንጠቀመው ቃል የትኛው ነው?"
                ),
                options_en=[
                    "sub",
                    "def",
                    "function",
                    "fn",
                ],
                options_am=[
                    "sub",
                    "def",
                    "function",
                    "fn",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `sub` stands for subroutine in Perl!",
                success_message_am="🌟 በትክክል! `sub` በፐርል ውስጥ ፈንክሽን መፍጠሪያ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="perl_ch7",
        order=7,
        title_en="Perl Ch 7: Capstone: Text String Parser",
        title_am="ፐርል ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የጽሁፍ ዳታ መተንተኛ (Text Parser)",
        description_en="Combine scalars, string operators, and printing into a text formatting tool.",
        description_am="ስካላሮችን፣ የጽሁፍ ማጣመሪያ ምልክቶችን እና print በማጣመር የጽሁፍ ዳታ አዘጋጅ ይገንቡ።",
        track="perl",
        steps=[
            TutorStep(
                id="perl_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📜 *Perl Capstone Project: Automated Text Formatter!* 🐪\n\n"
                    "Perl is the world champion of text manipulation.\n\n"
                    "In Perl, to concatenate (join) strings, we use the dot **`.`** operator:\n\n"
                    "```perl\nmy $first = \"Log\";\nmy $second = \"Entry\";\nprint($first . \": \" . $second);\n```\n\n"
                    "In this capstone, you will format a server log entry: `Status: 200 OK`!"
                ),
                message_am=(
                    "📜 *የፐርል ማጠቃለያ ፕሮጀክት፦ የጽሁፍ ዳታ ማዘጋጃ!* 🐪\n\n"
                    "ፐርል በጽሁፎች እና በዳታ አያያዝ በአለም ላይ እጅግ የተዋጣለት ቋንቋ ነው።\n\n"
                    "በፐርል ውስጥ ጽሁፎችን ለማጣመር የነጥብ **`.`** ምልክት እንጠቀማለን፦\n\n"
                    "```perl\nmy $first = \"Log\";\nmy $second = \"Entry\";\nprint($first . \": \" . $second);\n```\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት ውስጥ የሰርቨር ሎግ እናዘጋጃለን፦ `Status: 200 OK`!"
                ),
            ),
            TutorStep(
                id="perl_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete log entry formatter using the `.` operator!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```perl\nmy $code = 200;\nprint("Status: " . $code . " OK");\n```'
                ),
                message_am=(
                    "ሙሉውን የሰርቨር ሎግ አዘጋጅ ኮድ ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```perl\nmy $code = 200;\nprint("Status: " . $code . " OK");\n```'
                ),
                expected_code_output="Status: 200 OK",
                hint_en='Write `my $code = 200;` then `print("Status: " . $code . " OK");`.',
                hint_am='`my $code = 200;` ጽፈው በሁለተኛው መስመር `print("Status: " . $code . " OK");` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *SERVER LOG FORMATTED!* 📜🐪\n\n"
                    "You just built an automated text processing pipeline in Perl 5!"
                ),
                success_message_am=(
                    "🎉 *የሰርቨር ሎጉ ተዘጋጅቷል!* 📜🐪\n\n"
                    "እውነተኛ የጽሁፍ ማቀናበሪያ ኮድ በፐርል 5 ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="perl_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final Perl Master Question:*\n\n"
                    "Which operator concatenates (joins) two strings in Perl?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የፐርል ማጠቃለያ ጥያቄ፦*\n\n"
                    "በፐርል ውስጥ ሁለት ጽሁፎችን ለማጣመር የምንጠቀመው ምልክት የቱ ነው?"
                ),
                options_en=[
                    ". (Dot)",
                    "+ (Plus)",
                    "& (Ampersand)",
                    ", (Comma)",
                ],
                options_am=[
                    ". (ነጥብ)",
                    "+ (የመደመር ምልክት)",
                    "& (የአምፐርሳንድ ምልክት)",
                    ", (ኮማ)",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! In Perl, the dot `.` operator joins strings together!",
                success_message_am="🏆 እጅግ ድንቅ! በፐርል ውስጥ የነጥብ `.` ምልክት ጽሁፎችን ለማጣመር ያገለግላል!",
            ),
        ],
    ),
]
