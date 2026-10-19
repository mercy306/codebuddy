"""CSS curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

CSS_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="css_ch1",
        order=1,
        title_en="CSS Ch 1: Meet CSS & Text Colors",
        title_am="ሲኤስኤስ ምዕራፍ 1፦ ከCSS ጋር መተዋወቅ እና የጽሁፍ ቀለሞች",
        description_en="Learn how CSS brings plain HTML to life with colors and visual styling.",
        description_am="CSS ተራ የHTML ገጾችን በቀለማት እና በውበት እንዴት እንደሚያስውብ ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎨 *Welcome to CSS!* ✨\n\n"
                    "CSS stands for **Cascading Style Sheets**.\n\n"
                    "If HTML is the bare bricks of a house, **CSS is the paint, decorations, and lighting!**\n\n"
                    "A CSS rule has 3 parts:\n"
                    "1. **Selector**: What HTML tag to style (e.g. `h1`)\n"
                    "2. **Property**: What you want to change (e.g. `color`)\n"
                    "3. **Value**: The new setting (e.g. `blue;`)\n\n"
                    "```css\nh1 {\n  color: blue;\n}\n```"
                ),
                message_am=(
                    "🎨 *እንኳን ወደ CSS በደህና መጡ!* ✨\n\n"
                    "CSS ማለት **Cascading Style Sheets** ማለት ነው።\n\n"
                    "HTML የቤት ግንባታ ጡብ ከሆነ፣ **CSS ደግሞ ቀለሙ፣ ጌጡ እና ማብሪያ ማጥፊያው ነው!**\n\n"
                    "አንድ የCSS ህግ 3 ክፍሎች አሉት፦\n"
                    "1. **መራጭ (Selector)**፦ የትኛውን የHTML ታግ እንደምናስውብ (ለምሳሌ፦ `h1`)\n"
                    "2. **ባህሪ (Property)**፦ ምን መቀየር እንደምንፈልግ (ለምሳሌ፦ `color`)\n"
                    "3. **እሴት (Value)**፦ አዲሱ ቀለም ወይም መጠን (ለምሳሌ፦ `blue;`)\n\n"
                    "```css\nh1 {\n  color: blue;\n}\n```"
                ),
            ),
            TutorStep(
                id="css_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's make our `<h1>` headings vibrant blue!\n\n"
                    "👇 *Type this CSS rule in the chat and send:*\n"
                    "```css\nh1 {\n  color: blue;\n}\n```"
                ),
                message_am=(
                    "የ `<h1>` አርዕስታችንን ሰማያዊ ቀለም እናድርገው!\n\n"
                    "👇 *ይህንን የCSS ኮድ ጽፈው ይላኩ፦*\n"
                    "```css\nh1 {\n  color: blue;\n}\n```"
                ),
                expected_code_output="Style applied to <h1>:\n  - color: blue",
                hint_en='Write `h1 { color: blue; }` with curly braces and colon!',
                hint_am='በፈረንሳይ ቅንፍ `h1 { color: blue; }` ብለው ይጻፉ!',
                success_message_en=(
                    "🎉 *Look at that color!* Your heading is now styled with CSS!"
                ),
                success_message_am=(
                    "🎉 *አርዕስቱ ተውቧል!* የHTML አርዕስትዎ በCSS ሰማያዊ ቀለም ለብሷል!"
                ),
            ),
            TutorStep(
                id="css_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "In `color: blue;`, what punctuation mark ends the declaration line in CSS?"
                ),
                message_am=(
                    "በ `color: blue;` ላይ፣ የመስመሩን መጨረሻ የሚያመለክተው የትኛው ስርአተ-ነጥብ ነው?"
                ),
                options_en=[
                    "Semicolon ; 🔚",
                    "Question mark ?",
                    "Exclamation mark !",
                ],
                options_am=[
                    "ሴሚኮለን ; 🔚",
                    "የጥያቄ ምልክት ?",
                    "የቃለ-አጋኖ ምልክት !",
                ],
                correct_option_index=0,
                success_message_en="🎯 *Spot on!* Every CSS property line must end with a semicolon `;`.",
                success_message_am="🎯 *ትክክል ነው!* በCSS ውስጥ እያንዳንዱ የስራ መስመር በሴሚኮለን `;` ይጠናቀቃል።",
            ),
            TutorStep(
                id="css_ch1_s4",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You completed CSS Chapter 1!* 🎓\n\n"
                    "You know the formula: `selector { property: value; }`.\n\n"
                    "Ready to change background colors in Chapter 2?"
                ),
                message_am=(
                    "🏆 *የCSS ምዕራፍ 1ን አጠናቀዋል!* 🎓\n\n"
                    "የCSS ቀመርን አውቀዋል፦ `selector { property: value; }`።\n\n"
                    "በምዕራፍ 2 የጀርባ ቀለሞችን (Backgrounds) ለመቀየር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch2",
        order=2,
        title_en="CSS Ch 2: Background Colors",
        title_am="ሲኤስኤስ ምዕራፍ 2፦ የጀርባ ቀለሞች (Backgrounds)",
        description_en="Learn how background-color sets backgrounds for dark mode, cards, and pages.",
        description_am="`background-color` ለገጾች እና ለካርዶች የጀርባ ቀለም እንዴት እንደሚሰጥ ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌈 *Background Colors*\n\n"
                    "To color the background behind an element, we use **`background-color`**:\n"
                    "```css\nbody {\n  background-color: lightgray;\n}\n```\n"
                    "This paints the entire webpage canvas!"
                ),
                message_am=(
                    "🌈 *የጀርባ ቀለሞች*\n\n"
                    "ከጽሁፍ ጀርባ ያለውን ቦታ ቀለም ለማስያዝ **`background-color`**ን እንጠቀማለን፦\n"
                    "```css\nbody {\n  background-color: lightgray;\n}\n```\n"
                    "ይህ መላውን የድረገጽ ሰሌዳ ያሸበርቀዋል!"
                ),
            ),
            TutorStep(
                id="css_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's style a `.card` class with a yellow background!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```css\n.card {\n  background-color: yellow;\n}\n```"
                ),
                message_am=(
                    "ለካርድ የቢጫ ጀርባ ቀለም እንስጠው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```css\n.card {\n  background-color: yellow;\n}\n```"
                ),
                expected_code_output="Style applied to <.card>:\n  - background-color: yellow",
                hint_en='Write `.card { background-color: yellow; }`',
                hint_am='`.card { background-color: yellow; }` ብለው ይጻፉ',
                success_message_en=(
                    "🎉 *VIBRANT!* The card background is now glowing yellow!"
                ),
                success_message_am=(
                    "🎉 *አምሮበታል!* የካርዱ ጀርባ ደማቅ ቢጫ ቀለም ሆኗል!"
                ),
            ),
            TutorStep(
                id="css_ch2_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Background Colors!* 🎓\n\n"
                    "Now you can create Dark Mode themes and colorful cards.\n\n"
                    "Ready to control text sizing and fonts in Chapter 3?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 2ን (የጀርባ ቀለሞችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን የጨለማ ገጽታዎችን (Dark Mode) እና ያሸበረቁ ካርዶችን መስራት ይችላሉ።\n\n"
                    "በምዕራፍ 3 የፊደል መጠኖችን (Fonts) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch3",
        order=3,
        title_en="CSS Ch 3: Font Size & Typography",
        title_am="ሲኤስኤስ ምዕራፍ 3፦ የፊደል መጠኖች እና ቅርጾች (Fonts)",
        description_en="Learn how font-size and font-family control readable, beautiful text.",
        description_am="`font-size` እና `font-family` ጽሁፎችን እንዴት ግልጽ እና ውብ እንደሚያደርጉ ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔤 *Typography & Sizing*\n\n"
                    "Web text is measured in pixels (`px`):\n"
                    "• Small text: `14px`\n"
                    "• Regular body: `16px`\n"
                    "• Large headings: `32px`\n\n"
                    "We use **`font-size`** to make text bigger or smaller:\n"
                    "```css\np {\n  font-size: 18px;\n}\n```"
                ),
                message_am=(
                    "🔤 *የፊደል መጠኖች*\n\n"
                    "በድህረ-ገጽ ላይ ጽሁፎች በፒክሰል (`px`) ይሰላሉ፦\n"
                    "• አነስተኛ ጽሁፍ፦ `14px`\n"
                    "• መደበኛ ንባብ፦ `16px`\n"
                    "• ትልቅ አርዕስት፦ `32px`\n\n"
                    "ጽሁፍን ለማተለቅ ወይም ለማሳነስ **`font-size`**ን እንጠቀማለን፦\n"
                    "```css\np {\n  font-size: 18px;\n}\n```"
                ),
            ),
            TutorStep(
                id="css_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's make paragraph text 20px and green!\n\n"
                    "👇 *Type both styles inside the rule:*\n"
                    "```css\np {\n  font-size: 20px;\n  color: green;\n}\n```"
                ),
                message_am=(
                    "የአንቀጹን ጽሁፍ መጠን 20px እና አረንጓዴ ቀለም እናድርገው!\n\n"
                    "👇 *ሁለቱንም ስታይሎች በአንድ ላይ ጽፈው ይላኩ፦*\n"
                    "```css\np {\n  font-size: 20px;\n  color: green;\n}\n```"
                ),
                expected_code_output="Style applied to <p>:\n  - font-size: 20px\n  - color: green",
                hint_en='Line 1: `p {`\nLine 2: `  font-size: 20px;`\nLine 3: `  color: green;`\nLine 4: `}`',
                hint_am='መስመር 2፦ `font-size: 20px;`\nመስመር 3፦ `color: green;`',
                success_message_en=(
                    "🌟 *CRISP & READABLE!* Your text is now 20px large and green!"
                ),
                success_message_am=(
                    "🌟 *ግልጽ እና ውብ ሆኗል!* ጽሁፉ 20px እና አረንጓዴ ቀለም ለብሷል!"
                ),
            ),
            TutorStep(
                id="css_ch3_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Typography!* 🎓\n\n"
                    "Now you can adjust font scales across titles, captions, and body text.\n\n"
                    "Ready to learn the famous CSS Box Model in Chapter 4?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 3ን (የፊደል መጠኖችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን አርዕስቶችን እና ጽሁፎችን እንደፈለጉ ማተለቅ እና ማሳነስ ይችላሉ።\n\n"
                    "በምዕራፍ 4 ዝነኛውን የቦታ ክፍተት (Box Model) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch4",
        order=4,
        title_en="CSS Ch 4: Spacing (Padding & Margins)",
        title_am="ሲኤስኤስ ምዕራፍ 4፦ የቦታ ክፍተት (Padding እና Margin)",
        description_en="Learn the secret of web spacing that prevents elements from crowding.",
        description_am="`padding` እና `margin` ነገሮች እርስ በርስ እንዳይጨናነቁ ክፍተት እንዴት እንደሚሰጡ ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *The Spacing Secret: Padding vs Margin*\n\n"
                    "Beginners often confuse these two, but here is the trick:\n"
                    "• **Padding**: Space *inside* the box (like pillows inside a crate) 🛋️\n"
                    "• **Margin**: Space *outside* the box (keeping other elements away) 🚗\n\n"
                    "```css\n.card {\n  padding: 20px;\n}\n```"
                ),
                message_am=(
                    "📦 *የክፍተት ሚስጥር፦ Padding እና Margin*\n\n"
                    "ጀማሪዎች ሁለቱን ያምታቷቸዋል፤ ልዩነቱ ግን ይህ ነው፦\n"
                    "• **Padding**፦ በሳጥኑ *ውስጥ* የሚሰጥ ክፍተት 🛋️\n"
                    "• **Margin**፦ ከሳጥኑ *ውጭ* ሌሎች እንዳይጠጉ የሚሰጥ ክፍተት 🚗\n\n"
                    "```css\n.card {\n  padding: 20px;\n}\n```"
                ),
            ),
            TutorStep(
                id="css_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's give our card 20px breathing room with padding!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```css\n.card {\n  padding: 20px;\n}\n```"
                ),
                message_am=(
                    "ለካርዳችን 20px ውስጣዊ ክፍተት እንስጠው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```css\n.card {\n  padding: 20px;\n}\n```"
                ),
                expected_code_output="Style applied to <.card>:\n  - padding: 20px",
                hint_en='Write `.card { padding: 20px; }`',
                hint_am='`.card { padding: 20px; }` ብለው ይጻፉ',
                success_message_en=(
                    "🎉 *BREATHING ROOM!* The content inside the card no longer touches the edges!"
                ),
                success_message_am=(
                    "🎉 *ክፍተቱ ተስተካክሏል!* በካርዱ ውስጥ ያለው ጽሁፍ ከዳርቻው ጋር አይጋጭም!"
                ),
            ),
            TutorStep(
                id="css_ch4_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Web Spacing!* 🎓\n\n"
                    "Padding and Margins make websites look clean and professional.\n\n"
                    "Ready to round corners with `border-radius` in Chapter 5?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 4ን (ክፍተቶችን) አጠናቀዋል!* 🎓\n\n"
                    "Padding እና Margin ድህረ-ገጾችን ንጹህ እና ዘመናዊ ያደርጋሉ።\n\n"
                    "በምዕራፍ 5 ጠርዞችን ክብ ማድረግን (Borders) ለመማር ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch5",
        order=5,
        title_en="CSS Ch 5: Rounded Corners (Border Radius)",
        title_am="ሲኤስኤስ ምዕራፍ 5፦ ክብ ጠርዞች (Border Radius)",
        description_en="Learn how border-radius turns sharp boxes into sleek modern cards.",
        description_am="`border-radius` ሹል ሳጥኖችን ወደ ዘመናዊ ክብ ቅርጾች እንዴት እንደሚቀይር ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📱 *Modern Rounded Corners*\n\n"
                    "Modern mobile apps (like Instagram and Telegram) use smooth rounded corners.\n\n"
                    "In CSS, we use **`border-radius`**:\n"
                    "• Small rounding: `8px`\n"
                    "• Modern pill button: `25px`\n"
                    "• Perfect circle: `50%`\n\n"
                    "```css\nimg {\n  border-radius: 12px;\n}\n```"
                ),
                message_am=(
                    "📱 *ዘመናዊ ክብ ጠርዞች*\n\n"
                    "ዘመናዊ አፖች (እንደ ቴሌግራም እና ኢንስታግራም) ሹል ጠርዞችን በማጠፍ ክብ ያደርጋሉ።\n\n"
                    "በCSS ውስጥ ለዚህ **`border-radius`**ን እንጠቀማለን፦\n"
                    "• መጠነኛ ክብ፦ `8px`\n"
                    "• የአዝራር ቅርጽ፦ `25px`\n"
                    "• ፍጹም ክብ፦ `50%`\n\n"
                    "```css\nimg {\n  border-radius: 12px;\n}\n```"
                ),
            ),
            TutorStep(
                id="css_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's round our website images with 15px radius!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```css\nimg {\n  border-radius: 15px;\n}\n```"
                ),
                message_am=(
                    "የድረገጽ ፎቶዎችን ጠርዝ 15px እናክብበው!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```css\nimg {\n  border-radius: 15px;\n}\n```"
                ),
                expected_code_output="Style applied to <img>:\n  - border-radius: 15px",
                hint_en='Write `img { border-radius: 15px; }`',
                hint_am='`img { border-radius: 15px; }` ብለው ይጻፉ',
                success_message_en=(
                    "✨ *SLEEK & MODERN!* The sharp corners are smoothed out into modern curves!"
                ),
                success_message_am=(
                    "✨ *ዘመናዊ ቅርጽ ይዟል!* ሹል ጠርዞች ተስተካክለው ውብ ኩርባ ሆነዋል!"
                ),
            ),
            TutorStep(
                id="css_ch5_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Rounded Corners!* 🎓\n\n"
                    "Now you can style profile avatars, app cards, and badges.\n\n"
                    "Ready to style buttons that invite clicks in Chapter 6?"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 5ን (ክብ ጠርዞችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን የፕሮፋይል ፎቶዎችን እና ካርዶችን ማሳመር ይችላሉ።\n\n"
                    "በምዕራፍ 6 የሚማርኩ አዝራሮችን (Buttons) ለማስዋብ ዝግጁ ነዎት?"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch6",
        order=6,
        title_en="CSS Ch 6: Styling Buttons",
        title_am="ሲኤስኤስ ምዕራፍ 6፦ አዝራሮችን ማስዋብ",
        description_en="Learn how background, color, and padding transform plain buttons into irresistible buttons.",
        description_am="ቀለሞች እና ክፍተቶች ተራ አዝራሮችን እንዴት ውብ እንደሚያደርጓቸው ይማሩ።",
        track="css",
        steps=[
            TutorStep(
                id="css_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔘 *The Anatomy of a Beautiful Button*\n\n"
                    "Default HTML buttons look old and gray.\n\n"
                    "With CSS, we transform them into vibrant call-to-action buttons using:\n"
                    "1. `background-color: green;` (bold background)\n"
                    "2. `color: white;` (readable text)\n"
                    "3. `padding: 12px;` (comfortable click target)\n"
                    "4. `border-radius: 8px;` (smooth edges)"
                ),
                message_am=(
                    "🔘 *የውብ አዝራር ምስጢር*\n\n"
                    "ተራ የHTML አዝራር ግራጫ እና የደበዘዘ ነው።\n\n"
                    "በCSS አማካኝነት ግን ወደ ተወዳጅ አዝራር እንቀይረዋለን፦\n"
                    "1. `background-color: green;` (ደማቅ የጀርባ ቀለም)\n"
                    "2. `color: white;` (ግልጽ ነጭ ጽሁፍ)\n"
                    "3. `padding: 12px;` (ለመጫን ምቹ ክፍተት)\n"
                    "4. `border-radius: 8px;` (ለስላሳ ጠርዝ)"
                ),
            ),
            TutorStep(
                id="css_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's create a vibrant green action button!\n\n"
                    "👇 *Type this code in the chat and send:*\n"
                    "```css\nbutton {\n  background-color: green;\n  color: white;\n}\n```"
                ),
                message_am=(
                    "ደማቅ አረንጓዴ አዝራር እንስራ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```css\nbutton {\n  background-color: green;\n  color: white;\n}\n```"
                ),
                expected_code_output="Style applied to <button>:\n  - background-color: green\n  - color: white",
                hint_en='Line 1: `button {`\nLine 2: `  background-color: green;`\nLine 3: `  color: white;`\nLine 4: `}`',
                hint_am='መስመር 2፦ `background-color: green;`\nመስመር 3፦ `color: white;`',
                success_message_en=(
                    "🔥 *GORGEOUS BUTTON!* Green background with crisp white text!"
                ),
                success_message_am=(
                    "🔥 *ውብ አዝራር!* አረንጓዴ ጀርባ ከነጭ ጽሁፍ ጋር ተዋህዷል!"
                ),
            ),
            TutorStep(
                id="css_ch6_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏆 *You mastered Button Styling!* 🎓\n\n"
                    "Now you are ready for the ultimate milestone: Chapter 7 Capstone Project!"
                ),
                message_am=(
                    "🏆 *ምዕራፍ 6ን (አዝራሮችን) አጠናቀዋል!* 🎓\n\n"
                    "አሁን ለመጨረሻው ፈተና ዝግጁ ነዎት፦ ምዕራፍ 7 Capstone Project!"
                ),
            ),
        ],
    ),
    TutorChapter(
        id="css_ch7",
        order=7,
        title_en="CSS Ch 7: Capstone Project — Modern Profile Card",
        title_am="ሲኤስኤስ ምዕራፍ 7፦ የመጨረሻ ፕሮጀክት — ዘመናዊ የፕሮፋይል ካርድ",
        description_en="Combine Background, Padding, Border-Radius, and Colors into a complete UI card!",
        description_am="ቀለሞችን፣ ክፍተቶችን እና ቅርጾችን በማጣመር የተሟላ የድህረ-ገጽ ካርድ ይገንቡ!",
        track="css",
        steps=[
            TutorStep(
                id="css_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎨 *Welcome to your CSS Capstone Project!* 🏆\n\n"
                    "In real web design, every component (like an Amazon product card or a YouTube video card) "
                    "combines all the CSS rules you just learned:\n"
                    "• `background-color` (card color)\n"
                    "• `padding` (breathing room)\n"
                    "• `border-radius` (sleek rounded edges)\n"
                    "• `color` (readable text)\n\n"
                    "Let's assemble a complete `.profile-card` rule!"
                ),
                message_am=(
                    "🎨 *እንኳን ወደ CSS የመጨረሻ ፕሮጀክት በደህና መጡ!* 🏆\n\n"
                    "በእውነተኛ የድረገጽ ዲዛይን፣ እያንዳንዱ ካርድ (እንደ አማዞን ዕቃ ወይም የዩቲዩብ ቪዲዮ) "
                    "የተማርናቸውን የCSS ህጎች አጣምሮ ይይዛል፦\n"
                    "• `background-color` (የካርዱ ቀለም)\n"
                    "• `padding` (ውስጣዊ ክፍተት)\n"
                    "• `border-radius` (ክብ ጠርዞች)\n"
                    "• `color` (የጽሁፉ ቀለም)\n\n"
                    "ሙሉውን `.profile-card` በአንድ ላይ እንገንባ!"
                ),
            ),
            TutorStep(
                id="css_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "👇 *Type this complete profile card style in the chat and send:*\n"
                    "```css\n.profile-card {\n  background-color: white;\n  padding: 24px;\n  border-radius: 16px;\n}\n```"
                ),
                message_am=(
                    "👇 *ይህንን ሙሉ የፕሮፋይል ካርድ ስታይል ጽፈው ይላኩ፦*\n"
                    "```css\n.profile-card {\n  background-color: white;\n  padding: 24px;\n  border-radius: 16px;\n}\n```"
                ),
                expected_code_output="Style applied to <.profile-card>:\n  - background-color: white\n  - padding: 24px\n  - border-radius: 16px",
                hint_en='Assemble `background-color: white;`, `padding: 24px;`, and `border-radius: 16px;` inside `.profile-card { ... }`',
                hint_am='በ `.profile-card { ... }` ውስጥ `background-color: white;`፣ `padding: 24px;`፣ እና `border-radius: 16px;` አጣምረው ይጻፉ!',
                success_message_en=(
                    "🎊 *A WORK OF ART!* You just styled a complete modern UI component from scratch! 🎨✨"
                ),
                success_message_am=(
                    "🎊 *ድንቅ የጥበብ ስራ!* ዘመናዊ የድህረ-ገጽ ካርድን ከመሰረቱ አስውበዋል! 🎨✨"
                ),
            ),
            TutorStep(
                id="css_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🌟🎓 **CONGRATULATIONS, FULL-STACK DESIGNER!** 🎓🌟\n\n"
                    "You have officially mastered the foundations of CSS:\n"
                    "1. 🎨 CSS syntax (`selector { property: value; }`)\n"
                    "2. 🌈 Foreground & Background color design\n"
                    "3. 🔤 Font sizing and typography in pixels (`px`)\n"
                    "4. 📦 The Box Model (Padding & Margins)\n"
                    "5. 📱 Sleek rounded corners with `border-radius`\n"
                    "6. 🔘 Beautiful clickable button styling\n"
                    "7. 🏛️ Architecting complete modern UI components!\n\n"
                    "With **Python**, **JavaScript**, **HTML**, AND **CSS**, you possess the full skillset of a modern programmer! 🚀🔥"
                ),
                message_am=(
                    "🌟🎓 **እንኳን ደስ አለዎት! ሙሉ የድረገጽ ዲዛይነር ሆነዋል!** 🎓🌟\n\n"
                    "የCSS መሰረታዊ እውቀቶችን በሙሉ ጨርሰዋል፦\n"
                    "1. 🎨 የCSS አጻጻፍ ህግ (`selector { property: value; }`)\n"
                    "2. 🌈 የጽሁፍ እና የጀርባ ቀለማት ዲዛይን\n"
                    "3. 🔤 የፊደል መጠኖች በፒክሰል (`px`)\n"
                    "4. 📦 የቦታ ክፍተት (Padding እና Margin)\n"
                    "5. 📱 ዘመናዊ ክብ ጠርዞች በ `border-radius`\n"
                    "6. 🔘 የሚማርኩ አዝራሮችን ማስዋብ\n"
                    "7. 🏛️ የተሟሉ ዘመናዊ የድህረ-ገጽ ካርዶችን መገንባት!\n\n"
                    "አሁን **ፓይተንን፣ ጃቫስክሪፕትን፣ HTMLን እና CSSን** አጣምረው ይዘዋል! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_css_chapters() -> List[TutorChapter]:
    """Return all CSS chapters ordered."""
    return sorted(CSS_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_css_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve CSS tutor chapter by ID."""
    for ch in CSS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_css_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next CSS chapter ID."""
    chapters = get_all_css_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
