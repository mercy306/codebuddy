"""PHP curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

PHP_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="php_ch1",
        order=1,
        title_en="PHP Ch 1: Welcome to PHP & echo",
        title_am="ፒኤችፒ ምዕራፍ 1፦ ከፒኤችፒ ጋር መተዋወቅ እና echo",
        description_en="Discover the powerhouse behind 75% of websites on the internet.",
        description_am="የኢንተርኔት ድረ-ገጾችን 75 በመቶ የሚያንቀሳቅሰውን ፒኤችፒ (PHP) ቋንቋ ይማሩ።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🐘 *Welcome to PHP!* 🌐\n\n"
                    "PHP (Hypertext Preprocessor) is the legendary engine behind **WordPress, Wikipedia, "
                    "Laravel, and Facebook's original codebase**!\n\n"
                    "On the web, PHP runs on the server. Whenever a visitor visits a web page, PHP computes the "
                    "content and sends it to their screen.\n\n"
                    "In PHP, to display text, we use the `echo` command:\n\n"
                    "```php\necho \"Hello PHP\";\n```\n\n"
                    "- Every PHP statement ends with a semicolon `;`\n"
                    "- Text is placed inside quotes `\"...\"`"
                ),
                message_am=(
                    "🐘 *እንኳን ወደ ፒኤችፒ (PHP) በደህና መጡ!* 🌐\n\n"
                    "ፒኤችፒ እንደ **WordPress፣ Wikipedia፣ Laravel እና የመጀመሪያው የፌስቡክ (Facebook)** ኮድ የተገነባበት "
                    "የድህረ-ገጽ አለም ግዙፍ ሞተር ነው!\n\n"
                    "በድህረ-ገጽ ላይ ፒኤችፒ የሚሰራው በሰርቨር (Server) ላይ ነው። ተጠቃሚ ድረ-ገጹን ሲከፍት ፒኤችፒ መረጃውን አቀነባብሮ ያቀርባል።\n\n"
                    "በፒኤችፒ ውስጥ ጽሁፍ በስክሪኑ ላይ ለማውጣት `echo` የሚለውን ትዕዛዝ እንጠቀማለን፦\n\n"
                    "```php\necho \"Hello PHP\";\n```\n\n"
                    "- እያንዳንዱ የፒኤችፒ መስመር በሴሚኮለን `;` ይዘጋል\n"
                    "- ጽሁፍ በጥቅስ ምልክት `\"...\"` ውስጥ ይቀመጣል"
                ),
            ),
            TutorStep(
                id="php_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's output our first message with PHP!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```php\necho "Hello PHP";\n```'
                ),
                message_am=(
                    "በፒኤችፒ የመጀመሪያውን ጽሁፍ እናውጣ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\necho "Hello PHP";\n```'
                ),
                expected_code_output="Hello PHP",
                hint_en='Type `echo "Hello PHP";` with the semicolon `;` at the end.',
                hint_am='በመጨረሻ ላይ ሴሚኮለን በመጨመር `echo "Hello PHP";` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *AMAZING!* You just ran real PHP code on the server!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* እውነተኛ የፒኤችፒ (PHP) ኮድ በሰርቨሩ ላይ በተሳካ ሁኔታ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="php_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword is used in PHP to print or display output to the browser screen?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በፒኤችፒ ውስጥ መረጃዎችን እና ጽሁፎችን ለተጠቃሚው ለማሳየት የትኛው ቃል ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "echo",
                    "show",
                    "display",
                    "write",
                ],
                options_am=[
                    "echo",
                    "show",
                    "display",
                    "write",
                ],
                correct_option_index=0,
                hint_en="We used it in the previous step: `echo`!",
                hint_am="ባለፈው ደረጃ ላይ የተጠቀምንበት ቃል ነው፦ `echo`!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch2",
        order=2,
        title_en="PHP Ch 2: Variables with Dollar Sign ($)",
        title_am="ፒኤችፒ ምዕራፍ 2፦ ተለዋዋጮች በ $ ምልክት",
        description_en="Store data in memory and join strings together.",
        description_am="መረጃዎችን በ `$ ` ተለዋዋጭ ማህደረ-ትውስታ ውስጥ ማስቀመጥ እና ጽሁፎችን ማጣመር።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Variables in PHP always start with `$`!* 💵\n\n"
                    "Whenever you create or use a variable in PHP, prefix its name with a dollar sign `$`. For example:\n"
                    "```php\n$city = \"Addis Ababa\";\n```\n\n"
                    "To glue two strings together (concatenation), PHP uses a dot (`.`):\n"
                    "```php\necho \"Welcome to \" . $city;\n```"
                ),
                message_am=(
                    "📦 *በፒኤችፒ ውስጥ ተለዋዋጮች ሁልጊዜ በ `$` ምልክት ይጀምራሉ!* 💵\n\n"
                    "በፒኤችፒ ውስጥ ተለዋዋጭ (Variable) ስትፈጥሩ ወይም ስትጠሩ የዶላር ምልክት `$` ታስቀድማላችሁ፦\n"
                    "```php\n$city = \"Addis Ababa\";\n```\n\n"
                    "ሁለት ጽሁፎችን ለማያያዝ ደግሞ የነጥብ ምልክት (`.`) እንጠቀማለን፦\n"
                    "```php\necho \"Welcome to \" . $city;\n```"
                ),
            ),
            TutorStep(
                id="php_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `$name` variable and echo a greeting using the dot `.` operator!\n\n"
                    "👇 *Type and send this code:*\n"
                    '```php\n$name = "Abebe";\necho "Hello " . $name;\n```'
                ),
                message_am=(
                    "የ `$name` ተለዋዋጭ ፈጥረው በነጥብ `.` በማያያዝ ሰላምታ ያውጡ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\n$name = "Abebe";\necho "Hello " . $name;\n```'
                ),
                expected_code_output="Hello Abebe",
                hint_en='Write `$name = "Abebe"; echo "Hello " . $name;`',
                hint_am='`$name = "Abebe"; echo "Hello " . $name;` ብለው ይላኩ።',
                success_message_en=(
                    "🌟 *Superb!* You stored text in a `$name` variable and concatenated it with a dot `.`!"
                ),
                success_message_am=(
                    "🌟 *በጣም ድንቅ!* ጽሁፉን በ `$name` አስቀምጠው በነጥብ `.` አያይዘው አሳይተዋል!"
                ),
            ),
            TutorStep(
                id="php_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Which symbol is used in PHP to concatenate (glue) two strings together?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በፒኤችፒ ውስጥ ሁለት ጽሁፎችን ለማያያዝ (ለማጣመር) የትኛው ምልክት ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "The dot operator (.)",
                    "The plus sign (+)",
                    "The ampersand (&)",
                    "The comma (,)",
                ],
                options_am=[
                    "የነጥብ ምልክት (.)",
                    "የመደመር ምልክት (+)",
                    "የአምፐርሳንድ ምልክት (&)",
                    "ነጠላ ሰረዝ (,)",
                ],
                correct_option_index=0,
                hint_en="In PHP, strings are joined with a single period dot `.`, while `+` is reserved strictly for numbers!",
                hint_am="በፒኤችፒ ጽሁፎች የሚጣመሩት በነጥብ `.` ነው፤ `+` ለቁጥሮች ድምር ብቻ ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch3",
        order=3,
        title_en="PHP Ch 3: Numbers & Server Math",
        title_am="ፒኤችፒ ምዕራፍ 3፦ ቁጥሮች እና የሰርቨር ሂሳብ",
        description_en="Perform calculations for web stores, carts, and invoices.",
        description_am="ለድረ-ገጾች የግብይት፣ የዋጋ እና የካርጎ ሂሳብ ስሌቶችን ማከናወን።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔢 *Numbers and Math in PHP* 🛒\n\n"
                    "Every web store calculates shopping cart totals, discounts, and shipping fees.\n\n"
                    "PHP supports standard arithmetic operations:\n"
                    "- Addition: `+`\n"
                    "- Subtraction: `-`\n"
                    "- Multiplication: `*`\n"
                    "- Division: `/`\n\n"
                    "```php\n$price = 100;\n$discount = 20;\necho $price - $discount; // Outputs 80\n```"
                ),
                message_am=(
                    "🔢 *ቁጥሮች እና የሂሳብ ስሌት በፒኤችፒ* 🛒\n\n"
                    "በኢንተርኔት ላይ ያሉ መደብሮች የዕቃ ዋጋን፣ ቅናሽ እና የትራንስፖርት ክፍያን በፒኤችፒ ያሰላሉ።\n\n"
                    "መሰረታዊ የሂሳብ ምልክቶች፦\n"
                    "- መደመር፦ `+`\n"
                    "- መቀነስ፦ `-`\n"
                    "- ማባዛት፦ `*`\n"
                    "- ማካፈል፦ `/`\n\n"
                    "```php\n$price = 100;\n$discount = 20;\necho $price - $discount; // 80 ያወጣል\n```"
                ),
            ),
            TutorStep(
                id="php_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's calculate an online order total: `$item = 40` plus `$shipping = 10`.\n\n"
                    "👇 *Type and send this code:*\n"
                    '```php\n$item = 40;\n$shipping = 10;\necho $item + $shipping;\n```'
                ),
                message_am=(
                    "የዕቃ ዋጋ `$item = 40` እና የትራንስፖርት `$shipping = 10` ድምርን እናስላ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\n$item = 40;\n$shipping = 10;\necho $item + $shipping;\n```'
                ),
                expected_code_output="50",
                hint_en='Write `$item = 40; $shipping = 10; echo $item + $shipping;`',
                hint_am='`$item = 40; $shipping = 10; echo $item + $shipping;` ብለው ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* The server calculated `50` effortlessly!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ሰርቨሩ `50` የሚለውን ድምር ወዲያውኑ አሰላ!"
                ),
            ),
            TutorStep(
                id="php_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "What will this code output?\n"
                    "```php\n$a = 5;\n$b = 4;\necho $a * $b;\n```"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "ይህ የፒኤችፒ ኮድ ምን ውጤት ያወጣል?\n"
                    "```php\n$a = 5;\n$b = 4;\necho $a * $b;\n```"
                ),
                options_en=[
                    "20",
                    "9",
                    "54",
                    "1",
                ],
                options_am=[
                    "20",
                    "9",
                    "54",
                    "1",
                ],
                correct_option_index=0,
                hint_en="5 multiplied by 4 equals 20!",
                hint_am="5 ሲባዛ በ 4 ውጤቱ 20 ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch4",
        order=4,
        title_en="PHP Ch 4: Making Decisions with if / else",
        title_am="ፒኤችፒ ምዕራፍ 4፦ ውሳኔዎች በ if / else",
        description_en="Control flow based on conditions like user permissions and login states.",
        description_am="እንደ ተጠቃሚ ፍቃድ እና የይለፍ ቃል ሁኔታዎችን በ if/else መቆጣጠር።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Making Decisions with `if` and `else`* 🧠\n\n"
                    "Programs make choices using conditions:\n\n"
                    "```php\nif ($score >= 50) {\n    echo \"Pass\";\n} else {\n    echo \"Try Again\";\n}\n```\n\n"
                    "- The condition lives inside parentheses `( )`\n"
                    "- The action code lives inside curly brackets `{ }`"
                ),
                message_am=(
                    "🚦 *በ `if` እና `else` ውሳኔዎችን መወሰን* 🧠\n\n"
                    "የኮምፒውተር ፕሮግራሞች ሁኔታዎችን አይተው ይወስናሉ፦\n\n"
                    "```php\nif ($score >= 50) {\n    echo \"Pass\";\n} else {\n    echo \"Try Again\";\n}\n```\n\n"
                    "- መስፈርቱ በቅንፍ `( )` ውስጥ ይቀመጣል\n"
                    "- የሚሰራው ኮድ በፈረንሳይ ቅንፍ `{ }` ውስጥ ይጻፋል"
                ),
            ),
            TutorStep(
                id="php_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write an `if` statement to check if `$score = 75` is greater than or equal to `50`!\n\n"
                    "👇 *Type and send:*\n"
                    '```php\n$score = 75;\nif ($score >= 50) {\n    echo "Passed!";\n}\n```'
                ),
                message_am=(
                    "የ `$score = 75` ውጤት ከ `50` እኩል ወይም የሚበልጥ መሆኑን በ `if` ይፈትሹ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\n$score = 75;\nif ($score >= 50) {\n    echo "Passed!";\n}\n```'
                ),
                expected_code_output="Passed!",
                hint_en='Write `$score = 75; if ($score >= 50) { echo "Passed!"; }`',
                hint_am='`$score = 75; if ($score >= 50) { echo "Passed!"; }` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *YES!* The condition was met, and the server executed the block!"
                ),
                success_message_am=(
                    "🎉 *እሰይ!* መስፈርቱ ተሟልቶ ሰርቨሩ በፈረንሳይ ቅንፉ ውስጥ ያለውን ኮድ አስኬዷል!"
                ),
            ),
            TutorStep(
                id="php_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which comparison operator tests whether two values are strictly equal in type and value?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በፒኤችፒ ውስጥ ሁለት እሴቶች በአይነትም በቁጥርም ፍጹም እኩል መሆናቸውን የሚፈትሸው የትኛው ነው?"
                ),
                options_en=[
                    "=== (Triple equals)",
                    "= (Single equals)",
                    "!= (Not equals)",
                    "<= (Less than or equal)",
                ],
                options_am=[
                    "=== (ሶስት የእኩልነት ምልክት)",
                    "= (አንድ የእኩልነት ምልክት)",
                    "!= (እኩል ያልሆነ)",
                    "<= (አነስተኛ ወይም እኩል)",
                ],
                correct_option_index=0,
                hint_en="A single `=` assigns values, while `===` checks both value and type strictly!",
                hint_am="አንድ `=` ዋጋን ለመስጠት ሲሆን `===` ደግሞ እኩል መሆናቸውን በጥብቅ ለመፈተሽ ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch5",
        order=5,
        title_en="PHP Ch 5: Repeating with Loops",
        title_am="ፒኤችፒ ምዕራፍ 5፦ ዑደቶች በ for እና while",
        description_en="Automate repetitive tasks and counts with loops.",
        description_am="ተደጋጋሚ ስራዎችን እና ቆጠራዎችን በሉፕ (Loop) ማከናወን።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *Repeating with the `for` Loop* ⚡\n\n"
                    "Instead of typing the same code 10 times, a `for` loop does it automatically!\n\n"
                    "```php\nfor ($i = 1; $i <= 3; $i++) {\n    echo $i;\n}\n```\n\n"
                    "1. `$i = 1`: Start at 1\n"
                    "2. `$i <= 3`: Run while `$i` is less than or equal to 3\n"
                    "3. `$i++`: Add 1 after each cycle"
                ),
                message_am=(
                    "🔄 *በ `for` ሉፕ መድገም* ⚡\n\n"
                    "አንድን ኮድ ደጋግሞ ከመጻፍ ይልቅ በ `for` ሉፕ በራስ-ሰር እንዲደጋገም ይደረጋል፦\n\n"
                    "```php\nfor ($i = 1; $i <= 3; $i++) {\n    echo $i;\n}\n```\n\n"
                    "1. `$i = 1`፦ ከ 1 ጀምር\n"
                    "2. `$i <= 3`፦ ከ 3 እስኪያንስ ወይም እኩል እስኪሆን ድረስ ቀጥል\n"
                    "3. `$i++`፦ በእያንዳንዱ ዙር 1 ጨምር"
                ),
            ),
            TutorStep(
                id="php_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write a loop that counts from 1 to 3 with spaces!\n\n"
                    "👇 *Type and send:*\n"
                    '```php\nfor ($i = 1; $i <= 3; $i++) {\n    echo $i . " ";\n}\n```'
                ),
                message_am=(
                    "ከ 1 እስከ 3 የሚቆጥር የ `for` ሉፕ እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\nfor ($i = 1; $i <= 3; $i++) {\n    echo $i . " ";\n}\n```'
                ),
                expected_code_output="1 2 3",
                hint_en='Write `for ($i = 1; $i <= 3; $i++) { echo $i . " "; }`',
                hint_am='`for ($i = 1; $i <= 3; $i++) { echo $i . " "; }` ብለው ይላኩ።',
                success_message_en=(
                    "🔥 *OUTSTANDING!* You just automated repetition with a PHP `for` loop!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* በፒኤችፒ `for` ሉፕ በመጠቀም ድግግሞሽን አውቶሜት አድርገዋል!"
                ),
            ),
            TutorStep(
                id="php_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "What does the `$i++` shorthand operation do in PHP?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በፒኤችፒ ውስጥ `$i++` ምን ያደርጋል?"
                ),
                options_en=[
                    "Increments the variable $i by 1",
                    "Multiplies $i by 2",
                    "Resets $i to 0",
                    "Checks if $i is positive",
                ],
                options_am=[
                    "በተለዋዋጩ $i ላይ 1 ይደምራል",
                    "$i ን በ 2 ያባዛል",
                    "$i ን ወደ 0 ይመልሳል",
                    "$i ፖዘቲቭ መሆኑን ያረጋግጣል",
                ],
                correct_option_index=0,
                hint_en="`$i++` adds exactly 1 to `$i` each time (equivalent to `$i = $i + 1`)!",
                hint_am="`$i++` በተለዋዋጩ ላይ በትክክል 1 ይደምራል (ከ `$i = $i + 1` ጋር እኩል ነው)!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch6",
        order=6,
        title_en="PHP Ch 6: Associative Arrays (Key-Value)",
        title_am="ፒኤችፒ ምዕራፍ 6፦ አሶሼቲቭ አሬይ (Key-Value)",
        description_en="Manage structured records like user profiles and database rows.",
        description_am="እንደ ተጠቃሚ ፕሮፋይል ያሉ የተደራጁ መረጃዎችን በአሶሼቲቭ አሬይ ማስተዳደር።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🗂️ *Associative Arrays: PHP's Superpower!* 🔑\n\n"
                    "One of PHP's most famous features is the **Associative Array**, where every piece of data has a named label (key):\n\n"
                    "```php\n$user = [\n    \"name\" => \"Sara\",\n    \"role\" => \"Admin\"\n];\n\necho $user[\"role\"]; // Outputs Admin\n```\n\n"
                    "- The arrow `=>` pairs a key to its value\n"
                    "- Data is fetched using square brackets `[\"key\"]`"
                ),
                message_am=(
                    "🗂️ *አሶሼቲቭ አሬይ (Associative Arrays)፦ የፒኤችፒ ዋነኛ ጥንካሬ!* 🔑\n\n"
                    "በፒኤችፒ ውስጥ እያንዳንዱ መረጃ በስሙ የሚጠራበት አሶሼቲቭ አሬይ በጣም ተወዳጅ ነው፦\n\n"
                    "```php\n$user = [\n    \"name\" => \"Sara\",\n    \"role\" => \"Admin\"\n];\n\necho $user[\"role\"]; // Admin ያወጣል\n```\n\n"
                    "- የቀስት ምልክቱ `=>` ስሙን ከዋጋው ጋር ያገናኛል\n"
                    "- መረጃው የሚጠራው በካሬ ቅንፍ `[\"ቁልፍ\"]` ውስጥ ነው"
                ),
            ),
            TutorStep(
                id="php_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `$member` array with `\"role\" => \"Editor\"` and echo the role!\n\n"
                    "👇 *Type and send:*\n"
                    '```php\n$member = ["role" => "Editor"];\necho $member["role"];\n```'
                ),
                message_am=(
                    "የ `$member` አሬይ ፈጥረው የ `Editor` ሚናውን በስክሪኑ ላይ ያውጡ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\n$member = ["role" => "Editor"];\necho $member["role"];\n```'
                ),
                expected_code_output="Editor",
                hint_en='Write `$member = ["role" => "Editor"]; echo $member["role"];`',
                hint_am='`$member = ["role" => "Editor"]; echo $member["role"];` ብለው ይላኩ።',
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You accessed a structured key in a PHP associative array!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* በፒኤችፒ አሶሼቲቭ አሬይ ውስጥ ያለን መረጃ በስሙ ጠርተው አሳይተዋል!"
                ),
            ),
            TutorStep(
                id="php_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which symbol in PHP links a key to a value inside an associative array?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በአሶሼቲቭ አሬይ ውስጥ ስምን ከዋጋ ጋር የሚያገናኘው የትኛው ምልክት ነው?"
                ),
                options_en=[
                    "=> (Fat arrow)",
                    "-> (Single arrow)",
                    ":= (Colon equals)",
                    "== (Double equals)",
                ],
                options_am=[
                    "=> (ወፍራም ቀስት)",
                    "-> (ቀጭን ቀስት)",
                    ":= (ኮለን እኩል)",
                    "== (ድርብ እኩል)",
                ],
                correct_option_index=0,
                hint_en="The fat arrow `=>` points from key to value (e.g. `'name' => 'Sara'`)!",
                hint_am="ወፍራም ቀስት `=>` ከቁልፍ ወደ ዋጋ ያመለክታል (ለምሳሌ፦ `'name' => 'Sara'`)!",
            ),
        ],
    ),
    TutorChapter(
        id="php_ch7",
        order=7,
        title_en="PHP Ch 7: Functions & Web Capstone Project",
        title_am="ፒኤችፒ ምዕራፍ 7፦ ፈንክሽኖች እና የፕሮፋይል ጀነሬተር",
        description_en="Build reusable functions and construct a dynamic web user badge.",
        description_am="እንደገና ጥቅም ላይ የሚውሉ ፈንክሽኖችን በመገንባት የበይነመረብ ፕሮፋይል ባጅ መስራት።",
        track="php",
        steps=[
            TutorStep(
                id="php_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *Functions in PHP* 🛠️\n\n"
                    "A function is a reusable machine that takes input, does work, and returns a result:\n\n"
                    "```php\nfunction greetUser($name) {\n    return \"Hello, \" . $name;\n}\n\necho greetUser(\"Abebe\");\n```\n\n"
                    "Now let's build our grand capstone: A Dynamic User Badge Generator for a web app!"
                ),
                message_am=(
                    "🏗️ *ፈንክሽኖች (Functions) በፒኤችፒ* 🛠️\n\n"
                    "ፈንክሽን መረጃን ተቀብሎ ሰርቶ መልስ የሚሰጥ እንደገና ጥቅም ላይ የሚውል መሳሪያ ነው፦\n\n"
                    "```php\nfunction greetUser($name) {\n    return \"Hello, \" . $name;\n}\n\necho greetUser(\"Abebe\");\n```\n\n"
                    "አሁን የመጨረሻውን ታላቅ ፕሮጀክት እንገንባ፦ ለድህረ-ገጽ ተጠቃሚዎች የፕሮፋይል ባጅ ጀነሬተር!"
                ),
            ),
            TutorStep(
                id="php_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Define a function `makeBadge($user)` that returns `\"Verified: \" . $user` and echo it for `\"Liya\"`!\n\n"
                    "👇 *Type and send:*\n"
                    '```php\nfunction makeBadge($user) {\n    return "Verified: " . $user;\n}\necho makeBadge("Liya");\n```'
                ),
                message_am=(
                    "`makeBadge($user)` የሚል ፈንክሽን ፈጥረው `\"Verified: \" . $user` እንዲመልስ ያድርጉና ለ `\"Liya\"` አውጡት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```php\nfunction makeBadge($user) {\n    return "Verified: " . $user;\n}\necho makeBadge("Liya");\n```'
                ),
                expected_code_output="Verified: Liya",
                hint_en='Write the function `makeBadge($user)` returning `"Verified: " . $user;` then `echo makeBadge("Liya");`',
                hint_am='`function makeBadge($user) { return "Verified: " . $user; } echo makeBadge("Liya");` ብለው ይላኩ።',
                success_message_en=(
                    "🏆 *MASTERCLASS!* You have officially built a dynamic server-side function in PHP!"
                ),
                success_message_am=(
                    "🏆 *ታላቅ ድል!* በፒኤችፒ ሰርቨር ላይ የሚሰራ ፈንክሽን ገንብተው በተሳካ ሁኔታ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="php_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! PHP GRADUATE!** 🌟🎓\n\n"
                    "You have mastered the foundational backbone of the web with PHP:\n"
                    "1. 🐘 Server output with `echo` and semicolons `;`\n"
                    "2. 📦 Dollar variables `$` and string concatenation `.`\n"
                    "3. 🔢 E-commerce calculations and math\n"
                    "4. 🚦 Conditional logic with `if` / `else`\n"
                    "5. 🔄 Automated repetition with `for` loops\n"
                    "6. 🗂️ Associative arrays with keys and fat arrows `=>`\n"
                    "7. 🛠️ Reusable functions and web badge generation!\n\n"
                    "You are now ready to build real backends and dynamic web apps! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የፒኤችፒ ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "የድህረ-ገጽ አለምን መሰረት የያዘውን ፒኤችፒ በሚገባ ተምረዋል፦\n"
                    "1. 🐘 የሰርቨር ውጤት በ `echo` እና ሴሚኮለን `;`\n"
                    "2. 📦 የዶላር ምልክት ተለዋዋጮች `$` እና የጽሁፍ ማያያዣ `.`\n"
                    "3. 🔢 የድረ-ገጽ ሂሳብ እና ስሌቶች\n"
                    "4. 🚦 ብልህ ውሳኔዎች በ `if` / `else`\n"
                    "5. 🔄 አውቶሜሽን በ `for` ሉፖች\n"
                    "6. 🗂️ አሶሼቲቭ አሬይ እና የቀስት ምልክት `=>`\n"
                    "7. 🛠️ ፈንክሽኖች እና የፕሮፋይል ባጅ ጀነሬተር!\n\n"
                    "አሁን እውነተኛ የሰርቨር እና የድህረ-ገጽ ፕሮግራሞችን ለመገንባት ዝግጁ ነዎት! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_php_chapters() -> List[TutorChapter]:
    """Return all PHP tutor chapters ordered."""
    return sorted(PHP_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_php_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve PHP tutor chapter by ID."""
    for ch in PHP_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_php_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next PHP chapter ID."""
    chapters = get_all_php_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
