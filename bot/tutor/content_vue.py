"""Vue.js curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

VUE_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="vue_ch1",
        order=1,
        title_en="Vue Ch 1: Meet Vue.js & {{ Interpolation }}",
        title_am="ቪው ምዕራፍ 1፦ ከቪው ጋር መተዋወቅ እና {{ Interpolation }}",
        description_en="Learn the progressive, approachable frontend framework loved by developers worldwide.",
        description_am="በቀላሉ የሚለመደውን እና በዓለም ዙሪያ ተወዳጅ የሆነውን ቪው ጄኤስ (Vue.js) ይማሩ።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "💚 *Welcome to Vue.js!* ⚡✨\n\n"
                    "Created by Evan You, **Vue.js** is celebrated worldwide as the most approachable, friendly, and progressive frontend framework!\n\n"
                    "Vue bridges the simplicity of plain HTML/CSS with the full power of modern reactive JavaScript.\n\n"
                    "A Vue component typically defines:\n"
                    "- An HTML `template` describing the UI\n"
                    "- A `data()` function returning reactive state\n\n"
                    "To display reactive text, Vue uses **Double Curly Braces `{{ }}`** (mustache syntax):\n\n"
                    "```javascript\n{\n  template: `<h1>Hello {{ name }}!</h1>`,\n  data() {\n    return { name: 'Vue.js' };\n  }\n}\n```"
                ),
                message_am=(
                    "💚 *እንኳን ወደ ቪው ጄኤስ (Vue.js) በደህና መጡ!* ⚡✨\n\n"
                    "በኢቫን ዩ የተፈጠረው **Vue.js** ለመማር እጅግ ቀላል፣ ግልጽ እና ምቹ በመሆኑ በዓለም ዙሪያ በገንቢዎች ዘንድ እጅግ የተወደደ ነው!\n\n"
                    "ቪው የቀላል HTML አሰራርን ከዘመናዊ ሪአክቲቭ የጃቫስክሪፕት ሃይል ጋር ያጣምራል።\n\n"
                    "የቪው ኮምፖነንት በዋናነት የሚከተሉትን ያካትታል፦\n"
                    "- ምስሉን የሚያሳየው `template`\n"
                    "- ተለዋዋጭ መረጃዎችን የሚያዘጋጀው `data()` ፈንክሽን\n\n"
                    "መረጃን በስክሪኑ ላይ ለማውጣት ቪው **ድርብ የፈረንሳይ ቅንፍ `{{ }}`** ይጠቀማል፦\n\n"
                    "```javascript\n{\n  template: `<h1>Hello {{ name }}!</h1>`,\n  data() {\n    return { name: 'Vue.js' };\n  }\n}\n```"
                ),
            ),
            TutorStep(
                id="vue_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first Vue component displaying `<h1>Hello {{ name }}!</h1>`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<h1>Hello {{ name }}!</h1>`,\n  data() {\n    return { name: 'Vue.js' };\n  }\n}\n```"
                ),
                message_am=(
                    "`<h1>Hello {{ name }}!</h1>` የሚያሳይ የመጀመሪያውን የቪው ኮምፖነንት እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<h1>Hello {{ name }}!</h1>`,\n  data() {\n    return { name: 'Vue.js' };\n  }\n}\n```"
                ),
                expected_code_output="<h1>Hello Vue.js!</h1>",
                hint_en="Write the component object with `template` and `data()` returning `name: 'Vue.js'`.",
                hint_am="`template` እና `data()` በማካተት `name: 'Vue.js'` የሚመልስ የቪው ኮድ ይላኩ።",
                success_message_en=(
                    "🎉 *LOOK AT THAT!* You just rendered real reactive Vue.js 3 virtual DOM!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* እውነተኛ የቪው ጄኤስ (Vue.js 3) ኮድ በስኬት ሰርቶ ወጥቷል!"
                ),
            ),
            TutorStep(
                id="vue_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "What syntax does Vue.js use to inject dynamic data into HTML templates?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በቪው (Vue.js) ውስጥ መረጃዎችን በቴምፕሌት ውስጥ ለማሳየት የትኛው ምልክት ያገለግላል?"
                ),
                options_en=[
                    "{{ message }} (Double curly braces)",
                    "{ message } (Single curly brace)",
                    "${ message } (Template string)",
                    "#message# (Hash marks)",
                ],
                options_am=[
                    "{{ message }} (ድርብ የፈረንሳይ ቅንፍ)",
                    "{ message } (ነጠላ የፈረንሳይ ቅንፍ)",
                    "${ message } (የዶላር ምልክት)",
                    "#message# (የሃሽ ምልክት)",
                ],
                correct_option_index=0,
                hint_en="Double curly braces `{{ }}` bind data reactively into templates!",
                hint_am="ድርብ የፈረንሳይ ቅንፍ `{{ }}` መረጃን በቴምፕሌቱ ውስጥ ለማሳየት ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch2",
        order=2,
        title_en="Vue Ch 2: Reactive State with data()",
        title_am="ቪው ምዕራፍ 2፦ ሪአክቲቭ ዳታ በ data()",
        description_en="Manage component numbers, counts, and reactive state.",
        description_am="የኮምፖነንት መረጃዎችን እና ቁጥሮችን በ `data()` ማስተዳደር።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *The `data()` Option in Vue* 📊\n\n"
                    "In Vue's Options API, the `data()` function returns an object containing all reactive state:\n\n"
                    "```javascript\n{\n  template: `<h2>Likes: {{ count }}</h2>`,\n  data() {\n    return { count: 42 };\n  }\n}\n```\n\n"
                    "Vue automatically tracks dependencies. Whenever `count` changes, the UI updates instantly!"
                ),
                message_am=(
                    "📦 *የ `data()` አማራጭ በቪው* 📊\n\n"
                    "በቪው ውስጥ የ `data()` ፈንክሽን ሁሉንም ተለዋዋጭ መረጃዎች የያዘ ኦብጀክት ይመልሳል፦\n\n"
                    "```javascript\n{\n  template: `<h2>Likes: {{ count }}</h2>`,\n  data() {\n    return { count: 42 };\n  }\n}\n```\n\n"
                    "ቪው የመረጃዎችን ለውጥ በራስ-ሰር ይከታተላል፤ `count` በተቀየረ ቅጽበት ስክሪኑ ወዲያውኑ ይታደሳል!"
                ),
            ),
            TutorStep(
                id="vue_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a component displaying `<h2>Likes: {{ count }}</h2>` with `count: 42`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<h2>Likes: {{ count }}</h2>`,\n  data() {\n    return { count: 42 };\n  }\n}\n```"
                ),
                message_am=(
                    "`count: 42` በማድረግ `<h2>Likes: {{ count }}</h2>` የሚያሳይ የቪው ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<h2>Likes: {{ count }}</h2>`,\n  data() {\n    return { count: 42 };\n  }\n}\n```"
                ),
                expected_code_output="<h2>Likes: 42</h2>",
                hint_en="Write `template: '<h2>Likes: {{ count }}</h2>'` and return `{ count: 42 }` in `data()`.",
                hint_am="`template: '<h2>Likes: {{ count }}</h2>'` እና በ `data()` ውስጥ `count: 42` አድርገው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* Vue resolved the reactive count and rendered `<h2>Likes: 42</h2>`!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* ቪው መረጃውን አንብቦ `<h2>Likes: 42</h2>` ብሎ በስክሪኑ ላይ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="vue_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "What must the `data` option in a Vue component be?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በቪው ኮምፖነንት ውስጥ `data` ምን አይነት መሆን አለበት?"
                ),
                options_en=[
                    "A function that returns an object",
                    "A plain number",
                    "A SQL query string",
                    "A CSS stylesheet",
                ],
                options_am=[
                    "ኦብጀክት የሚመልስ ፈንክሽን",
                    "ተራ ቁጥር",
                    "የ SQL ትዕዛዝ",
                    "የ CSS ስታይል",
                ],
                correct_option_index=0,
                hint_en="In components, `data()` is always a function so each instance gets a clean copy of state!",
                hint_am="በኮምፖነንቶች ውስጥ እያንዳንዱ ክፍል የራሱ ገለልተኛ ዳታ እንዲኖረው `data()` ሁልጊዜ ፈንክሽን ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch3",
        order=3,
        title_en="Vue Ch 3: Attribute Binding with v-bind & :",
        title_am="ቪው ምዕራፍ 3፦ የባህሪ ማሰሪያ በ v-bind እና :",
        description_en="Bind HTML attributes and states dynamically with colon shorthand.",
        description_am="የድህረ-ገጽ ኤለመንት ባህሪያትን በኮለን `:` ምልክት ከኮድ ጋር ማሰር።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔗 *Attribute Binding: `v-bind:` or Shorthand `:`* 📦\n\n"
                    "In HTML, normal attribute values are static. To bind an attribute dynamically to JavaScript data, "
                    "Vue uses the `v-bind:` directive—or simply a colon (`:`):\n\n"
                    "```html\n<button :disabled=\"isDisabled\">Submit</button>\n```\n\n"
                    "- If `isDisabled` is `true`, the button is disabled!\n"
                    "- If `false`, the attribute is omitted.\n"
                    "- `:disabled` is clean, concise, and standard in all Vue apps!"
                ),
                message_am=(
                    "🔗 *የባህሪ ማሰሪያ፦ `v-bind:` ወይም አጭሩ የኮለን `:` ምልክት* 📦\n\n"
                    "በመደበኛ HTML ላይ የኤለመንት ባህሪያት ቋሚ ናቸው። ከዳታ ጋር ለማስተሳሰር ቪው `v-bind:` ወይም "
                    "በቀላሉ የኮለን (`:`) ምልክትን ይጠቀማል፦\n\n"
                    "```html\n<button :disabled=\"isDisabled\">Submit</button>\n```\n\n"
                    "- `isDisabled` እውነት (`true`) ከሆነ አዝራሩ ይሰናከላል!\n"
                    "- ሀሰት (`false`) ከሆነ አይሰናከልም።\n"
                    "- የኮለን (`:`) አጻጻፍ በሁሉም የቪው መተግበሪያዎች ውስጥ ዋነኛ መደበኛ መንገድ ነው!"
                ),
            ),
            TutorStep(
                id="vue_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Bind a button's disabled state with `:disabled=\"isDisabled\"` where `isDisabled: true`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<button :disabled=\"isDisabled\">Submit</button>`,\n  data() {\n    return { isDisabled: true };\n  }\n}\n```"
                ),
                message_am=(
                    "`isDisabled: true` በማድረግ አዝራሩን በ `:disabled=\"isDisabled\"` አስረው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<button :disabled=\"isDisabled\">Submit</button>`,\n  data() {\n    return { isDisabled: true };\n  }\n}\n```"
                ),
                expected_code_output="<button disabled>Submit</button>",
                hint_en='Write `template: \'<button :disabled="isDisabled">Submit</button>\'` with `isDisabled: true`.',
                hint_am='`<button :disabled="isDisabled">Submit</button>` በማለት በ `data()` ውስጥ `isDisabled: true` ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* Vue evaluated `:disabled` and added the HTML `disabled` attribute!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ቪው `:disabled` የሚለውን አንብቦ አዝራሩን በስክሪኑ ላይ አሰናክሎታል!"
                ),
            ),
            TutorStep(
                id="vue_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "What is the standard shorthand symbol for the `v-bind:` directive in Vue.js?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በቪው (Vue.js) ውስጥ የ `v-bind:` አጭር መለያ ምልክት የትኛው ነው?"
                ),
                options_en=[
                    ": (Colon)",
                    "@ (At sign)",
                    "# (Hash)",
                    "$ (Dollar)",
                ],
                options_am=[
                    ": (ኮለን)",
                    "@ (አት ምልክት)",
                    "# (ሃሽ)",
                    "$ (ዶላር)",
                ],
                correct_option_index=0,
                hint_en="The colon `:` is shorthand for `v-bind:` (e.g., `:src`, `:class`, `:disabled`)!",
                hint_am="የኮለን `:` ምልክት የ `v-bind:` አጭር መለያ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch4",
        order=4,
        title_en="Vue Ch 4: Event Handling with v-on & @",
        title_am="ቪው ምዕራፍ 4፦ ክስተቶች በ v-on እና @",
        description_en="Listen to button taps and clicks with the @ shorthand symbol.",
        description_am="የተጠቃሚዎችን ክሊክ እና ንክኪ በ `@` ምልክት ማስተናገድ።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *Event Handling: `v-on:` or Shorthand `@`* 🖱️\n\n"
                    "To listen to DOM events like button clicks, form submits, or keystrokes, "
                    "Vue provides the `v-on:` directive—with the popular shorthand `@`:\n\n"
                    "```html\n<button @click=\"count++\">Clicks: {{ count }}</button>\n```\n\n"
                    "- `@click` listens for clicks\n"
                    "- `count++` increments the reactive counter directly\n"
                    "- Quick summary: **`:` is for data, `@` is for events!**"
                ),
                message_am=(
                    "⚡ *የክስተቶች አያያዝ፦ `v-on:` ወይም አጭሩ የ `@` ምልክት* 🖱️\n\n"
                    "እንደ ክሊክ ወይም ጽሁፍ መላክ ያሉ ክስተቶችን ለማዳመጥ ቪው `v-on:` ወይም አጭሩን የ `@` ምልክት ይጠቀማል፦\n\n"
                    "```html\n<button @click=\"count++\">Clicks: {{ count }}</button>\n```\n\n"
                    "- `@click` ክሊክ ሲደረግ ያዳምጣል\n"
                    "- `count++` ቆጣሪውን በቀጥታ 1 ይጨምረዋል\n"
                    "- ፈጣን ማጠቃለያ፦ **`:` ለዳታ፣ `@` ለክስተቶች (Events)!**"
                ),
            ),
            TutorStep(
                id="vue_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a button with `@click=\"count++\"` displaying `Clicks: {{ count }}` with `count: 7`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<button @click=\"count++\">Clicks: {{ count }}</button>`,\n  data() {\n    return { count: 7 };\n  }\n}\n```"
                ),
                message_am=(
                    "`count: 7` በማድረግ በ `@click=\"count++\"` የተሳሰረ አዝራር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<button @click=\"count++\">Clicks: {{ count }}</button>`,\n  data() {\n    return { count: 7 };\n  }\n}\n```"
                ),
                expected_code_output="<button>Clicks: 7</button>",
                hint_en='Write `<button @click="count++">Clicks: {{ count }}</button>` with `count: 7`.',
                hint_am='`<button @click="count++">Clicks: {{ count }}</button>` በማለት በ `data()` ውስጥ `count: 7` ይላኩ።',
                success_message_en=(
                    "🎉 *TERRIFIC!* You wired a reactive click event listener in Vue!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* የክሊክ ክስተትን በቪው ኮምፖነንት ውስጥ በተሳካ ሁኔታ አሰሩ!"
                ),
            ),
            TutorStep(
                id="vue_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "What is the standard shorthand symbol for `v-on:` (event listening) in Vue?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በቪው ውስጥ ለክስተት ማዳመጫ (`v-on:`) አጭር መለያ የሆነው የትኛው ምልክት ነው?"
                ),
                options_en=[
                    "@ (At sign, e.g. @click)",
                    ": (Colon)",
                    "# (Hash)",
                    "! (Exclamation)",
                ],
                options_am=[
                    "@ (የአት ምልክት፣ ለምሳሌ፦ @click)",
                    ": (ኮለን)",
                    "# (ሃሽ)",
                    "! (የአጋኖ ምልክት)",
                ],
                correct_option_index=0,
                hint_en="The `@` symbol is shorthand for `v-on:`!",
                hint_am="የ `@` ምልክት የ `v-on:` አጭር መለያ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch5",
        order=5,
        title_en="Vue Ch 5: Conditional Rendering with v-if",
        title_am="ቪው ምዕራፍ 5፦ ሁኔታዎችን በ v-if መወሰን",
        description_en="Conditionally render or remove elements using the v-if directive.",
        description_am="ኤለመንቶች በሁኔታዎች ላይ ተመስርተው እንዲወጡ በ `v-if` መቆጣጠር።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Conditional Rendering: `v-if`* 🧠\n\n"
                    "The `v-if` directive conditionally renders an element only when its expression returns a truthy value:\n\n"
                    "```html\n<p v-if=\"isAwesome\">Vue is Awesome!</p>\n```\n\n"
                    "- If `isAwesome` is `true`, the text appears\n"
                    "- If `false`, Vue does not render the element into the DOM at all!"
                ),
                message_am=(
                    "🚦 *ሁኔታዎችን አይቶ ማሳየት፦ `v-if`* 🧠\n\n"
                    "`v-if` የተሰጠው መስፈርት እውነት ሲሆን ብቻ ኤለመንቱን በስክሪኑ ላይ ያወጣል፦\n\n"
                    "```html\n<p v-if=\"isAwesome\">Vue is Awesome!</p>\n```\n\n"
                    "- `isAwesome` እውነት (`true`) ከሆነ ጽሁፉ ይወጣል\n"
                    "- ሀሰት (`false`) ከሆነ ግን ከድህረ-ገጹ ላይ ሙሉ በሙሉ ይወገዳል!"
                ),
            ),
            TutorStep(
                id="vue_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a component with `<p v-if=\"isAwesome\">Vue is Awesome!</p>` where `isAwesome: true`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<p v-if=\"isAwesome\">Vue is Awesome!</p>`,\n  data() {\n    return { isAwesome: true };\n  }\n}\n```"
                ),
                message_am=(
                    "`isAwesome: true` በማድረግ በ `v-if=\"isAwesome\"` ሁኔታን የሚፈትሽ ኮድ ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<p v-if=\"isAwesome\">Vue is Awesome!</p>`,\n  data() {\n    return { isAwesome: true };\n  }\n}\n```"
                ),
                expected_code_output="<p>Vue is Awesome!</p>",
                hint_en='Write `<p v-if="isAwesome">Vue is Awesome!</p>` and return `{ isAwesome: true }` in `data()`.',
                hint_am='`<p v-if="isAwesome">Vue is Awesome!</p>` በማለት በ `data()` ውስጥ `isAwesome: true` ይላኩ።',
                success_message_en=(
                    "🔥 *OUTSTANDING!* Vue verified the condition and rendered the element!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* ቪው መስፈርቱ እውነት መሆኑን አረጋግጦ ጽሁፉን አውጥቷል!"
                ),
            ),
            TutorStep(
                id="vue_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "What happens to an HTML element when its `v-if` condition evaluates to `false`?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የ `v-if` መስፈርት ሀሰት (`false`) ሲሆን በኤለመንቱ ላይ ምን ይከሰታል?"
                ),
                options_en=[
                    "It is completely removed from the DOM document",
                    "It turns red",
                    "It sends an email",
                    "It reboots the browser",
                ],
                options_am=[
                    "ከድህረ-ገጹ ላይ ሙሉ በሙሉ ይወገዳል",
                    "ቀለሙ ወደ ቀይ ይቀየራል",
                    "ኢሜይል ይልካል",
                    "ብራውዘሩን ያጠፋዋል",
                ],
                correct_option_index=0,
                hint_en="`v-if` destroys and detaches the element from the DOM when false!",
                hint_am="`v-if` ሀሰት ሲሆን ኤለመንቱን ከድህረ-ገጹ ላይ ሙሉ በሙሉ ያጠፋዋል!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch6",
        order=6,
        title_en="Vue Ch 6: List Rendering with v-for",
        title_am="ቪው ምዕራፍ 6፦ ዝርዝሮችን በ v-for ማውጣት",
        description_en="Loop over arrays and collections to generate dynamic repeated elements.",
        description_am="የመረጃ ዝርዝሮችን በ `v-for` አማካኝነት በድህረ-ገጽ ላይ መደርደር።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📋 *List Rendering with `v-for`* 🔄\n\n"
                    "To display a list of items based on an array, Vue provides the `v-for` directive:\n\n"
                    "```html\n<ul>\n    <li v-for=\"item in items\" :key=\"item\">{{ item }}</li>\n</ul>\n```\n\n"
                    "- `item in items` iterates through each element\n"
                    "- `:key` gives Vue a unique identifier for optimal DOM updates!"
                ),
                message_am=(
                    "📋 *ዝርዝሮችን በ `v-for` ማውጣት* 🔄\n\n"
                    "የአሬይ መረጃዎችን በድህረ-ገጽ ላይ ለመደርደር ቪው `v-for` የተባለውን መመሪያ ይጠቀማል፦\n\n"
                    "```html\n<ul>\n    <li v-for=\"item in items\" :key=\"item\">{{ item }}</li>\n</ul>\n```\n\n"
                    "- `item in items` በእያንዳንዱ ዙር የአንድን እቃ ስም ይይዛል\n"
                    "- `:key` ደግሞ ቪው መረጃዎችን በፍጥነት እንዲያስተዳድር ልዩ መለያ ይሰጠዋል!"
                ),
            ),
            TutorStep(
                id="vue_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Render a list `<ul><li v-for=\"item in items\" :key=\"item\">{{ item }}</li></ul>` with 3 items!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\n{\n  template: `<ul><li v-for=\"item in items\" :key=\"item\">{{ item }}</li></ul>`,\n  data() {\n    return { items: ['Vue', 'Vite', 'Pinia'] };\n  }\n}\n```"
                ),
                message_am=(
                    "3 የቪው መሳሪያዎችን በ `v-for` የሚያሳይ ዝርዝር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<ul><li v-for=\"item in items\" :key=\"item\">{{ item }}</li></ul>`,\n  data() {\n    return { items: ['Vue', 'Vite', 'Pinia'] };\n  }\n}\n```"
                ),
                expected_code_output="<ul><li>Vue</li><li>Vite</li><li>Pinia</li></ul>",
                hint_en="Use `v-for=\"item in items\"` inside `<ul>...</ul>` with the array returned in `data()`.",
                hint_am="በ `<ul>` ውስጥ `v-for=\"item in items\"` በማድረግ አሬዩን በ `data()` መልሰው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* Vue looped through your array and stamped out list items!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* ቪው አሬዩን አንብቦ ለእያንዳንዱ መረጃ የዝርዝር ታግ አውጥቷል!"
                ),
            ),
            TutorStep(
                id="vue_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which Vue directive is used to render a list of items by iterating over an array?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በቪው ውስጥ አሬይን በማዞር ዝርዝር ኤለመንቶችን ለማውጣት የትኛው መመሪያ ያገለግላል?"
                ),
                options_en=[
                    "v-for",
                    "v-loop",
                    "v-repeat",
                    "v-each",
                ],
                options_am=[
                    "v-for",
                    "v-loop",
                    "v-repeat",
                    "v-each",
                ],
                correct_option_index=0,
                hint_en="The directive is `v-for`!",
                hint_am="መመሪያው `v-for` ይባላል!",
            ),
        ],
    ),
    TutorChapter(
        id="vue_ch7",
        order=7,
        title_en="Vue Ch 7: Profile Card Capstone Project",
        title_am="ቪው ምዕራፍ 7፦ የቪው ፕሮፋይል ካርድ ፕሮጀክት",
        description_en="Combine templates, data(), interpolation, and styling into a production Vue card.",
        description_am="ቴምፕሌት፣ ዳታ እና ኢንተርፖሌሽንን በማጣመር የተሟላ የቪው ካርድ መስራት።",
        track="vue",
        steps=[
            TutorStep(
                id="vue_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Building a Vue Profile Card!* 🌟\n\n"
                    "Let's combine everything you've learned into a complete production Vue component:\n"
                    "1. Clean HTML template with classes\n"
                    "2. Nested object state in `data()`: `user: { name: 'Liya', role: 'Vue Architect' }`\n"
                    "3. Mustache interpolation `{{ user.name }}` and `{{ user.role }}`\n"
                    "4. Production component structure!"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የቪው ፕሮፋይል ካርድ!* 🌟\n\n"
                    "እስካሁን የተማርነውን በሙሉ በማጣመር የተሟላ የቪው ካርድ እንገነባለን፦\n"
                    "1. የተስተካከለ የ HTML ቴምፕሌት\n"
                    "2. በ `data()` ውስጥ ያለ ኦብጀክት፦ `user: { name: 'Liya', role: 'Vue Architect' }`\n"
                    "3. ድርብ የፈረንሳይ ቅንፍ ማሳያ `{{ user.name }}` እና `{{ user.role }}`\n"
                    "4. የተሟላ የኮምፖነንት መዋቅር!"
                ),
            ),
            TutorStep(
                id="vue_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a component rendering `<div class=\"card\"><h2>{{ user.name }}</h2><p>Role: {{ user.role }}</p></div>`!\n\n"
                    "👇 *Type and send:*\n"
                    "```javascript\n{\n  template: `<div class=\"card\"><h2>{{ user.name }}</h2><p>Role: {{ user.role }}</p></div>`,\n  data() {\n    return {\n      user: { name: 'Liya', role: 'Vue Architect' }\n    };\n  }\n}\n```"
                ),
                message_am=(
                    "`user: { name: 'Liya', role: 'Vue Architect' }` የያዘ የቪው ፕሮፋይል ካርድ ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\n{\n  template: `<div class=\"card\"><h2>{{ user.name }}</h2><p>Role: {{ user.role }}</p></div>`,\n  data() {\n    return {\n      user: { name: 'Liya', role: 'Vue Architect' }\n    };\n  }\n}\n```"
                ),
                expected_code_output='<div class="card"><h2>Liya</h2><p>Role: Vue Architect</p></div>',
                hint_en='Write the component with the card template and nested user object in data().',
                hint_am='በካርዱ ውስጥ `{{ user.name }}` እና `{{ user.role }}` በማሳየት ይላኩ።',
                success_message_en=(
                    "🏆 *VUE.JS MASTER!* You have officially built a production-ready Vue 3 component!"
                ),
                success_message_am=(
                    "🏆 *የቪው (Vue.js) ባለሙያ!* እውነተኛ ዘመናዊ የቪው 3 ኮምፖነንት ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="vue_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! VUE.JS GRADUATE!** 🌟🎓\n\n"
                    "You have conquered the progressive frontend framework:\n"
                    "1. 💚 Component templates & `{{ }}` interpolation\n"
                    "2. 📦 Reactive state management with `data()`\n"
                    "3. 🔗 Attribute binding with `:bind` shorthand\n"
                    "4. ⚡ Event handling with `@click` shorthand\n"
                    "5. 🚦 Conditional rendering with `v-if`\n"
                    "6. 📋 Dynamic list looping with `v-for` and `:key`\n"
                    "7. 🏗️ Modern UI profile card assembly!\n\n"
                    "You now know all of the Big Three frontend frameworks: **React, Angular, AND Vue.js**! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የቪው (Vue.js) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "ተወዳጁን የድህረ-ገጽ ፍሬምወርክ በሚገባ ተምረዋል፦\n"
                    "1. 💚 የኮምፖነንት ቴምፕሌት እና `{{ }}` ኢንተርፖሌሽን\n"
                    "2. 📦 ሪአክቲቭ ዳታ በ `data()`\n"
                    "3. 🔗 የባህሪ ማሰሪያ በኮለን `:`\n"
                    "4. ⚡ ክስተቶች በ `@click`\n"
                    "5. 🚦 ሁኔታዎችን በ `v-if` መቆጣጠር\n"
                    "6. 📋 ዝርዝሮችን በ `v-for` እና በ `:key` ማውጣት\n"
                    "7. 🏗️ የተሟሉ የድህረ-ገጽ ካርዶችን መገንባት!\n\n"
                    "አሁን ሦስቱንም ታላላቅ የድህረ-ገጽ ፊት መገንቢያዎች አጠናቀዋል፦ **React፣ Angular፣ እና Vue.js**! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_vue_chapters() -> List[TutorChapter]:
    """Return all Vue tutor chapters ordered."""
    return sorted(VUE_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_vue_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve Vue tutor chapter by ID."""
    for ch in VUE_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_vue_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next Vue chapter ID."""
    chapters = get_all_vue_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
