"""Linux Bash Shell curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

BASH_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="bash_ch1",
        order=1,
        title_en="Bash Ch 1: Welcome to Linux Terminal & echo",
        title_am="ሊኑክስ ባሽ ምዕራፍ 1፦ ከሊኑክስ ተርሚናል ጋር መተዋወቅ እና echo",
        description_en="Learn how servers, cloud infrastructure, and DevOps are powered by Linux Bash.",
        description_am="የክላውድ ሰርቨሮች እና DevOps በሊኑክስ ባሽ (Bash) እንዴት እንደሚንቀሳቀሱ ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🐧 *Welcome to Linux Bash!* 💻\n\n"
                    "Over **96% of the world's top 1 million web servers** and 100% of the world's top 500 supercomputers run on **Linux**!\n\n"
                    "Cloud platforms (AWS, Azure, Google Cloud, Docker) are controlled through the Linux command shell called **Bash**.\n\n"
                    "In Bash, the most fundamental command to print words or messages is **`echo`**:\n\n"
                    "```bash\necho \"Hello Linux\"\n```\n\n"
                    "No classes, no boilerplate, just pure direct command line power!"
                ),
                message_am=(
                    "🐧 *እንኳን ወደ ሊኑክስ ባሽ (Linux Bash) በደህና መጡ!* 💻\n\n"
                    "በዓለም ላይ ካሉ 1 ሚሊዮን ዋና ዋና የኢንተርኔት ሰርቨሮች ውስጥ ከ**96% በላይ የሚሆኑት** በ**ሊኑክስ (Linux)** ነው የሚሰሩት!\n\n"
                    "እንደ AWS, Google Cloud, እና Docker ያሉ የክላውድ ሲስተሞች የሚተዳደሩት በ**ባሽ (Bash)** ትዕዛዞች አማካኝነት ነው።\n\n"
                    "በባሽ ውስጥ ጽሁፍ በስክሪኑ ላይ ለማውጣት የምንጠቀመው ቀላሉ ትዕዛዝ **`echo`** ነው፦\n\n"
                    "```bash\necho \"Hello Linux\"\n```\n\n"
                    "ምንም አይነት ተጨማሪ አሰልቺ ቅንፎች ሳያስፈልጉት በቀጥታ ይሰራል!"
                ),
            ),
            TutorStep(
                id="bash_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's print our first words on the Linux terminal!\n\n"
                    "👇 *Type this command in the chat and send:*\n"
                    '```bash\necho "Hello Linux"\n```'
                ),
                message_am=(
                    "በሊኑክስ ተርሚናል ላይ የመጀመሪያውን ጽሁፍ እናሳትም!\n\n"
                    "👇 *ይህንን ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    '```bash\necho "Hello Linux"\n```'
                ),
                expected_code_output="Hello Linux",
                hint_en='Write `echo "Hello Linux"` and send.',
                hint_am='`echo "Hello Linux"` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *COMMAND EXECUTED!* You just ran real Linux Bash on the terminal!"
                ),
                success_message_am=(
                    "🎉 *ትዕዛዙ ተፈጽሟል!* እውነተኛ የሊኑክስ ባሽ ትዕዛዝ አሁን በተርሚናሉ ላይ አሰርተዋል!"
                ),
            ),
            TutorStep(
                id="bash_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which Linux Bash command prints text to the screen?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በሊኑክስ ባሽ ውስጥ በማያ ገጹ ላይ ጽሁፍ እንዲታይ የሚያደርገው ትዕዛዝ የትኛው ነው?"
                ),
                options_en=[
                    "echo",
                    "print",
                    "say",
                    "show",
                ],
                options_am=[
                    "echo",
                    "print",
                    "say",
                    "show",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `echo` is the universal output command in Bash!",
                success_message_am="🌟 በትክክል! `echo` በባሽ ውስጥ ጽሁፍ ለማሳየት የሚያገለግል ዋነኛ ትዕዛዝ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch2",
        order=2,
        title_en="Bash Ch 2: Shell Variables",
        title_am="ሊኑክስ ባሽ ምዕራፍ 2፦ የተርሚናል ተለዋዋጮች (Variables)",
        description_en="Learn how to store server configurations and retrieve them using $.",
        description_am="የሰርቨር ቅንብሮችን በተለዋዋጭ ውስጥ እንዴት እንደምናስቀምጥ እና በ$ ምልክት እንደምናወጣ ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Storing Data in Bash Variables*\n\n"
                    "In Bash, you create a variable by typing `NAME=value` (with **NO spaces** around `=`):\n\n"
                    "```bash\nSERVER=\"Web01\"\n```\n\n"
                    "To read the value back, you **must put a dollar sign `$` in front**:\n\n"
                    "```bash\necho \"Connected to $SERVER\"\n```"
                ),
                message_am=(
                    "📦 *መረጃዎችን በባሽ ተለዋዋጮች ውስጥ ማስቀመጥ*\n\n"
                    "በባሽ ውስጥ ተለዋዋጭ ስንፈጥር በ `=` ዙሪያ **ምንም ክፍተት (space) ሳናደርግ** `NAME=value` ብለን እንጽፋለን፦\n\n"
                    "```bash\nSERVER=\"Web01\"\n```\n\n"
                    "የተቀመጠውን መረጃ ለመጥራት ደግሞ ከስሙ ፊት ለፊት **የዶላር ምልክት `$`** እናደርጋለን፦\n\n"
                    "```bash\necho \"Connected to $SERVER\"\n```"
                ),
            ),
            TutorStep(
                id="bash_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create `USER=\"Admin\"` and print `Welcome $USER`!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```bash\nUSER="Admin"\necho "Welcome $USER"\n```'
                ),
                message_am=(
                    "`USER=\"Admin\"` ፈጥረው `Welcome $USER` ብለው ያትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```bash\nUSER="Admin"\necho "Welcome $USER"\n```'
                ),
                expected_code_output="Welcome Admin",
                hint_en='Write `USER="Admin"` on first line, then `echo "Welcome $USER"` on second line.',
                hint_am='በመጀመሪያው መስመር `USER="Admin"` በሁለተኛው መስመር `echo "Welcome $USER"` ብለው ይጻፉ።',
                success_message_en=(
                    "🎉 *Variable loaded!* You used the `$` expansion to print the stored admin name!"
                ),
                success_message_am=(
                    "🎉 *ተለዋዋጩ ሰርቷል!* የ `$` ምልክት በመጠቀም የአድሚኑን ስም በተሳካ ሁኔታ አውጥተዋል!"
                ),
            ),
            TutorStep(
                id="bash_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Bash, which symbol must you place before a variable name to read its value?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በሊኑክስ ባሽ ውስጥ የአንድን ተለዋዋጭ ዋጋ ለማንበብ ከስሙ በፊት የምናስቀምጠው ምልክት የትኛው ነው?"
                ),
                options_en=[
                    "$ (Dollar sign)",
                    "@ (At sign)",
                    "# (Hash sign)",
                    "& (Ampersand)",
                ],
                options_am=[
                    "$ (የዶላር ምልክት)",
                    "@ (የአት ምልክት)",
                    "# (የሃሽ ምልክት)",
                    "& (የአምፐርሳንድ ምልክት)",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! The `$` prefix expands variable values in Bash!",
                success_message_am="🌟 በትክክል! የ `$` ምልክት በባሽ ውስጥ የተለዋዋጩን ዋጋ ለማውጣት ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch3",
        order=3,
        title_en="Bash Ch 3: Command Arithmetic",
        title_am="ሊኑክስ ባሽ ምዕራፍ 3፦ የተርሚናል ሂሳብ ስሌት",
        description_en="Learn how the shell calculates disk usage, server memory, and numbers.",
        description_am="ተርሚናሉ የሰርቨር ሜሞሪን እና ቁጥሮችን እንዴት እንደሚያሰላ ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🧮 *Doing Math in Bash: `$(( ... ))`*\n\n"
                    "In Bash, if you type `echo 10 + 20`, it literally prints the text `10 + 20`.\n\n"
                    "To tell the shell to perform real math calculation, we wrap the formula inside double parentheses:\n"
                    "**`$(( 10 + 20 ))`**\n\n"
                    "```bash\necho $(( 10 + 20 ))\n# Outputs: 30\n```"
                ),
                message_am=(
                    "🧮 *በባሽ ውስጥ ሂሳብ ማሰላት፦ `$(( ... ))`*\n\n"
                    "በባሽ ውስጥ `echo 10 + 20` ብለው ቢጽፉ ጽሁፉን እንዳለ `10 + 20` ብሎ ነው የሚያወጣው።\n\n"
                    "ትክክለኛውን የሂሳብ ስሌት እንዲሰራ በሁለት ቅንፎች ውስጥ **`$(( ... ))`** እናስገባዋለን፦\n\n"
                    "```bash\necho $(( 10 + 20 ))\n# ውጤቱ: 30\n```"
                ),
            ),
            TutorStep(
                id="bash_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Calculate the total server RAM: 16 GB + 32 GB!\n\n"
                    "👇 *Type this command in the chat and send:*\n"
                    "```bash\necho $(( 16 + 32 ))\n```"
                ),
                message_am=(
                    "አጠቃላይ የሰርቨሩን ራም (RAM) እንደምር፦ 16 + 32!\n\n"
                    "👇 *ይህንን ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```bash\necho $(( 16 + 32 ))\n```"
                ),
                expected_code_output="48",
                hint_en="Write `echo $(( 16 + 32 ))` and send.",
                hint_am="`echo $(( 16 + 32 ))` ብለው ጽፈው ይላኩ።",
                success_message_en=(
                    "🎉 *48 calculated!* You just ran shell arithmetic with `$(( ))`!"
                ),
                success_message_am=(
                    "🎉 *48 ተሰልቷል!* በባሽ ተርሚናል ውስጥ የሂሳብ ስሌትን በትክክል ሰርተዋል!"
                ),
            ),
            TutorStep(
                id="bash_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which wrapper tells Bash to perform a mathematical calculation?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በባሽ ውስጥ የሂሳብ ስሌት እንዲሰራ የምንጠቀመው የትኛውን ቅርጽ ነው?"
                ),
                options_en=[
                    "$(( ... ))",
                    "${{ ... }}",
                    "$( ... )",
                    "$[ ... ]",
                ],
                options_am=[
                    "$(( ... ))",
                    "${{ ... }}",
                    "$( ... )",
                    "$[ ... ]",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Double parentheses `$(( ))` perform integer arithmetic in Bash!",
                success_message_am="🌟 በትክክል! `$(( ))` በባሽ ውስጥ የሂሳብ ስሌት መስሪያ ምልክት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch4",
        order=4,
        title_en="Bash Ch 4: Server Checks with if / else",
        title_am="ሊኑክስ ባሽ ምዕራፍ 4፦ የሰርቨር ቁጥጥር በ if እና else",
        description_en="Learn how servers monitor disk space and trigger alerts using if conditions.",
        description_am="ሰርቨሮች የዲስክ ቦታን እንዴት እንደሚፈትሹ እና ማስጠንቀቂያ እንደሚሰጡ ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Automated Server Monitoring with if / else*\n\n"
                    "Servers monitor their own health automatically using Bash conditions.\n\n"
                    "In Bash, the condition is written in square brackets `[ ... ]` with spaces around the brackets:\n\n"
                    "```bash\ndisk=85\nif [ $disk -ge 80 ]; then\n    echo \"Warning: High Disk!\"\nelse\n    echo \"Disk Healthy\"\nfi\n```\n\n"
                    "- `-ge` means **Greater than or Equal to**\n"
                    "- `fi` ends the `if` block (`if` spelled backwards!)"
                ),
                message_am=(
                    "🚦 *የሰርቨር ቁጥጥር በ if እና else*\n\n"
                    "ሰርቨሮች ጤናማነታቸውን በየሰኮንዱ በራሳቸው የሚቆጣጠሩት በባሽ ስክሪፕት አማካኝነት ነው።\n\n"
                    "በባሽ ውስጥ መስፈርቱን በካሬ ቅንፍ `[ ... ]` ውስጥ በክፍተት (space) እናስገባለን፦\n\n"
                    "```bash\ndisk=85\nif [ $disk -ge 80 ]; then\n    echo \"Warning: High Disk!\"\nelse\n    echo \"Disk Healthy\"\nfi\n```\n\n"
                    "- `-ge` ማለት **እኩል ወይም የሚበልጥ** ማለት ነው\n"
                    "- `fi` የ `if` መዝጊያ ነው (`if`ን ገልብጦ ማንበብ!)"
                ),
            ),
            TutorStep(
                id="bash_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Check server status when `cpu=90`!\n\n"
                    "👇 *Type this script in the chat and send:*\n"
                    "```bash\ncpu=90\nif [ $cpu -ge 80 ]; then\n    echo \"Alert: CPU Overloaded\"\nfi\n```"
                ),
                message_am=(
                    "የሰርቨሩ ሲፒዩ `cpu=90` ሲሆን ማስጠንቀቂያ እንዲሰጥ ያድርጉ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```bash\ncpu=90\nif [ $cpu -ge 80 ]; then\n    echo \"Alert: CPU Overloaded\"\nfi\n```"
                ),
                expected_code_output="Alert: CPU Overloaded",
                hint_en='Write the if condition checking `$cpu -ge 80` and close with `fi`.',
                hint_am='`$cpu -ge 80` መሆኑን መርምረው በ `fi` በመዝጋት ይላኩ።',
                success_message_en=(
                    "🚨 *ALERT TRIGGERED!* You just wrote a real DevOps infrastructure monitoring check!"
                ),
                success_message_am=(
                    "🚨 *ማስጠንቀቂያው ሰርቷል!* እውነተኛ የሰርቨር ቁጥጥር ስክሪፕት በባሽ ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="bash_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "How do you close an `if` block in a Linux Bash script?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በሊኑክስ ባሽ ውስጥ የ `if` ትዕዛዝ ሲያበቃ በመጨረሻ ላይ ምን ተብሎ ይዘጋል?"
                ),
                options_en=[
                    "fi",
                    "endif",
                    "}",
                    "stop",
                ],
                options_am=[
                    "fi",
                    "endif",
                    "}",
                    "stop",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `fi` is `if` backwards, closing the condition!",
                success_message_am="🌟 በትክክል! `fi` የ `if` መዝጊያ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch5",
        order=5,
        title_en="Bash Ch 5: Server Loops with for",
        title_am="ሊኑክስ ባሽ ምዕራፍ 5፦ የሰርቨር ሉፖች (for Loops)",
        description_en="Learn how DevOps engineers automate tasks across multiple servers using for loops.",
        description_am="የDevOps መሐንዲሶች በበርካታ ሰርቨሮች ላይ ስራዎችን በ for ሉፕ እንዴት እንደሚያቀላጥፉ ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔄 *Batch Automation: The for Loop*\n\n"
                    "If a company has 100 servers to restart, an engineer doesn't do it manually.\n\n"
                    "In Bash, the `for` loop syntax is:\n\n"
                    "```bash\nfor server in srv1 srv2 srv3; do\n    echo \"Pinging $server\"\ndone\n```\n\n"
                    "- `do` starts the actions\n"
                    "- `done` ends the loop"
                ),
                message_am=(
                    "🔄 *ተደጋጋሚ ስራዎችን በ for ሉፕ ማቀላጠፍ*\n\n"
                    "አንድ ድርጅት 100 ሰርቨሮች ቢኖሩት፣ መሐንዲሱ በእጁ አንድ በአንድ አይከፍታቸውም።\n\n"
                    "በባሽ ውስጥ የ `for` ሉፕ አጻጻፍ፦\n\n"
                    "```bash\nfor server in srv1 srv2 srv3; do\n    echo \"Pinging $server\"\ndone\n```\n\n"
                    "- `do` ድርጊቶቹን ያስጀምራል\n"
                    "- `done` ሉፑን ያጠናቅቃል"
                ),
            ),
            TutorStep(
                id="bash_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Loop through 3 server nodes (app1, app2, app3) and print each!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```bash\nfor node in app1 app2 app3; do\n    echo \"Node: $node\"\ndone\n```"
                ),
                message_am=(
                    "በ3ቱ የሰርቨር ኖዶች (app1, app2, app3) ላይ በማሽከርከር እያንዳንዳቸውን አትሙ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```bash\nfor node in app1 app2 app3; do\n    echo \"Node: $node\"\ndone\n```"
                ),
                expected_code_output="Node: app1\nNode: app2\nNode: app3",
                hint_en='Write `for node in app1 app2 app3; do echo "Node: $node"; done`.',
                hint_am='`for node in app1 app2 app3; do echo "Node: $node"; done` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *All 3 nodes contacted!* Your automated batch deployment loop succeeded!"
                ),
                success_message_am=(
                    "🎉 *3ቱም ኖዶች ተጠርተዋል!* የተርሚናል አውቶሜሽን ሉፕዎ በሚገባ ሰርቷል!"
                ),
            ),
            TutorStep(
                id="bash_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword marks the end of a `for` loop in Bash?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በባሽ ውስጥ የ `for` ሉፕ ማብቂያ ምልክት ቃል የቱ ነው?"
                ),
                options_en=[
                    "done",
                    "end",
                    "finish",
                    "close",
                ],
                options_am=[
                    "done",
                    "end",
                    "finish",
                    "close",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `done` terminates `for` and `while` loops in Bash!",
                success_message_am="🌟 በትክክል! `done` በባሽ ውስጥ የሉፕ መዝጊያ ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch6",
        order=6,
        title_en="Bash Ch 6: Shell Functions",
        title_am="ሊኑክስ ባሽ ምዕራፍ 6፦ የተርሚናል ፈንክሽኖች (Shell Functions)",
        description_en="Learn how to bundle reusable server maintenance tasks into functions.",
        description_am="ተደጋጋሚ የሰርቨር ስራዎችን በፈንክሽን ውስጥ እንዴት እንደምናጠቃልል ይማሩ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚙️ *Reusable Scripts: Bash Functions*\n\n"
                    "In Linux administration, you can define custom commands called **Functions**:\n\n"
                    "```bash\nbackup() {\n    echo \"Starting Backup...\"\n    echo \"Backup Completed!\"\n}\n```\n\n"
                    "To run it, simply type its name: `backup`!"
                ),
                message_am=(
                    "⚙️ *እንደገና ጥቅም ላይ የሚውሉ ስክሪፕቶች፦ የባሽ ፈንክሽኖች*\n\n"
                    "በሊኑክስ አስተዳደር ውስጥ የራሳችንን ትዕዛዝ በ**ፈንክሽን** መልክ መፍጠር እንችላለን፦\n\n"
                    "```bash\nbackup() {\n    echo \"Starting Backup...\"\n    echo \"Backup Completed!\"\n}\n```\n\n"
                    "ለማስኬድ ስሙን ብቻ መጥራት በቂ ነው፦ `backup`!"
                ),
            ),
            TutorStep(
                id="bash_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a function `deploy` that prints `Code Deployed!` and call it!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    '```bash\ndeploy() {\n    echo "Code Deployed!"\n}\ndeploy\n```'
                ),
                message_am=(
                    "`deploy` የተባለ ፈንክሽን ሰርተው `Code Deployed!` እንዲያትም ጥሩት!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```bash\ndeploy() {\n    echo "Code Deployed!"\n}\ndeploy\n```'
                ),
                expected_code_output="Code Deployed!",
                hint_en='Define `deploy() { echo "Code Deployed!"; }` then invoke `deploy`.',
                hint_am='ፈንክሽኑን ከፈጠሩ በኋላ መጨረሻ ላይ `deploy` ብለው በመጥራት ይላኩ።',
                success_message_en=(
                    "🎉 *Function Executed!* Your server deployment automation ran smoothly!"
                ),
                success_message_am=(
                    "🎉 *ፈንክሽኑ ሰርቷል!* የሰርቨር አውቶሜሽን ትዕዛዝዎ በተሳካ ሁኔታ ተፈጽሟል!"
                ),
            ),
            TutorStep(
                id="bash_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "How do you call/execute a Bash function named `start_server`?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "`start_server` የተባለን የባሽ ፈንክሽን ለማስኬድ እንዴት እንጠራዋለን?"
                ),
                options_en=[
                    "start_server",
                    "call start_server()",
                    "run(start_server)",
                    "execute:start_server",
                ],
                options_am=[
                    "start_server",
                    "call start_server()",
                    "run(start_server)",
                    "execute:start_server",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! In Bash, you simply type the function name like any normal command!",
                success_message_am="🌟 በትክክል! በባሽ ውስጥ ልክ እንደማንኛውም ተራ ትዕዛዝ የስሙን ቃል ብቻ መጻፍ በቂ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="bash_ch7",
        order=7,
        title_en="Bash Ch 7: Capstone: Cloud Health Monitor",
        title_am="ሊኑክስ ባሽ ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የክላውድ ሰርቨር ጤና ተቆጣጣሪ",
        description_en="Combine variables, arithmetic, and conditions to build an automated DevOps health monitor.",
        description_am="ተለዋዋጮችን፣ ሂሳብን፣ እና ሁኔታዎችን በማጣመር እውነተኛ የክላውድ ሰርቨር ተቆጣጣሪ ይገንቡ።",
        track="bash",
        steps=[
            TutorStep(
                id="bash_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "☁️ *Bash Capstone Project: Automated Cloud Health Monitor!* 🚀\n\n"
                    "You've learned:\n"
                    "1. `echo` to output status\n"
                    "2. Shell variables and `$` expansion\n"
                    "3. `$(( ))` for shell math\n"
                    "4. `if / else` with `[ $val -ge 80 ]`\n"
                    "5. Automation with loops and functions\n\n"
                    "In this capstone, you will build an automated check that calculates used RAM percentage and reports status:\n"
                    "- `used=8`\n"
                    "- `total=10`\n"
                    "- Calculate percent: `pct=$(( (used * 100) / total ))`\n"
                    "- Print: `RAM Usage: 80%`"
                ),
                message_am=(
                    "☁️ *የባሽ ማጠቃለያ ፕሮጀክት፦ የክላውድ ሰርቨር ጤና ተቆጣጣሪ!* 🚀\n\n"
                    "እስካሁን የተማርናቸው፦\n"
                    "1. `echo` ውጤትን ለማሳየት\n"
                    "2. ተለዋዋጮች እና የ `$` ምልክት\n"
                    "3. `$(( ))` ለሂሳብ ስሌት\n"
                    "4. `if` እና `else` ለውሳኔዎች\n"
                    "5. ሉፖች እና ፈንክሽኖች\n\n"
                    "በዚህ ማጠቃለያ ፕሮጀክት የሰርቨር ራም አጠቃቀምን በመቶኛ አስልተን ሪፖርት የሚያደርግ አውቶሜሽን እንሰራለን፦\n"
                    "- ጥቅም ላይ የዋለ: `used=8`\n"
                    "- አጠቃላይ: `total=10`\n"
                    "- በመቶኛ ስሌት: `pct=$(( (used * 100) / total ))`\n"
                    "- ማሳወቅ: `RAM Usage: 80%`"
                ),
            ),
            TutorStep(
                id="bash_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete cloud RAM monitor!\n\n"
                    "👇 *Type this script in the chat and send:*\n"
                    '```bash\nused=8\ntotal=10\npct=$(( (used * 100) / total ))\necho "RAM Usage: $pct%"\n```'
                ),
                message_am=(
                    "ሙሉውን የክላውድ ሰርቨር ራም ተቆጣጣሪ ስክሪፕት ጽፈን እንላክ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    '```bash\nused=8\ntotal=10\npct=$(( (used * 100) / total ))\necho "RAM Usage: $pct%"\n```'
                ),
                expected_code_output="RAM Usage: 80%",
                hint_en='Write the RAM calculation and `echo "RAM Usage: $pct%"`.',
                hint_am='የስሌቱን ቀመር እና `echo "RAM Usage: $pct%"` ብለው ጽፈው ይላኩ።',
                success_message_en=(
                    "🎉 *SERVER REPORT GENERATED!* ☁️💻\n\n"
                    "You just built an automated DevOps monitoring script in Linux Bash!\n\n"
                    "RAM Usage calculated at 80%! You have command-line cloud engineering skills!"
                ),
                success_message_am=(
                    "🎉 *የሰርቨር ሪፖርት ወጥቷል!* ☁️💻\n\n"
                    "እውነተኛ የክላውድ ሰርቨር ተቆጣጣሪ ስክሪፕት በሊኑክስ ባሽ ገንብተዋል!\n\n"
                    "የራም አጠቃቀሙ 80% መሆኑን አረጋግጧል! አሁን የሊኑክስ ተርሚናልን ጠንቅቀው አውቀዋል!"
                ),
            ),
            TutorStep(
                id="bash_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final Linux Bash Master Question:*\n\n"
                    "What does the term 'DevOps' frequently rely on Linux Bash scripts for?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የሊኑክስ ባሽ ማጠቃለያ ጥያቄ፦*\n\n"
                    "በዘመናዊው የቴክኖሎጂ ዘርፍ (DevOps) ውስጥ የሊኑክስ ባሽ ዋነኛ ጥቅም ምንድነው?"
                ),
                options_en=[
                    "Automating cloud servers and software deployments",
                    "Designing 3D animations",
                    "Editing audio files",
                    "Drawing digital sketches",
                ],
                options_am=[
                    "የክላውድ ሰርቨሮችን እና የአፕሊኬሽን ጭነቶችን በራስ-ሰር ማቀላጠፍ (Automation)",
                    "የ3D አኒሜሽን ዲዛይን ለመስራት",
                    "የድምጽ ፋይሎችን ለማስተካከል",
                    "ስዕሎችን ለመሳል",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! You have mastered the fundamentals of Linux Bash and Shell Automation!",
                success_message_am="🏆 እጅግ ድንቅ! የሊኑክስ ባሽ (Bash) እና የተርሚናል አውቶሜሽን መሰረታዊ ነገሮችን በሚገባ አጠናቀዋል!",
            ),
        ],
    ),
]
