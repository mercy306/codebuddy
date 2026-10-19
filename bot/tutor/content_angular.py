"""Angular enterprise curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

ANGULAR_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="ng_ch1",
        order=1,
        title_en="Angular Ch 1: Welcome to Angular & {{ Interpolation }}",
        title_am="አንጉላር ምዕራፍ 1፦ ከአንጉላር ጋር መተዋወቅ እና Interpolation",
        description_en="Learn Google's enterprise framework for building robust, scalable web applications.",
        description_am="በጉግል (Google) የተሰራውን እና ለትላልቅ ተቋማት የሚሆነውን አንጉላር (Angular) ቋንቋ ይማሩ።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🅰️ *Welcome to Angular!* 🛡️⚡\n\n"
                    "Developed and maintained by **Google**, Angular is the enterprise titan of frontend web development!\n\n"
                    "Thousands of top banks, airlines, healthcare portals, and enterprise dashboards rely on Angular "
                    "because of its rock-solid TypeScript architecture and powerful built-in tooling.\n\n"
                    "In Angular, an application is composed of **Components**:\n"
                    "- A TypeScript class that manages the data (`name = 'Angular'`)\n"
                    "- An HTML template that defines the UI\n\n"
                    "To display dynamic data on the screen, Angular uses **Template Interpolation** with double curly braces `{{ }}`:\n\n"
                    "```typescript\n@Component({\n  selector: 'app-welcome',\n  template: `<h1>Hello {{ name }}!</h1>`\n})\nexport class WelcomeComponent {\n  name = 'Angular';\n}\n```"
                ),
                message_am=(
                    "🅰️ *እንኳን ወደ አንጉላር (Angular) በደህና መጡ!* 🛡️⚡\n\n"
                    "በ **ጉግል (Google)** የተሰራው እና የሚመራው አንጉላር ለትላልቅ የድርጅት፣ የባንክ እና የመንግስት ድህረ-ገጾች "
                    "ዋነኛ መሪ የሆነ የፍሮንት-ኤንድ ፍሬምወርክ ነው!\n\n"
                    "አንጉላር የሚገነባው በታይፕስክሪፕት (TypeScript) ላይ ሲሆን እጅግ ጠንካራና አስተማማኝ ስርዓት አለው።\n\n"
                    "በአንጉላር ውስጥ መተግበሪያዎች የሚሰሩት በ **ኮምፖነንቶች (Components)** ነው፦\n"
                    "- መረጃዎችን የሚይዝ የታይፕስክሪፕት ክላስ (`name = 'Angular'`)\n"
                    "- ምስሉን የሚያሳየው የ HTML ቴምፕሌት\n\n"
                    "መረጃዎችን በስክሪኑ ላይ ለማውጣት አንጉላር በድርብ የፈረንሳይ ቅንፍ **Interpolation `{{ }}`** ይጠቀማል፦\n\n"
                    "```typescript\n@Component({\n  selector: 'app-welcome',\n  template: `<h1>Hello {{ name }}!</h1>`\n})\nexport class WelcomeComponent {\n  name = 'Angular';\n}\n```"
                ),
            ),
            TutorStep(
                id="ng_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first Angular component displaying `<h1>Hello {{ name }}!</h1>`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```typescript\n@Component({\n  selector: 'app-welcome',\n  template: `<h1>Hello {{ name }}!</h1>`\n})\nexport class WelcomeComponent {\n  name = 'Angular';\n}\n```"
                ),
                message_am=(
                    "`<h1>Hello {{ name }}!</h1>` የሚያሳይ የመጀመሪያውን የአንጉላር ኮምፖነንት እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-welcome',\n  template: `<h1>Hello {{ name }}!</h1>`\n})\nexport class WelcomeComponent {\n  name = 'Angular';\n}\n```"
                ),
                expected_code_output="<h1>Hello Angular!</h1>",
                hint_en="Write the `@Component` with `template: '<h1>Hello {{ name }}!</h1>'` and `name = 'Angular';`",
                hint_am="`@Component` ጽፈው በ `template` ውስጥ `{{ name }}` እና በክላሱ ውስጥ `name = 'Angular';` በማድረግ ይላኩ።",
                success_message_en=(
                    "🎉 *BRAVO!* You just defined and rendered your first enterprise Angular component!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* የመጀመሪያውን የአንጉላር ኮምፖነንት በተሳካ ሁኔታ ሰርተው አስኬደዋል!"
                ),
            ),
            TutorStep(
                id="ng_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "Which syntax is used in Angular templates to display component data on screen (Interpolation)?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በአንጉላር ቴምፕሌት ውስጥ መረጃን በስክሪኑ ላይ ለማሳየት (Interpolation) የትኛው ምልክት ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "{{ propertyName }} (double curly braces)",
                    "{ propertyName } (single curly brace)",
                    "${ propertyName } (dollar sign)",
                    "[[ propertyName ]] (double square brackets)",
                ],
                options_am=[
                    "{{ propertyName }} (ድርብ የፈረንሳይ ቅንፍ)",
                    "{ propertyName } (ነጠላ የፈረንሳይ ቅንፍ)",
                    "${ propertyName } (የዶላር ምልክት)",
                    "[[ propertyName ]] (ድርብ የካሬ ቅንፍ)",
                ],
                correct_option_index=0,
                hint_en="Angular uses double curly braces `{{ }}`, affectionately called 'mustache syntax'!",
                hint_am="አንጉላር መረጃን ለማሳየት ድርብ የፈረንሳይ ቅንፍ `{{ }}` ይጠቀማል!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch2",
        order=2,
        title_en="Angular Ch 2: Component Properties & State",
        title_am="አንጉላር ምዕራፍ 2፦ የኮምፖነንት ዳታ እና ተለዋዋጮች",
        description_en="Manage component numbers, strings, and statistics in the TypeScript class.",
        description_am="በታይፕስክሪፕት ክላስ ውስጥ ቁጥሮችን እና የዳሽቦርድ መረጃዎችን ማስተዳደር።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *Component Properties & Data* 📊\n\n"
                    "In Angular, the TypeScript class is the source of truth for your component's state:\n\n"
                    "```typescript\nexport class StatsComponent {\n  count = 100;\n}\n```\n\n"
                    "Whenever the template encounters `{{ count }}`, Angular reads the property directly from the class instance and displays `100`!"
                ),
                message_am=(
                    "📦 *የኮምፖነንት ዳታ እና ተለዋዋጮች* 📊\n\n"
                    "በአንጉላር ውስጥ የታይፕስክሪፕት ክላሱ የኮምፖነንቱ ዋና የመረጃ ማዕከል ነው፦\n\n"
                    "```typescript\nexport class StatsComponent {\n  count = 100;\n}\n```\n\n"
                    "ቴምፕሌቱ `{{ count }}` ሲያገኝ አንጉላር ከክላሱ ውስጥ ቁጥሩን አንብቦ `100` ብሎ ያሳያል!"
                ),
            ),
            TutorStep(
                id="ng_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `StatsComponent` displaying `<h2>Active Users: {{ count }}</h2>` with `count = 100;`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```typescript\n@Component({\n  selector: 'app-stats',\n  template: `<h2>Active Users: {{ count }}</h2>`\n})\nexport class StatsComponent {\n  count = 100;\n}\n```"
                ),
                message_am=(
                    "`count = 100;` የያዘ `StatsComponent` ፈጥረው `<h2>Active Users: {{ count }}</h2>` አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-stats',\n  template: `<h2>Active Users: {{ count }}</h2>`\n})\nexport class StatsComponent {\n  count = 100;\n}\n```"
                ),
                expected_code_output="<h2>Active Users: 100</h2>",
                hint_en="Write the component with `template: '<h2>Active Users: {{ count }}</h2>'` and `count = 100;`",
                hint_am="`template: '<h2>Active Users: {{ count }}</h2>'` እና በክላሱ ውስጥ `count = 100;` በማድረግ ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* Angular resolved the class property and updated the template!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* አንጉላር የክላሱን መረጃ አንብቦ በስክሪኑ ላይ በትክክል አሳይቷል!"
                ),
            ),
            TutorStep(
                id="ng_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Which programming language is used to write Angular component classes?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የአንጉላር ኮምፖነንት ክላሶችን ለመጻፍ የትኛው የፕሮግራሚንግ ቋንቋ ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "TypeScript (strictly typed JavaScript)",
                    "PHP",
                    "C++",
                    "Perl",
                ],
                options_am=[
                    "ታይፕስክሪፕት (TypeScript)",
                    "ፒኤችፒ (PHP)",
                    "ሲ++ (C++)",
                    "ፐርል (Perl)",
                ],
                correct_option_index=0,
                hint_en="Angular is built from the ground up on TypeScript!",
                hint_am="አንጉላር ከመሰረቱ የተገነባው በታይፕስክሪፕት (TypeScript) ላይ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch3",
        order=3,
        title_en="Angular Ch 3: Property Binding with [ ]",
        title_am="አንጉላር ምዕራፍ 3፦ የፕሮፐርቲ ማሰሪያ በካሬ ቅንፍ [ ]",
        description_en="Bind HTML attributes directly to TypeScript variables using square brackets.",
        description_am="የድህረ-ገጽ ኤለመንት ንብረቶችን በካሬ ቅንፍ `[ ]` ከኮድ ጋር ማስተሳሰር።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔗 *Property Binding: Square Brackets `[ ]`* 📦\n\n"
                    "In HTML, an attribute value is normally just static text. "
                    "In Angular, wrapping an attribute in square brackets `[ ]` tells Angular: *'Bind this attribute directly to my TypeScript variable!'*\n\n"
                    "```html\n<button [disabled]=\"isDisabled\">Submit</button>\n```\n\n"
                    "- If `isDisabled` is `true`, the button becomes disabled!\n"
                    "- If `isDisabled` is `false`, the button is enabled!\n"
                    "- Memory hook: **Square brackets `[ ]` = Target to Property**"
                ),
                message_am=(
                    "🔗 *የፕሮፐርቲ ማሰሪያ፦ የካሬ ቅንፍ `[ ]`* 📦\n\n"
                    "በመደበኛ HTML ላይ የኤለመንት ንብረቶች ቋሚ ናቸው። "
                    "በአንጉላር ውስጥ ግን ንብረቱን በካሬ ቅንፍ `[ ]` ስናቅፈው ከታይፕስክሪፕት ተለዋዋጩ ጋር በቀጥታ ይተሳሰራል፦\n\n"
                    "```html\n<button [disabled]=\"isDisabled\">Submit</button>\n```\n\n"
                    "- `isDisabled` እውነት (`true`) ከሆነ አዝራሩ ይሰናከላል (Disabled ይሆናል)!\n"
                    "- `isDisabled` ሀሰት (`false`) ከሆነ አዝራሩ ይሰራል!\n"
                    "- ማስታወሻ፦ **የካሬ ቅንፍ `[ ]` መረጃን ከክላስ ወደ ኤለመንት ያስተላልፋል**"
                ),
            ),
            TutorStep(
                id="ng_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Bind a button's disabled state with `[disabled]=\"isDisabled\"` where `isDisabled = true;`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```typescript\n@Component({\n  selector: 'app-btn',\n  template: `<button [disabled]=\"isDisabled\">Submit</button>`\n})\nexport class BtnComponent {\n  isDisabled = true;\n}\n```"
                ),
                message_am=(
                    "`isDisabled = true;` በማድረግ የአዝራሩን ሁኔታ በ `[disabled]=\"isDisabled\"` አስረው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-btn',\n  template: `<button [disabled]=\"isDisabled\">Submit</button>`\n})\nexport class BtnComponent {\n  isDisabled = true;\n}\n```"
                ),
                expected_code_output="<button disabled>Submit</button>",
                hint_en='Write `template: \'<button [disabled]="isDisabled">Submit</button>\'` with `isDisabled = true;`',
                hint_am='`<button [disabled]="isDisabled">Submit</button>` ብለው በክላሱ ውስጥ `isDisabled = true;` በማድረግ ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* Angular evaluated `[disabled]` and disabled the HTML button!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* አንጉላር `[disabled]` የሚለውን አንብቦ አዝራሩን በስክሪኑ ላይ አሰናክሎታል!"
                ),
            ),
            TutorStep(
                id="ng_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "Which bracket type is used in Angular templates for Property Binding (data flowing from component to DOM)?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በአንጉላር ውስጥ መረጃን ከኮድ ወደ HTML ኤለመንት ለማሰር የትኛው ቅንፍ ጥቅም ላይ ይውላል?"
                ),
                options_en=[
                    "[ ] (Square brackets)",
                    "( ) (Parentheses)",
                    "{ } (Curly braces)",
                    "< > (Angle brackets)",
                ],
                options_am=[
                    "[ ] (የካሬ ቅንፍ)",
                    "( ) (መደበኛ ቅንፍ)",
                    "{ } (የፈረንሳይ ቅንፍ)",
                    "< > (የአንግል ቅንፍ)",
                ],
                correct_option_index=0,
                hint_en="Square brackets `[ ]` bind properties to the DOM!",
                hint_am="የካሬ ቅንፍ `[ ]` መረጃን ወደ ድህረ-ገጹ ለማሰር ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch4",
        order=4,
        title_en="Angular Ch 4: Event Binding with ( )",
        title_am="አንጉላር ምዕራፍ 4፦ ክስተቶች እና ክሊክ በቅንፍ ( )",
        description_en="Listen to button clicks and user interactions using parentheses.",
        description_am="የተጠቃሚዎችን ክሊክ እና ንክኪ በቅንፍ `( )` መቀበል።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *Event Binding: Parentheses `( )`* 🖱️\n\n"
                    "While square brackets `[ ]` send data INTO the DOM, "
                    "**parentheses `( )` listen for events coming OUT of the DOM**!\n\n"
                    "```html\n<button (click)=\"increment()\">Clicks: {{ count }}</button>\n```\n\n"
                    "- `(click)` listens for the mouse click event\n"
                    "- `increment()` calls the method inside your TypeScript class\n"
                    "- Rule of thumb: **Parentheses `( )` = Events & Actions**"
                ),
                message_am=(
                    "⚡ *የክስተቶች ማሰሪያ፦ መደበኛ ቅንፍ `( )`* 🖱️\n\n"
                    "የካሬ ቅንፍ `[ ]` መረጃን ወደ ድህረ-ገጹ ሲልክ፣ "
                    "**መደበኛ ቅንፍ `( )` ደግሞ ከተጠቃሚው የሚመጡ ክስተቶችን (Events) ያዳምጣል**!\n\n"
                    "```html\n<button (click)=\"increment()\">Clicks: {{ count }}</button>\n```\n\n"
                    "- `(click)` የክሊክ ክስተትን ያዳምጣል\n"
                    "- `increment()` በታይፕስክሪፕት ክላስ ውስጥ ያለውን ፈንክሽን ይጠራል\n"
                    "- ማስታወሻ፦ **መደበኛ ቅንፍ `( )` ለክስተቶች እና ለተግባር ያገለግላል**"
                ),
            ),
            TutorStep(
                id="ng_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a button with `(click)=\"increment()\"` displaying `Clicks: {{ count }}` with `count = 5;`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```typescript\n@Component({\n  selector: 'app-counter',\n  template: `<button (click)=\"increment()\">Clicks: {{ count }}</button>`\n})\nexport class CounterComponent {\n  count = 5;\n}\n```"
                ),
                message_am=(
                    "`count = 5;` በማድረግ በ `(click)=\"increment()\"` የተሳሰረ አዝራር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-counter',\n  template: `<button (click)=\"increment()\">Clicks: {{ count }}</button>`\n})\nexport class CounterComponent {\n  count = 5;\n}\n```"
                ),
                expected_code_output='<button (click)="increment()">Clicks: 5</button>',
                hint_en='Write `(click)="increment()"` with `Clicks: {{ count }}` and `count = 5;`',
                hint_am='`template: \'<button (click)="increment()">Clicks: {{ count }}</button>\'` በማድረግ ይላኩ።',
                success_message_en=(
                    "🎉 *TERRIFIC!* You wired event binding and template interpolation together!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* የክስተት ማሰሪያን እና የዳታ ማሳያን በአንድ ላይ አጣመሩ!"
                ),
            ),
            TutorStep(
                id="ng_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "What brackets are used in Angular for Event Binding (e.g. click, submit)?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በአንጉላር ውስጥ ለክስተቶች (ለምሳሌ፦ click ወይም submit) የትኛው ቅንፍ ያገለግላል?"
                ),
                options_en=[
                    "( ) (Parentheses)",
                    "[ ] (Square brackets)",
                    "{{ }} (Double curlies)",
                    "< > (Angle brackets)",
                ],
                options_am=[
                    "( ) (መደበኛ ቅንፍ)",
                    "[ ] (የካሬ ቅንፍ)",
                    "{{ }} (ድርብ የፈረንሳይ ቅንፍ)",
                    "< > (የአንግል ቅንፍ)",
                ],
                correct_option_index=0,
                hint_en="Parentheses `( )` catch events like clicks and key presses!",
                hint_am="መደበኛ ቅንፍ `( )` እንደ ክሊክ ያሉ ክስተቶችን ለመቀበል ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch5",
        order=5,
        title_en="Angular Ch 5: Conditional Display with *ngIf",
        title_am="አንጉላር ምዕራፍ 5፦ ሁኔታዎችን በ *ngIf ማሳየት",
        description_en="Show or remove elements dynamically based on boolean conditions.",
        description_am="ሁኔታዎችን አይቶ መረጃዎችን በ `*ngIf` መርጦ ማሳየት።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚦 *Structural Directives: `*ngIf`* 🧠\n\n"
                    "In Angular, directives starting with an asterisk `*` modify the actual DOM structure.\n\n"
                    "The `*ngIf` directive conditionally adds or completely removes an element from the page:\n\n"
                    "```html\n<p *ngIf=\"isLoggedIn\">Welcome Back!</p>\n```\n\n"
                    "- If `isLoggedIn` is `true`, the `<p>` element is rendered\n"
                    "- If `false`, the element is completely detached from the DOM!"
                ),
                message_am=(
                    "🚦 *መዋቅራዊ መመሪያዎች፦ `*ngIf`* 🧠\n\n"
                    "በአንጉላር ውስጥ በኮከብ `*` የሚጀምሩ መመሪያዎች የድህረ-ገጹን መዋቅር በቀጥታ ይለውጣሉ (Structural Directives ይባላሉ)።\n\n"
                    "`*ngIf` ሁኔታዎችን አይቶ ኤለመንቶችን በስክሪኑ ላይ ያወጣል ወይም ሙሉ በሙሉ ያጠፋል፦\n\n"
                    "```html\n<p *ngIf=\"isLoggedIn\">Welcome Back!</p>\n```\n\n"
                    "- `isLoggedIn` እውነት (`true`) ከሆነ `<p>` ይታያል\n"
                    "- ሀሰት (`false`) ከሆነ ደግሞ ከድህረ-ገጹ ላይ ሙሉ በሙሉ ይወገዳል!"
                ),
            ),
            TutorStep(
                id="ng_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write an `AuthComponent` using `*ngIf=\"isLoggedIn\"` where `isLoggedIn = true;`!\n\n"
                    "👇 *Type and send:*\n"
                    "```typescript\n@Component({\n  selector: 'app-auth',\n  template: `<p *ngIf=\"isLoggedIn\">Welcome Back!</p>`\n})\nexport class AuthComponent {\n  isLoggedIn = true;\n}\n```"
                ),
                message_am=(
                    "`isLoggedIn = true;` በማድረግ በ `*ngIf=\"isLoggedIn\"` ሁኔታን የሚፈትሽ ኮምፖነንት ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-auth',\n  template: `<p *ngIf=\"isLoggedIn\">Welcome Back!</p>`\n})\nexport class AuthComponent {\n  isLoggedIn = true;\n}\n```"
                ),
                expected_code_output="<p>Welcome Back!</p>",
                hint_en='Write `<p *ngIf="isLoggedIn">Welcome Back!</p>` and `isLoggedIn = true;`',
                hint_am='`<p *ngIf="isLoggedIn">Welcome Back!</p>` እና `isLoggedIn = true;` ብለው ይላኩ።',
                success_message_en=(
                    "🔥 *OUTSTANDING!* Angular evaluated `*ngIf` as true and inserted the element!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* አንጉላር `*ngIf` እውነት መሆኑን አረጋግጦ ጽሁፉን አውጥቷል!"
                ),
            ),
            TutorStep(
                id="ng_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Why does `*ngIf` begin with an asterisk `*` in Angular?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በአንጉላር ውስጥ `*ngIf` በኮከብ `*` የሚጀምረው ለምንድን ነው?"
                ),
                options_en=[
                    "It is a structural directive that adds or removes elements from the DOM tree",
                    "To multiply numbers",
                    "To hide passwords",
                    "Because it is an optional comment",
                ],
                options_am=[
                    "የድህረ-ገጹን መዋቅር የሚቀይር (ኤለመንት የሚጨምር ወይም የሚቀንስ) መመሪያ ስለሆነ",
                    "ቁጥሮችን ለማባዛት",
                    "የይለፍ ቃል ለመደበቅ",
                    "አስተያየት (Comment) ስለሆነ",
                ],
                correct_option_index=0,
                hint_en="Asterisks `*` mark structural directives that reshape the DOM layout!",
                hint_am="ኮከብ `*` የድህረ-ገጹን መዋቅር የሚቀይሩ መመሪያዎችን መለያ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch6",
        order=6,
        title_en="Angular Ch 6: Rendering Lists with *ngFor",
        title_am="አንጉላር ምዕራፍ 6፦ ዝርዝሮችን በ *ngFor መደርደር",
        description_en="Loop over collections and arrays to generate repetitive UI elements.",
        description_am="የመረጃ ዝርዝሮችን በ `*ngFor` በመጠቀም በድህረ-ገጽ ላይ ማውጣት።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📋 *Looping Lists with `*ngFor`* 🔄\n\n"
                    "Whenever you have an array of items (like products, emails, or user profiles), "
                    "the `*ngFor` structural directive stamps out an HTML element for each item in the list:\n\n"
                    "```html\n<ul>\n    <li *ngFor=\"let s of skills\">{{ s }}</li>\n</ul>\n```\n\n"
                    "- `let s` creates a local variable for each item in the array\n"
                    "- `of skills` points to the array property in your component class"
                ),
                message_am=(
                    "📋 *ዝርዝሮችን በ `*ngFor` መደርደር* 🔄\n\n"
                    "የዕቃዎች፣ የደብዳቤዎች ወይም የተጠቃሚዎች ዝርዝር ሲኖረን፣ `*ngFor` የተባለው መመሪያ ለእያንዳንዱ መረጃ "
                    "አዲስ የ HTML ኤለመንት ያወጣል፦\n\n"
                    "```html\n<ul>\n    <li *ngFor=\"let s of skills\">{{ s }}</li>\n</ul>\n```\n\n"
                    "- `let s` በእያንዳንዱ ዙር የአንድን እቃ ስም ይይዛል\n"
                    "- `of skills` በክላሱ ውስጥ ያለውን አሬይ ይጠቁማል"
                ),
            ),
            TutorStep(
                id="ng_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `SkillsComponent` rendering `<li *ngFor=\"let s of skills\">{{ s }}</li>` with 3 skills!\n\n"
                    "👇 *Type and send:*\n"
                    "```typescript\n@Component({\n  selector: 'app-skills',\n  template: `<ul><li *ngFor=\"let s of skills\">{{ s }}</li></ul>`\n})\nexport class SkillsComponent {\n  skills = ['TypeScript', 'Angular', 'RxJS'];\n}\n```"
                ),
                message_am=(
                    "የ 3 ክህሎቶች ዝርዝርን በ `*ngFor` የሚያሳይ `SkillsComponent` ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-skills',\n  template: `<ul><li *ngFor=\"let s of skills\">{{ s }}</li></ul>`\n})\nexport class SkillsComponent {\n  skills = ['TypeScript', 'Angular', 'RxJS'];\n}\n```"
                ),
                expected_code_output="<ul><li>TypeScript</li><li>Angular</li><li>RxJS</li></ul>",
                hint_en="Write the `*ngFor=\"let s of skills\"` inside `<ul>...</ul>` with the 3 skills in the array.",
                hint_am="በ `<ul>` ውስጥ `*ngFor=\"let s of skills\"` በማድረግ 3ቱን ክህሎቶች በአሬይ ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* Angular stamped out list elements for each item in the array!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* አንጉላር ለአሬዩ አባላት በሙሉ የዝርዝር ታጎችን አውጥቷል!"
                ),
            ),
            TutorStep(
                id="ng_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In `*ngFor=\"let s of skills\"`, what is `s`?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ `*ngFor=\"let s of skills\"` ውስጥ `s` ምንድን ነው?"
                ),
                options_en=[
                    "A template loop variable holding the current item",
                    "A CSS style class",
                    "A database table name",
                    "An operating system thread",
                ],
                options_am=[
                    "የእያንዳንዱን ዙር ወቅታዊ መረጃ የሚይዝ ተለዋዋጭ",
                    "የ CSS ስታይል ክላስ",
                    "የዳታቤዝ ሰንጠረዥ ስም",
                    "የኮምፒውተር ፕሮሰሰር ትዕዛዝ",
                ],
                correct_option_index=0,
                hint_en="`let s` represents the current item in the current loop iteration!",
                hint_am="`let s` በወቅቱ እየዞረ ያለውን የአሬይ አባል የሚወክል ተለዋዋጭ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="ng_ch7",
        order=7,
        title_en="Angular Ch 7: Enterprise Dashboard Card Capstone",
        title_am="አንጉላር ምዕራፍ 7፦ የአንጉላር ዳሽቦርድ ካርድ ፕሮጀክት",
        description_en="Assemble components, classes, interpolation, and styling into an enterprise dashboard card.",
        description_am="ክላሶችን፣ ቴምፕሌትን እና ኢንተርፖሌሽንን በማጣመር ሙሉ የዳሽቦርድ ካርድ መስራት።",
        track="angular",
        steps=[
            TutorStep(
                id="ng_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Enterprise User Card!* 🏛️🌟\n\n"
                    "Now, let's assemble everything you've learned into a complete enterprise Angular card:\n"
                    "1. `@Component` decorator with selector and template\n"
                    "2. TypeScript component class with `name` and `role` properties\n"
                    "3. Double curly brace interpolation `{{ name }}` and `{{ role }}`\n"
                    "4. Production dashboard structure!"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የአንጉላር ዳሽቦርድ ካርድ!* 🏛️🌟\n\n"
                    "እስካሁን የተማርነውን በሙሉ በማጣመር የተሟላ የዳሽቦርድ ካርድ እንገነባለን፦\n"
                    "1. `@Component` ዴኮሬተር ከቴምፕሌት ጋር\n"
                    "2. የታይፕስክሪፕት ክላስ ከ `name` እና `role` ዳታ ጋር\n"
                    "3. ድርብ የፈረንሳይ ቅንፍ ማሳያ `{{ name }}` እና `{{ role }}`\n"
                    "4. የተስተካከለ የካርድ መዋቅር!"
                ),
            ),
            TutorStep(
                id="ng_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `UserCardComponent` with `name = 'Liya';` and `role = 'Lead Architect';` inside `<div class=\"card\">`!\n\n"
                    "👇 *Type and send:*\n"
                    "```typescript\n@Component({\n  selector: 'app-user-card',\n  template: `<div class=\"card\"><h2>{{ name }}</h2><p>Role: {{ role }}</p></div>`\n})\nexport class UserCardComponent {\n  name = 'Liya';\n  role = 'Lead Architect';\n}\n```"
                ),
                message_am=(
                    "`name = 'Liya';` እና `role = 'Lead Architect';` የያዘ `UserCardComponent` በ `<div class=\"card\">` ውስጥ ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```typescript\n@Component({\n  selector: 'app-user-card',\n  template: `<div class=\"card\"><h2>{{ name }}</h2><p>Role: {{ role }}</p></div>`\n})\nexport class UserCardComponent {\n  name = 'Liya';\n  role = 'Lead Architect';\n}\n```"
                ),
                expected_code_output='<div class="card"><h2>Liya</h2><p>Role: Lead Architect</p></div>',
                hint_en='Write `UserCardComponent` with the template card and class properties `name` and `role`.',
                hint_am='`UserCardComponent` ጽፈው በቴምፕሌቱ ውስጥ `{{ name }}` እና `{{ role }}` በማሳየት ይላኩ።',
                success_message_en=(
                    "🏆 *ENTERPRISE ANGULAR ARCHITECT!* You have officially built a production-ready enterprise Angular component!"
                ),
                success_message_am=(
                    "🏆 *የአንጉላር ባለሙያ!* ለትላልቅ ተቋማት የሚሆን እውነተኛ የአንጉላር ኮምፖነንት ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="ng_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! ANGULAR GRADUATE!** 🌟🎓\n\n"
                    "You have conquered Google's enterprise framework:\n"
                    "1. 🅰️ Component architecture & `@Component` decorators\n"
                    "2. 🪄 Template interpolation with `{{ }}`\n"
                    "3. 📦 TypeScript class properties & data binding\n"
                    "4. 🔗 Property binding with square brackets `[ ]`\n"
                    "5. ⚡ Event listening with parentheses `( )`\n"
                    "6. 🚦 Structural control flow with `*ngIf`\n"
                    "7. 📋 Data repetition with `*ngFor` & dashboard assembly!\n\n"
                    "You are now ready to build large-scale enterprise web systems with Angular! 🚀🏛️🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የአንጉላር (Angular) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "የጉግልን ታላቅ የድርጅት ፍሬምወርክ በሚገባ ተምረዋል፦\n"
                    "1. 🅰️ የኮምፖነንት አወቃቀር እና የ `@Component` ዴኮሬተር\n"
                    "2. 🪄 መረጃን በ `{{ }}` ማሳየት\n"
                    "3. 📦 የታይፕስክሪፕት ክላስ ዳታ\n"
                    "4. 🔗 የፕሮፐርቲ ማሰሪያ በካሬ ቅንፍ `[ ]`\n"
                    "5. ⚡ ክስተቶችን በቅንፍ `( )` መቀበል\n"
                    "6. 🚦 ሁኔታዎችን በ `*ngIf` መቆጣጠር\n"
                    "7. 📋 ዝርዝሮችን በ `*ngFor` መደርደር እና የዳሽቦርድ ግንባታ!\n\n"
                    "አሁን ለትላልቅ ድርጅቶችና ባንኮች የሚሆኑ ግዙፍ ስርዓቶችን በአንጉላር ለመገንባት ዝግጁ ነዎት! 🚀🏛️🔥"
                ),
            ),
        ],
    ),
]


def get_all_angular_chapters() -> List[TutorChapter]:
    """Return all Angular tutor chapters ordered."""
    return sorted(ANGULAR_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_angular_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve Angular tutor chapter by ID."""
    for ch in ANGULAR_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_angular_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next Angular chapter ID."""
    chapters = get_all_angular_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
