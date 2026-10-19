"""HTML curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

HTML_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="html_ch1",
        order=1,
        title_en="HTML Ch 1: Meet HTML & Your First Web Heading",
        title_am="ኤችቲኤምኤል ምዕራፍ 1፦ ከHTML ጋር መተዋወቅ እና የመጀመሪያ አርዕስት",
        description_en="Learn how HTML builds the skeleton of every website on the Internet.",
        description_am="HTML በኢንተርኔት ላይ ያሉ ድህረ-ገጾችን መዋቅር እንዴት እንደሚገነባ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📄 *Welcome to HTML!* 🌐\n\n"
                    "HTML stands for **HyperText Markup Language**.\n\n"
                    "It is NOT a math programming language like Python—it is a **structure language**! "
                    "HTML is the skeleton of every webpage in the world, from Google to YouTube.\n\n"
                    "HTML uses **Tags** wrapped in angle brackets `< >`. Most tags come in pairs:\n"
                    "• Opening tag: `<h1>`\n"
                    "• Closing tag: `</h1>` (notice the slash `/`!)\n\n"
                    "Ready to build your very first web title?"
                ),
                message_am=(
                    "📄 *እንኳን ወደ HTML በደህና መጡ!* 🌐\n\n"
                    "HTML ማለት **HyperText Markup Language** ማለት ነው።\n\n"
                    "እንደ ፓይተን የሂሳብ ቋንቋ ሳይሆን፣ **የመዋቅር (Structure) ቋንቋ** ነው! "
                    "ከጉግል እስከ ዩቲዩብ ድረስ በዓለም ላይ ያሉ ድህረ-ገጾች በሙሉ አጥንታቸው የተገነባው በHTML ነው።\n\n"
                    "HTML በ `< >` ቅንፍ ውስጥ የሚገቡ **ታጎችን (Tags)** ይጠቀማል። አብዛኞቹ ታጎች በጥንድ ይመጣሉ፦\n"
                    "• መክፈቻ ታግ፦ `<h1>`\n"
                    "• መዝጊያ ታግ፦ `</h1>` (የስላሽ `/` ምልክቷን ልብ ይበሉ!)\n\n"
                    "የመጀመሪያውን የድህረ-ገጽ አርዕስት ለመስራት ዝግጁ ነዎት?"
                ),
            ),
            TutorStep(
                id="html_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "The `<h1>` tag creates the biggest, boldest heading on a page!\n\n"
                    "👇 *Type this exact code in the chat and send:*\n"
                    "```html\n<h1>Welcome to My Website</h1>\n```"
                ),
                message_am=(
                    "የ `<h1>` ታግ በድህረ-ገጽ ላይ ትልቁን እና ጎላ ያለውን ዋና አርዕስት ይፈጥራል!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<h1>Welcome to My Website</h1>\n```"
                ),
                expected_code_output="# Welcome to My Website",
                hint_en="Start with `<h1>`, write the text, and close with `</h1>`!",
                hint_am="በ `<h1>` ይጀምሩ፣ ጽሁፉን ጽፈው በ `</h1>` ይዝጉት!",
                success_message_en=(
                    "🎉 *Look at that web heading!* You just created your first HTML element!"
                ),
                success_message_am=(
                    "🎉 *የድህረ-ገጽ አርዕስትዎ ወጥቷል!* የመጀመሪያውን የHTML ኤለመንት በተሳካ ሁኔታ ፈጥረዋል!"
                ),
            ),
            TutorStep(
                id="html_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "What makes a closing tag different from an opening tag in HTML?"
                ),
                message_am=(
                    "በHTML ውስጥ መዝጊያ ታግ ከመክፈቻ ታግ በምን ይለያል?"
                ),
                options_en=[
                    "It has a forward slash like </h1> 🛑",
                    "It is written in all capital letters",
                    "Closing tags do not exist in HTML",
                ],
                options_am=[
                    "የፊት ስላሽ ምልክት አለው እንደ </h1> 🛑",
                    "በትልልቅ ፊደላት ይጻፋል",
                    "በHTML ውስጥ መዝጊያ ታግ የሚባል ነገር የለም",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* The forward slash `/` tells the browser: *\"The heading ends here!\"*",
                success_message_am="🎯 *ትክክል ነው!* የስላሽ `/` ምልክት ለብራውዘሩ *\"አርዕስቱ እዚህ ጋር አብቅቷል!\"* ብሎ ይነግረዋል።",
            ),
            TutorStep(
                id="html_ch1_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You completed HTML Chapter 1!* 🎓\n\n"
                    "You learned:\n"
                    "1. HTML gives structure to the entire Web.\n"
                    "2. Tags come in pairs: `<tag>` and `</tag>`.\n"
                    "3. `<h1>` creates the main page title.\n\n"
                    "Ready to add paragraphs and text in Chapter 2?"
                ),
                message_am=(
                    "🏆 *የHTML ምዕራፍ 1ን አጠናቀዋል!* 🎓\n\n"
                    "ምን ተማሩ?፦\n"
                    "1. HTML ለድህረ-ገጾች መዋቅር ይሰጣል።\n"
                    "2. ታጎች በጥንድ ይመጣሉ፦ `<tag>` እና `</tag>`።\n"
                    "3. `<h1>` ዋናውን የገጽ አርዕስት ይፈጥራል።\n\n"
                    "በምዕራፍ 2 አንቀጾችን (Paragraphs) ለመጻፍ ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch2",
        order=2,
        title_en="HTML Ch 2: Paragraphs & Text Formatting",
        title_am="ኤችቲኤምኤል ምዕራፍ 2፦ አንቀጾች እና የጽሁፍ ቅርጾች",
        description_en="Learn how the p tag writes body text and how b makes text bold.",
        description_am="የ `p` ታግ ጽሁፎችን እንዴት እንደሚጽፍ እና `b` ጽሁፍን እንዴት እንደሚያደምቅ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📝 *Paragraphs with `<p>`*\n\n"
                    "When you read articles on the web, every regular paragraph of text is wrapped "
                    "in a `<p>` tag:\n"
                    "```html\n<p>This is a paragraph.</p>\n```\n"
                    "Browsers automatically add clean spacing above and below every `<p>`."
                ),
                message_am=(
                    "📝 *አንቀጾች በ `<p>`*\n\n"
                    "በድህረ-ገጽ ላይ የምናነባቸው ማብራሪያዎች እና ጽሁፎች በሙሉ በ `<p>` (Paragraph) ታግ ውስጥ ይቀመጣሉ፦\n"
                    "```html\n<p>ይህ አንቀጽ ነው።</p>\n```\n"
                    "ብራውዘሮች በየአንቀጹ መሃል ተገቢውን ክፍተት ራሳቸው ያስተካክላሉ።"
                ),
            ),
            TutorStep(
                id="html_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's combine a heading `<h2>` and a paragraph `<p>`!\n\n"
                    "👇 *Type both lines in one message and send:*\n"
                    "```html\n<h2>About Me</h2>\n<p>I am learning to code!</p>\n```"
                ),
                message_am=(
                    "ንዑስ አርዕስት `<h2>` እና አንቀጽ `<p>`ን አጣምረን እንስራ!\n\n"
                    "👇 *ሁለቱንም መስመሮች በአንድ መልእክት ጽፈው ይላኩ፦*\n"
                    "```html\n<h2>About Me</h2>\n<p>I am learning to code!</p>\n```"
                ),
                expected_code_output="## About Me\nI am learning to code!",
                hint_en='Line 1: `<h2>About Me</h2>`\nLine 2: `<p>I am learning to code!</p>`',
                hint_am='መስመር 1፦ `<h2>About Me</h2>`\nመስመር 2፦ `<p>I am learning to code!</p>`',
                success_message_en=(
                    "🎉 *Look at that page structure!* A heading followed by styled body text!"
                ),
                success_message_am=(
                    "🎉 *የገጹ አቀማመጥ ተስተካክሏል!* ንዑስ አርዕስት እና ተከታይ ጽሁፍ በአግባቡ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="html_ch2_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Paragraphs!* 🎓\n\n"
                    "Now you can write articles, descriptions, and blog posts.\n\n"
                    "Ready to make clickable links with `<a>` in Chapter 3?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 2ን (አንቀጾችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን ጽሁፎችን እና መግለጫዎችን በድህረ-ገጽ ላይ ማዘጋጀት ይችላሉ።\n\n"
                    "በምዕራፍ 3 ተጫነው ወደ ሌላ ቦታ የሚወስዱ ሊንኮችን (Links) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch3",
        order=3,
        title_en="HTML Ch 3: Clickable Links (The Web's Superpower)",
        title_am="ኤችቲኤምኤል ምዕራፍ 3፦ ሊንኮች (የድህረ-ገጽ ዋነኛ ሀይል)",
        description_en="Learn how the anchor tag a connects the entire World Wide Web together.",
        description_am="የ `a` ታግ ዓለም አቀፉን ድህረ-ገጽ እርስ በርስ እንዴት እንደሚያገናኝ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔗 *Links: The Anchor Tag `<a>`*\n\n"
                    "Why is it called the \"Web\"? Because every page is linked to other pages!\n\n"
                    "To create a link, we use the `<a>` tag with an **attribute** named `href`:\n"
                    "```html\n<a href=\"https://google.com\">Search Google</a>\n```\n"
                    "• `href` tells the browser WHERE to go.\n"
                    "• The text inside is what the user clicks!"
                ),
                message_am=(
                    "🔗 *ሊንኮች፦ የ `<a>` ታግ*\n\n"
                    "የዓለም ድር (Web) የተባለው ገጾች በሙሉ እርስ በርስ ስለሚገናኙ ነው!\n\n"
                    "ሊንክ ለመፍጠር የ `<a>` ታግን ከ `href` አድራሻ ጋር እንጠቀማለን፦\n"
                    "```html\n<a href=\"https://google.com\">Search Google</a>\n```\n"
                    "• `href` ወዴት ገጽ መሄድ እንዳለበት ይነግራል\n"
                    "• መሃል ላይ ያለው ጽሁፍ ተጠቃሚው የሚጫነው ቃል ነው!"
                ),
            ),
            TutorStep(
                id="html_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write a clickable link to Python's website!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```html\n<a href=\"https://python.org\">Learn Python</a>\n```"
                ),
                message_am=(
                    "ወደ ፓይተን ገጽ የሚወስድ ሊንክ እንስራ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<a href=\"https://python.org\">Learn Python</a>\n```"
                ),
                expected_code_output="Learn Python",
                hint_en='Write `<a href="https://python.org">Learn Python</a>`',
                hint_am='`<a href="https://python.org">Learn Python</a>` ብለው ይጻፉ',
                success_message_en=(
                    "🌐 *CLICKABLE!* When placed in a browser, clicking 'Learn Python' navigates straight there!"
                ),
                success_message_am=(
                    "🌐 *ሊንኩ ሰርቷል!* በብራውዘር ውስጥ 'Learn Python'ን ሲጫኑ በቀጥታ ወደ ገጹ ይወስዳል!"
                ),
            ),
            TutorStep(
                id="html_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "What attribute specifies the URL destination inside an `<a>` tag?"
                ),
                message_am=(
                    "በ `<a>` ታግ ውስጥ የገጹን አድራሻ (URL) ለመግለጽ የምንጠቀመው የትኛውን ባህሪ (Attribute) ነው?"
                ),
                options_en=[
                    "href 🔗",
                    "src",
                    "goto",
                ],
                options_am=[
                    "href 🔗",
                    "src",
                    "goto",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* `href` stands for Hypertext Reference.",
                success_message_am="🎯 *ትክክል ነው!* `href` (Hypertext Reference) የሊንኩ መድረሻ አድራሻ ነው።",
            ),
            TutorStep(
                id="html_ch3_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Links!* 🎓\n\n"
                    "You know the secret that connects all 2 billion websites together.\n\n"
                    "Ready to learn how to organize items with Lists in Chapter 4?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 3ን (ሊንኮችን) አጠናቀዋል!* 🎓\n\n"
                    "ሁሉንም ድህረ-ገጾች እርስ በርስ የሚያገናኘውን ሚስጥር አውቀዋል።\n\n"
                    "በምዕራፍ 4 ዝርዝሮችን (Lists) በHTML ለማደራጀት ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch4",
        order=4,
        title_en="HTML Ch 4: Bulleted & Numbered Lists",
        title_am="ኤችቲኤምኤል ምዕራፍ 4፦ ነጥብ ያላቸው እና ቁጥር ያላቸው ዝርዝሮች",
        description_en="Learn how ul and li build navigation menus, feature lists, and recipe ingredients.",
        description_am="`ul` እና `li` የሜኑ ዝርዝሮችን እና ማውጫዎችን እንዴት እንደሚገነቡ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📋 *Lists in HTML: `<ul>` and `<li>`*\n\n"
                    "Whenever you see bullet points on a webpage or a top navigation bar, "
                    "it is an **Unordered List** (`<ul>`) containing **List Items** (`<li>`):\n"
                    "```html\n<ul>\n  <li>Apple</li>\n  <li>Banana</li>\n</ul>\n```\n"
                    "• `<ul>` creates the list container.\n"
                    "• Each `<li>` is one bullet point!"
                ),
                message_am=(
                    "📋 *ዝርዝሮች በHTML፦ `<ul>` እና `<li>`*\n\n"
                    "በድህረ-ገጾች ላይ የምናያቸው የነጥብ ዝርዝሮች ወይም የላይኛው ሜኑ በ `<ul>` እና በ `<li>` ይሰራሉ፦\n"
                    "```html\n<ul>\n  <li>Apple</li>\n  <li>Banana</li>\n</ul>\n```\n"
                    "• `<ul>` የዝርዝሩ መያዣ ሳጥን ነው\n"
                    "• እያንዳንዱ `<li>` (List Item) አንድ ነጥብ ነው!"
                ),
            ),
            TutorStep(
                id="html_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create a list of your 2 favorite coding languages!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```html\n<ul>\n  <li>Python</li>\n  <li>HTML</li>\n</ul>\n```"
                ),
                message_am=(
                    "የምንማራቸውን 2 የኮዲንግ ቋንቋዎች በዝርዝር እናስቀምጥ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<ul>\n  <li>Python</li>\n  <li>HTML</li>\n</ul>\n```"
                ),
                expected_code_output="• Python\n• HTML",
                hint_en='Open `<ul>`, put two `<li>` items, and close with `</ul>`!',
                hint_am='በ `<ul>` ይክፈቱ፣ ሁለት `<li>` አስገብተው በ `</ul>` ይዝጉ!',
                success_message_en=(
                    "🎉 *Look at those clean bullet points!* You created a structured HTML list!"
                ),
                success_message_am=(
                    "🎉 *የነጥብ ዝርዝርዎ በሚገባ ወጥቷል!* የተዋቀረ የHTML ዝርዝር ሰርተዋል!"
                ),
            ),
            TutorStep(
                id="html_ch4_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Lists!* 🎓\n\n"
                    "Every website navbar, dropdown menu, and settings list uses this structure.\n\n"
                    "Ready to add interactive clickable Buttons in Chapter 5?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 4ን (ዝርዝሮችን) አጠናቀዋል!* 🎓\n\n"
                    "የድህረ-ገጾች ሜኑ እና ማውጫ በሙሉ በዚህ መዋቅር ይሰራል።\n\n"
                    "በምዕራፍ 5 ተጫነው የሚሰሩ አዝራሮችን (Buttons) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch5",
        order=5,
        title_en="HTML Ch 5: Interactive Buttons & Form Inputs",
        title_am="ኤችቲኤምኤል ምዕራፍ 5፦ አዝራሮች (Buttons) እና መጻፊያ ሳጥኖች",
        description_en="Learn how button and input create login forms and interactive web controls.",
        description_am="`button` እና `input` የመግቢያ ፎርሞችን እና አዝራሮችን እንዴት እንደሚፈጥሩ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔘 *Interactive Buttons: `<button>`*\n\n"
                    "A website isn't just for reading—users want to interact!\n\n"
                    "The `<button>` tag creates a real, clickable button that users can press:\n"
                    "```html\n<button>Submit Application</button>\n```\n"
                    "When paired with JavaScript, pressing this button can send data, play sounds, or submit forms!"
                ),
                message_am=(
                    "🔘 *አዝራሮች፦ የ `<button>` ታግ*\n\n"
                    "ድህረ-ገጽ ለንባብ ብቻ ሳይሆን ሰዎች ተጭነው የሚጠቀሙበት ነው!\n\n"
                    "የ `<button>` ታግ ተጠቃሚዎች የሚጫኑትን እውነተኛ አዝራር ይፈጥራል፦\n"
                    "```html\n<button>አመልክት</button>\n```\n"
                    "ይህ አዝራር ከጃቫስክሪፕት ጋር ሲጣመር መልእክት ይልካል፣ ድምጽ ያሰማል፣ ወይም ፎርም ያስገባል!"
                ),
            ),
            TutorStep(
                id="html_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create an interactive Sign Up button!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```html\n<button>Sign Up Now</button>\n```"
                ),
                message_am=(
                    "የመመዝገቢያ አዝራር እንፍጠር!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<button>Sign Up Now</button>\n```"
                ),
                expected_code_output="[Button: Sign Up Now]",
                hint_en='Write `<button>Sign Up Now</button>` with open and closing tags!',
                hint_am='`<button>Sign Up Now</button>` ብለው ይጻፉ!',
                success_message_en=(
                    "🎉 *Look at that button!* You now know how call-to-action buttons are made!"
                ),
                success_message_am=(
                    "🎉 *አዝራሩ ተፈጥሯል!* በድህረ-ገጾች ላይ ያሉ አዝራሮች እንዴት እንደሚሰሩ አውቀዋል!"
                ),
            ),
            TutorStep(
                id="html_ch5_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Buttons!* 🎓\n\n"
                    "Now you can create action elements for any app or site.\n\n"
                    "Ready to learn how to add Images and media in Chapter 6?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 5ን (አዝራሮችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን ለማንኛውም ገጽ አዝራሮችን መፍጠር ይችላሉ።\n\n"
                    "በምዕራፍ 6 ፎቶዎችን (Images) በድህረ-ገጽ ላይ ማካተት ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch6",
        order=6,
        title_en="HTML Ch 6: Adding Images to Websites",
        title_am="ኤችቲኤምኤል ምዕራፍ 6፦ ፎቶዎችን በድህረ-ገጽ ላይ ማካተት",
        description_en="Learn how the self-closing img tag displays photos, logos, and illustrations.",
        description_am="የ `img` ታግ ፎቶዎችን፣ ሎጎዎችን እና ስዕሎችን እንዴት እንደሚያሳይ ይማሩ።",
        track="html",
        steps=[
            TutorStep(
                id="html_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🖼️ *Images with `<img>`*\n\n"
                    "Unlike headings or paragraphs, images do NOT wrap text—they are **self-closing**!\n\n"
                    "To show a photo, we use two key attributes:\n"
                    "• `src`: The source location/URL of the image file.\n"
                    "• `alt`: A short description for people with screen readers or slow internet.\n\n"
                    "```html\n<img src=\"profile.jpg\" alt=\"My Profile Photo\">\n```"
                ),
                message_am=(
                    "🖼️ *ፎቶዎች በ `<img>`*\n\n"
                    "ከአርዕስት ወይም አንቀጽ በተለየ፣ ፎቶዎች መሃላቸው ጽሁፍ ስለማይገባ **ራሳቸውን የሚዘጉ (Self-closing)** ናቸው!\n\n"
                    "ፎቶ ለማሳየት ሁለት ዋና ባህሪያትን እንጠቀማለን፦\n"
                    "• `src`፦ የፎቶው መገኛ አድራሻ (Source)\n"
                    "• `alt`፦ ፎቶው ካልከፈተ የሚነበብ አጭር መግለጫ\n\n"
                    "```html\n<img src=\"profile.jpg\" alt=\"የእኔ ፎቶ\">\n```"
                ),
            ),
            TutorStep(
                id="html_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write an image tag for a website logo!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```html\n<img src=\"logo.png\" alt=\"CodeBuddy Logo\">\n```"
                ),
                message_am=(
                    "ለድረገጽ ሎጎ የሚሆን የፎቶ ታግ እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<img src=\"logo.png\" alt=\"CodeBuddy Logo\">\n```"
                ),
                expected_code_output="[Image: CodeBuddy Logo]",
                hint_en='Write `<img src="logo.png" alt="CodeBuddy Logo">` (no closing tag needed!)',
                hint_am='`<img src="logo.png" alt="CodeBuddy Logo">` ብለው ይጻፉ (መዝጊያ ታግ አያስፈልገውም!)',
                success_message_en=(
                    "🌟 *PERFECT!* The image tag tells the browser to load the image and display the description!"
                ),
                success_message_am=(
                    "🌟 *በጣም ትክክል!* የፎቶ ታጉ ብራውዘሩ ምስሉን አውጥቶ እንዲያሳይ ያዘዋል!"
                ),
            ),
            TutorStep(
                id="html_ch6_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Images!* 🎓\n\n"
                    "Now you know Headings, Paragraphs, Links, Lists, Buttons, and Images.\n\n"
                    "Ready for the grand finale: Chapter 7 Capstone Project — Building a complete Profile Webpage?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 6ን (ፎቶዎችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን አርዕስቶችን፣ አንቀጾችን፣ ሊንኮችን፣ ዝርዝሮችን፣ አዝራሮችን እና ፎቶዎችን አውቀዋል።\n\n"
                    "ለመጨረሻው ፕሮጀክት ዝግጁ ነዎት? ምዕራፍ 7፦ ሙሉ የፕሮፋይል ድህረ-ገጽ (Capstone Project)!"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="html_ch7",
        order=7,
        title_en="HTML Ch 7: Capstone Project — Complete Profile Webpage",
        title_am="ኤችቲኤምኤል ምዕራፍ 7፦ የመጨረሻ ፕሮጀክት — ሙሉ የፕሮፋይል ድህረ-ገጽ",
        description_en="Combine Headings, Paragraphs, Lists, and Buttons into a complete webpage card!",
        description_am="አርዕስቶችን፣ ጽሁፎችን፣ ዝርዝሮችን እና አዝራሮችን በማጣመር ሙሉ ድህረ-ገጽ ይገንቡ!",
        track="html",
        steps=[
            TutorStep(
                id="html_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *Welcome to your HTML Capstone Project!* 🏆\n\n"
                    "Every web developer starts by building their personal portfolio card.\n\n"
                    "In this chapter, you will assemble:\n"
                    "1. A Main Heading `<h1>`\n"
                    "2. A Bio Paragraph `<p>`\n"
                    "3. A Skills List `<ul>` with `<li>`\n"
                    "4. A Contact Button `<button>`\n\n"
                    "Let's build your complete webpage!"
                ),
                message_am=(
                    "🏗️ *እንኳን ወደ HTML የመጨረሻ ፕሮጀክት በደህና መጡ!* 🏆\n\n"
                    "ማንኛውም የድረገጽ ገንቢ ጉዞውን የሚጀምረው የራሱን የፕሮፋይል ገጽ በመገንባት ነው።\n\n"
                    "በዚህ ምዕራፍ የሚከተሉትን በአንድ ላይ እናጣምራለን፦\n"
                    "1. ዋና አርዕስት `<h1>`\n"
                    "2. የመግቢያ አንቀጽ `<p>`\n"
                    "3. የክህሎት ዝርዝር `<ul>` እና `<li>`\n"
                    "4. የመገናኛ አዝራር `<button>`\n\n"
                    "ሙሉውን ድህረ-ገጽ አብረን እንገንባ!"
                ),
            ),
            TutorStep(
                id="html_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "👇 *Type this complete personal webpage card in the chat and send:*\n"
                    "```html\n<h1>Coder Profile</h1>\n<p>I build web pages!</p>\n<ul>\n  <li>HTML</li>\n</ul>\n<button>Hire Me</button>\n```"
                ),
                message_am=(
                    "👇 *ይህንን ሙሉ የፕሮፋይል ድህረ-ገጽ ኮድ ጽፈው ይላኩ፦*\n"
                    "```html\n<h1>Coder Profile</h1>\n<p>I build web pages!</p>\n<ul>\n  <li>HTML</li>\n</ul>\n<button>Hire Me</button>\n```"
                ),
                expected_code_output="# Coder Profile\nI build web pages!\n• HTML [Button: Hire Me]",
                hint_en='Assemble `<h1>`, `<p>`, `<ul><li>HTML</li></ul>`, and `<button>Hire Me</button>`!',
                hint_am='`<h1>`፣ `<p>`፣ `<ul><li>HTML</li></ul>`፣ እና `<button>Hire Me</button>`ን በአንድ ላይ ጽፈው ይላኩ!',
                success_message_en=(
                    "🎊 *YOU BUILT A COMPLETE, BEAUTIFULLY STRUCTURED WEBPAGE!* 🌐✨\n\n"
                    "Look at your page come to life: Heading, Bio, Skills List, and Action Button!"
                ),
                success_message_am=(
                    "🎊 *ሙሉ በሙሉ የተዋቀረ ድህረ-ገጽ ሰርተዋል!* 🌐✨\n\n"
                    "የገጽዎ ውጤት ወጥቷል፦ አርዕስት፣ መግለጫ፣ የክህሎት ማውጫ እና አዝራር በአንድ ላይ ተገጣጥመዋል!"
                ),
            ),
            TutorStep(
                id="html_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌟🎓 **CONGRATULATIONS, WEB DEVELOPER!** 🎓🌟\n\n"
                    "You have officially graduated from the CodeBuddy HTML Track!\n\n"
                    "📜 **What You Now Truly Understand:**\n"
                    "1. 📄 How the World Wide Web structures documents\n"
                    "2. 📌 Headings (`<h1>`, `<h2>`) for titles and sections\n"
                    "3. 📝 Paragraphs (`<p>`) for content and articles\n"
                    "4. 🔗 Clickable links (`<a>`) connecting pages\n"
                    "5. 📋 Lists (`<ul>`, `<li>`) for navigation and items\n"
                    "6. 🔘 Interactive buttons (`<button>`) for user actions\n"
                    "7. 🖼️ Self-closing tags like `<img>`\n"
                    "8. 🏗️ How to assemble complete websites from scratch!\n\n"
                    "Together with **Python** and **JavaScript**, you now know the full trifecta of coding! 🚀🔥"
                ),
                message_am=(
                    "🌟🎓 **እንኳን ደስ አለዎት! የድረገጽ ገንቢ ሆነዋል!** 🎓🌟\n\n"
                    "የኮድበዲ የHTML ትምህርትን በከፍተኛ ውጤት አጠናቀዋል!\n\n"
                    "📜 **በጥልቀት የተረዱት እውቀት፦**\n"
                    "1. 📄 ዓለም አቀፉ ድህረ-ገጽ ገጾችን እንዴት እንደሚያዋቅር\n"
                    "2. 📌 አርዕስቶች (`<h1>`፣ `<h2>`) ለርዕስ እና ለክፍሎች\n"
                    "3. 📝 አንቀጾች (`<p>`) ለጽሁፍ እና ለመግለጫዎች\n"
                    "4. 🔗 ሊንኮች (`<a>`) ገጾችን እርስ በርስ ለማገናኘት\n"
                    "5. 📋 ዝርዝሮች (`<ul>`፣ `<li>`) ለማውጫ እና ለሜኑ\n"
                    "6. 🔘 አዝራሮች (`<button>`) ለተጠቃሚዎች ተግባር\n"
                    "7. 🖼️ ራሳቸውን የሚዘጉ ታጎች እንደ `<img>`\n"
                    "8. 🏗️ ሙሉ ድህረ-ገጽን ከመሰረቱ መገንባት!\n\n"
                    "አሁን **ፓይተንን፣ ጃቫስክሪፕትን እና HTMLን** አጣምረው ያውቃሉ! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_html_chapters() -> List[TutorChapter]:
    """Return all HTML chapters ordered."""
    return sorted(HTML_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_html_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve HTML tutor chapter by ID."""
    for ch in HTML_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_html_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next HTML chapter ID."""
    chapters = get_all_html_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
