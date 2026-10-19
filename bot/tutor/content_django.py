"""Django curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

DJANGO_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="django_ch1",
        order=1,
        title_en="Django Ch 1: Meet Django & HttpResponse",
        title_am="ዲጃንጎ ምዕራፍ 1፦ ከዲጃንጎ ጋር መተዋወቅ እና HttpResponse",
        description_en="Learn the high-level Python web framework that powers Instagram and Pinterest.",
        description_am="እንደ ኢንስታግራም ያሉ ታላላቅ ድህረ-ገጾችን የሚያንቀሳቅሰውን የዲጃንጎ ፍሬምወርክ ይማሩ።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎸 *Welcome to Django!* 🐍✨\n\n"
                    "Known as *'The web framework for perfectionists with deadlines'*, **Django** is the "
                    "most comprehensive and powerful full-stack Python web framework in the world!\n\n"
                    "In Django, when a browser visits a page, Django passes an `HttpRequest` object into a "
                    "**View function**. The view does its work and returns an `HttpResponse` containing the HTML or text:\n\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef home_view(request):\n    return HttpResponse('Hello Django!')\n```"
                ),
                message_am=(
                    "🎸 *እንኳን ወደ ዲጃንጎ (Django) በደህና መጡ!* 🐍✨\n\n"
                    "በዓለም ላይ እጅግ ታዋቂ እና የተሟላ የፓይተን የድህረ-ገጽ ፍሬምወርክ የሆነው **ዲጃንጎ** "
                    "እንደ ኢንስታግራም እና ስፖቲፋይ ያሉ ታላላቅ ስርዓቶችን ያንቀሳቅሳል!\n\n"
                    "በዲጃንጎ ውስጥ ተጠቃሚ ገጽ ሲጠይቅ፣ ጥያቄው ወደ **ቪው (View) ፈንክሽን** ይላካል። "
                    "ፈንክሽኑ ስራውን ሰርቶ በ `HttpResponse` አማካኝነት ምላሽ ይመልሳል፦\n\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef home_view(request):\n    return HttpResponse('Hello Django!')\n```"
                ),
            ),
            TutorStep(
                id="django_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first Django view function returning `HttpResponse('Hello Django!')`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef home_view(request):\n    return HttpResponse('Hello Django!')\n```"
                ),
                message_am=(
                    "`HttpResponse('Hello Django!')` የሚመልስ የመጀመሪያውን የዲጃንጎ ቪው ፈንክሽን እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef home_view(request):\n    return HttpResponse('Hello Django!')\n```"
                ),
                expected_code_output="Hello Django!",
                hint_en="Define `home_view(request)` and return `HttpResponse('Hello Django!')`.",
                hint_am="`home_view(request)` ፈንክሽን ጽፈው `HttpResponse('Hello Django!')` መልሰው ይላኩ።",
                success_message_en=(
                    "🎉 *BOOM!* Your Django view received an HTTP request and delivered `Hello Django!`!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* የዲጃንጎ ቪው ፈንክሽንዎ ጥያቄውን ተቀብሎ `Hello Django!` ብሎ መልሷል!"
                ),
            ),
            TutorStep(
                id="django_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In Django, what object must every standard view function return?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በዲጃንጎ ውስጥ እያንዳንዱ መደበኛ የቪው ፈንክሽን ምን አይነት ኦብጀክት መመለስ አለበት?"
                ),
                options_en=[
                    "An HttpResponse (or its subclasses)",
                    "A raw SQL connection",
                    "A CSS stylesheet",
                    "A Python list",
                ],
                options_am=[
                    "HttpResponse (ወይም የሱ ንዑስ ክፍል)",
                    "የ SQL ዳታቤዝ ግንኙነት",
                    "የ CSS ስታይል ፋይል",
                    "ተራ የፓይተን ሊስት",
                ],
                correct_option_index=0,
                hint_en="Every view must return an `HttpResponse` instance!",
                hint_am="እያንዳንዱ ቪው `HttpResponse` ወይም የሱን ንዑስ ክፍል መመለስ አለበት!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch2",
        order=2,
        title_en="Django Ch 2: REST APIs with JsonResponse",
        title_am="ዲጃንጎ ምዕራፍ 2፦ የ REST API መረጃዎችን በ JsonResponse መላክ",
        description_en="Serve structured JSON data for mobile apps and modern frontends.",
        description_am="ለሞባይል እና ለድህረ-ገጽ አፖች የ JSON መረጃዎችን በ `JsonResponse` ማዘጋጀት።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📦 *REST APIs & `JsonResponse`* 📊\n\n"
                    "Modern web and mobile applications often need JSON data rather than HTML.\n\n"
                    "Django provides `JsonResponse`, a subclass of `HttpResponse` that automatically serializes "
                    "Python dictionaries into JSON format and sets `Content-Type: application/json`:\n\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef status_view(request):\n    return JsonResponse({'status': 'online', 'framework': 'Django'})\n```"
                ),
                message_am=(
                    "📦 *የ REST API መረጃዎች እና `JsonResponse`* 📊\n\n"
                    "ዘመናዊ አፕሊኬሽኖች ከድህረ-ገጽ ይልቅ የ JSON መረጃዎችን ይፈልጋሉ።\n\n"
                    "ዲጃንጎ የፓይተን ዲክሽነሪዎችን በቀጥታ ወደ JSON የሚቀይር `JsonResponse` የተባለ ክፍል አለው፦\n\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef status_view(request):\n    return JsonResponse({'status': 'online', 'framework': 'Django'})\n```"
                ),
            ),
            TutorStep(
                id="django_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a view returning `JsonResponse({'status': 'online', 'framework': 'Django'})`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef status_view(request):\n    return JsonResponse({'status': 'online', 'framework': 'Django'})\n```"
                ),
                message_am=(
                    "`JsonResponse({'status': 'online', 'framework': 'Django'})` የሚመልስ የዲጃንጎ ቪው ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef status_view(request):\n    return JsonResponse({'status': 'online', 'framework': 'Django'})\n```"
                ),
                expected_code_output='{"status": "online", "framework": "Django"}',
                hint_en="Return `JsonResponse({'status': 'online', 'framework': 'Django'})` inside `status_view`.",
                hint_am="በ `status_view` ውስጥ `JsonResponse(...)` በመጠቀም መልስ ይላኩ።",
                success_message_en=(
                    "🌟 *PERFECT!* You served structured JSON directly from Django with proper MIME headers!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* ከዲጃንጎ ሰርቨርዎ ላይ የተሟላ የ JSON መረጃ በስኬት አቅርበዋል!"
                ),
            ),
            TutorStep(
                id="django_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which Django class serializes Python dictionaries into JSON responses?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የፓይተን ዲክሽነሪ መረጃዎችን ወደ JSON ቀይሮ የሚልከው የዲጃንጎ ክፍል የትኛው ነው?"
                ),
                options_en=[
                    "JsonResponse",
                    "JsonParser",
                    "DictResponse",
                    "HttpResponseText",
                ],
                options_am=[
                    "JsonResponse",
                    "JsonParser",
                    "DictResponse",
                    "HttpResponseText",
                ],
                correct_option_index=0,
                hint_en="Use `JsonResponse` to return JSON data!",
                hint_am="የ JSON መረጃዎችን ለመላክ `JsonResponse` ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch3",
        order=3,
        title_en="Django Ch 3: Template Engine & {{ Context }}",
        title_am="ዲጃንጎ ምዕራፍ 3፦ የዲጃንጎ ቴምፕሌት እና {{ Context }}",
        description_en="Separate presentation from business logic using the Django Template Language (DTL).",
        description_am="የድህረ-ገጽ እይታን በዲጃንጎ ቴምፕሌት አማካኝነት ከኮድ መለየት።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎨 *The Django Template Language (DTL)* 📝\n\n"
                    "To keep HTML clean and separated from Python logic, Django features a built-in template engine.\n\n"
                    "Using double curly braces `{{ variable }}`, templates can render dynamic values provided by a `Context` dictionary:\n\n"
                    "```python\nfrom django.template import Template, Context\n\ntemplate = Template('<h1>Welcome to {{ site_name }}!</h1>')\ncontext = Context({'site_name': 'CodeBuddy'})\noutput = template.render(context)\n```"
                ),
                message_am=(
                    "🎨 *የዲጃንጎ ቴምፕሌት ቋንቋ (DTL)* 📝\n\n"
                    "የድህረ-ገጽ ዲዛይን ከፓይተን ኮድ ጋር እንዳይደባለቅ ዲጃንጎ የተለየ የቴምፕሌት አሰራር ይጠቀማል።\n\n"
                    "በድርብ የፈረንሳይ ቅንፍ `{{ variable }}` አማካኝነት ከ `Context` የሚመጡ መረጃዎች በገጹ ላይ ይወጣሉ፦\n\n"
                    "```python\nfrom django.template import Template, Context\n\ntemplate = Template('<h1>Welcome to {{ site_name }}!</h1>')\ncontext = Context({'site_name': 'CodeBuddy'})\noutput = template.render(context)\n```"
                ),
            ),
            TutorStep(
                id="django_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Render a template displaying `<h1>Welcome to {{ site_name }}!</h1>` with `site_name: CodeBuddy`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.template import Template, Context\n\ntemplate = Template('<h1>Welcome to {{ site_name }}!</h1>')\ncontext = Context({'site_name': 'CodeBuddy'})\noutput = template.render(context)\n```"
                ),
                message_am=(
                    "`site_name: CodeBuddy` በማድረግ `<h1>Welcome to {{ site_name }}!</h1>` የሚያወጣ የቴምፕሌት ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.template import Template, Context\n\ntemplate = Template('<h1>Welcome to {{ site_name }}!</h1>')\ncontext = Context({'site_name': 'CodeBuddy'})\noutput = template.render(context)\n```"
                ),
                expected_code_output="<h1>Welcome to CodeBuddy!</h1>",
                hint_en="Create `Template(...)` and `Context({'site_name': 'CodeBuddy'})`, then call `template.render(context)`.",
                hint_am="`Template(...)` እና `Context(...)` ፈጥረው `template.render(context)` ይጥሩ።",
                success_message_en=(
                    "🎯 *SPOT ON!* Django evaluated the template variable and rendered clean HTML!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ዲጃንጎ ቴምፕሌቱን ከዳታው ጋር አዋህዶ ንጹህ HTML አዘጋጅቷል!"
                ),
            ),
            TutorStep(
                id="django_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "What syntax does the Django Template Language use to inject dynamic variables into HTML?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በዲጃንጎ ቴምፕሌት ውስጥ ተለዋዋጭ መረጃዎችን ለማሳየት የትኛው ምልክት ያገለግላል?"
                ),
                options_en=[
                    "{{ variable }} (Double curly braces)",
                    "{ variable } (Single curly brace)",
                    "${ variable } (Template literal)",
                    "# variable # (Hash marks)",
                ],
                options_am=[
                    "{{ variable }} (ድርብ የፈረንሳይ ቅንፍ)",
                    "{ variable } (ነጠላ የፈረንሳይ ቅንፍ)",
                    "${ variable } (የዶላር ምልክት)",
                    "# variable # (የሃሽ ምልክት)",
                ],
                correct_option_index=0,
                hint_en="Double curly braces `{{ }}` output variables in Django templates!",
                hint_am="ድርብ የፈረንሳይ ቅንፍ `{{ }}` መረጃዎችን በቴምፕሌት ውስጥ ለማሳየት ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch4",
        order=4,
        title_en="Django Ch 4: URL Routing with path()",
        title_am="ዲጃንጎ ምዕራፍ 4፦ የመንገድ ቅንብር በ path()",
        description_en="Route incoming URLs to their corresponding Python view functions.",
        description_am="የሚጠየቁ ሊንኮችን ወደ ተገቢው የቪው ፈንክሽን በ `path()` መምራት።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🗺️ *URL Routing with `path()`* 🛣️\n\n"
                    "Django maps incoming web URLs to view functions using `urlpatterns` and the `path()` helper:\n\n"
                    "```python\nfrom django.urls import path\nfrom django.http import HttpResponse\n\ndef about_view(request):\n    return HttpResponse('About CodeBuddy Learning Platform')\n\nurlpatterns = [\n    path('about/', about_view),\n]\n```\n\n"
                    "When users visit `/about/`, Django matches the path and executes `about_view(request)`!"
                ),
                message_am=(
                    "🗺️ *የሊንኮች መንገድ በ `path()`* 🛣️\n\n"
                    "ዲጃንጎ የሚጠየቁ የድህረ-ገጽ ሊንኮችን ከቪው ፈንክሽኖች ጋር የሚያገናኘው በ `path()` እና በ `urlpatterns` አማካኝነት ነው፦\n\n"
                    "```python\nfrom django.urls import path\nfrom django.http import HttpResponse\n\ndef about_view(request):\n    return HttpResponse('About CodeBuddy Learning Platform')\n\nurlpatterns = [\n    path('about/', about_view),\n]\n```\n\n"
                    "ተጠቃሚው `/about/` ብሎ ሲጠይቅ ዲጃንጎ በቀጥታ `about_view(request)`ን ያሰራዋል!"
                ),
            ),
            TutorStep(
                id="django_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Define an `about_view` returning `'About CodeBuddy Learning Platform'` and register it in `urlpatterns`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.urls import path\nfrom django.http import HttpResponse\n\ndef about_view(request):\n    return HttpResponse('About CodeBuddy Learning Platform')\n\nurlpatterns = [\n    path('about/', about_view),\n]\n```"
                ),
                message_am=(
                    "`'About CodeBuddy Learning Platform'` የሚመልስ `about_view` ጽፈው በ `urlpatterns` ውስጥ አስመዝግበው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.urls import path\nfrom django.http import HttpResponse\n\ndef about_view(request):\n    return HttpResponse('About CodeBuddy Learning Platform')\n\nurlpatterns = [\n    path('about/', about_view),\n]\n```"
                ),
                expected_code_output="About CodeBuddy Learning Platform",
                hint_en="Define `about_view` and assign `urlpatterns = [path('about/', about_view)]`.",
                hint_am="`about_view`ን ከጻፉ በኋላ በ `urlpatterns = [path('about/', about_view)]` ውስጥ ይመድቡት።",
                success_message_en=(
                    "🔥 *OUTSTANDING!* Django routed the URL through `urlpatterns` directly to your view!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* ዲጃንጎ ሊንኩን በመለየት በቀጥታ ወደ እርስዎ ቪው ፈንክሽን መርቶታል!"
                ),
            ),
            TutorStep(
                id="django_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which function in `django.urls` is standard for defining URL-to-view route entries?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በ `django.urls` ውስጥ ሊንኮችን ከቪው ፈንክሽን ጋር ለማገናኘት መደበኛ የሆነው የትኛው ፈንክሽን ነው?"
                ),
                options_en=[
                    "path()",
                    "route()",
                    "connect()",
                    "link()",
                ],
                options_am=[
                    "path()",
                    "route()",
                    "connect()",
                    "link()",
                ],
                correct_option_index=0,
                hint_en="Use `path('route/', view_func)`!",
                hint_am="`path('route/', view_func)` ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch5",
        order=5,
        title_en="Django Ch 5: Dynamic Path Converters",
        title_am="ዲጃንጎ ምዕራፍ 5፦ ተለዋዋጭ የመንገድ መለያዎች",
        description_en="Capture dynamic URL parameters using path converters like <int:user_id>.",
        description_am="እንደ `<int:user_id>` ያሉ ተለዋዋጭ መለያዎችን ከሊንክ ላይ መቀበል።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "⚡ *Dynamic Path Converters* 🔢\n\n"
                    "When building user profiles or blog posts, URLs contain IDs like `/users/42/`.\n\n"
                    "Django captures these values in path converters such as `<int:user_id>` and passes them "
                    "as keyword arguments directly into your view:\n\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef user_profile(request, user_id):\n    return HttpResponse(f'Profile of User #{user_id}')\n```\n\n"
                    "The `int` converter guarantees that `user_id` is parsed directly as an integer!"
                ),
                message_am=(
                    "⚡ *ተለዋዋጭ የመንገድ መለያዎች* 🔢\n\n"
                    "እንደ የተጠቃሚ መለያ ያሉ መረጃዎችን ከሊንክ ላይ ለመቀበል ዲጃንጎ እንደ `<int:user_id>` ያሉ መለያዎችን ይጠቀማል፦\n\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef user_profile(request, user_id):\n    return HttpResponse(f'Profile of User #{user_id}')\n```\n\n"
                    "`int` መለያው `user_id` ቁጥር መሆኑን አረጋግጦ ወደ ፈንክሽኑ ያስተላልፈዋል!"
                ),
            ),
            TutorStep(
                id="django_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a `user_profile(request, user_id)` view returning `f'Profile of User #{user_id}'`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef user_profile(request, user_id):\n    return HttpResponse(f'Profile of User #{user_id}')\n```"
                ),
                message_am=(
                    "`f'Profile of User #{user_id}'` የሚመልስ `user_profile(request, user_id)` ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.http import HttpResponse\n\ndef user_profile(request, user_id):\n    return HttpResponse(f'Profile of User #{user_id}')\n```"
                ),
                expected_code_output="Profile of User #42",
                hint_en="Define `user_profile(request, user_id)` returning `HttpResponse(f'Profile of User #{user_id}')`.",
                hint_am="`user_profile(request, user_id)` ፈንክሽን ጽፈው `HttpResponse(f'Profile of User #{user_id}')` ይመልሱ።",
                success_message_en=(
                    "🎉 *TERRIFIC!* Django passed the captured URL parameter and returned User #42's profile!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* ዲጃንጎ የቁጥር መለያውን ወስዶ የተጠቃሚ #42ን ፕሮፋይል በተሳካ ሁኔታ አሳይቷል!"
                ),
            ),
            TutorStep(
                id="django_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In the path definition `'articles/<int:year>/'`, what does `<int:...>` ensure?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "`'articles/<int:year>/'` በሚለው መንገድ ውስጥ `<int:...>` ምንን ያረጋግጣል?"
                ),
                options_en=[
                    "It matches only integer digits and passes year as a Python int",
                    "It encrypts the year with a hash",
                    "It converts the year to binary code",
                    "It deletes old articles",
                ],
                options_am=[
                    "ቁጥሮችን ብቻ በመለየት ወደ ፓይተን int ይቀይረዋል",
                    "ዓመቱን በምስጢር ኮድ ይደብቀዋል",
                    "ወደ ባይነሪ ይቀይረዋል",
                    "የቆዩ ጽሁፎችን ይሰርዛል",
                ],
                correct_option_index=0,
                hint_en="`<int:...>` matches positive integers and converts them to `int`!",
                hint_am="`<int:...>` ቁጥሮችን ብቻ በመቀበል ወደ ፓይተን integer ይቀይራል!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch6",
        order=6,
        title_en="Django Ch 6: Database Models with Django ORM",
        title_am="ዲጃንጎ ምዕራፍ 6፦ የዳታቤዝ ሞዴሎች በዲጃንጎ ORM",
        description_en="Define relational database tables and models directly in Python classes.",
        description_am="የዳታቤዝ ሰንጠረዦችን በቀጥታ በፓይተን ክላሶች (ORM) መገንባት።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🗄️ *The Django ORM (Object-Relational Mapper)* 🏛️\n\n"
                    "Instead of writing raw SQL commands by hand, Django lets you define database models in pure Python!\n\n"
                    "Each subclass of `models.Model` represents a database table, and attributes represent columns:\n\n"
                    "```python\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=100)\n    students = models.IntegerField(default=0)\n\n    def __str__(self):\n        return f'{self.title} ({self.students} enrolled)'\n\n    class Meta:\n        app_label = 'learn'\n```"
                ),
                message_am=(
                    "🗄️ *የዲጃንጎ ORM (Object-Relational Mapper)* 🏛️\n\n"
                    "የ SQL ትዕዛዞችን በእጅ ከመጻፍ ይልቅ ዲጃንጎ የዳታቤዝ ሰንጠረዦችን በንጹህ የፓይተን ክላሶች እንድንገልጽ ያስችለናል!\n\n"
                    "እያንዳንዱ የ `models.Model` ክላስ አንድ የዳታቤዝ ሰንጠረዥን ይወክላል፦\n\n"
                    "```python\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=100)\n    students = models.IntegerField(default=0)\n\n    def __str__(self):\n        return f'{self.title} ({self.students} enrolled)'\n\n    class Meta:\n        app_label = 'learn'\n```"
                ),
            ),
            TutorStep(
                id="django_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Define a `Course` model with `title`, `students`, and a descriptive `__str__` method!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```python\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=100)\n    students = models.IntegerField(default=0)\n\n    def __str__(self):\n        return f'{self.title} ({self.students} enrolled)'\n\n    class Meta:\n        app_label = 'learn'\n```"
                ),
                message_am=(
                    "`title`፣ `students` እና `__str__` የያዘ የ `Course` ሞዴል ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=100)\n    students = models.IntegerField(default=0)\n\n    def __str__(self):\n        return f'{self.title} ({self.students} enrolled)'\n\n    class Meta:\n        app_label = 'learn'\n```"
                ),
                expected_code_output="Django Web Development (250 enrolled)",
                hint_en="Define `Course(models.Model)` with `title = models.CharField(...)` and `def __str__(self): ...`.",
                hint_am="`Course(models.Model)` ክላስ ጽፈው `title` እና `students` መስኮችን ያካትቱ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* Django initialized your ORM model and verified its schema definition!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* ዲጃንጎ የዳታቤዝ ሞዴልዎን በተሳካ ሁኔታ አንብቦ አዋቅሮታል!"
                ),
            ),
            TutorStep(
                id="django_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In Django, what base class do all database models inherit from?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በዲጃንጎ ውስጥ ሁሉም የዳታቤዝ ሞዴሎች ከየትኛው ዋና ክላስ ይወረሳሉ?"
                ),
                options_en=[
                    "django.db.models.Model",
                    "django.views.View",
                    "django.urls.Path",
                    "django.http.HttpResponse",
                ],
                options_am=[
                    "django.db.models.Model",
                    "django.views.View",
                    "django.urls.Path",
                    "django.http.HttpResponse",
                ],
                correct_option_index=0,
                hint_en="All Django models inherit from `models.Model`!",
                hint_am="ሁሉም የዲጃንጎ ሞዴሎች ከ `models.Model` ይወረሳሉ!",
            ),
        ],
    ),
    TutorChapter(
        id="django_ch7",
        order=7,
        title_en="Django Ch 7: Full-Stack Developer Profile Capstone",
        title_am="ዲጃንጎ ምዕራፍ 7፦ የተሟላ የፕሮፋይል API ፕሮጀክት",
        description_en="Combine Django views, JsonResponse, and metadata into a production endpoint.",
        description_am="የዲጃንጎ ቪው፣ JsonResponse እና መረጃዎችን በማጣመር የተሟላ የፕሮጀክት API መስራት።",
        track="django",
        steps=[
            TutorStep(
                id="django_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Production Django Profile API!* 🌟\n\n"
                    "Let's combine everything you've mastered into a production-grade Django endpoint:\n"
                    "1. Clean Python function-based view\n"
                    "2. `JsonResponse` with HTTP status headers\n"
                    "3. Complete developer metadata: `developer`, `framework`, and `role`!\n\n"
                    "Ready to complete your Django graduation?"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የዲጃንጎ ፕሮፋይል API!* 🌟\n\n"
                    "እስካሁን የተማርነውን በሙሉ በማጣመር እውነተኛ የዲጃንጎ API እንገነባለን፦\n"
                    "1. ንጹህ የፓይተን ቪው ፈንክሽን\n"
                    "2. የተሟላ የ `JsonResponse` ምላሽ\n"
                    "3. የገንቢ መረጃዎች፦ `developer`፣ `framework`፣ እና `role`!\n\n"
                    "የዲጃንጎ ምረቃዎን ለማጠናቀቅ ዝግጁ ነዎት?"
                ),
            ),
            TutorStep(
                id="django_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write a view `developer_profile(request)` returning `{ 'developer': 'Liya', 'framework': 'Django', 'role': 'Full-Stack Python Engineer' }`!\n\n"
                    "👇 *Type and send:*\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef developer_profile(request):\n    return JsonResponse({\n        'developer': 'Liya',\n        'framework': 'Django',\n        'role': 'Full-Stack Python Engineer'\n    })\n```"
                ),
                message_am=(
                    "`developer_profile(request)` የሚመልስ የተሟላ የዲጃንጎ ቪው ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```python\nfrom django.http import JsonResponse\n\ndef developer_profile(request):\n    return JsonResponse({\n        'developer': 'Liya',\n        'framework': 'Django',\n        'role': 'Full-Stack Python Engineer'\n    })\n```"
                ),
                expected_code_output='{"developer": "Liya", "framework": "Django", "role": "Full-Stack Python Engineer"}',
                hint_en="Return the dictionary inside `JsonResponse({...})` in `developer_profile(request)`.",
                hint_am="በ `developer_profile(request)` ውስጥ ዲክሽነሪውን በ `JsonResponse` መልሰው ይላኩ።",
                success_message_en=(
                    "🏆 *DJANGO MASTER!* You have officially built and deployed a production Django API endpoint!"
                ),
                success_message_am=(
                    "🏆 *የዲጃንጎ (Django) ባለሙያ!* እውነተኛ ዘመናዊ የዲጃንጎ API ሰርቨር በስኬት ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="django_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! DJANGO GRADUATE!** 🌟🎓\n\n"
                    "You have conquered the premier Python web framework:\n"
                    "1. 🎸 `HttpResponse` & Web View architectures\n"
                    "2. 📦 Structured REST APIs with `JsonResponse`\n"
                    "3. 🎨 DTL Templates with `{{ Context }}`\n"
                    "4. 🗺️ URL Routing with `path()` & `urlpatterns`\n"
                    "5. ⚡ Dynamic URL converters with `<int:id>`\n"
                    "6. 🗄️ Relational database models with Django ORM\n"
                    "7. 🏗️ Modern Full-Stack Python backend microservices!\n\n"
                    "You are now ready to build production web applications with Django and Python! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የዲጃንጎ (Django) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "ተወዳጁን የፓይተን የድህረ-ገጽ ፍሬምወርክ በሚገባ ተምረዋል፦\n"
                    "1. 🎸 `HttpResponse` እና የቪው አሰራር\n"
                    "2. 📦 የ REST API መረጃዎችን በ `JsonResponse` ማዘጋጀት\n"
                    "3. 🎨 የዲጃንጎ ቴምፕሌት በ `{{ Context }}`\n"
                    "4. 🗺️ የሊንኮች መንገድ በ `path()` እና `urlpatterns`\n"
                    "5. ⚡ ተለዋዋጭ መለያዎች በ `<int:id>`\n"
                    "6. 🗄️ የዳታቤዝ ሞዴሎች በዲጃንጎ ORM\n"
                    "7. 🏗️ የተሟሉ ዘመናዊ የጀርባ ሰርቨሮችን መገንባት!\n\n"
                    "አሁን በዲጃንጎ እና በፓይተን የተሟሉ ድህረ-ገጾችን ለመገንባት ሙሉ በሙሉ ብቁ ነዎት! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_django_chapters() -> List[TutorChapter]:
    """Return all Django tutor chapters ordered."""
    return sorted(DJANGO_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_django_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve Django tutor chapter by ID."""
    for ch in DJANGO_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_django_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next Django chapter ID."""
    chapters = get_all_django_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
