"""React / JSX curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

REACT_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="react_ch1",
        order=1,
        title_en="React Ch 1: Meet React & JSX",
        title_am="ሪያክት ምዕራፍ 1፦ ከሪያክት እና ጄኤስኤክስ ጋር መተዋወቅ",
        description_en="Discover the world's most popular frontend UI library created by Meta.",
        description_am="በሜታ (Meta/Facebook) የተሰራውን እና አለምን እየመራ ያለውን ሪያክት (React) ይማሩ።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚛️ *Welcome to React!* 🚀\n\n"
                    "React is the world's #1 frontend UI library, powering **Instagram, Netflix, Airbnb, and WhatsApp Web**!\n\n"
                    "In traditional web development, you write HTML in one file and JavaScript in another. "
                    "React changed the world by introducing **JSX (JavaScript XML)**: writing HTML tags directly inside your JavaScript code!\n\n"
                    "```jsx\n<h1>Hello React!</h1>\n```\n\n"
                    "Notice that this looks like HTML, but it is supercharged by the JavaScript engine underneath!"
                ),
                message_am=(
                    "⚛️ *እንኳን ወደ ሪያክት (React) በደህና መጡ!* 🚀\n\n"
                    "ሪያክት በዓለም ላይ ቁጥር 1 የድህረ-ገጽ ፊት (UI) መገንቢያ ሲሆን፣ እንደ **Instagram፣ Netflix፣ Airbnb እና WhatsApp** "
                    "ያሉ ግዙፍ መተግበሪያዎች የተሰሩበት ነው!\n\n"
                    "በቀድሞው አሰራር HTML እና ጃቫስክሪፕት በተለያዩ ፋይሎች ይጻፉ ነበር። "
                    "ሪያክት ግን **JSX (JavaScript XML)** የተባለ አስደናቂ መንገድ አስተዋወቀ፦ የ HTML ታጎችን በቀጥታ በጃቫስክሪፕት ውስጥ መጻፍ!\n\n"
                    "```jsx\n<h1>Hello React!</h1>\n```\n\n"
                    "ይህ የ HTML ታግ ይመስላል፤ ነገር ግን በውስጡ ሙሉ የጃቫስክሪፕት ሃይል አለው!"
                ),
            ),
            TutorStep(
                id="react_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first React JSX element!\n\n"
                    "👇 *Type this exact code in the chat and send:*\n"
                    "```jsx\n<h1>Hello React!</h1>\n```"
                ),
                message_am=(
                    "የመጀመሪያውን የሪያክት JSX ኤለመንት እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\n<h1>Hello React!</h1>\n```"
                ),
                expected_code_output="<h1>Hello React!</h1>",
                hint_en="Write `<h1>Hello React!</h1>` with opening and closing tags.",
                hint_am="የመክፈቻና የመዝጊያ ታጎችን በመጠቀም `<h1>Hello React!</h1>` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *BOOM!* You just transformed JSX and rendered real React virtual DOM!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* የሪያክት JSX ኮድ ተቀይሮ እውነተኛ የድህረ-ገጽ ኤለመንት ሆኖ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="react_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What does JSX allow developers to do in React?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ውስጥ JSX ምን አይነት ጥቅም ይሰጣል?"
                ),
                options_en=[
                    "Write HTML-like tags directly inside JavaScript",
                    "Connect to SQL databases directly",
                    "Format text with CSS only",
                    "Compile C language kernels",
                ],
                options_am=[
                    "የ HTML ታጎችን በቀጥታ በጃቫስክሪፕት ኮድ ውስጥ ለመጻፍ",
                    "በቀጥታ ከዳታቤዝ ጋር ለመገናኘት",
                    "በ CSS ብቻ ጽሁፍ ለማስዋብ",
                    "የሲ (C) ቋንቋን ለማቀናበር",
                ],
                correct_option_index=0,
                hint_en="JSX lets us write markup tags seamlessly inside JavaScript!",
                hint_am="JSX የድህረ-ገጽ ታጎችን በቀጥታ በጃቫስክሪፕት ውስጥ እንድንጽፍ ያስችለናል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch2",
        order=2,
        title_en="React Ch 2: Building Your First Component",
        title_am="ሪያክት ምዕራፍ 2፦ የመጀመሪያው የሪያክት ኮምፖነንት",
        description_en="Learn how reusable Lego-brick functions build complete web apps.",
        description_am="እንደ ሌጎ (Lego) የሚገጣጠሙ እንደገና ጥቅም ላይ የሚውሉ ኮምፖነንቶችን መገንባት።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🧱 *React Components: The Lego Blocks of UI* 🧩\n\n"
                    "In React, a **Component** is simply a JavaScript function that returns JSX!\n\n"
                    "```jsx\nfunction Welcome() {\n    return <h2>Welcome to CodeBuddy!</h2>;\n}\n```\n\n"
                    "⚠️ **CRITICAL RULE**: In React, component names **MUST start with a Capital Letter** (e.g. `Welcome`, `Header`, `Button`).\n\n"
                    "Lowercase tags like `<h1>` or `<div>` are treated as built-in HTML, while Capitalized names tell React: *'This is my custom component!'*"
                ),
                message_am=(
                    "🧱 *የሪያክት ኮምፖነንቶች፦ የድህረ-ገጽ መገንቢያ ጡቦች* 🧩\n\n"
                    "በሪያክት ውስጥ **ኮምፖነንት (Component)** ማለት JSX የሚመልስ ተራ የጃቫስክሪፕት ፈንክሽን ነው!\n\n"
                    "```jsx\nfunction Welcome() {\n    return <h2>Welcome to CodeBuddy!</h2>;\n}\n```\n\n"
                    "⚠️ **ዋነኛ ህግ**፦ በሪያክት ውስጥ የኮምፖነንት ስም **ሁልጊዜ በካፒታል ፊደል መጀመር አለበት** (ለምሳሌ፦ `Welcome`፣ `Header`፣ `Button`)።\n\n"
                    "በትንሽ ፊደል የተጻፉ እንደ `<h1>` ያሉት መደበኛ የ HTML ታጎች ሲሆኑ፣ በካፒታል ሲጀምሩ ግን ሪያክት የራሳችን ልዩ ኮምፖነንት መሆኑን ያውቃል!"
                ),
            ),
            TutorStep(
                id="react_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create your first React component called `Welcome` that returns `<h2>Welcome to CodeBuddy!</h2>`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```jsx\nfunction Welcome() {\n    return <h2>Welcome to CodeBuddy!</h2>;\n}\n```"
                ),
                message_am=(
                    "`Welcome` የሚል ኮምፖነንት ፈጥረው `<h2>Welcome to CodeBuddy!</h2>` ይመልሱ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction Welcome() {\n    return <h2>Welcome to CodeBuddy!</h2>;\n}\n```"
                ),
                expected_code_output="<h2>Welcome to CodeBuddy!</h2>",
                hint_en="Define `function Welcome() { return <h2>Welcome to CodeBuddy!</h2>; }`",
                hint_am="`function Welcome() { return <h2>Welcome to CodeBuddy!</h2>; }` ብለው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You just authored your very first reusable React component!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* የመጀመሪያውን እንደገና ጥቅም ላይ የሚውል የሪያክት ኮምፖነንት በተሳካ ሁኔታ ሰርተዋል!"
                ),
            ),
            TutorStep(
                id="react_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Why must custom React component function names start with a Capital letter?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ውስጥ የኮምፖነንት ስሞች በካፒታል ፊደል መጀመር ያለባቸው ለምንድን ነው?"
                ),
                options_en=[
                    "To distinguish them from native lowercase HTML tags like <div> or <p>",
                    "Because lowercase is illegal in JavaScript",
                    "To make them run faster in memory",
                    "To hide them from search engines",
                ],
                options_am=[
                    "ከመደበኛ የ HTML ታጎች (እንደ <div> ወይም <p>) ለመለየት",
                    "በትንሽ ፊደል መጻፍ በጃቫስክሪፕት ስለማይፈቀድ",
                    "በማህደረ-ትውስታ ውስጥ ፈጣን እንዲሆኑ ለማድረግ",
                    "ከፍለጋ ሞተሮች ለመደበቅ",
                ],
                correct_option_index=0,
                hint_en="Capital letters tell React it's a custom component rather than a built-in DOM element!",
                hint_am="ካፒታል ፊደላት ሪያክት የራሳችን የተሰራ ኮምፖነንት መሆኑን እንዲያውቅ ያስችሉታል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch3",
        order=3,
        title_en="React Ch 3: Dynamic Data with Curly Braces { }",
        title_am="ሪያክት ምዕራፍ 3፦ ተለዋዋጭ መረጃዎች በፈረንሳይ ቅንፍ",
        description_en="Inject JavaScript variables, math, and strings directly into your UI.",
        description_am="ተለዋዋጭ መረጃዎችን እና ስሌቶችን በ `{ }` አማካኝነት በድህረ-ገጽ ላይ ማሳየት።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🪄 *Curly Braces `{ }`: The Magic Window to JavaScript* ✨\n\n"
                    "Inside JSX, you can escape back into JavaScript anytime by wrapping code in curly braces `{ }`!\n\n"
                    "```jsx\nfunction Profile() {\n    const name = \"Sara\";\n    return <h3>Hello, {name}!</h3>;\n}\n```\n\n"
                    "Inside `{ }`, you can write:\n"
                    "- Variable names: `{name}`\n"
                    "- Arithmetic math: `{2 + 2}` (outputs `4`)\n"
                    "- Function calls: `{name.toUpperCase()}`"
                ),
                message_am=(
                    "🪄 *የፈረንሳይ ቅንፍ `{ }`፦ ወደ ጃቫስክሪፕት መመለሻ መስኮት* ✨\n\n"
                    "በ JSX ውስጥ የፈረንሳይ ቅንፍ `{ }` በመክፈት ማንኛውንም የጃቫስክሪፕት ተለዋዋጭ ወይም ስሌት ማስገባት ይችላሉ!\n\n"
                    "```jsx\nfunction Profile() {\n    const name = \"Sara\";\n    return <h3>Hello, {name}!</h3>;\n}\n```\n\n"
                    "በ `{ }` ውስጥ የሚከተሉትን ማከናወን ይቻላል፦\n"
                    "- የተለዋዋጭ ስም፦ `{name}`\n"
                    "- የሂሳብ ስሌት፦ `{2 + 2}` (`4` ያወጣል)\n"
                    "- ፈንክሽኖችን መጥራት፦ `{name.toUpperCase()}`"
                ),
            ),
            TutorStep(
                id="react_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Define a `Greeting` component with `const name = \"Sara\";` and display `<h3>Hello, {name}!</h3>`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```jsx\nfunction Greeting() {\n    const name = \"Sara\";\n    return <h3>Hello, {name}!</h3>;\n}\n```"
                ),
                message_am=(
                    "`Greeting` የሚል ኮምፖነንት ፈጥረው በ `const name = \"Sara\";` በኩል `<h3>Hello, {name}!</h3>` አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction Greeting() {\n    const name = \"Sara\";\n    return <h3>Hello, {name}!</h3>;\n}\n```"
                ),
                expected_code_output="<h3>Hello, Sara!</h3>",
                hint_en='Write `function Greeting() { const name = "Sara"; return <h3>Hello, {name}!</h3>; }`',
                hint_am='`function Greeting() { const name = "Sara"; return <h3>Hello, {name}!</h3>; }` ብለው ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* React seamlessly evaluated `{name}` and rendered `Hello, Sara!`"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ሪያክት `{name}` የሚለውን ተለዋዋጭ በቅጽበት አንብቦ `Hello, Sara!` ብሎ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="react_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "What will this JSX render?\n"
                    "```jsx\n<p>Total: {10 + 15}</p>\n```"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "ይህ የ JSX ኮድ በስክሪኑ ላይ ምን ያወጣል?\n"
                    "```jsx\n<p>Total: {10 + 15}</p>\n```"
                ),
                options_en=[
                    "<p>Total: 25</p>",
                    "<p>Total: 10 + 15</p>",
                    "<p>Total: {25}</p>",
                    "Syntax Error",
                ],
                options_am=[
                    "<p>Total: 25</p>",
                    "<p>Total: 10 + 15</p>",
                    "<p>Total: {25}</p>",
                    "የሰዋሰው ስህተት",
                ],
                correct_option_index=0,
                hint_en="Inside `{ }`, JavaScript computes 10 + 15 = 25!",
                hint_am="በ `{ }` ውስጥ 10 + 15 ተሰልቶ 25 ይሆናል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch4",
        order=4,
        title_en="React Ch 4: Passing Props (Parameters)",
        title_am="ሪያክት ምዕራፍ 4፦ ፕሮፕስ (Props) - መረጃን ማስተላለፍ",
        description_en="Pass customizable data into components to make them flexible and reusable.",
        description_am="መረጃዎችን በፕሮፕስ (Props) ወደ ኮምፖነንቶች በማስተላለፍ ተለዋዋጭ ማድረግ።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎁 *Props: Component Inputs* 📨\n\n"
                    "Just like functions take arguments, React components take **Props** (short for properties)!\n\n"
                    "```jsx\nfunction UserBadge(props) {\n    return <p>User: {props.name}</p>;\n}\n```\n\n"
                    "- When someone uses the component: `<UserBadge name=\"Abebe\" />`\n"
                    "- Inside the component, `props.name` becomes `\"Abebe\"`!\n"
                    "- Props make one component reusable for millions of different users!"
                ),
                message_am=(
                    "🎁 *ፕሮፕስ (Props)፦ የኮምፖነንት ግብአቶች* 📨\n\n"
                    "ልክ ፈንክሽኖች መረጃዎችን እንደሚቀበሉ ሁሉ፣ የሪያክት ኮምፖነንቶችም **Props** ይቀበላሉ!\n\n"
                    "```jsx\nfunction UserBadge(props) {\n    return <p>User: {props.name}</p>;\n}\n```\n\n"
                    "- ኮምፖነንቱ ሲጠራ፦ `<UserBadge name=\"Abebe\" />`\n"
                    "- በኮምፖነንቱ ውስጥ `props.name` የ `\"Abebe\"` ዋጋን ይይዛል!\n"
                    "- ፕሮፕስ አንድን ኮምፖነንት ለሚሊዮን ተጠቃሚዎች እንድንጠቀምበት ያደርገዋል!"
                ),
            ),
            TutorStep(
                id="react_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `UserBadge(props)` component that displays `<p>User: {props.name}</p>`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction UserBadge(props) {\n    return <p>User: {props.name}</p>;\n}\n```"
                ),
                message_am=(
                    "`UserBadge(props)` የሚል ኮምፖነንት ጽፈው `<p>User: {props.name}</p>` ይመልሱ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction UserBadge(props) {\n    return <p>User: {props.name}</p>;\n}\n```"
                ),
                expected_code_output="<p>User: Abebe</p>",
                hint_en="Write `function UserBadge(props) { return <p>User: {props.name}</p>; }`",
                hint_am="`function UserBadge(props) { return <p>User: {props.name}</p>; }` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *TERRIFIC!* The engine supplied the prop and rendered `<p>User: Abebe</p>`!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* ኮምፖነንቱ ፕሮፕሱን ተቀብሎ `<p>User: Abebe</p>` ብሎ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="react_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In React, are props mutable (can a child component change its own props directly)?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ውስጥ አንድ ኮምፖነንት የተቀበለውን ፕሮፕስ (Props) በራሱ ፍላጎት መቀየር ይችላል?"
                ),
                options_en=[
                    "No, props are read-only (immutable)",
                    "Yes, props can be modified anytime",
                    "Only on weekends",
                    "Only if written in CSS",
                ],
                options_am=[
                    "አይችልም፤ ፕሮፕስ የማይለወጥ (Read-only) ነው",
                    "አዎ፤ በማንኛውም ጊዜ መቀየር ይቻላል",
                    "ቅዳሜና እሁድ ብቻ",
                    "በ CSS ከተጻፈ ብቻ",
                ],
                correct_option_index=0,
                hint_en="React enforces one-way data flow: props are strictly read-only for child components!",
                hint_am="በሪያክት ውስጥ ፕሮፕስ አይቀየርም (Read-only ነው)፤ መረጃ ሁልጊዜ ከወላጅ ወደ ልጅ ይፈሳል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch5",
        order=5,
        title_en="React Ch 5: Conditional Rendering",
        title_am="ሪያክት ምዕራፍ 5፦ ሁኔታዎችን አይቶ ማሳየት",
        description_en="Show or hide elements based on user status, login states, or flags.",
        description_am="እንደ ተጠቃሚ ሁኔታ እና የመግቢያ ፈቃድ መረጃዎችን መርጦ ማሳየት።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Conditional Rendering in React* 🧠\n\n"
                    "In web apps, you often want to show different buttons depending on whether a user is online or offline.\n\n"
                    "Inside JSX, the cleanest way to make decisions is the **Ternary Operator (`? :`)**:\n\n"
                    "```jsx\nfunction Status(props) {\n    return <span>{props.online ? \"Online\" : \"Offline\"}</span>;\n}\n```\n\n"
                    "- If `props.online` is `true`, it renders `\"Online\"`\n"
                    "- If `false`, it renders `\"Offline\"`"
                ),
                message_am=(
                    "🚦 *ሁኔታዎችን አይቶ ማሳየት (Conditional Rendering)* 🧠\n\n"
                    "በድህረ-ገጽ ላይ ተጠቃሚው ገብቷል ወይስ አልገባም የሚለውን አይተን የተለያየ ነገር እናሳያለን።\n\n"
                    "በ JSX ውስጥ ውሳኔዎችን ለመወሰን ቀላሉ መንገድ **ተርነሪ ኦፕሬተር (`? :`)** ነው፦\n\n"
                    "```jsx\nfunction Status(props) {\n    return <span>{props.online ? \"Online\" : \"Offline\"}</span>;\n}\n```\n\n"
                    "- `props.online` እውነት ከሆነ `\"Online\"` ያወጣል\n"
                    "- ሀሰት ከሆነ ደግሞ `\"Offline\"` ያሳያል"
                ),
            ),
            TutorStep(
                id="react_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `Status(props)` component that renders `<span>{props.online ? \"Online\" : \"Offline\"}</span>`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction Status(props) {\n    return <span>{props.online ? \"Online\" : \"Offline\"}</span>;\n}\n```"
                ),
                message_am=(
                    "`Status(props)` የሚል ኮምፖነንት ጽፈው `<span>{props.online ? \"Online\" : \"Offline\"}</span>` ይመልሱ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction Status(props) {\n    return <span>{props.online ? \"Online\" : \"Offline\"}</span>;\n}\n```"
                ),
                expected_code_output="<span>Online</span>",
                hint_en='Write `function Status(props) { return <span>{props.online ? "Online" : "Offline"}</span>; }`',
                hint_am='`function Status(props) { return <span>{props.online ? "Online" : "Offline"}</span>; }` ብለው ይላኩ።',
                success_message_en=(
                    "🔥 *OUTSTANDING!* You just built smart conditional UI with React!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* በሪያክት ሁኔታዎችን አይቶ የሚወስን ብልህ ድህረ-ገጽ ገነቡ!"
                ),
            ),
            TutorStep(
                id="react_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Which operator is most commonly used inside JSX curly braces `{ }` for inline if/else decisions?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ JSX ፈረንሳይ ቅንፍ `{ }` ውስጥ ለቀላል ውሳኔዎች በብዛት ጥቅም ላይ የሚውለው የትኛው ነው?"
                ),
                options_en=[
                    "The ternary operator (condition ? trueVal : falseVal)",
                    "if-else statements directly inside tags",
                    "switch statements inside quotes",
                    "while loops",
                ],
                options_am=[
                    "ተርነሪ ኦፕሬተር (መስፈርት ? እውነት : ሀሰት)",
                    "የ if-else ቃላት በቀጥታ በታጎች ውስጥ",
                    "የ switch ቃላት በጥቅስ ውስጥ",
                    "የ while ሉፖች",
                ],
                correct_option_index=0,
                hint_en="Ternary expressions return a value inline directly into JSX!",
                hint_am="ተርነሪ ኦፕሬተር በአንድ መስመር ውስጥ ውጤትን በቀጥታ ወደ JSX ይመልሳል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch6",
        order=6,
        title_en="React Ch 6: Rendering Lists with .map()",
        title_am="ሪያክት ምዕራፍ 6፦ ዝርዝሮችን በ .map() ማሳየት",
        description_en="Transform JavaScript arrays of data into dynamic lists of UI elements.",
        description_am="የዳታ ዝርዝሮችን በ `.map()` ወደ ድህረ-ገጽ ኤለመንቶች መቀየር።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📋 *Rendering Lists with `.map()`* 🗺️\n\n"
                    "In React, we never write manual loops to render lists. We use the JavaScript `.map()` array method!\n\n"
                    "```jsx\nfunction TechList() {\n    const skills = [\"HTML\", \"CSS\", \"React\"];\n    return (\n        <ul>\n            {skills.map(skill => (\n                <li key={skill}>{skill}</li>\n            ))}\n        </ul>\n    );\n}\n```\n\n"
                    "- `.map()` transforms each item in the array into an `<li>` element.\n"
                    "- The `key` attribute gives React a unique ID to track each item efficiently!"
                ),
                message_am=(
                    "📋 *ዝርዝሮችን በ `.map()` ማሳየት* 🗺️\n\n"
                    "በሪያክት ውስጥ ዝርዝር መረጃዎችን ለማሳየት የጃቫስክሪፕት `.map()` ዘዴን እንጠቀማለን፦\n\n"
                    "```jsx\nfunction TechList() {\n    const skills = [\"HTML\", \"CSS\", \"React\"];\n    return (\n        <ul>\n            {skills.map(skill => (\n                <li key={skill}>{skill}</li>\n            ))}\n        </ul>\n    );\n}\n```\n\n"
                    "- `.map()` በአሬይ ውስጥ ያለውን እያንዳንዱን መረጃ ወደ `<li>` ይቀይረዋል\n"
                    "- `key` ደግሞ ሪያክት እያንዳንዱን መረጃ ለይቶ እንዲከታተል ልዩ መታወቂያ ይሰጠዋል!"
                ),
            ),
            TutorStep(
                id="react_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `TechList` component mapping `[\"HTML\", \"CSS\", \"React\"]` to list items with a `key`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction TechList() {\n    const skills = [\"HTML\", \"CSS\", \"React\"];\n    return (\n        <ul>\n            {skills.map(s => <li key={s}>{s}</li>)}\n        </ul>\n    );\n}\n```"
                ),
                message_am=(
                    "`TechList` የሚል ኮምፖነንት ፈጥረው `[\"HTML\", \"CSS\", \"React\"]` በ `.map()` አማካኝነት በ `<ul>` ውስጥ አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction TechList() {\n    const skills = [\"HTML\", \"CSS\", \"React\"];\n    return (\n        <ul>\n            {skills.map(s => <li key={s}>{s}</li>)}\n        </ul>\n    );\n}\n```"
                ),
                expected_code_output="<ul><li>HTML</li><li>CSS</li><li>React</li></ul>",
                hint_en="Use `skills.map(s => <li key={s}>{s}</li>)` inside `<ul>...</ul>`",
                hint_am="በ `<ul>` ውስጥ `skills.map(s => <li key={s}>{s}</li>)` ብለው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You rendered a dynamic list using `.map()` and keys!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* በ `.map()` በመጠቀም ተለዋዋጭ ዝርዝርን በድህረ-ገጽ ላይ አሳይተዋል!"
                ),
            ),
            TutorStep(
                id="react_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Why does React require a unique `key` prop when rendering lists of elements?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ውስጥ ዝርዝር ኤለመንቶችን ስናወጣ `key` የሚያስፈልገው ለምንድን ነው?"
                ),
                options_en=[
                    "To efficiently track which items changed, added, or removed in the DOM",
                    "To unlock encrypted database rows",
                    "To change the font color to blue",
                    "To satisfy CSS selectors",
                ],
                options_am=[
                    "የየትኛው መረጃ እንደተቀየረ ወይም እንደተሰረዘ ሪያክት በቀላሉ ለማወቅና ድህረ-ገጹን ፈጣን ለማድረግ",
                    "የተቆለፉ ዳታቤዞችን ለመክፈት",
                    "የጽሁፉን ቀለም ወደ ሰማያዊ ለመቀየር",
                    "የ CSS መመሪያዎችን ለማሟላት",
                ],
                correct_option_index=0,
                hint_en="The `key` prop optimizes React's virtual DOM reconciliation algorithm!",
                hint_am="`key` ሪያክት የትኛው መረጃ እንደተጨመረ ወይም እንደተቀነሰ ለይቶ ድህረ-ገጹን እጅግ ፈጣን እንዲያደርገው ይረዳል!",
            ),
        ],
    ),
    TutorChapter(
        id="react_ch7",
        order=7,
        title_en="React Ch 7: Profile Card Capstone Project",
        title_am="ሪያክት ምዕራፍ 7፦ የኢንተራክቲቭ ካርድ ፕሮጀክት",
        description_en="Assemble components, objects, classes, and JSX into a production web card.",
        description_am="ኮምፖነንቶችን፣ መረጃዎችን እና JSX በማጣመር ሙሉ የድህረ-ገጽ ፕሮፋይል ካርድ መስራት።",
        track="react",
        steps=[
            TutorStep(
                id="react_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Building a Production React Card!* 🌟\n\n"
                    "Notice one important JSX detail: In standard HTML, we write `class=\"card\"`. "
                    "In React JSX, because `class` is a reserved JavaScript keyword, we use **`className=\"card\"`**!\n\n"
                    "Now, let's combine:\n"
                    "1. Functional components\n"
                    "2. JavaScript objects (`user`)\n"
                    "3. Curly brace `{ }` interpolation\n"
                    "4. Modern clean JSX structure!"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የሪያክት ፕሮፋይል ካርድ!* 🌟\n\n"
                    "አንድ ወሳኝ የ JSX ህግ፦ በመደበኛ HTML ላይ `class=\"card\"` ይጻፋል። "
                    "በሪያክት ውስጥ ግን `class` የጃቫስክሪፕት የተከለከለ ቃል ስለሆነ **`className=\"card\"`** ተብሎ ይጻፋል!\n\n"
                    "አሁን የሚከተሉትን እናጣምራለን፦\n"
                    "1. የኮምፖነንት ፈንክሽን\n"
                    "2. የጃቫስክሪፕት ኦብጀክት (`user`)\n"
                    "3. የፈረንሳይ ቅንፍ `{ }` መረጃ ማሳያ\n"
                    "4. የተስተካከለ ዘመናዊ JSX መዋቅር!"
                ),
            ),
            TutorStep(
                id="react_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `ProfileCard` component rendering a user's name and role in a `className=\"card\"` container!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction ProfileCard() {\n    const user = { name: \"Liya\", role: \"Developer\" };\n    return (\n        <div className=\"card\">\n            <h2>{user.name}</h2>\n            <p>{user.role}</p>\n        </div>\n    );\n}\n```"
                ),
                message_am=(
                    "`ProfileCard` የሚል ኮምፖነንት ጽፈው የተጠቃሚውን ስምና የስራ ሚና በ `className=\"card\"` ውስጥ አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction ProfileCard() {\n    const user = { name: \"Liya\", role: \"Developer\" };\n    return (\n        <div className=\"card\">\n            <h2>{user.name}</h2>\n            <p>{user.role}</p>\n        </div>\n    );\n}\n```"
                ),
                expected_code_output='<div class="card"><h2>Liya</h2><p>Developer</p></div>',
                hint_en='Write `ProfileCard` returning `<div className="card"><h2>{user.name}</h2><p>{user.role}</p></div>`',
                hint_am='`ProfileCard` ፈጥረው በ `className="card"` ውስጥ ስምና ሚናውን በ `<h2>` እና `<p>` አሳይተው ይላኩ።',
                success_message_en=(
                    "🏆 *MASTER OF REACT!* You have officially built a real, modern React component and virtual DOM tree!"
                ),
                success_message_am=(
                    "🏆 *የሪያክት ባለሙያ!* እውነተኛ ዘመናዊ የሪያክት ኮምፖነንት ገንብተው በተሳካ ሁኔታ አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="react_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! REACT GRADUATE!** 🌟🎓\n\n"
                    "You have mastered the frontend engine of the modern web:\n"
                    "1. ⚛️ Virtual DOM & JSX syntax\n"
                    "2. 🧱 Building Capitalized functional components\n"
                    "3. 🪄 Dynamic JavaScript interpolation with `{ }`\n"
                    "4. 🎁 Reusable custom UI with `props`\n"
                    "5. 🚦 Smart conditional rendering with `? :`\n"
                    "6. 📋 Dynamic data iteration with `.map()` & `key`\n"
                    "7. 🏗️ Modern UI assembly with `className` and cards!\n\n"
                    "You are now ready to build real-world web apps with React! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የሪያክት (React) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "የዘመናዊ ድህረ-ገጽ ግንባታ ቁንጮ የሆነውን ሪያክት በሚገባ ተምረዋል፦\n"
                    "1. ⚛️ የቨርቹዋል DOM እና JSX አጻጻፍ\n"
                    "2. 🧱 በካፒታል የሚጀምሩ ፈንክሽናል ኮምፖነንቶች\n"
                    "3. 🪄 መረጃዎችን በፈረንሳይ ቅንፍ `{ }` ማሳየት\n"
                    "4. 🎁 ተለዋዋጭ መረጃዎችን በ `props` ማስተላለፍ\n"
                    "5. 🚦 ሁኔታዎችን አይቶ መወሰን በ `? :`\n"
                    "6. 📋 ዝርዝሮችን በ `.map()` እና በ `key` ማውጣት\n"
                    "7. 🏗️ ሙሉ የድህረ-ገጽ ካርዶችን በ `className` መገንባት!\n\n"
                    "አሁን እውነተኛ የድህረ-ገጽ አፕሊኬሽኖችን በሪያክት ለመገንባት ሙሉ በሙሉ ዝግጁ ነዎት! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_react_chapters() -> List[TutorChapter]:
    """Return all React tutor chapters ordered."""
    return sorted(REACT_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_react_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve React tutor chapter by ID."""
    for ch in REACT_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_react_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next React chapter ID."""
    chapters = get_all_react_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
