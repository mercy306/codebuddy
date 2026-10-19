"""TypeScript curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

TYPESCRIPT_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="ts_ch1",
        order=1,
        title_en="TypeScript Ch 1: JavaScript with Superpowers",
        title_am="ታይፕስክሪፕት ምዕራፍ 1፦ ጃቫስክሪፕት ከታላቅ ሀይል ጋር",
        description_en="Learn how TypeScript brings type safety and prevents bugs before code runs.",
        description_am="ታይፕስክሪፕት ኮድ ከመሰራቱ በፊት ስህተቶችን እንዴት እንደሚያስቀር ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔷 *Welcome to TypeScript!* 🛡️\n\n"
                    "TypeScript is modern JavaScript with **Type Safety**.\n\n"
                    "Developed by Microsoft, it is now the industry standard used by Google, Meta, Netflix, and Uber.\n\n"
                    "In JavaScript, you can accidentally put text into a math calculation and break an entire website. "
                    "In TypeScript, you add type annotations (like `: string` or `: number`):\n\n"
                    "```typescript\nlet greeting: string = \"Hello TypeScript\";\nconsole.log(greeting);\n```"
                ),
                message_am=(
                    "🔷 *እንኳን ወደ ታይፕስክሪፕት (TypeScript) በደህና መጡ!* 🛡️\n\n"
                    "ታይፕስክሪፕት ማለት የ**ዳታ አይነቶች ጥበቃ (Type Safety)** የተጨመረበት ዘመናዊ ጃቫስክሪፕት ነው።\n\n"
                    "በማይክሮሶፍት የተሰራ ሲሆን ዛሬ እንደ Google፣ Netflix፣ እና Uber ባሉ ግዙፍ የቴክኖሎጂ ኩባንያዎች ውስጥ ዋነኛ መመዘኛ ሆኗል።\n\n"
                    "በጃቫስክሪፕት ውስጥ በስህተት ጽሁፍን በቁጥር ውስጥ አስገብተው ሙሉ ዌብሳይት ሊያበላሹ ይችላሉ። "
                    "በታይፕስክሪፕት ግን ከስሙ ቀጥሎ አይነት ይገልጻሉ (ለምሳሌ `: string` ወይም `: number`)፦\n\n"
                    "```typescript\nlet greeting: string = \"Hello TypeScript\";\nconsole.log(greeting);\n```"
                ),
            ),
            TutorStep(
                id="ts_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare a typed string variable and print it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```typescript\nlet greeting: string = "Hello TypeScript";\nconsole.log(greeting);\n```'
                ),
                message_am=(
                    "የታይፕስክሪፕት ተለዋዋጭ ፈጥረው በconsole.log ያትሙት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```typescript\nlet greeting: string = "Hello TypeScript";\nconsole.log(greeting);\n```'
                ),
                expected_code_output="Hello TypeScript",
                hint_en='Write `let greeting: string = "Hello TypeScript";` then `console.log(greeting);`.',
                hint_am='`let greeting: string = "Hello TypeScript";` ጽፈው በሁለተኛው መስመር `console.log(greeting);` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Safe and typed!* You just ran your first TypeScript code!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* የመጀመሪያውን የታይፕስክሪፕት ኮድ በተሳካ ሁኔታ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="ts_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In TypeScript, how do you specify that a variable must only hold text?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በታይፕስክሪፕት ውስጥ አንድ ተለዋዋጭ ጽሁፍ ብቻ እንዲይዝ እንዴት እንገልጻለን?"
                ),
                options_en=[
                    ": string",
                    ": text",
                    ": word",
                    ": char",
                ],
                options_am=[
                    ": string",
                    ": text",
                    ": word",
                    ": char",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `: string` is the type annotation for text in TypeScript!",
                success_message_am="🌟 በትክክል! `: string` ለጽሁፎች የምንጠቀመው የዳታ አይነት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch2",
        order=2,
        title_en="TypeScript Ch 2: Primitive Types (number, boolean)",
        title_am="ታይፕስክሪፕት ምዕራፍ 2፦ መሰረታዊ የዳታ አይነቶች (number, boolean)",
        description_en="Learn typed numbers and booleans that protect your calculations.",
        description_am="የሂሳብ ስሌቶችን ስህተት የሚከላከሉትን number እና boolean ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔢 *Numbers and Booleans in TypeScript*\n\n"
                    "TypeScript gives you clean primitives:\n"
                    "- **`number`**: For integers and decimals (`let price: number = 19.99;`)\n"
                    "- **`boolean`**: For true / false (`let isReady: boolean = true;`)\n\n"
                    "If you ever try to do `price = \"cheap\";`, TypeScript catches the error immediately before users ever see it!"
                ),
                message_am=(
                    "🔢 *ቁጥሮች እና ቡሊያኖች በታይፕስክሪፕት*\n\n"
                    "ታይፕስክሪፕት ግልጽ የዳታ አይነቶች አሉት፦\n"
                    "- **`number`**፦ ለሙሉ እና ነጥብ ላላቸው ቁጥሮች (`let price: number = 19.99;`)\n"
                    "- **`boolean`**፦ ለእውነት ወይም ሐሰት (`let isReady: boolean = true;`)\n\n"
                    "በስህተት `price = \"cheap\";` ብለው ቢጽፉ፣ ታይፕስክሪፕት ኮዱ ሳይሰራ ወዲያውኑ ስህተቱን ያሳውቃል!"
                ),
            ),
            TutorStep(
                id="ts_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a typed number `let age: number = 25;` and print `age + 5`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```typescript\nlet age: number = 25;\nconsole.log(age + 5);\n```"
                ),
                message_am=(
                    "`let age: number = 25;` ፈጥረው የ `age + 5`ን ድምር ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\nlet age: number = 25;\nconsole.log(age + 5);\n```"
                ),
                expected_code_output="30",
                hint_en="Write `let age: number = 25;` then `console.log(age + 5);`.",
                hint_am="`let age: number = 25;` ጽፈው በሁለተኛው መስመር `console.log(age + 5);` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Math verified!* 25 + 5 = 30 safely calculated!"
                ),
                success_message_am=(
                    "🎉 *ስሌቱ ሰርቷል!* 25 + 5 = 30 በሰላም ተሰልቷል!"
                ),
            ),
            TutorStep(
                id="ts_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which TypeScript type only accepts `true` or `false`?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በታይፕስክሪፕት ውስጥ `true` ወይም `false` ብቻ የሚቀበለው የዳታ አይነት የትኛው ነው?"
                ),
                options_en=[
                    "boolean",
                    "binary",
                    "flag",
                    "number",
                ],
                options_am=[
                    "boolean",
                    "binary",
                    "flag",
                    "number",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `boolean` represents truth values!",
                success_message_am="🌟 ትክክል! `boolean` የእውነት ወይም የሐሰት እሴት መያዣ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch3",
        order=3,
        title_en="TypeScript Ch 3: Typed Arrays",
        title_am="ታይፕስክሪፕት ምዕራፍ 3፦ የታይፕ አሬዮች (Typed Arrays)",
        description_en="Learn how to ensure arrays only hold elements of one exact type.",
        description_am="አሬዮች የተወሰነ የዳታ አይነት ብቻ እንዲይዙ እንዴት እንደምናደርግ ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📚 *Typed Arrays: Keeping Lists Consistent*\n\n"
                    "In plain JS, an array can accidentally mix strings, numbers, and objects.\n\n"
                    "In TypeScript, you put brackets `[]` after the type:\n"
                    "- `number[]` -> List containing only numbers\n"
                    "- `string[]` -> List containing only text\n\n"
                    "```typescript\nlet scores: number[] = [90, 85, 95];\n```"
                ),
                message_am=(
                    "📚 *የተወሰነ አይነት ያላቸው አሬዮች (Typed Arrays)*\n\n"
                    "በተራ ጃቫስክሪፕት ውስጥ በአንድ አሬይ ውስጥ ጽሁፍ፣ ቁጥር እና የተለያዩ ነገሮች ተቀላቅለው ሊገቡ ይችላሉ።\n\n"
                    "በታይፕስክሪፕት ግን ከታይፑ ቀጥሎ የካሬ ቅንፍ `[]` በማድረግ ቁጥጥር እናደርጋለን፦\n"
                    "- `number[]` -> ቁጥሮችን ብቻ የያዘ ዝርዝር\n"
                    "- `string[]` -> ጽሁፎችን ብቻ የያዘ ዝርዝር\n\n"
                    "```typescript\nlet scores: number[] = [90, 85, 95];\n```"
                ),
            ),
            TutorStep(
                id="ts_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `string[]` array with names and print the first element at index 0!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```typescript\nlet cities: string[] = ["Addis", "Hawassa"];\nconsole.log(cities[0]);\n```'
                ),
                message_am=(
                    "የከተሞች `string[]` አሬይ ፈጥረው የመጀመሪያውን ከተማ (ኢንዴክስ 0) ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```typescript\nlet cities: string[] = ["Addis", "Hawassa"];\nconsole.log(cities[0]);\n```'
                ),
                expected_code_output="Addis",
                hint_en='Write `let cities: string[] = ["Addis", "Hawassa"];` then print index 0.',
                hint_am='አሬዩን ፈጥረው በሁለተኛው መስመር `console.log(cities[0]);` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *City accessed!* Addis printed from your typed array!"
                ),
                success_message_am=(
                    "🎉 *የመጀመሪያው ከተማ መጣ!* አዲስ አበባ (Addis) ከዝርዝሩ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="ts_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "How do you declare an array of numbers in TypeScript?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በታይፕስክሪፕት ውስጥ የቁጥሮች ዝርዝር (Array) መሆኑን በምን እንገልጻለን?"
                ),
                options_en=[
                    "number[]",
                    "Array(number)",
                    "[number]",
                    "numbers{}",
                ],
                options_am=[
                    "number[]",
                    "Array(number)",
                    "[number]",
                    "numbers{}",
                ],
                correct_option_index=0,
                success_message_en="🌟 Correct! `number[]` is the standard TypeScript array syntax!",
                success_message_am="🌟 ትክክል! `number[]` የቁጥሮች አሬይ መግለጫ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch4",
        order=4,
        title_en="TypeScript Ch 4: Interfaces & Custom Types",
        title_am="ታይፕስክሪፕት ምዕራፍ 4፦ ኢንተርፌስ (Interfaces) እና የራስ ዳታ ሞዴሎች",
        description_en="Learn how to define clear blueprints for objects using interfaces.",
        description_am="ኢንተርፌስ (interface) በመጠቀም ለዳታችን እንዴት ንድፍ (Blueprint) እንደምናዘጋጅ ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📐 *Blueprints for Data: Interfaces*\n\n"
                    "When building user accounts, you want every user to have a `name` and `age`.\n\n"
                    "An **`interface`** defines a strict contract for an object:\n\n"
                    "```typescript\ninterface Student {\n  name: string;\n  score: number;\n}\n```\n\n"
                    "Now, if someone forgets the score, TypeScript warns you immediately!"
                ),
                message_am=(
                    "📐 *የዳታ ንድፎች፦ ኢንተርፌስ (Interfaces)*\n\n"
                    "የተጠቃሚዎችን መረጃ ስናደራጅ እያንዳንዱ ሰው `name` እና `score` እንዲኖረው እንፈልጋለን።\n\n"
                    "**`interface`** የአንድን መረጃ ቅርጽ አስቀድሞ የሚወስን ጥብቅ ውል ነው፦\n\n"
                    "```typescript\ninterface Student {\n  name: string;\n  score: number;\n}\n```\n\n"
                    "አሁን አንድ ሰው ውጤት (score) ማስገባት ቢረሳ ታይፕስክሪፕት ወዲያውኑ ያስጠነቅቃል!"
                ),
            ),
            TutorStep(
                id="ts_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a student object using an interface and print their name!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```typescript\ninterface Student { name: string; score: number; }\nlet s: Student = { name: \"Sara\", score: 95 };\nconsole.log(s.name);\n```"
                ),
                message_am=(
                    "ኢንተርፌስ ተጠቅመው የተማሪ መረጃ ፈጥረው ስሟን ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\ninterface Student { name: string; score: number; }\nlet s: Student = { name: \"Sara\", score: 95 };\nconsole.log(s.name);\n```"
                ),
                expected_code_output="Sara",
                hint_en='Define `interface Student` then create `let s: Student` and print `s.name`.',
                hint_am='ኢንተርፌሱን ከፈጠሩ በኋላ `let s: Student` ብለው በማስገባት `console.log(s.name);` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *Interface instantiated!* Sara matched your Student contract perfectly!"
                ),
                success_message_am=(
                    "🎉 *ኢንተርፌሱ ሰርቷል!* ሳራ (Sara) በትክክል የተማሪውን ንድፍ አሟልታ ተፈጥራለች!"
                ),
            ),
            TutorStep(
                id="ts_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What TypeScript keyword defines the shape and structure of an object?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በታይፕስክሪፕት ውስጥ የአንድን መረጃ (Object) ቅርጽ ለመወሰን የምንጠቀመው ቃል የቱ ነው?"
                ),
                options_en=[
                    "interface",
                    "blueprint",
                    "schema",
                    "struct",
                ],
                options_am=[
                    "interface",
                    "blueprint",
                    "schema",
                    "struct",
                ],
                correct_option_index=0,
                success_message_en="🌟 Exactly right! `interface` defines object shapes in TypeScript!",
                success_message_am="🌟 በትክክል! `interface` የኦብጀክት ቅርጽን ለመወሰን ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch5",
        order=5,
        title_en="TypeScript Ch 5: Typed Functions",
        title_am="ታይፕስክሪፕት ምዕራፍ 5፦ የታይፕ ፈንክሽኖች (Typed Functions)",
        description_en="Learn how to type function parameters and return values.",
        description_am="ፈንክሽኖች የሚቀበሉትን እና የሚመልሱትን የዳታ አይነት እንዴት እንደምንቆጣጠር ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚙️ *Typed Functions: Safe Inputs & Outputs*\n\n"
                    "In TypeScript, you protect functions by declaring:\n"
                    "1. The type of each parameter `(a: number, b: number)`\n"
                    "2. The return type `: number`\n\n"
                    "```typescript\nfunction add(a: number, b: number): number {\n  return a + b;\n}\n```\n\n"
                    "No one can accidentally pass text into your math function!"
                ),
                message_am=(
                    "⚙️ *የታይፕ ፈንክሽኖች፦ አስተማማኝ ግብዓት እና ውጤት*\n\n"
                    "በታይፕስክሪፕት ውስጥ ፈንክሽኖችን ጥበቃ የምናደርግላቸው፦\n"
                    "1. የሚቀበሏቸውን እሴቶች አይነት በመግለጽ `(a: number, b: number)`\n"
                    "2. የሚመልሱትን ውጤት አይነት በመወሰን `: number`\n\n"
                    "```typescript\nfunction add(a: number, b: number): number {\n  return a + b;\n}\n```\n\n"
                    "ማንም ሰው በስህተት ጽሁፍን ወደ ሂሳብ ፈንክሽንዎ ውስጥ ማስገባት አይችልም!"
                ),
            ),
            TutorStep(
                id="ts_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a function `double(n: number): number` and call it with 20!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```typescript\nfunction double(n: number): number {\n  return n * 2;\n}\nconsole.log(double(20));\n```"
                ),
                message_am=(
                    "የሚያባዛ ፈንክሽን `double(n: number): number` ጽፈው በ 20 ጥሩት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\nfunction double(n: number): number {\n  return n * 2;\n}\nconsole.log(double(20));\n```"
                ),
                expected_code_output="40",
                hint_en="Write the typed function and print `double(20)`.",
                hint_am="ፈንክሽኑን በትክክል ጽፈው `console.log(double(20));` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Doubled with safety!* 20 * 2 = 40 returned with guaranteed type safety!"
                ),
                success_message_am=(
                    "🎉 *በጥንቃቄ ተባዛ!* 20 * 2 = 40 በሙሉ ጥበቃ ተሰልቷል!"
                ),
            ),
            TutorStep(
                id="ts_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In `function greet(name: string): string`, where is the return type located?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በ `function greet(name: string): string` ውስጥ የመመለሻው ውጤት አይነት (Return type) የቱ ነው?"
                ),
                options_en=[
                    "After the parentheses `: string`",
                    "Before function",
                    "Inside the parentheses",
                    "Inside curly braces",
                ],
                options_am=[
                    "ከቅንፉ ውጪ መጨረሻ ላይ ያለው `: string`",
                    "ከfunction በፊት ያለው",
                    "በቅንፉ ውስጥ ያለው",
                    "በፈረንሳይ ቅንፉ ውስጥ ያለው",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Return types are placed right after the parameter parentheses!",
                success_message_am="🌟 በትክክል! ፈንክሽኑ የሚመልሰው አይነት ከቅንፉ ቀጥሎ ይቀመጣል!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch6",
        order=6,
        title_en="TypeScript Ch 6: Union Types (Either / Or)",
        title_am="ታይፕስክሪፕት ምዕራፍ 6፦ ዩኒየን ታይፕስ (Union Types - ይሄ ወይም ያ)",
        description_en="Learn how union types | allow flexible yet safe values.",
        description_am="የፓይፕ | ምልክት በመጠቀም ተለዋዋጮች ከአንድ በላይ የተወሰኑ አይነቶችን እንዲይዙ ማድረግን ይማሩ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔀 *Flexible Safety: Union Types (`|`)*\n\n"
                    "What if an ID can be either a number (e.g. `101`) or a string (e.g. `\"USR-101\"`)?\n\n"
                    "TypeScript lets you combine types using the pipe `|` operator:\n\n"
                    "```typescript\nlet id: string | number = 101;\nid = \"USR-101\"; // Both are completely valid!\n```\n\n"
                    "This gives you flexibility without sacrificing safety!"
                ),
                message_am=(
                    "🔀 *ተለዋዋጭ ግን አስተማማኝ፦ ዩኒየን ታይፕስ (`|`)*\n\n"
                    "የአንድ ሰው መለያ ቁጥር (ID) ቁጥር (ለምሳሌ `101`) ወይም ጽሁፍ (ለምሳሌ `\"USR-101\"`) ሊሆን ቢችልስ?\n\n"
                    "ታይፕስክሪፕት በፓይፕ `|` ምልክት አማካኝነት ሁለቱንም እንድንፈቅድ ያስችለናል፦\n\n"
                    "```typescript\nlet id: string | number = 101;\nid = \"USR-101\"; // ሁለቱም ይሰራሉ!\n```\n\n"
                    "ይህ ጥበቃውን ሳያጠፋ ተለዋዋጭነትን ይሰጠናል!"
                ),
            ),
            TutorStep(
                id="ts_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Declare a union variable `let status: string | number = 200;` and print it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```typescript\nlet status: string | number = 200;\nconsole.log(status);\n```"
                ),
                message_am=(
                    "`let status: string | number = 200;` ፈጥረው በconsole.log ያትሙት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\nlet status: string | number = 200;\nconsole.log(status);\n```"
                ),
                expected_code_output="200",
                hint_en="Write `let status: string | number = 200;` then `console.log(status);`.",
                hint_am="`let status: string | number = 200;` ጽፈው በሁለተኛው መስመር `console.log(status);` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *Union type active!* You accepted a number while preserving string compatibility!"
                ),
                success_message_am=(
                    "🎉 *ዩኒየን ታይፕ ሰርቷል!* ቁጥርን ተቀብሎ ለጽሁፍም ክፍት የሆነ ጥበቃ አድርገዋል!"
                ),
            ),
            TutorStep(
                id="ts_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which symbol represents a Union Type in TypeScript?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በታይፕስክሪፕት ውስጥ የዩኒየን ታይፕ (ይህ ወይም ያ) መለያ ምልክት የቱ ነው?"
                ),
                options_en=[
                    "| (Pipe)",
                    "& (Ampersand)",
                    "|| (Double Pipe)",
                    "+ (Plus)",
                ],
                options_am=[
                    "| (Pipe)",
                    "& (Ampersand)",
                    "|| (Double Pipe)",
                    "+ (Plus)",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! The single pipe `|` denotes a Union Type in TypeScript!",
                success_message_am="🌟 ትክክል! የ `|` ምልክት በታይፕስክሪፕት ውስጥ ዩኒየን ታይፕን ያመለክታል!",
            ),
        ],
    ),
    TutorChapter(
        id="ts_ch7",
        order=7,
        title_en="TypeScript Ch 7: Capstone: E-Commerce Cart Checkout",
        title_am="ታይፕስክሪፕት ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የኢ-ኮሜርስ የግዢ ጋሪ",
        description_en="Combine interfaces, typed arrays, and functions to calculate a shopping total.",
        description_am="ኢንተርፌስን፣ አሬይን፣ እና ፈንክሽንን በማጣመር አስተማማኝ የኦንላይን ግዢ ካልኩሌተር ይገንቡ።",
        track="typescript",
        steps=[
            TutorStep(
                id="ts_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🛒 *TypeScript Capstone: The E-Commerce Cart!* 💳\n\n"
                    "Real shopping websites (Amazon, Shopify) manage thousands of checkout transactions every second.\n\n"
                    "In this capstone, you will create:\n"
                    "1. An `interface CartItem` with `name: string` and `price: number`\n"
                    "2. Two items: Shoes ($50) and Shirt ($30)\n"
                    "3. Calculate the total and print: `Total: $80`"
                ),
                message_am=(
                    "🛒 *የታይፕስክሪፕት ማጠቃለያ ፕሮጀክት፦ የኢ-ኮሜርስ የግዢ ጋሪ!* 💳\n\n"
                    "ትልልቅ የኦንላይን መገበያያ ዌብሳይቶች (እንደ Amazon ያሉ) በየሰከንዱ በሺዎች የሚቆጠሩ የክፍያ ስሌቶችን ያካሂዳሉ።\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት ውስጥ፦\n"
                    "1. `interface CartItem` (`name: string` እና `price: number`) እንፈጥራለን\n"
                    "2. ሁለት እቃዎችን እናስገባለን (ጫማ $50 እና ሸሚዝ $30)\n"
                    "3. አጠቃላይ ድምሩን አስልተን እናሳውቃለን፦ `Total: $80`"
                ),
            ),
            TutorStep(
                id="ts_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete typed checkout calculation!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```typescript\ninterface CartItem { name: string; price: number; }\nlet item1: CartItem = { name: "Shoes", price: 50 };\nlet item2: CartItem = { name: "Shirt", price: 30 };\nlet total: number = item1.price + item2.price;\nconsole.log("Total: $" + total);\n```'
                ),
                message_am=(
                    "ሙሉውን የታይፕስክሪፕት የግዢ ጋሪ ስሌት ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```typescript\ninterface CartItem { name: string; price: number; }\nlet item1: CartItem = { name: "Shoes", price: 50 };\nlet item2: CartItem = { name: "Shirt", price: 30 };\nlet total: number = item1.price + item2.price;\nconsole.log("Total: $" + total);\n```'
                ),
                expected_code_output="Total: $80",
                hint_en='Write the CartItem interface and sum the prices into `Total: $" + total`.',
                hint_am='የ CartItem ኢንተርፌስን ሰርተው ድምሩን በ `Total: $" + total` ያትሙ።',
                success_message_en=(
                    "🎉 *CHECKOUT VERIFIED!* 🛒💳\n\n"
                    "You just built a bulletproof, enterprise-grade e-commerce checkout logic in TypeScript!"
                ),
                success_message_am=(
                    "🎉 *ክፍያው ተረጋግጧል!* 🛒💳\n\n"
                    "ምንም አይነት ስህተት የማይገባበት እውነተኛ የኦንላይን መገበያያ የሂሳብ ሲስተም በታይፕስክሪፕት ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="ts_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final TypeScript Master Question:*\n\n"
                    "What happens to TypeScript type annotations when running in production?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የታይፕስክሪፕት ማጠቃለያ ጥያቄ፦*\n\n"
                    "ታይፕስክሪፕት ፕሮግራም ወደ ስራ (Production) ሲገባ የታይፕ ምልክቶቹ (Annotations) ምን ይሆናሉ?"
                ),
                options_en=[
                    "They are stripped away into pure, ultra-fast JavaScript",
                    "They slow down the server",
                    "They stay inside the final HTML",
                    "They are encrypted into passwords",
                ],
                options_am=[
                    "ተወግደው ወደ ንጹህ እና እጅግ ፈጣን ጃቫስክሪፕት ይቀየራሉ",
                    "ሰርቨሩን ያዘገዩታል",
                    "በመጨረሻው HTML ውስጥ ይቀመጣሉ",
                    "ወደ ምስጢር ቁጥር ይቀየራሉ",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! TypeScript checks everything during development, then strips types for lightning-fast execution!",
                success_message_am="🏆 እጅግ ድንቅ! ታይፕስክሪፕት በምንሰራበት ጊዜ ስህተቶችን በሙሉ ያርማል፤ ወደ ስራ ሲገባ ግን ወደ ፈጣን ጃቫስክሪፕት ይቀየራል!",
            ),
        ],
    ),
]
