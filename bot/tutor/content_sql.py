"""SQL curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

# Standard seed database table for students to practice with
SQL_SEED_SCRIPT = """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    score INTEGER
);

INSERT INTO students (id, name, age, city, score) VALUES
(1, 'Abebe', 21, 'Addis Ababa', 88),
(2, 'Sara', 23, 'Hawassa', 95),
(3, 'Dawit', 20, 'Addis Ababa', 74),
(4, 'Tigist', 22, 'Bahir Dar', 91);
"""

SQL_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="sql_ch1",
        order=1,
        title_en="SQL Ch 1: Meet SQL & Reading Data (SELECT)",
        title_am="ኤስኪውኤል ምዕራፍ 1፦ ከSQL ጋር መተዋወቅ እና ዳታ ማንበብ (SELECT)",
        description_en="Discover what databases are and how to query rows using SELECT.",
        description_am="ዳታቤዝ ምን እንደሆነ እና SELECT በመጠቀም መረጃን እንዴት ማውጣት እንደሚቻል ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🗄️ *Welcome to SQL & Databases!* 📊\n\n"
                    "Almost every app in the world (Telegram, YouTube, Banks) stores its information inside a **Database**.\n\n"
                    "Think of a database like an organized digital spreadsheet with tables, rows, and columns.\n\n"
                    "To talk to a database, we use **SQL** (*Structured Query Language*).\n\n"
                    "The most important SQL command is **`SELECT`** — it means *'Computer, show me this data!'*.\n\n"
                    "The asterisk `*` means *'everything / all columns'*."
                ),
                message_am=(
                    "🗄️ *እንኳን ወደ SQL እና ዳታቤዝ (Databases) በደህና መጡ!* 📊\n\n"
                    "በዓለም ላይ ያሉ ሁሉም አፖች (ቴሌግራም፣ ዩቲዩብ፣ ባንኮች) መረጃዎቻቸውን የሚያስቀምጡት በ**ዳታቤዝ (Database)** ውስጥ ነው።\n\n"
                    "ዳታቤዝን እንደተደራጀ ዲጂታል ሰንጠረዥ (ሰንጠረዦች፣ ረድፎች እና ዓምዶች ያሉት) አድርገው ያስቡት።\n\n"
                    "ከዳታቤዝ ጋር ለመነጋገር የምንጠቀመው ቋንቋ **SQL** ይባላል።\n\n"
                    "ዋነኛው የSQL ትዕዛዝ **`SELECT`** ነው — ትርጉሙም *'ይህን መረጃ አሳየኝ!'* ማለት ነው።\n\n"
                    "ኮከብ ምልክት `*` ደግሞ *'ሁሉንም አምዶች አምጣልኝ'* ማለት ነው።"
                ),
            ),
            TutorStep(
                id="sql_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's see all students stored in our classroom database table!\n\n"
                    "👇 *Type this SQL query in the chat and send:*\n"
                    "```sql\nSELECT * FROM students;\n```"
                ),
                message_am=(
                    "በዳታቤዛችን ውስጥ ያሉትን ሁሉንም ተማሪዎች እንመልከት!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nSELECT * FROM students;\n```"
                ),
                expected_code_contains="students",
                hint_en="Type `SELECT * FROM students;` exactly as shown with a semicolon at the end.",
                hint_am="`SELECT * FROM students;` ብለው በትክክል ጽፈው ይላኩ።",
                success_message_en=(
                    "🎉 *Look at that beautiful table!* You just queried your first real database table!"
                ),
                success_message_am=(
                    "🎉 *ሰንጠረዡን አዩት!* የመጀመሪያውን የዳታቤዝ ጥያቄዎን በተሳካ ሁኔታ ፈጽመዋል!"
                ),
            ),
            TutorStep(
                id="sql_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In the SQL query `SELECT * FROM students;`, what does the `*` symbol represent?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "`SELECT * FROM students;` በሚለው ትዕዛዝ ውስጥ የ `*` ምልክት ምንን ያመለክታል?"
                ),
                options_en=[
                    "Only the first student",
                    "All columns in the table",
                    "Delete everything",
                    "Multiply by 2",
                ],
                options_am=[
                    "የመጀመሪያውን ተማሪ ብቻ",
                    "በሰንጠረዡ ውስጥ ያሉትን ሁሉንም አምዶች",
                    "ሁሉንም አጥፋ",
                    "በ2 አባዛ",
                ],
                correct_option_index=1,
                success_message_en="🌟 Spot on! `*` instructs SQL to retrieve every single column!",
                success_message_am="🌟 ትክክል! `*` ማለት በሰንጠረዡ ያሉትን አምዶች በሙሉ አምጣልኝ ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch2",
        order=2,
        title_en="SQL Ch 2: Picking Columns",
        title_am="ኤስኪውኤል ምዕራፍ 2፦ የተወሰኑ አምዶችን መምረጥ",
        description_en="Learn how to choose only specific columns instead of fetching everything.",
        description_am="ሁሉንም ከማምጣት ይልቅ የምንፈልጋቸውን አምዶች ብቻ እንዴት መምረጥ እንደምንችል ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📑 *Fetching Specific Columns*\n\n"
                    "In real applications with millions of users, asking for `SELECT *` downloads too much unnecessary data.\n\n"
                    "If you only need a person's name and city, simply list them separated by commas:\n\n"
                    "```sql\nSELECT name, city FROM students;\n```\n\n"
                    "This keeps apps fast and lightweight!"
                ),
                message_am=(
                    "📑 *የተወሰኑ አምዶችን ብቻ መምረጥ*\n\n"
                    "ሚሊዮኖች ተጠቃሚ ባላቸው ትልልቅ አፖች ውስጥ ሁሉንም አምዶች `SELECT *` ብሎ መጠየቅ ሲስተሙን ያዝገዋል፤ አላስፈላጊ ዳታም ያባክናል።\n\n"
                    "የተማሪውን ስም እና ከተማ ብቻ ከፈለጉ በኮማ በመለየት መጥራት ይችላሉ፦\n\n"
                    "```sql\nSELECT name, city FROM students;\n```\n\n"
                    "ይህ ዳታቤዙ ፈጣን እና ቀልጣፋ እንዲሆን ያደርጋል!"
                ),
            ),
            TutorStep(
                id="sql_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's fetch just the `name` and `score` of all students!\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nSELECT name, score FROM students;\n```"
                ),
                message_am=(
                    "የተማሪዎችን ስም (`name`) እና ውጤት (`score`) ብቻ እንጥራ!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nSELECT name, score FROM students;\n```"
                ),
                expected_code_contains="score",
                hint_en="Write `SELECT name, score FROM students;` exactly.",
                hint_am="`SELECT name, score FROM students;` ብለው ጽፈው ይላኩ።",
                success_message_en=(
                    "🎯 *Clean and precise!* Notice how only `name` and `score` were displayed, leaving out age and city!"
                ),
                success_message_am=(
                    "🎯 *ግሩም ስራ!* አዩት? `name` እና `score` ብቻ መጡ፤ እድሜ እና ከተማ ቀርተዋል!"
                ),
            ),
            TutorStep(
                id="sql_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "How do you request multiple columns in a SQL SELECT statement?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በSELECT ትዕዛዝ ውስጥ ከአንድ በላይ አምዶችን እንዴት እንጠይቃለን?"
                ),
                options_en=[
                    "Separate their names with commas `,`",
                    "Wrap them in brackets `[ ]`",
                    "Write a new SELECT for each column",
                    "Put an AND between them",
                ],
                options_am=[
                    "ስማቸውን በኮማ `,` በመለየት",
                    "በቅንፍ `[ ]` ውስጥ በማስገባት",
                    "ለእያንዳንዱ አምድ አዲስ SELECT በመጻፍ",
                    "በመካከላቸው AND በመጻፍ",
                ],
                correct_option_index=0,
                success_message_en="🌟 Exactly right! Commas separate multiple columns in SELECT!",
                success_message_am="🌟 በትክክል! በኮማ `,` በመለየት የምንፈልጋቸውን አምዶች መጥራት እንችላለን!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch3",
        order=3,
        title_en="SQL Ch 3: Filtering with WHERE",
        title_am="ኤስኪውኤል ምዕራፍ 3፦ በWHERE መረጃን ማጣራት",
        description_en="Learn how to filter rows using the WHERE clause and comparison conditions.",
        description_am="WHERE በመጠቀም የምንፈልገውን መስፈርት የሚያሟሉ መረጃዎችን ብቻ እንዴት ማጣራት እንደሚቻል ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔍 *Filtering with WHERE*\n\n"
                    "What if you don't want *all* students, but only students from a specific city, or students with top scores?\n\n"
                    "We use the **`WHERE`** clause!\n\n"
                    "For example, to find students with scores higher than 80:\n\n"
                    "```sql\nSELECT name, score FROM students WHERE score > 80;\n```\n\n"
                    "Only rows that match the condition are returned!"
                ),
                message_am=(
                    "🔍 *በWHERE መረጃን ማጣራት*\n\n"
                    "ሁሉንም ተማሪዎች ሳይሆን ከአንድ የተወሰነ ከተማ ያሉትን ወይም ከፍተኛ ውጤት ያስመዘገቡትን ብቻ መፈለግ ቢፈልጉስ?\n\n"
                    "**`WHERE`** የተባለውን የSQL ቃል እንጠቀማለን!\n\n"
                    "ለምሳሌ ውጤታቸው ከ80 በላይ የሆኑትን ተማሪዎች ለማግኘት፦\n\n"
                    "```sql\nSELECT name, score FROM students WHERE score > 80;\n```\n\n"
                    "መስፈርቱን የሚያሟሉት ረድፎች ብቻ ይመጣሉ!"
                ),
            ),
            TutorStep(
                id="sql_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Find all students who scored 90 or higher!\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nSELECT name, score FROM students WHERE score >= 90;\n```"
                ),
                message_am=(
                    "ውጤታቸው 90 ወይም ከዚያ በላይ የሆኑ ተማሪዎችን ያግኙ!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nSELECT name, score FROM students WHERE score >= 90;\n```"
                ),
                expected_code_contains=">=",
                hint_en="Write `SELECT name, score FROM students WHERE score >= 90;`.",
                hint_am="`SELECT name, score FROM students WHERE score >= 90;` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *Filtering master!* Notice only Sara (95) and Tigist (91) were returned!"
                ),
                success_message_am=(
                    "🎉 *አጣርተው አወጡ!* መስፈርቱን ያሟሉት ሳራ (95) እና ትዕግስት (91) ብቻ ተመርጠው ቀርበዋል!"
                ),
            ),
            TutorStep(
                id="sql_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which SQL clause is used to filter rows based on a condition?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በአንድ መስፈርት መሰረት መረጃን አጣርቶ ለማውጣት የምንጠቀመው የትኛውን የSQL ቃል ነው?"
                ),
                options_en=[
                    "WHERE",
                    "FILTER BY",
                    "SEARCH",
                    "WHEN",
                ],
                options_am=[
                    "WHERE",
                    "FILTER BY",
                    "SEARCH",
                    "WHEN",
                ],
                correct_option_index=0,
                success_message_en="🌟 Correct! `WHERE` is the universal filtering keyword in SQL!",
                success_message_am="🌟 ትክክል! `WHERE` በSQL ውስጥ መረጃን ለማጣራት የሚያገለግል ቃል ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch4",
        order=4,
        title_en="SQL Ch 4: Sorting with ORDER BY",
        title_am="ኤስኪውኤል ምዕራፍ 4፦ በORDER BY መደርደር",
        description_en="Learn how to sort database records ascending (ASC) or descending (DESC).",
        description_am="መረጃዎችን በቅደም ተከተል ከትንሽ ወደ ትልቅ (ASC) ወይም ከትልቅ ወደ ትንሽ (DESC) እንዴት መደርደር እንደሚቻል ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📶 *Sorting Data with ORDER BY*\n\n"
                    "By default, databases return data in whatever order it was added.\n\n"
                    "To sort results, we use **`ORDER BY`** followed by the column name:\n\n"
                    "- **`ASC`** (Ascending): Low to high (A to Z, 1 to 100). This is default.\n"
                    "- **`DESC`** (Descending): High to low (Z to A, 100 to 1).\n\n"
                    "For a leaderboard from highest score to lowest:\n"
                    "```sql\nSELECT name, score FROM students ORDER BY score DESC;\n```"
                ),
                message_am=(
                    "📶 *መረጃዎችን በORDER BY መደርደር*\n\n"
                    "ዳታቤዝ መረጃዎችን ሲያመጣ በተመዘገቡበት ቅደም ተከተል ነው የሚያመጣው።\n\n"
                    "በቅደም ተከተል ለመደርደር **`ORDER BY`** የሚለውን ቃል እንጠቀማለን፦\n\n"
                    "- **`ASC`**፦ ከትንሽ ወደ ትልቅ (ከሀ እስከ ፐ፣ ከ1 እስከ 100)\n"
                    "- **`DESC`**፦ ከትልቅ ወደ ትንሽ (ከ100 ወደ 1)\n\n"
                    "የከፍተኛ ውጤት ባለቤቶችን ከመጀመሪያው እስከ መጨረሻው ለመደርደር፦\n"
                    "```sql\nSELECT name, score FROM students ORDER BY score DESC;\n```"
                ),
            ),
            TutorStep(
                id="sql_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's see our student leaderboard sorted with highest scores at the top!\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nSELECT name, score FROM students ORDER BY score DESC;\n```"
                ),
                message_am=(
                    "የተማሪዎችን ውጤት ከከፍተኛ ወደ ዝቅተኛ ደርድረን እንመልከት!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nSELECT name, score FROM students ORDER BY score DESC;\n```"
                ),
                expected_code_contains="ORDER BY",
                hint_en="Write `SELECT name, score FROM students ORDER BY score DESC;`.",
                hint_am="`SELECT name, score FROM students ORDER BY score DESC;` ብለው ይጻፉ።",
                success_message_en=(
                    "🏆 *Leaderboard sorted!* Sara (95) is #1, Tigist (91) is #2, Abebe (88) is #3, and Dawit (74) is #4!"
                ),
                success_message_am=(
                    "🏆 *በደረጃ ተደረደሩ!* ሳራ (95) 1ኛ፣ ትዕግስት (91) 2ኛ፣ አበበ (88) 3ኛ፣ እና ዳዊት (74) 4ኛ ሆነው ተቀምጠዋል!"
                ),
            ),
            TutorStep(
                id="sql_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which keyword makes `ORDER BY` sort from highest to lowest?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "በ `ORDER BY` ጊዜ ከከፍተኛ ወደ ዝቅተኛ ለመደርደር የትኛውን ቃል እንጠቀማለን?"
                ),
                options_en=[
                    "DESC",
                    "DOWN",
                    "HIGH",
                    "ASC",
                ],
                options_am=[
                    "DESC",
                    "DOWN",
                    "HIGH",
                    "ASC",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! `DESC` stands for Descending (highest first)!",
                success_message_am="🌟 ትክክል! `DESC` ማለት Descending (ከትልቅ ወደ ትንሽ) ማለት ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch5",
        order=5,
        title_en="SQL Ch 5: Inserting New Data (INSERT INTO)",
        title_am="ኤስኪውኤል ምዕራፍ 5፦ አዲስ መረጃ መመዝገብ (INSERT INTO)",
        description_en="Learn how new user accounts or records are added to tables using INSERT INTO.",
        description_am="INSERT INTO በመጠቀም አዲስ ተጠቃሚ ወይም መረጃ ወደ ሰንጠረዥ እንዴት እንደሚገባ ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "✍️ *Adding Records with INSERT INTO*\n\n"
                    "When a new person signs up for an app, the app runs an **`INSERT INTO`** command to store them!\n\n"
                    "Syntax:\n"
                    "```sql\nINSERT INTO table_name (column1, column2)\nVALUES ('Value1', 123);\n```\n\n"
                    "Notice:\n"
                    "- Text values use single quotes `'...'`\n"
                    "- Numbers do not need quotes!"
                ),
                message_am=(
                    "✍️ *በINSERT INTO አዲስ መረጃ መመዝገብ*\n\n"
                    "አንድ አዲስ ተጠቃሚ በአንድ አፕ ላይ አካውንት ሲከፍት፣ አፑ መረጃውን ለማስቀመጥ **`INSERT INTO`** የሚለውን ትዕዛዝ ይጠቀማል!\n\n"
                    "አጻጻፉ፦\n"
                    "```sql\nINSERT INTO ሰንጠረዥ (አምድ1, አምድ2)\nVALUES ('እሴት1', 123);\n```\n\n"
                    "ልብ ይበሉ፦\n"
                    "- ጽሁፎች በአንድ ነጠላ ጥቅስ `'...'` ውስጥ ይቀመጣሉ\n"
                    "- ቁጥሮች ጥቅስ አያስፈልጋቸውም!"
                ),
            ),
            TutorStep(
                id="sql_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's register a new student named 'Hanan', age 21, city 'Gondar', score 93!\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nINSERT INTO students (name, age, city, score) VALUES ('Hanan', 21, 'Gondar', 93);\n```"
                ),
                message_am=(
                    "ሀናን የተባለች አዲስ ተማሪ እንመዝግብ (ስም: Hanan, እድሜ: 21, ከተማ: Gondar, ውጤት: 93)!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nINSERT INTO students (name, age, city, score) VALUES ('Hanan', 21, 'Gondar', 93);\n```"
                ),
                expected_code_contains="INSERT INTO",
                hint_en="Write `INSERT INTO students (name, age, city, score) VALUES ('Hanan', 21, 'Gondar', 93);`.",
                hint_am="`INSERT INTO students (name, age, city, score) VALUES ('Hanan', 21, 'Gondar', 93);` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *New student inserted!* Hanan has officially been saved into the database!"
                ),
                success_message_am=(
                    "🎉 *አዲስ ተማሪ ተመዘገበች!* የሀናን መረጃ በዳታቤዙ ውስጥ በሚገባ ተቀምጧል!"
                ),
            ),
            TutorStep(
                id="sql_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which SQL statement is used to add brand new rows to a database table?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "አዲስ ረድፍ መረጃ ወደ ሰንጠረዥ ለማስገባት የምንጠቀመው የትኛውን ትዕዛዝ ነው?"
                ),
                options_en=[
                    "INSERT INTO",
                    "ADD RECORD",
                    "APPEND TO",
                    "CREATE ROW",
                ],
                options_am=[
                    "INSERT INTO",
                    "ADD RECORD",
                    "APPEND TO",
                    "CREATE ROW",
                ],
                correct_option_index=0,
                success_message_en="🌟 Correct! `INSERT INTO` is how databases store new records!",
                success_message_am="🌟 ትክክል! አዲስ መረጃ ወደ ሰንጠረዥ ለማስገባት `INSERT INTO` እንጠቀማለን!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch6",
        order=6,
        title_en="SQL Ch 6: Updating & Deleting (UPDATE & DELETE)",
        title_am="ኤስኪውኤል ምዕራፍ 6፦ መረጃን ማስተካከል እና ማጥፋት (UPDATE & DELETE)",
        description_en="Learn how to modify existing records with UPDATE and remove records with DELETE.",
        description_am="UPDATE በመጠቀም መረጃን እንዴት ማስተካከል እና DELETE በመጠቀም እንዴት መሰረዝ እንደሚቻል ይማሩ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🛠️ *Updating & Deleting Records*\n\n"
                    "People change passwords, update profile pictures, and close accounts.\n\n"
                    "1. **`UPDATE`**: Modifies existing data.\n"
                    "```sql\nUPDATE students SET score = 99 WHERE name = 'Sara';\n```\n\n"
                    "2. **`DELETE`**: Removes records.\n"
                    "```sql\nDELETE FROM students WHERE name = 'Dawit';\n```\n\n"
                    "⚠️ *CRITICAL RULE*: Always include `WHERE`! Without `WHERE`, you will accidentally update or delete EVERY ROW in the entire table!"
                ),
                message_am=(
                    "🛠️ *መረጃን ማስተካከል እና ማጥፋት*\n\n"
                    "ሰዎች የይለፍ ቃላቸውን ይቀይራሉ፣ መረጃቸውን ያሻሽላሉ፣ አንዳንዴም አካውንታቸውን ይሰርዛሉ።\n\n"
                    "1. **`UPDATE`**፦ ያለን መረጃ ለማስተካከል\n"
                    "```sql\nUPDATE students SET score = 99 WHERE name = 'Sara';\n```\n\n"
                    "2. **`DELETE`**፦ መረጃን ለማጥፋት\n"
                    "```sql\nDELETE FROM students WHERE name = 'Dawit';\n```\n\n"
                    "⚠️ *እጅግ ወሳኝ ማስጠንቀቂያ*፦ ሁልጊዜም `WHERE` መጠቀምዎን አይርሱ! `WHERE` ከሌለ የሰንጠረዡን መረጃ በሙሉ በስህተት ያጠፉታል ወይም ይቀይሩታል!"
                ),
            ),
            TutorStep(
                id="sql_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Abebe retook his test and scored 100! Update his score in the database.\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nUPDATE students SET score = 100 WHERE name = 'Abebe';\n```"
                ),
                message_am=(
                    "አበበ ፈተናውን በድጋሚ ወስዶ 100 አገኘ! ውጤቱን በዳታቤዙ ውስጥ አስተካክሉ (Update አድርጉ)።\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nUPDATE students SET score = 100 WHERE name = 'Abebe';\n```"
                ),
                expected_code_contains="UPDATE",
                hint_en="Write `UPDATE students SET score = 100 WHERE name = 'Abebe';`.",
                hint_am="`UPDATE students SET score = 100 WHERE name = 'Abebe';` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *Score updated!* Abebe's record is now updated to 100!"
                ),
                success_message_am=(
                    "🎉 *ውጤቱ ተስተካክሏል!* የአበበ ውጤት ወደ 100 ተቀይሯል!"
                ),
            ),
            TutorStep(
                id="sql_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What happens if you run `DELETE FROM students;` without a `WHERE` clause?"
                ),
                message_am=(
                    "🧠 *የግንዛቤ ማረጋገጫ ጥያቄ፦*\n\n"
                    "`DELETE FROM students;` ብለው `WHERE` ሳይጠቀሙ ብትጽፉ ምን ይከሰታል?"
                ),
                options_en=[
                    "It will delete every single student in the table!",
                    "It will only delete the last student",
                    "SQL will show an error and do nothing",
                    "It will delete the database file",
                ],
                options_am=[
                    "በሰንጠረዡ ውስጥ ያሉትን ተማሪዎች በሙሉ ያጠፋቸዋል!",
                    "የመጨረሻውን ተማሪ ብቻ ያጠፋል",
                    "SQL ስህተት አሳይቶ ምንም አያደርግም",
                    "የዳታቤዝ ፋይሉን ያጠፋል",
                ],
                correct_option_index=0,
                success_message_en="🌟 Spot on! Without `WHERE`, DELETE clears out the entire table!",
                success_message_am="🌟 በትክክል! `WHERE` ከሌለ ሙሉ ሰንጠረዡ ባዶ ሆኖ ይጠፋል፤ ስለዚህ ጥንቃቄ ማድረግ ያስፈልጋል!",
            ),
        ],
    ),
    TutorChapter(
        id="sql_ch7",
        order=7,
        title_en="SQL Ch 7: Capstone Project: School Analytics System",
        title_am="ኤስኪውኤል ምዕራፍ 7፦ ማጠቃለያ ፕሮጀክት፦ የትምህርት ቤት ዳታ አናሊቲክስ",
        description_en="Combine SELECT, WHERE, and ORDER BY to build a real school honor roll report.",
        description_am="SELECT, WHERE, እና ORDER BY በማጣመር እውነተኛ የደረጃ ተማሪዎች ሪፖርት አውጡ።",
        track="sql",
        steps=[
            TutorStep(
                id="sql_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓 *SQL Capstone Project: School Honor Roll Report!* 🏆\n\n"
                    "You've learned:\n"
                    "1. `SELECT` to read data\n"
                    "2. Picking specific columns (`name, score`)\n"
                    "3. `WHERE` to filter high achievers\n"
                    "4. `ORDER BY` to rank them from #1 downwards\n"
                    "5. `INSERT` & `UPDATE` to modify records\n\n"
                    "Now, the school principal needs an **Honor Roll Report**!\n"
                    "They need only the **name** and **score** of students with score **>= 85**, ordered with the highest scores on top!"
                ),
                message_am=(
                    "🎓 *የSQL ማጠቃለያ ፕሮጀክት፦ የደረጃ ተማሪዎች ሪፖርት!* 🏆\n\n"
                    "እስካሁን የተማርናቸው፦\n"
                    "1. `SELECT` መረጃን ለማውጣት\n"
                    "2. የተወሰኑ አምዶችን መምረጥ (`name, score`)\n"
                    "3. `WHERE` ከፍተኛ ውጤት ያመጡትን ለማጣራት\n"
                    "4. `ORDER BY` ከ1ኛ ጀምሮ ለመደርደር\n"
                    "5. `INSERT` እና `UPDATE` አዲስ መረጃ ለማስገባት እና ለማስተካከል\n\n"
                    "አሁን የትምህርት ቤቱ ርዕሰ መምህር የደረጃ ተማሪዎችን ሪፖርት ፈልገዋል!\n"
                    "የሚፈልጉት ውጤታቸው **>= 85** የሆኑትን ተማሪዎች **ስም (name)** እና **ውጤት (score)** ብቻ ሲሆን፣ ከከፍተኛ ወደ ዝቅተኛ መደርደር አለበት!"
                ),
            ),
            TutorStep(
                id="sql_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write the complete Honor Roll analytics query!\n\n"
                    "👇 *Type this query and send:*\n"
                    "```sql\nSELECT name, score FROM students WHERE score >= 85 ORDER BY score DESC;\n```"
                ),
                message_am=(
                    "ሙሉውን የደረጃ ተማሪዎች ሪፖርት ጥያቄ አዘጋጅተን እንላክ!\n\n"
                    "👇 *ይህንን የSQL ትዕዛዝ ጽፈው ይላኩ፦*\n"
                    "```sql\nSELECT name, score FROM students WHERE score >= 85 ORDER BY score DESC;\n```"
                ),
                expected_code_contains="ORDER BY score DESC",
                hint_en="Write `SELECT name, score FROM students WHERE score >= 85 ORDER BY score DESC;`.",
                hint_am="`SELECT name, score FROM students WHERE score >= 85 ORDER BY score DESC;` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *MAGNIFICENT WORK!* 🎓\n\n"
                    "You just produced a professional database analytics report!\n\n"
                    "Sara (95) and Tigist (91) are on the Honor Roll! You now have a solid command of SQL databases!"
                ),
                success_message_am=(
                    "🎉 *ድንቅ ስራ!* 🎓\n\n"
                    "ትክክለኛ እና ሙያዊ የሆነ የዳታቤዝ ሪፖርት አውጥተዋል!\n\n"
                    "ሳራ (95) እና ትዕግስት (91) የደረጃ ተማሪዎች ሆነው ወጥተዋል! አሁን የSQL ዳታቤዝን ጠንቅቀው አውቀዋል!"
                ),
            ),
            TutorStep(
                id="sql_ch7_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Final SQL Master Question:*\n\n"
                    "In a complete SQL query, what is the correct order of clauses?"
                ),
                message_am=(
                    "🧠 *የመጨረሻው የSQL ማጠቃለያ ጥያቄ፦*\n\n"
                    "በአንድ ሙሉ የSQL ጥያቄ ውስጥ ትክክለኛው የቃላት ቅደም ተከተል የትኛው ነው?"
                ),
                options_en=[
                    "SELECT ... FROM ... WHERE ... ORDER BY ...",
                    "ORDER BY ... SELECT ... WHERE ... FROM ...",
                    "WHERE ... FROM ... SELECT ... ORDER BY ...",
                    "FROM ... WHERE ... ORDER BY ... SELECT ...",
                ],
                options_am=[
                    "SELECT ... FROM ... WHERE ... ORDER BY ...",
                    "ORDER BY ... SELECT ... WHERE ... FROM ...",
                    "WHERE ... FROM ... SELECT ... ORDER BY ...",
                    "FROM ... WHERE ... ORDER BY ... SELECT ...",
                ],
                correct_option_index=0,
                success_message_en="🏆 OUTSTANDING! You have mastered the fundamentals of SQL databases!",
                success_message_am="🏆 እጅግ ድንቅ! የSQL ዳታቤዝ መሰረታዊ ነገሮችን በሚገባ አጠናቀዋል!",
            ),
        ],
    ),
]
