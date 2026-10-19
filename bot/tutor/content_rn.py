"""React Native mobile curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

RN_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="rn_ch1",
        order=1,
        title_en="React Native Ch 1: Welcome to Mobile Apps & View / Text",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 1፦ የሞባይል አፕሊኬሽን እና View / Text",
        description_en="Learn how to build real iOS and Android native smartphone apps.",
        description_am="ለአንድሮይድ እና ለአይፎን (iOS) እውነተኛ የሞባይል አፕሊኬሽኖችን መገንባት ይማሩ።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📱 *Welcome to React Native!* 📲✨\n\n"
                    "React Native lets you build real, high-performance native mobile apps for both **iOS (iPhone) and Android** "
                    "using a single codebase!\n\n"
                    "Major apps like **Instagram, Discord, Facebook, Pinterest, and Coinbase** run on React Native.\n\n"
                    "⚠️ **THE #1 GOLDEN RULE OF MOBILE APPS**:\n"
                    "Smartphones do not have HTML! There is NO `<div>`, `<p>`, or `<h1>`.\n\n"
                    "Instead, we use native mobile building blocks:\n"
                    "- `<View>` is the mobile container (like `<div>`)\n"
                    "- `<Text>` is the text component (all words MUST be inside `<Text>`)"
                ),
                message_am=(
                    "📱 *እንኳን ወደ ሪያክት ኔቲቭ (React Native) በደህና መጡ!* 📲✨\n\n"
                    "ሪያክት ኔቲቭ በአንድ ኮድ ብቻ ለ **አንድሮይድ (Android) እና ለአይፎን (iOS)** የሚሰሩ እውነተኛ "
                    "የሞባይል አፕሊኬሽኖችን እንድትገነቡ ያስችላችኋል!\n\n"
                    "እንደ **Instagram፣ Discord፣ Facebook፣ Pinterest እና Coinbase** ያሉ ታላላቅ አፖች በሪያክት ኔቲቭ የተሰሩ ናቸው።\n\n"
                    "⚠️ **የሞባይል አፕሊኬሽን ቁጥር 1 ወርቃማ ህግ**፦\n"
                    "በስማርትፎኖች ላይ የድህረ-ገጽ HTML ታጎች የሉም! ምንም አይነት `<div>`፣ `<p>` ወይም `<h1>` አይሰራም።\n\n"
                    "በእነሱ ምትክ የሞባይል ክፍሎችን እንጠቀማለን፦\n"
                    "- `<View>` የሞባይል ማቀፊያ ሳጥን ነው (እንደ `<div>`)\n"
                    "- `<Text>` የጽሁፍ ማሳያ ነው (ማንኛውም ጽሁፍ በ `<Text>` ውስጥ መሆን አለበት)"
                ),
            ),
            TutorStep(
                id="rn_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first native mobile UI element!\n\n"
                    "Wrap `<Text>Hello Mobile App!</Text>` inside a `<View>` container:\n\n"
                    "👇 *Type and send this code:*\n"
                    "```jsx\n<View>\n    <Text>Hello Mobile App!</Text>\n</View>\n```"
                ),
                message_am=(
                    "የመጀመሪያውን የሞባይል አፕሊኬሽን ኤለመንት እንጻፍ!\n\n"
                    "`<Text>Hello Mobile App!</Text>` የሚለውን በ `<View>` ውስጥ አቅፈው ይላኩ፦\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\n<View>\n    <Text>Hello Mobile App!</Text>\n</View>\n```"
                ),
                expected_code_output="<View><Text>Hello Mobile App!</Text></View>",
                hint_en="Write `<View><Text>Hello Mobile App!</Text></View>`",
                hint_am="`<View><Text>Hello Mobile App!</Text></View>` ብለው ይላኩ።",
                success_message_en=(
                    "🎉 *BOOM!* You just structured real native mobile views for iOS and Android!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* ለአይፎንና ለአንድሮይድ የሚሰራ እውነተኛ የሞባይል እይታ (View) ገነቡ!"
                ),
            ),
            TutorStep(
                id="rn_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In React Native, can you put raw text directly inside a `<View>` without wrapping it in a `<Text>` component?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ኔቲቭ ውስጥ ጽሁፍን በ `<Text>` ውስጥ ሳያደርጉ በቀጥታ በ `<View>` ውስጥ ማስቀመጥ ይቻላል?"
                ),
                options_en=[
                    "No! All strings must be rendered inside a <Text> component",
                    "Yes, any tag can hold text",
                    "Only on Android, not iOS",
                    "Only inside buttons",
                ],
                options_am=[
                    "አይቻልም! ማንኛውም ጽሁፍ በ <Text> ኮምፖነንት ውስጥ መሆን አለበት",
                    "አዎ፤ ማንኛውም ታግ ጽሁፍ መያዝ ይችላል",
                    "በአንድሮይድ ብቻ ይቻላል",
                    "በአዝራር (Button) ውስጥ ብቻ",
                ],
                correct_option_index=0,
                hint_en="React Native strictly crashes with a red screen if text is outside `<Text>`!",
                hint_am="በሪያክት ኔቲቭ ውስጥ ጽሁፍ ከ `<Text>` ውጪ ከተጻፈ አፑ ቀይ ስክሪን አሳይቶ ይቆማል!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch2",
        order=2,
        title_en="React Native Ch 2: Building Your First Mobile Screen",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 2፦ የመጀመሪያው የሞባይል ስክሪን",
        description_en="Construct functional smartphone screen components.",
        description_am="ሙሉ የስማርትፎን ስክሪን ኮምፖነንቶችን መገንባት።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📲 *Smartphone Screen Components* 📱\n\n"
                    "A smartphone screen in React Native is simply a component that returns native mobile views:\n\n"
                    "```jsx\nfunction HomeScreen() {\n    return (\n        <View>\n            <Text>Welcome to CodeBuddy Mobile!</Text>\n        </View>\n    );\n}\n```\n\n"
                    "React Native compiles this JavaScript into real native UIKit views on iOS, and Android ViewGroups on Android!"
                ),
                message_am=(
                    "📲 *የስማርትፎን ስክሪን ኮምፖነንቶች* 📱\n\n"
                    "የሞባይል ስክሪን በሪያክት ኔቲቭ ውስጥ የሞባይል ቪው የሚመልስ ፈንክሽናል ኮምፖነንት ነው፦\n\n"
                    "```jsx\nfunction HomeScreen() {\n    return (\n        <View>\n            <Text>Welcome to CodeBuddy Mobile!</Text>\n        </View>\n    );\n}\n```\n\n"
                    "ሪያክት ኔቲቭ ይህንን ኮድ በአይፎን ላይ ወደ እውነተኛ የ iOS UIView፣ በአንድሮይድ ላይ ደግሞ ወደ Android View ይቀይረዋል!"
                ),
            ),
            TutorStep(
                id="rn_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `HomeScreen` component returning `<View><Text>Welcome to CodeBuddy Mobile!</Text></View>`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```jsx\nfunction HomeScreen() {\n    return (\n        <View>\n            <Text>Welcome to CodeBuddy Mobile!</Text>\n        </View>\n    );\n}\n```"
                ),
                message_am=(
                    "`HomeScreen` የሚል ኮምፖነንት ፈጥረው `<View><Text>Welcome to CodeBuddy Mobile!</Text></View>` ይመልሱ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction HomeScreen() {\n    return (\n        <View>\n            <Text>Welcome to CodeBuddy Mobile!</Text>\n        </View>\n    );\n}\n```"
                ),
                expected_code_output="<View><Text>Welcome to CodeBuddy Mobile!</Text></View>",
                hint_en="Define `function HomeScreen() { return ( <View><Text>Welcome to CodeBuddy Mobile!</Text></View> ); }`",
                hint_am="`function HomeScreen() { return ( <View><Text>Welcome to CodeBuddy Mobile!</Text></View> ); }` ብለው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You just defined a full mobile app screen!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* ሙሉ የሞባይል መተግበሪያ ስክሪን በተሳካ ሁኔታ ገነቡ!"
                ),
            ),
            TutorStep(
                id="rn_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "What makes React Native apps feel smoother and faster than ordinary mobile web pages?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የሪያክት ኔቲቭ አፕሊኬሽኖች ከመደበኛ የድህረ-ገጽ ገጾች ይልቅ እጅግ ፈጣን እንዲሆኑ ያደረጋቸው ምንድን ነው?"
                ),
                options_en=[
                    "They render real native iOS and Android OS widgets directly",
                    "They do not use memory",
                    "They only work without internet",
                    "They are converted to video files",
                ],
                options_am=[
                    "በቀጥታ የስልኩን እውነተኛ የ iOS እና የአንድሮይድ ዊጅቶች ስለሚጠቀሙ",
                    "ማህደረ-ትውስታ ስለማይጠቀሙ",
                    "ያለ ኢንተርኔት ብቻ ስለሚሰሩ",
                    "ወደ ቪዲዮ ፋይል ስለሚቀየሩ",
                ],
                correct_option_index=0,
                hint_en="React Native bridges your code directly to the phone's native UI thread!",
                hint_am="ሪያክት ኔቲቭ ኮድዎን በቀጥታ ከስልኩ እውነተኛ የግራፊክስ ሞተር ጋር ያገናኘዋል!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch3",
        order=3,
        title_en="React Native Ch 3: Mobile Styling & Flexbox",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 3፦ የሞባይል ስታይሊንግ እና ፍሌክስቦክስ",
        description_en="Style mobile views with Flexbox layout and the style attribute.",
        description_am="የሞባይል ስክሪኖችን በፍሌክስቦክስ (Flexbox) እና ስታይል ማስዋብ።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎨 *Styling on Mobile Screens* 📐\n\n"
                    "In React Native, styling is written using JavaScript objects via the `style` prop:\n\n"
                    "```jsx\n<View style={{ backgroundColor: \"#2563eb\", padding: 16 }}>\n    <Text style={{ color: \"#ffffff\" }}>React Native</Text>\n</View>\n```\n\n"
                    "🌟 **KEY DIFFERENCE FROM THE WEB**:\n"
                    "On the web, Flexbox lays out items horizontally by default (`flexDirection: 'row'`).\n\n"
                    "On smartphones, because screens are tall, **React Native defaults to `flexDirection: 'column'`** (stacking vertically from top to bottom)!"
                ),
                message_am=(
                    "🎨 *የሞባይል ስክሪን ስታይሊንግ* 📐\n\n"
                    "በሪያክት ኔቲቭ ውስጥ ስታይሎች በጃቫስክሪፕት ኦብጀክት በ `style` አማካኝነት ይጻፋሉ፦\n\n"
                    "```jsx\n<View style={{ backgroundColor: \"#2563eb\", padding: 16 }}>\n    <Text style={{ color: \"#ffffff\" }}>React Native</Text>\n</View>\n```\n\n"
                    "🌟 **ከድህረ-ገጽ የሚለይበት ዋነኛ ነጥብ**፦\n"
                    "በኮምፒውተር ድረ-ገጽ ላይ Flexbox መረጃዎችን በአግድም (`row`) ያስቀምጣል።\n\n"
                    "በስማርትፎን ግን ስክሪኑ ረጅም በመሆኑ **በነባሪነት ወደ ታች ይደረድራል (`flexDirection: 'column'`)**!"
                ),
            ),
            TutorStep(
                id="rn_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Style a banner with `backgroundColor: \"#2563eb\"` and white text!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```jsx\n<View style={{ backgroundColor: \"#2563eb\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Mobile App</Text>\n</View>\n```"
                ),
                message_am=(
                    "የሰማያዊ ዳራ `backgroundColor: \"#2563eb\"` እና የነጭ ጽሁፍ ባነር ስታይል ሰርተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\n<View style={{ backgroundColor: \"#2563eb\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Mobile App</Text>\n</View>\n```"
                ),
                expected_code_output='<View style="background-color:#2563eb"><Text style="color:#ffffff">Mobile App</Text></View>',
                hint_en='Write `<View style={{ backgroundColor: "#2563eb" }}><Text style={{ color: "#ffffff" }}>Mobile App</Text></View>`',
                hint_am='`<View style={{ backgroundColor: "#2563eb" }}><Text style={{ color: "#ffffff" }}>Mobile App</Text></View>` ብለው ይላኩ።',
                success_message_en=(
                    "🎯 *SPOT ON!* You styled native mobile views with background color and text styling!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* የሞባይል እይታዎችን በዳራ ቀለም እና በጽሁፍ ስታይል አስዋቡ!"
                ),
            ),
            TutorStep(
                id="rn_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "What is the default `flexDirection` in React Native?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በሪያክት ኔቲቭ ውስጥ ነባሪው የ `flexDirection` አቅጣጫ የትኛው ነው?"
                ),
                options_en=[
                    "column (vertical stacking from top to bottom)",
                    "row (horizontal left to right)",
                    "diagonal",
                    "circular",
                ],
                options_am=[
                    "column (በቁመት ከላይ ወደ ታች መደርደር)",
                    "row (በአግድም ከግራ ወደ ቀኝ)",
                    "ሰያፍ",
                    "ክብ",
                ],
                correct_option_index=0,
                hint_en="Phones are held vertically, so components stack as a column by default!",
                hint_am="ስልኮች በቁመት ስለሚያዙ ኤለመንቶች በነባሪነት በቁመት (column) ይደረደራሉ!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch4",
        order=4,
        title_en="React Native Ch 4: Touch & Buttons with TouchableOpacity",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 4፦ መንካት እና በተን በ TouchableOpacity",
        description_en="Respond to smartphone screen finger taps with responsive feedback.",
        description_am="የተጠቃሚዎችን የስክሪን ንክኪ በቅጽበት ማስተናገድ።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "👆 *Touch & Interaction: `TouchableOpacity`* 📱\n\n"
                    "Smartphones don't have mouse cursors or hover states—everything is powered by finger taps!\n\n"
                    "React Native provides **`TouchableOpacity`**:\n"
                    "When a user presses it, it dims its opacity slightly so the user instantly feels their touch registered!\n\n"
                    "```jsx\n<TouchableOpacity style={{ backgroundColor: \"#10b981\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Tap Me</Text>\n</TouchableOpacity>\n```"
                ),
                message_am=(
                    "👆 *ንክኪ እና አዝራር፦ `TouchableOpacity`* 📱\n\n"
                    "በስማርትፎን ላይ ማውዝ የለም፤ ሁሉም ነገር በጣት ንክኪ ነው የሚሰራው!\n\n"
                    "ሪያክት ኔቲቭ **`TouchableOpacity`** የተባለ ድንቅ ኮምፖነንት አለው፦\n"
                    "ተጠቃሚው ሲነካው ቀለሙ በጥቂቱ ፈዘዝ በማለት ስልኩ ንክኪውን መቀበሉን ያረጋግጥለታል!\n\n"
                    "```jsx\n<TouchableOpacity style={{ backgroundColor: \"#10b981\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Tap Me</Text>\n</TouchableOpacity>\n```"
                ),
            ),
            TutorStep(
                id="rn_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a touchable button with `backgroundColor: \"#10b981\"` and `<Text>Tap Me</Text>`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\n<TouchableOpacity style={{ backgroundColor: \"#10b981\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Tap Me</Text>\n</TouchableOpacity>\n```"
                ),
                message_am=(
                    "`backgroundColor: \"#10b981\"` ያለው የንክኪ አዝራር እና `<Text>Tap Me</Text>` ሰርተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\n<TouchableOpacity style={{ backgroundColor: \"#10b981\" }}>\n    <Text style={{ color: \"#ffffff\" }}>Tap Me</Text>\n</TouchableOpacity>\n```"
                ),
                expected_code_output='<TouchableOpacity style="background-color:#10b981"><Text style="color:#ffffff">Tap Me</Text></TouchableOpacity>',
                hint_en='Write `<TouchableOpacity style={{ backgroundColor: "#10b981" }}><Text style={{ color: "#ffffff" }}>Tap Me</Text></TouchableOpacity>`',
                hint_am='`<TouchableOpacity style={{ backgroundColor: "#10b981" }}><Text style={{ color: "#ffffff" }}>Tap Me</Text></TouchableOpacity>` ብለው ይላኩ።',
                success_message_en=(
                    "🎉 *TERRIFIC!* You built an interactive touchable mobile button!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* ለንክኪ ምላሽ የሚሰጥ እውነተኛ የሞባይል አዝራር ገነቡ!"
                ),
            ),
            TutorStep(
                id="rn_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "What visual feedback does `TouchableOpacity` provide when a user taps it?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "ተጠቃሚው ሲጫነው `TouchableOpacity` ምን አይነት የእይታ ምላሽ ይሰጣል?"
                ),
                options_en=[
                    "Dims its opacity (transparency) momentarily",
                    "Changes the phone's ringtone",
                    "Turns off the screen",
                    "Shakes the entire phone",
                ],
                options_am=[
                    "ግልጽነቱ (Opacity) ለቅጽበት ፈዘዝ ይላል",
                    "የስልኩን ጥሪ ድምጽ ይቀይራል",
                    "ስክሪኑን ያጠፋዋል",
                    "ስልኩን ያንቀጠቅጠዋል",
                ],
                correct_option_index=0,
                hint_en="It reduces opacity to confirm the press!",
                hint_am="ንክኪው መድረሱን ለማሳወቅ ቀለሙን ለቅጽበት ፈዘዝ ያደርጋል!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch5",
        order=5,
        title_en="React Native Ch 5: Scrollable Feeds with ScrollView",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 5፦ የሚንሸራሸሩ ገጾች በ ScrollView",
        description_en="Enable vertical scrolling when screen content exceeds phone height.",
        description_am="የሞባይል ስክሪኑ ሲሞላ መረጃዎች ወደ ላይና ወደ ታች እንዲንሸራሸሩ ማድረግ።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📜 *Scrollable Feeds: `<ScrollView>`* 📱\n\n"
                    "On web browsers, if a page is long, the browser automatically adds a scrollbar.\n\n"
                    "On mobile phones, **`<View>` DOES NOT SCROLL by default**! If content overflows, it gets clipped off screen!\n\n"
                    "To allow users to swipe and scroll through feeds, we wrap content inside **`<ScrollView>`**:\n\n"
                    "```jsx\n<ScrollView>\n    <Text>Post 1</Text>\n    <Text>Post 2</Text>\n    <Text>Post 3</Text>\n</ScrollView>\n```"
                ),
                message_am=(
                    "📜 *የሚንሸራሸሩ ገጾች፦ `<ScrollView>`* 📱\n\n"
                    "በኮምፒውተር ድረ-ገጾች ላይ መረጃ ሲበዛ ስክሪኑ በራሱ ይንሸራሸራል (Scroll ያደርጋል)።\n\n"
                    "በሞባይል ስልኮች ላይ ግን **`<View>` በነባሪነት አይንሸራሸርም**! መረጃው ከስክሪኑ ከወጣ ተቆርጦ ይቀራል!\n\n"
                    "ተጠቃሚው በጣቱ እየገፋ መረጃዎችን እንዲያይ በ **`<ScrollView>`** ውስጥ እናቅፈዋለን፦\n\n"
                    "```jsx\n<ScrollView>\n    <Text>Post 1</Text>\n    <Text>Post 2</Text>\n    <Text>Post 3</Text>\n</ScrollView>\n```"
                ),
            ),
            TutorStep(
                id="rn_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Build a scrollable feed wrapping two `<Text>` items inside `<ScrollView>`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\n<ScrollView>\n    <Text>Feed Item 1</Text>\n    <Text>Feed Item 2</Text>\n</ScrollView>\n```"
                ),
                message_am=(
                    "ሁለት የጽሁፍ እቃዎችን በ `<ScrollView>` ውስጥ በማቀፍ የሚንሸራሸር ፊድ ገጽ ይስሩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\n<ScrollView>\n    <Text>Feed Item 1</Text>\n    <Text>Feed Item 2</Text>\n</ScrollView>\n```"
                ),
                expected_code_output="<ScrollView><Text>Feed Item 1</Text><Text>Feed Item 2</Text></ScrollView>",
                hint_en="Write `<ScrollView><Text>Feed Item 1</Text><Text>Feed Item 2</Text></ScrollView>`",
                hint_am="`<ScrollView><Text>Feed Item 1</Text><Text>Feed Item 2</Text></ScrollView>` ብለው ይላኩ።",
                success_message_en=(
                    "🔥 *OUTSTANDING!* You created a smooth swipeable mobile feed!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* በጣት እየተገፋ የሚንሸራሸር የሞባይል ገጽ ገነቡ!"
                ),
            ),
            TutorStep(
                id="rn_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Concept Check:*\n\n"
                    "Why must you use `<ScrollView>` instead of regular `<View>` when content is taller than the phone screen?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "መረጃው ከሞባይል ስክሪኑ ሲረዝም ከመደበኛው `<View>` ይልቅ `<ScrollView>` መጠቀም ያለብን ለምንድን ነው?"
                ),
                options_en=[
                    "Because <View> does not scroll and cuts off overflow content",
                    "Because <View> cannot hold text",
                    "To change the font size",
                    "To activate the camera",
                ],
                options_am=[
                    "<View> በነባሪነት ስለማይንሸራሸር ትርፍ መረጃዎችን ቆርጦ ስለሚያስቀር",
                    "<View> ጽሁፍ መያዝ ስለማይችል",
                    "የፊደል መጠኑን ለመቀየር",
                    "ካሜራውን ለማብራት",
                ],
                correct_option_index=0,
                hint_en="Without ScrollView, content overflowing the bottom of the screen is unreachable!",
                hint_am="ያለ ScrollView ከስክሪኑ በታች ያለው መረጃ ተቆርጦ ስለሚቀር ሊታይ አይችልም!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch6",
        order=6,
        title_en="React Native Ch 6: Mobile Props & Contact Card",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 6፦ የሞባይል ፕሮፕስ እና ኮንታክት ካርድ",
        description_en="Pass contact information and phone numbers into reusable mobile cards.",
        description_am="የተጠቃሚዎችን ስልክ እና መረጃ በፕሮፕስ ወደ ሞባይል ካርድ ማስተላለፍ።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📱 *Mobile Components with Props* 📇\n\n"
                    "In mobile apps like WhatsApp or Telegram, every chat item and contact card is the same component displaying different props:\n\n"
                    "```jsx\nfunction ContactCard(props) {\n    return (\n        <View>\n            <Text>{props.name}</Text>\n            <Text>{props.phone}</Text>\n        </View>\n    );\n}\n```\n\n"
                    "This creates modular, reusable native UI elements for your entire app!"
                ),
                message_am=(
                    "📱 *የሞባይል ኮምፖነንቶች በፕሮፕስ* 📇\n\n"
                    "እንደ ዋትስአፕ ወይም ቴሌግራም ባሉ የሞባይል አፖች ውስጥ እያንዳንዱ የሰው ስም እና ስልክ ቁጥር ተመሳሳይ ኮምፖነንት ነው፦\n\n"
                    "```jsx\nfunction ContactCard(props) {\n    return (\n        <View>\n            <Text>{props.name}</Text>\n            <Text>{props.phone}</Text>\n        </View>\n    );\n}\n```\n\n"
                    "ይህም በመላው መተግበሪያዎ ውስጥ እንደገና ጥቅም ላይ የሚውሉ የሞባይል ክፍሎችን ለመገንባት ያገለግላል!"
                ),
            ),
            TutorStep(
                id="rn_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `ContactCard(props)` component displaying `props.name` and `props.phone`!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction ContactCard(props) {\n    return (\n        <View>\n            <Text>{props.name}</Text>\n            <Text>{props.phone}</Text>\n        </View>\n    );\n}\n```"
                ),
                message_am=(
                    "`ContactCard(props)` የሚል ኮምፖነንት ጽፈው `props.name` እና `props.phone` አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction ContactCard(props) {\n    return (\n        <View>\n            <Text>{props.name}</Text>\n            <Text>{props.phone}</Text>\n        </View>\n    );\n}\n```"
                ),
                expected_code_output="<View><Text>Sara</Text><Text>+251 91 123 4567</Text></View>",
                hint_en="Write `ContactCard(props)` returning `<View><Text>{props.name}</Text><Text>{props.phone}</Text></View>`",
                hint_am="`ContactCard(props)` ጽፈው በ `<View>` ውስጥ ስም እና ስልክ ቁጥሩን በ `<Text>` አሳይተው ይላኩ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You created a reusable native contact card component!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* እንደገና ጥቅም ላይ የሚውል የሞባይል ኮንታክት ካርድ ሰሩ!"
                ),
            ),
            TutorStep(
                id="rn_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Can the same `ContactCard` component be used to display thousands of different contacts?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "አንድ `ContactCard` ኮምፖነንት ለሺዎች ለሚቆጠሩ የተለያዩ ተጠቃሚዎች ማገልገል ይችላል?"
                ),
                options_en=[
                    "Yes, by passing different props to each instance",
                    "No, you must create a new component file for each person",
                    "Only if they have the same name",
                    "Only on tablets",
                ],
                options_am=[
                    "አዎ፤ ለእያንዳንዱ ሰው የተለያየ ፕሮፕስ (Props) በማስተላለፍ",
                    "አይችልም፤ ለእያንዳንዱ ሰው አዲስ ኮምፖነንት መጻፍ አለበት",
                    "ተመሳሳይ ስም ካላቸው ብቻ",
                    "በትልቅ ታብሌት ላይ ብቻ",
                ],
                correct_option_index=0,
                hint_en="Props make a single component render infinite variations of data!",
                hint_am="ፕሮፕስ አንድን ኮምፖነንት ላልተገደበ የተለያዩ መረጃዎች እንድንጠቀምበት ያደርገዋል!",
            ),
        ],
    ),
    TutorChapter(
        id="rn_ch7",
        order=7,
        title_en="React Native Ch 7: Smartphone Profile Screen Capstone",
        title_am="ሪያክት ኔቲቭ ምዕራፍ 7፦ የተሟላ የሞባይል ፕሮፋይል ስክሪን ፕሮጀክት",
        description_en="Construct a complete production smartphone profile screen with views, styles, and touch buttons.",
        description_am="ቪው፣ ቴክስት፣ ስታይል እና የንክኪ አዝራሮችን በማጣመር ሙሉ የሞባይል ስክሪን መስራት።",
        track="react_native",
        steps=[
            TutorStep(
                id="rn_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Full Mobile Profile Screen!* 📱🌟\n\n"
                    "Now we combine everything you've learned into a complete production mobile screen:\n"
                    "1. `<View>` containers\n"
                    "2. Styled `<Text>` typography\n"
                    "3. Native Flexbox styling (`backgroundColor`, `color`)\n"
                    "4. Interactive `<TouchableOpacity>` action button!\n\n"
                    "Let's build the User Profile Screen for a smartphone app!"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የስማርትፎን ፕሮፋይል ስክሪን!* 📱🌟\n\n"
                    "እስካሁን የተማርነውን በሙሉ በማጣመር የተሟላ የሞባይል ስክሪን እንገነባለን፦\n"
                    "1. የ `<View>` ማቀፊያ ሳጥኖች\n"
                    "2. በስታይል የተዋቡ የ `<Text>` ጽሁፎች\n"
                    "3. የሞባይል ፍሌክስቦክስ ስታይሎች (`backgroundColor`፣ `color`)\n"
                    "4. የ `<TouchableOpacity>` የንክኪ አዝራር!\n\n"
                    "አሁን ለሞባይል አፕሊኬሽን የሚሆን የፕሮፋይል ስክሪን እንገንባ!"
                ),
            ),
            TutorStep(
                id="rn_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `MobileProfile` component with `<Text>` for name and role, plus a `<TouchableOpacity>` follow button!\n\n"
                    "👇 *Type and send:*\n"
                    "```jsx\nfunction MobileProfile() {\n    return (\n        <View style={{ backgroundColor: \"#f3f4f6\" }}>\n            <Text style={{ color: \"#111827\" }}>Sara Ahmed</Text>\n            <TouchableOpacity style={{ backgroundColor: \"#2563eb\" }}>\n                <Text style={{ color: \"#ffffff\" }}>Follow</Text>\n            </TouchableOpacity>\n        </View>\n    );\n}\n```"
                ),
                message_am=(
                    "`MobileProfile` የሚል ኮምፖነንት ጽፈው ስም እና ሚናውን በ `<Text>` እንዲሁም የፎሎው አዝራር በ `<TouchableOpacity>` አሳይተው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```jsx\nfunction MobileProfile() {\n    return (\n        <View style={{ backgroundColor: \"#f3f4f6\" }}>\n            <Text style={{ color: \"#111827\" }}>Sara Ahmed</Text>\n            <TouchableOpacity style={{ backgroundColor: \"#2563eb\" }}>\n                <Text style={{ color: \"#ffffff\" }}>Follow</Text>\n            </TouchableOpacity>\n        </View>\n    );\n}\n```"
                ),
                expected_code_output='<View style="background-color:#f3f4f6"><Text style="color:#111827">Sara Ahmed</Text><TouchableOpacity style="background-color:#2563eb"><Text style="color:#ffffff">Follow</Text></TouchableOpacity></View>',
                hint_en='Write `MobileProfile` returning a `<View>` with styled `<Text>` and a `<TouchableOpacity>` containing white text.',
                hint_am='`MobileProfile` ጽፈው በ `<View>` ውስጥ `<Text>` እና የ `<TouchableOpacity>` አዝራር አሳይተው ይላኩ።',
                success_message_en=(
                    "🏆 *MOBILE APP MASTER!* You have officially built a production-ready mobile screen for iOS and Android!"
                ),
                success_message_am=(
                    "🏆 *የሞባይል አፕሊኬሽን ባለሙያ!* ለአይፎን እና ለአንድሮይድ የሚሆን እውነተኛ የሞባይል ስክሪን ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="rn_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! REACT NATIVE GRADUATE!** 🌟🎓\n\n"
                    "You have officially mastered native cross-platform mobile development:\n"
                    "1. 📱 Native View and Text layout\n"
                    "2. 📲 Multi-screen component architecture\n"
                    "3. 🎨 Flexbox mobile column styling\n"
                    "4. 👆 Finger tap interactions with `TouchableOpacity`\n"
                    "5. 📜 Swipeable feeds with `ScrollView`\n"
                    "6. 📇 Reusable mobile cards with props\n"
                    "7. 🏗️ Complete production smartphone profile screens!\n\n"
                    "You are now ready to build and publish real apps to the Apple App Store and Google Play Store! 🚀📱🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የሪያክት ኔቲቭ (React Native) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "ለስማርትፎኖች የሚሰሩ እውነተኛ የሞባይል አፖችን መገንባት በሚገባ ተምረዋል፦\n"
                    "1. 📱 የሞባይል View እና Text አጠቃቀም\n"
                    "2. 📲 ባለብዙ ስክሪን የሞባይል መዋቅር\n"
                    "3. 🎨 የሞባይል ፍሌክስቦክስ ስታይሎች\n"
                    "4. 👆 የጣት ንክኪ አዝራሮች በ `TouchableOpacity`\n"
                    "5. 📜 የሚንሸራሸሩ ገጾች በ `ScrollView`\n"
                    "6. 📇 እንደገና ጥቅም ላይ የሚውሉ የሞባይል ካርዶች\n"
                    "7. 🏗️ የተሟሉ የስማርትፎን ስክሪኖች!\n\n"
                    "አሁን ለአፕል አፕ ስቶር (App Store) እና ለጎግል ፕሌይ ስቶር (Play Store) አፖችን ለመገንባት ሙሉ በሙሉ ዝግጁ ነዎት! 🚀📱🔥"
                ),
            ),
        ],
    ),
]


def get_all_rn_chapters() -> List[TutorChapter]:
    """Return all React Native tutor chapters ordered."""
    return sorted(RN_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_rn_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve React Native tutor chapter by ID."""
    for ch in RN_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_rn_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next React Native chapter ID."""
    chapters = get_all_rn_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
