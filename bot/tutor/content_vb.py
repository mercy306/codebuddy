"""Visual Basic curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

VB_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="vb_ch1",
        order=1,
        title_en="Visual Basic Ch 1: Clean English Coding",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 1፦ ግልጽ እና ቀላል የእንግሊዝኛ ኮዲንግ",
        description_en="Discover Visual Basic, designed specifically to be human-readable and beginner-friendly.",
        description_am="ለጀማሪዎች እንዲመች በእንግሊዝኛ ቋንቋ አጻጻፍ የተሰራውን ቪዥዋል ቤዚክ (Visual Basic) ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "💎 *Welcome to Visual Basic (.NET)!* ✨\n\n"
                    "Visual Basic (VB) was created by Microsoft with one mission: **make programming feel like reading plain English!**\n\n"
                    "Instead of confusing symbols like `{ }` and `;`, Visual Basic uses natural words like `Then`, `End If`, and `Next`.\n\n"
                    "To print text to the screen, we write:\n"
                    "`Console.WriteLine(\"Your Text\")`\n\n"
                    "*(Notice: No semicolon at the end! Visual Basic is wonderfully clean!)*"
                ),
                message_am=(
                    "💎 *እንኳን ወደ ቪዥዋል ቤዚክ (Visual Basic) በደህና መጡ!* ✨\n\n"
                    "ቪዥዋል ቤዚክ በማይክሮሶፍት የተፈጠረ ሲሆን ዋነኛ ዓላማው፦ **ኮዲንግ ልክ እንደ ተራ ንባብ ቀላል እንዲሆን ማድረግ ነው!**\n\n"
                    "እንደ `{ }` እና `;` ያሉ ውስብስብ ምልክቶች ፈንታ እንደ `Then`፣ `End If`፣ እና `Next` ያሉ ግልጽ ቃላትን ይጠቀማል።\n\n"
                    "ጽሁፍ በስክሪኑ ላይ ለማውጣት የምንጽፈው፦\n"
                    "`Console.WriteLine(\"ጽሁፍ እዚህ\")`\n\n"
                    "*(ልብ ይበሉ፦ መጨረሻው ላይ ሴሚኮለን አያስፈልግም! ቪዥዋል ቤዚክ እጅግ ንጹህ ነው!)*"
                ),
            ),
            TutorStep(
                id="vb_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first words in Visual Basic!\n\n"
                    "👇 *Type this line in the chat and send:*\n"
                    '```vb\nConsole.WriteLine("Hello Visual Basic")\n```'
                ),
                message_am=(
                    "በቪዥዋል ቤዚክ የመጀመሪያውን ጽሁፍ እናሳትም!\n\n"
                    "👇 *ይህንን መስመር ጽፈው ይላኩ፦*\n"
                    '```vb\nConsole.WriteLine("Hello Visual Basic")\n```'
                ),
                expected_code_output="Hello Visual Basic",
                hint_en='Write `Console.WriteLine("Hello Visual Basic")` (no semicolon needed).',
                hint_am='`Console.WriteLine("Hello Visual Basic")` ብለው ጽፈው ይላኩ (ሴሚኮለን አያስፈልግም)።',
                success_message_en=(
                    "🎉 *COMPILED & EXECUTED!* You just ran your first Visual Basic code!"
                ),
                success_message_am=(
                    "🎉 *ኮዱ ሰርቷል!* የመጀመሪያውን የቪዥዋል ቤዚክ ኮድ በተሳካ ሁኔታ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="vb_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Do Visual Basic statements require semicolons `;` at the end of each line?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ በእያንዳንዱ መስመር መጨረሻ ላይ ሴሚኮለን `;` ያስፈልጋል?"
                ),
                options_en=[
                    "No, semicolons are NOT needed in Visual Basic",
                    "Yes, every line must have a semicolon",
                    "Only on the first line",
                    "Only inside brackets",
                ],
                options_am=[
                    "አያስፈልግም፣ በቪዥዋል ቤዚክ ሴሚኮለን አያስፈልግም",
                    "አዎ፣ እያንዳንዱ መስመር ሴሚኮለን ያስፈልገዋል",
                    "በመጀመሪያው መስመር ብቻ",
                    "በቅንፍ ውስጥ ብቻ",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Visual Basic uses clean line breaks instead of semicolons!",
                success_message_am="🌟 በትክክል! ቪዥዋል ቤዚክ ሴሚኮለን አያስፈልገውም!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch2",
        order=2,
        title_en="Visual Basic Ch 2: Declaring Variables with Dim",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 2፦ ተለዋዋጮችን በDim መፍጠር",
        description_en="Learn the famous Dim ... As ... syntax of Visual Basic.",
        description_am="ዝነኛውን የቪዥዋል ቤዚክ Dim ... As ... የተለዋዋጭ አሰራር ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *The Famous `Dim ... As` Syntax*\n\n"
                    "In Visual Basic, declaring a variable reads like an English sentence:\n\n"
                    "```vb\nDim name As String = \"Dawit\"\nDim score As Integer = 90\n```\n\n"
                    "- `Dim` means *'Create a variable'* (short for Dimension)\n"
                    "- `As Integer` defines whole numbers\n"
                    "- `As String` defines text"
                ),
                message_am=(
                    "📦 *የታወቀው የ `Dim ... As` አሰራር*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ ተለዋዋጭ መፍጠር ልክ እንደ እንግሊዝኛ አረፍተ ነገር ይነበባል፦\n\n"
                    "```vb\nDim name As String = \"Dawit\"\nDim score As Integer = 90\n```\n\n"
                    "- `Dim` ማለት *'ተለዋዋጭ ፍጠር'* ማለት ነው (ከ Dimension የመጣ)\n"
                    "- `As Integer` ለሙሉ ቁጥሮች\n"
                    "- `As String` ለጽሁፎች"
                ),
            ),
            TutorStep(
                id="vb_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare `Dim price As Integer = 50` and print `price * 2`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```vb\nDim price As Integer = 50\nConsole.WriteLine(price * 2)\n```"
                ),
                message_am=(
                    "`Dim price As Integer = 50` ፈጥረው የ `price * 2` ውጤት ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```vb\nDim price As Integer = 50\nConsole.WriteLine(price * 2)\n```"
                ),
                expected_code_output="100",
                hint_en="Write `Dim price As Integer = 50` then `Console.WriteLine(price * 2)`.",
                hint_am="`Dim price As Integer = 50` ጽፈው በሁለተኛው መስመር `Console.WriteLine(price * 2)` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Variables mastered!* 50 * 2 = 100 printed cleanly!"
                ),
                success_message_am=(
                    "🎉 *ተለዋዋጩ ሰርቷል!* 50 * 2 = 100 በተሳካ ሁኔታ ተሰልቷል!"
                ),
            ),
            TutorStep(
                id="vb_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword is used to declare variables in Visual Basic?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ ተለዋዋጭ ለመፍጠር የምንጠቀመው ቃል የትኛው ነው?"
                ),
                options_en=[
                    "Dim",
                    "let",
                    "var",
                    "make",
                ],
                options_am=[
                    "Dim",
                    "let",
                    "var",
                    "make",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `Dim` is the classic variable keyword in Visual Basic!",
                success_message_am="🌟 በትክክል! `Dim` በቪዥዋል ቤዚክ ውስጥ ተለዋዋጭ መፍጠሪያ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch3",
        order=3,
        title_en="Visual Basic Ch 3: Decisions with If ... Then",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 3፦ ውሳኔዎች በ If ... Then ... End If",
        description_en="Learn readable conditional logic with English keywords.",
        description_am="በእንግሊዝኛ ቃላት ግልጽ ውሳኔዎችን እንዴት እንደምንወስን ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Natural Decisions: If ... Then ... End If*\n\n"
                    "In Visual Basic, conditions read naturally without braces:\n\n"
                    "```vb\nDim score As Integer = 85\nIf score >= 50 Then\n    Console.WriteLine(\"Passed\")\nEnd If\n```\n\n"
                    "Notice the words: `If condition Then ... End If`!"
                ),
                message_am=(
                    "🚦 *ተፈጥሯዊ ውሳኔዎች፦ If ... Then ... End If*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ ሁኔታዎች ያለ ምንም ቅንፍ በቀላሉ ይነበባሉ፦\n\n"
                    "```vb\nDim score As Integer = 85\nIf score >= 50 Then\n    Console.WriteLine(\"Passed\")\nEnd If\n```\n\n"
                    "ቃላቱን ልብ ይበሉ፦ `If ... Then ... End If`!"
                ),
            ),
            TutorStep(
                id="vb_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write an If condition to check if `score >= 50` and print `Passed`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```vb\nDim score As Integer = 85\nIf score >= 50 Then\n    Console.WriteLine("Passed")\nEnd If\n```'
                ),
                message_am=(
                    "ውጤቱ `score >= 50` መሆኑን መርምረው `Passed` የሚል ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```vb\nDim score As Integer = 85\nIf score >= 50 Then\n    Console.WriteLine("Passed")\nEnd If\n```'
                ),
                expected_code_output="Passed",
                hint_en='Write `If score >= 50 Then`, print "Passed", and close with `End If`.',
                hint_am='`If score >= 50 Then` ጽፈው በ `End If` በመዝጋት ይላኩ።',
                success_message_en=(
                    "🎉 *Condition evaluated!* Score was 85, so 'Passed' was printed!"
                ),
                success_message_am=(
                    "🎉 *ውሳኔው ተላለፈ!* ውጤቱ 85 ስለሆነ 'Passed' የሚለው ታትሟል!"
                ),
            ),
            TutorStep(
                id="vb_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "How is an `If` statement closed in Visual Basic?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ የ `If` ትዕዛዝ ሲጠናቀቅ በምን ቃል ይዘጋል?"
                ),
                options_en=[
                    "End If",
                    "fi",
                    "}",
                    "Close If",
                ],
                options_am=[
                    "End If",
                    "fi",
                    "}",
                    "Close If",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `End If` cleanly marks the conclusion of the condition!",
                success_message_am="🌟 በትክክል! `End If` የውሳኔ መዝጊያ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch4",
        order=4,
        title_en="Visual Basic Ch 4: Counting with For ... Next Loops",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 4፦ በ For ... Next ሉፖች መቁጠር",
        description_en="Learn readable counting loops from start to finish.",
        description_am="ከመጀመሪያ እስከ መጨረሻ የሚቆጥሩ ግልጽ ሉፖችን ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *The Cleanest Loop in Coding: `For i = 1 To 3 ... Next`*\n\n"
                    "In Visual Basic, counting is poetic:\n\n"
                    "```vb\nFor i = 1 To 3\n    Console.WriteLine(i)\nNext\n```\n\n"
                    "No semicolons, no `i++`. It literally says: *'For i equal 1 To 3, do this, then go to Next!'*"
                ),
                message_am=(
                    "🔄 *በጣም ግልጹ የሉፕ አሰራር፦ `For i = 1 To 3 ... Next`*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ ቆጠራ ልክ እንደ ንባብ ነው፦\n\n"
                    "```vb\nFor i = 1 To 3\n    Console.WriteLine(i)\nNext\n```\n\n"
                    "ምንም አይነት ሴሚኮለን ወይም `i++` የለውም። በቀጥታ፦ *'ለ i ከ 1 እስከ 3 ይህንን አድርግ፣ ከዚያ ወደ ቀጣዩ (Next) ሂድ'* ይላል!"
                ),
            ),
            TutorStep(
                id="vb_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Count from 1 to 3 using `For ... Next`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```vb\nFor i = 1 To 3\n    Console.WriteLine(i)\nNext\n```"
                ),
                message_am=(
                    "በ `For ... Next` በመጠቀም ከ 1 እስከ 3 እንቁጠር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```vb\nFor i = 1 To 3\n    Console.WriteLine(i)\nNext\n```"
                ),
                expected_code_output="1\n2\n3",
                hint_en="Write `For i = 1 To 3`, print `i`, and close with `Next`.",
                hint_am="`For i = 1 To 3` ጽፈው በ `Next` በመዝጋት ይላኩ።",
                success_message_en=(
                    "🎉 *Loop complete!* 1, 2, 3 printed cleanly!"
                ),
                success_message_am=(
                    "🎉 *ሉፑ ሰርቷል!* 1, 2, 3 በራሱ ተቆጥሮ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="vb_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword closes a `For` loop in Visual Basic?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ የ `For` ሉፕ መዝጊያ ቃል የቱ ነው?"
                ),
                options_en=[
                    "Next",
                    "End For",
                    "done",
                    "loop",
                ],
                options_am=[
                    "Next",
                    "End For",
                    "done",
                    "loop",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `Next` tells Visual Basic to advance to the next iteration!",
                success_message_am="🌟 በትክክል! `Next` ወደ ቀጣዩ ዙር የሚያሳልፍ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch5",
        order=5,
        title_en="Visual Basic Ch 5: Arrays & Lists",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 5፦ አሬዮች እና ዝርዝሮች (Arrays)",
        description_en="Learn how to store multiple values in Visual Basic arrays.",
        description_am="ብዙ መረጃዎችን በአንድ ላይ በቪዥዋል ቤዚክ አሬይ ውስጥ እንዴት እንደምናስቀምጥ ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📚 *Storing Collections in Visual Basic*\n\n"
                    "In Visual Basic, you create an array of items like this:\n\n"
                    "```vb\nDim colors() As String = {\"Red\", \"Green\", \"Blue\"}\n```\n\n"
                    "To access an item, we use round parentheses `(0)`:\n"
                    "`Console.WriteLine(colors(0))` prints `Red`!"
                ),
                message_am=(
                    "📚 *መረጃዎችን በቪዥዋል ቤዚክ አሬይ ውስጥ ማከማቸት*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ የቀለማት አሬይ እንዲህ እንፈጥራለን፦\n\n"
                    "```vb\nDim colors() As String = {\"Red\", \"Green\", \"Blue\"}\n```\n\n"
                    "የመጀመሪያውን እቃ ለማውጣት በክብ ቅንፍ `(0)` እንጠራዋለን፦\n"
                    "`Console.WriteLine(colors(0))` 'Red' ብሎ ያትማል!"
                ),
            ),
            TutorStep(
                id="vb_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a colors array and print the first color at index 0!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```vb\nDim colors() As String = {"Red", "Blue"}\nConsole.WriteLine(colors(0))\n```'
                ),
                message_am=(
                    "የቀለማት አሬይ ፈጥረው በመጀመሪያው ቦታ (ኢንዴክስ 0) ያለውን ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```vb\nDim colors() As String = {"Red", "Blue"}\nConsole.WriteLine(colors(0))\n```'
                ),
                expected_code_output="Red",
                hint_en='Write `Dim colors() As String = {"Red", "Blue"}` then print `colors(0)`.',
                hint_am='አሬዩን ፈጥረው በሁለተኛው መስመር `Console.WriteLine(colors(0))` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Array accessed!* Red retrieved from index 0!"
                ),
                success_message_am=(
                    "🎉 *ቀለሙ መጥቷል!* 'Red' ከኢንዴክስ 0 በተሳካ ሁኔታ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="vb_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Visual Basic, which brackets are used to access an array element like `colors(0)`?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ የአሬይ እቃዎችን ለማግኘት የምንጠቀመው የትኛውን ቅንፍ ነው?"
                ),
                options_en=[
                    "Round parentheses ( )",
                    "Square brackets [ ]",
                    "Curly braces { }",
                    "Angle brackets < >",
                ],
                options_am=[
                    "ክብ ቅንፍ ( )",
                    "ካሬ ቅንፍ [ ]",
                    "የፈረንሳይ ቅንፍ { }",
                    "የጎንዮሽ ቅንፍ < >",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Visual Basic famously uses round parentheses `( )` for array indexing!",
                success_message_am="🌟 በትክክል! ቪዥዋል ቤዚክ ለአሬይ ክብ ቅንፍ `( )` ይጠቀማል!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch6",
        order=6,
        title_en="Visual Basic Ch 6: Subs and Functions",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 6፦ Sub እና Function (ተግባራት)",
        description_en="Learn the difference between Sub (action) and Function (returns a value).",
        description_am="በ Sub (ተግባር ፈጻሚ) እና በ Function (ውጤት መላሽ) መካከል ያለውን ልዩነት ይማሩ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚙️ *Sub vs Function in Visual Basic*\n\n"
                    "Visual Basic makes a crystal-clear distinction:\n\n"
                    "1. **`Sub`**: Performs an action, returns nothing.\n"
                    "2. **`Function`**: Calculates and returns a value.\n\n"
                    "```vb\nFunction DoubleNum(x As Integer) As Integer\n    Return x * 2\nEnd Function\n```"
                ),
                message_am=(
                    "⚙️ *Sub እና Function በቪዥዋል ቤዚክ*\n\n"
                    "ቪዥዋል ቤዚክ በሁለቱ መካከል ግልጽ ልዩነት አለው፦\n\n"
                    "1. **`Sub`**፦ ተግባርን ይፈጽማል እንጂ ምንም ዋጋ አይመልስም\n"
                    "2. **`Function`**፦ አስልቶ ውጤት ይመልሳል\n\n"
                    "```vb\nFunction DoubleNum(x As Integer) As Integer\n    Return x * 2\nEnd Function\n```"
                ),
            ),
            TutorStep(
                id="vb_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Use `Math.Max(30, 70)` to find and print the larger number!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```vb\nDim result As Integer = Math.Max(30, 70)\nConsole.WriteLine(result)\n```"
                ),
                message_am=(
                    "ትልቁን ቁጥር ለማግኘት `Math.Max(30, 70)` ተጠቅመው ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```vb\nDim result As Integer = Math.Max(30, 70)\nConsole.WriteLine(result)\n```"
                ),
                expected_code_output="70",
                hint_en="Write `Dim result As Integer = Math.Max(30, 70)` then `Console.WriteLine(result)`.",
                hint_am="`Dim result As Integer = Math.Max(30, 70)` ጽፈው በሁለተኛው መስመር `Console.WriteLine(result)` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Function calculated!* 70 correctly evaluated as the maximum!"
                ),
                success_message_am=(
                    "🎉 *ፈንክሽኑ ሰርቷል!* 70 ትልቁ ቁጥር ሆኖ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="vb_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Visual Basic, which block is used when you want to return a calculated value?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ የተሰላን ውጤት መመለስ ስንፈልግ የምንጠቀመው የቱን ነው?"
                ),
                options_en=[
                    "Function",
                    "Sub",
                    "Void",
                    "Action",
                ],
                options_am=[
                    "Function",
                    "Sub",
                    "Void",
                    "Action",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `Function` returns data, while `Sub` only executes actions!",
                success_message_am="🌟 በትክክል! `Function` ውጤት ይመልሳል፣ `Sub` ግን ድርጊት ብቻ ይፈጽማል!",
            ),
        ],
    ),
    TutorChapter(
        id="vb_ch7",
        order=7,
        title_en="Visual Basic Ch 7: Capstone: Business Invoice Calculator",
        title_am="ቪዥዋል ቤዚክ ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የንግድ ደረሰኝ (Invoice) ካልኩሌተር",
        description_en="Combine Dim variables, tax calculations, and string joining into a complete business invoice.",
        description_am="ተለዋዋጮችን፣ የታክስ ስሌትን እና ጽሁፍን በማጣመር የቢዝነስ ደረሰኝ ካልኩሌተር ይገንቡ።",
        track="vb",
        steps=[
            TutorStep(
                id="vb_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "💼 *Visual Basic Capstone: The Business Invoice!* 🧾\n\n"
                    "Visual Basic is famous for powering enterprise back-office and accounting software worldwide.\n\n"
                    "In this capstone, you will calculate an invoice total:\n"
                    "1. Item price: `Dim price As Integer = 100`\n"
                    "2. Tax amount: `Dim tax As Integer = 15`\n"
                    "3. Total: `Dim total As Integer = price + tax`\n"
                    "4. Print: `Invoice Total: 115`"
                ),
                message_am=(
                    "💼 *የቪዥዋል ቤዚክ ማጠቃለያ ፕሮጀክት፦ የንግድ ደረሰኝ ካልኩሌተር!* 🧾\n\n"
                    "ቪዥዋል ቤዚክ በዓለም ዙሪያ ያሉ የንግድ ድርጅቶች እና የሂሳብ አያያዝ ሲስተሞች ዋነኛ ቋንቋ ነው።\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት የደረሰኝ ስሌት እንሰራለን፦\n"
                    "1. የእቃው ዋጋ: `Dim price As Integer = 100`\n"
                    "2. ታክስ: `Dim tax As Integer = 15`\n"
                    "3. አጠቃላይ ድምር: `Dim total As Integer = price + tax`\n"
                    "4. ማሳወቅ: `Invoice Total: 115`"
                ),
            ),
            TutorStep(
                id="vb_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete invoice total calculation!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```vb\nDim price As Integer = 100\nDim tax As Integer = 15\nDim total As Integer = price + tax\nConsole.WriteLine("Invoice Total: " & total)\n```'
                ),
                message_am=(
                    "ሙሉውን የደረሰኝ ስሌት ኮድ ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```vb\nDim price As Integer = 100\nDim tax As Integer = 15\nDim total As Integer = price + tax\nConsole.WriteLine("Invoice Total: " & total)\n```'
                ),
                expected_code_output="Invoice Total: 115",
                hint_en='Write the invoice calculation and `Console.WriteLine("Invoice Total: " & total)`.',
                hint_am='የደረሰኙን ስሌት እና `Console.WriteLine("Invoice Total: " & total)` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *INVOICE CALCULATED!* 💼🧾\n\n"
                    "You just built an enterprise-ready business billing logic in Visual Basic!"
                ),
                success_message_am=(
                    "🎉 *ደረሰኙ ተሰልቷል!* 💼🧾\n\n"
                    "እውነተኛ የንግድ ደረሰኝ ካልኩሌተር በቪዥዋል ቤዚክ ገነቡ!"
                ),
            ),
            TutorStep(
                id="vb_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final Visual Basic Master Question:*\n\n"
                    "Which symbol is the preferred string concatenation operator in Visual Basic?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የቪዥዋል ቤዚክ ማጠቃለያ ጥያቄ፦*\n\n"
                    "በቪዥዋል ቤዚክ ውስጥ ጽሁፍን እና ቁጥርን ለማጣመር ተመራጩ ምልክት የትኛው ነው?"
                ),
                options_en=[
                    "& (Ampersand)",
                    "# (Hash)",
                    ": (Colon)",
                    "~ (Tilde)",
                ],
                options_am=[
                    "& (የአምፐርሳንድ ምልክት)",
                    "# (የሃሽ ምልክት)",
                    ": (የኮለን ምልክት)",
                    "~ (የቲልዴ ምልክት)",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! In Visual Basic, `&` safely glues text and numbers together without type confusion!",
                success_message_am="🏆 እጅግ ድንቅ! በቪዥዋል ቤዚክ የ `&` ምልክት ጽሁፍን እና ቁጥሮችን ያለምንም ስህተት ለማጣመር ያገለግላል!",
            ),
        ],
    ),
]
