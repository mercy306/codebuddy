"""Express.js curriculum content for the interactive conversational tutor."""

from __future__ import annotations

from typing import List, Optional
from bot.tutor.models import TutorChapter, TutorStep, StepType

EXPRESS_TUTOR_CHAPTERS: List[TutorChapter] = [
    TutorChapter(
        id="express_ch1",
        order=1,
        title_en="Express Ch 1: Meet Express.js & First Server",
        title_am="ኤክስፕረስ ምዕራፍ 1፦ ከኤክስፕረስ ጋር መተዋወቅ እና የመጀመሪያው ሰርቨር",
        description_en="Learn the minimalist, blazing-fast web framework that powers Node.js backends.",
        description_am="የኖድ (Node.js) የጀርባ አሰራርን የሚያንቀሳቅሰውን ፈጣን እና ተወዳጅ የኤክስፕረስ ፍሬምወርክ ይማሩ።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch1_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🚂 *Welcome to Express.js!* 🌐⚡\n\n"
                    "**Express.js** is the most popular backend web framework in the JavaScript world! "
                    "It sits on top of Node.js and gives you simple, powerful tools to build web servers and APIs.\n\n"
                    "To create an Express server:\n"
                    "1. Import Express: `const express = require('express');`\n"
                    "2. Create the app: `const app = express();`\n"
                    "3. Define a route: `app.get('/', (req, res) => res.send('Hello Express!'));`\n\n"
                    "The `req` (Request) object holds incoming data from users, and `res` (Response) sends data back!"
                ),
                message_am=(
                    "🚂 *እንኳን ወደ ኤክስፕረስ (Express.js) በደህና መጡ!* 🌐⚡\n\n"
                    "**Express.js** በጃቫስክሪፕት ዓለም ውስጥ እጅግ ተወዳጅ የሆነው የጀርባ (Backend) የድህረ-ገጽ ፍሬምወርክ ነው! "
                    "በኖድ (Node.js) ላይ ተመስርቶ የድህረ-ገጽ ሰርቨሮችን እና APIዎችን በቀላሉ ለመገንባት ያስችላል።\n\n"
                    "የኤክስፕረስ ሰርቨር ለመገንባት፦\n"
                    "1. ኤክስፕረስን ማስመጣት፦ `const express = require('express');`\n"
                    "2. አፑን መፍጠር፦ `const app = express();`\n"
                    "3. የጥሪ መንገድ (Route) መወሰን፦ `app.get('/', (req, res) => res.send('Hello Express!'));`\n\n"
                    "`req` ከተጠቃሚው የሚመጣውን መረጃ ሲይዝ፣ `res` ደግሞ ወደ ተጠቃሚው መልስ ለመላክ ያገለግላል!"
                ),
            ),
            TutorStep(
                id="express_ch1_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Let's write your first Express server responding with `'Hello Express!'` at the root path `'/'`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => {\n  res.send('Hello Express!');\n});\n```"
                ),
                message_am=(
                    "በዋናው መስመር `'/'` ላይ `'Hello Express!'` የሚመልስ የመጀመሪያውን ሰርቨር እንጻፍ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => {\n  res.send('Hello Express!');\n});\n```"
                ),
                expected_code_output="Hello Express!",
                hint_en="Write `app.get('/', (req, res) => res.send('Hello Express!'));`.",
                hint_am="`app.get('/', (req, res) => res.send('Hello Express!'));` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *BOOM!* Your Express server received an HTTP GET request and sent back `Hello Express!`!"
                ),
                success_message_am=(
                    "🎉 *በጣም ድንቅ!* የኤክስፕረስ ሰርቨርዎ የ GET ጥያቄ ተቀብሎ `Hello Express!` ብሎ መልሷል!"
                ),
            ),
            TutorStep(
                id="express_ch1_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Brain Check:*\n\n"
                    "In an Express route handler `(req, res) => { ... }`, what is the purpose of the `res` object?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በኤክስፕረስ `(req, res) => { ... }` ውስጥ የ `res` ኦብጀክት ዋና ጥቅም ምንድን ነው?"
                ),
                options_en=[
                    "To send HTTP responses back to the client",
                    "To restart the computer operating system",
                    "To style HTML elements with CSS",
                    "To compile TypeScript code into bytecode",
                ],
                options_am=[
                    "የ HTTP ምላሾችን ወደ ተጠቃሚው መላክ",
                    "ኮምፒውተሩን እንደገና ማስነሳት",
                    "የ HTML ገጾችን በ CSS ማስዋብ",
                    "የታይፕስክሪፕት ኮድን ወደ ባይትኮድ መቀየር",
                ],
                correct_option_index=0,
                hint_en="`res` stands for Response—used with `res.send()`, `res.json()`, and `res.status()`!",
                hint_am="`res` የምላሽ (Response) መለያ ሲሆን መልሶችን ለመላክ ያገለግላል!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch2",
        order=2,
        title_en="Express Ch 2: Building REST APIs with res.json()",
        title_am="ኤክስፕረስ ምዕራፍ 2፦ የ REST API ዳታዎችን በ res.json() መላክ",
        description_en="Send structured JSON responses to power modern frontend apps and mobile clients.",
        description_am="ለድህረ-ገጾች እና ለሞባይል አፖች የ JSON መረጃዎችን በ `res.json()` ማዘጋጀት።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch2_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📊 *REST APIs & JSON Responses* 📦\n\n"
                    "Modern mobile apps (React Native) and frontend websites (React, Angular, Vue) communicate with backends using **JSON** (JavaScript Object Notation).\n\n"
                    "Express makes this effortless with `res.json()`:\n\n"
                    "```javascript\napp.get('/api/status', (req, res) => {\n  res.json({ status: 'online', users: 100 });\n});\n```\n\n"
                    "Express automatically converts your JavaScript object into JSON text and sets the HTTP header `Content-Type: application/json`!"
                ),
                message_am=(
                    "📊 *የ REST API እና የ JSON ምላሾች* 📦\n\n"
                    "ዘመናዊ የሞባይል አፖች (React Native) እና የፊት ድህረ-ገጾች (React, Angular, Vue) ከጀርባ ሰርቨር ጋር የሚገናኙት በ **JSON** መረጃ ቅርጽ ነው!\n\n"
                    "ኤክስፕረስ ይህንን በ `res.json()` እጅግ ቀላል ያደርገዋል፦\n\n"
                    "```javascript\napp.get('/api/status', (req, res) => {\n  res.json({ status: 'online', users: 100 });\n});\n```\n\n"
                    "ኤክስፕረስ የጃቫስክሪፕት ኦብጀክቱን በራስ-ሰር ወደ JSON ይቀይረዋል እንዲሁም የ `Content-Type: application/json` ራስጌ ያዘጋጃል!"
                ),
            ),
            TutorStep(
                id="express_ch2_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create an endpoint `/api/status` returning `{ status: 'online', users: 100 }` with `res.json()`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/api/status', (req, res) => {\n  res.json({ status: 'online', users: 100 });\n});\n```"
                ),
                message_am=(
                    "`/api/status` ላይ `{ status: 'online', users: 100 }` የሚመልስ የኤክስፕረስ API ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/api/status', (req, res) => {\n  res.json({ status: 'online', users: 100 });\n});\n```"
                ),
                expected_code_output='{"status":"online","users":100}',
                hint_en="Call `res.json({ status: 'online', users: 100 })` inside `app.get('/api/status', ...)`.",
                hint_am="በ `/api/status` ውስጥ `res.json({ status: 'online', users: 100 })` ብለው ይጻፉ።",
                success_message_en=(
                    "🌟 *PERFECT!* You served real REST JSON from Express with status online!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* እውነተኛ የ REST API JSON መረጃ ከኤክስፕረስ ሰርቨርዎ ላይ በተሳካ ሁኔታ አቅርበዋል!"
                ),
            ),
            TutorStep(
                id="express_ch2_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which method in Express sends JavaScript objects formatted as JSON with the proper Content-Type?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "በኤክስፕረስ ውስጥ የጃቫስክሪፕት መረጃዎችን በ JSON ቅርጽ የሚመልሰው የትኛው ዘዴ ነው?"
                ),
                options_en=[
                    "res.json()",
                    "res.html()",
                    "res.writeDatabase()",
                    "res.echo()",
                ],
                options_am=[
                    "res.json()",
                    "res.html()",
                    "res.writeDatabase()",
                    "res.echo()",
                ],
                correct_option_index=0,
                hint_en="`res.json()` serializes objects and sends JSON data!",
                hint_am="`res.json()` መረጃን ወደ JSON ቀይሮ ይልካል!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch3",
        order=3,
        title_en="Express Ch 3: Dynamic Routes with req.params",
        title_am="ኤክስፕረስ ምዕራፍ 3፦ ተለዋዋጭ መንገዶች በ req.params",
        description_en="Capture dynamic values from URL paths such as user IDs or order numbers.",
        description_am="ከሊንኮች ላይ የተጠቃሚ መለያዎችን (ID) በ `req.params` መቀበል።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch3_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎯 *Dynamic Route Parameters: `req.params`* 🔍\n\n"
                    "Real web apps have millions of users. Instead of creating routes for every user, "
                    "Express lets you define dynamic placeholders using a colon (`:`):\n\n"
                    "```javascript\napp.get('/users/:id', (req, res) => {\n  res.send(`User ID: ${req.params.id}`);\n});\n```\n\n"
                    "- When someone visits `/users/42`, `req.params.id` becomes `'42'`!\n"
                    "- When someone visits `/users/99`, `req.params.id` becomes `'99'`!"
                ),
                message_am=(
                    "🎯 *ተለዋዋጭ የጥሪ መንገዶች፦ `req.params`* 🔍\n\n"
                    "መተግበሪያዎች በሚሊዮን የሚቆጠሩ ተጠቃሚዎች አሏቸው። ለእያንዳንዱ ተጠቃሚ ለየብቻ ከመጻፍ ይልቅ "
                    "ኤክስፕረስ በኮለን (`:`) ምልክት ተለዋዋጭ መለያዎችን እንድንይዝ ይፈቅዳል፦\n\n"
                    "```javascript\napp.get('/users/:id', (req, res) => {\n  res.send(`User ID: ${req.params.id}`);\n});\n```\n\n"
                    "- ተጠቃሚው `/users/42` ብሎ ሲጠይቅ `req.params.id` ዋጋው `'42'` ይሆናል!\n"
                    "- `/users/99` ሲጠይቅ ደግሞ ዋጋው `'99'` ይሆናል!"
                ),
            ),
            TutorStep(
                id="express_ch3_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Define a route `/users/:id` that responds with `User ID: ${req.params.id}`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/users/:id', (req, res) => {\n  res.send(`User ID: ${req.params.id}`);\n});\n```"
                ),
                message_am=(
                    "`User ID: ${req.params.id}` የሚመልስ የ `/users/:id` መስመር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/users/:id', (req, res) => {\n  res.send(`User ID: ${req.params.id}`);\n});\n```"
                ),
                expected_code_output="User ID: 42",
                hint_en="Use `app.get('/users/:id', (req, res) => res.send(`User ID: ${req.params.id}`));`.",
                hint_am="`app.get('/users/:id', ...)` በማለት በ `req.params.id` ዋጋውን ያሳዩ።",
                success_message_en=(
                    "🎯 *SPOT ON!* Express captured the URL segment and extracted `User ID: 42`!"
                ),
                success_message_am=(
                    "🎯 *ትክክል!* ኤክስፕረስ ከሊንኩ ላይ ቁጥሩን ወስዶ `User ID: 42` ብሎ መልሷል!"
                ),
            ),
            TutorStep(
                id="express_ch3_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Quick Question:*\n\n"
                    "In the route pattern `'/posts/:slug'`, where is the value of `:slug` accessed in the handler?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "`'/posts/:slug'` በሚለው መንገድ ውስጥ የ `:slug` ዋጋ በኮድ ውስጥ የት ይገኛል?"
                ),
                options_en=[
                    "req.params.slug",
                    "req.body.slug",
                    "req.headers.slug",
                    "req.database.slug",
                ],
                options_am=[
                    "req.params.slug",
                    "req.body.slug",
                    "req.headers.slug",
                    "req.database.slug",
                ],
                correct_option_index=0,
                hint_en="Route parameters are always accessed on `req.params`!",
                hint_am="የመስመር መለያዎች ሁልጊዜ በ `req.params` ውስጥ ይገኛሉ!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch4",
        order=4,
        title_en="Express Ch 4: Query Strings with req.query",
        title_am="ኤክስፕረስ ምዕራፍ 4፦ የመፈለጊያ ቃላትን በ req.query ማንበብ",
        description_en="Read optional search filters and pagination parameters from URLs.",
        description_am="ከመፈለጊያ ሊንኮች ላይ መረጃዎችን በ `req.query` መለየት።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch4_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🔍 *Query Strings: `req.query`* 🔎\n\n"
                    "When users search Google, filter items on an e-commerce shop, or paginate results, "
                    "they use **query strings** in the URL after a question mark (`?`):\n\n"
                    "`/search?q=nodejs`\n\n"
                    "In Express, query parameters are parsed automatically into `req.query`:\n\n"
                    "```javascript\napp.get('/search', (req, res) => {\n  res.send(`Search results for: ${req.query.q}`);\n});\n```"
                ),
                message_am=(
                    "🔍 *የመፈለጊያ ቃላት፦ `req.query`* 🔎\n\n"
                    "ተጠቃሚዎች በጉግል ሲፈልጉ፣ በመገበያያ ገጾች ላይ እቃዎችን ሲያጣሩ ወይም ገጾችን ሲቀያይሩ "
                    "ከጥያቄ ምልክት (`?`) በኋላ የሚመጡ **የመፈለጊያ ቃላትን (Query Strings)** ይጠቀማሉ፦\n\n"
                    "`/search?q=nodejs`\n\n"
                    "በኤክስፕረስ ውስጥ እነዚህ መረጃዎች በራስ-ሰር በ `req.query` ውስጥ ይቀመጣሉ፦\n\n"
                    "```javascript\napp.get('/search', (req, res) => {\n  res.send(`Search results for: ${req.query.q}`);\n});\n```"
                ),
            ),
            TutorStep(
                id="express_ch4_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Create a `/search` endpoint that returns `Search results for: ${req.query.q}`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/search', (req, res) => {\n  res.send(`Search results for: ${req.query.q}`);\n});\n```"
                ),
                message_am=(
                    "`Search results for: ${req.query.q}` የሚመልስ የ `/search` መስመር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/search', (req, res) => {\n  res.send(`Search results for: ${req.query.q}`);\n});\n```"
                ),
                expected_code_output="Search results for: nodejs",
                hint_en="Respond with `Search results for: ${req.query.q}` inside `app.get('/search', ...)`.",
                hint_am="በ `/search` ውስጥ `Search results for: ${req.query.q}` ብለው ይመልሱ።",
                success_message_en=(
                    "🔥 *OUTSTANDING!* Express parsed the query parameter and returned search results for nodejs!"
                ),
                success_message_am=(
                    "🔥 *ድንቅ ስራ!* ኤክስፕረስ የመፈለጊያ ቃሉን አንብቦ ለ nodejs ውጤቶችን አሳይቷል!"
                ),
            ),
            TutorStep(
                id="express_ch4_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "In the URL `/products?category=shoes&limit=10`, how do you access the category value in Express?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "`/products?category=shoes&limit=10` በሚለው ሊንክ ውስጥ የ category ዋጋ በኤክስፕረስ እንዴት ይነበባል?"
                ),
                options_en=[
                    "req.query.category",
                    "req.params.category",
                    "req.body.category",
                    "req.headers.category",
                ],
                options_am=[
                    "req.query.category",
                    "req.params.category",
                    "req.body.category",
                    "req.headers.category",
                ],
                correct_option_index=0,
                hint_en="URL query parameters after `?` are stored in `req.query`!",
                hint_am="ከ `?` በኋላ ያሉ የመፈለጊያ መረጃዎች በ `req.query` ውስጥ ይቀመጣሉ!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch5",
        order=5,
        title_en="Express Ch 5: Middleware Magic with app.use()",
        title_am="ኤክስፕረስ ምዕራፍ 5፦ መካከለኛ አሰራሮች በ app.use() እና next()",
        description_en="Intercept and enhance requests before they reach your route handlers.",
        description_am="ጥያቄዎች ከመስተናገዳቸው በፊት በ `app.use()` እና `next()` መቆጣጠር።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch5_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🛡️ *The Power of Middleware* ⚙️\n\n"
                    "**Middleware** functions are the backbone of Express. They run in sequence before your routes, "
                    "allowing you to authenticate users, log requests, or attach data to the `req` object:\n\n"
                    "```javascript\napp.use((req, res, next) => {\n  req.role = 'Admin';\n  next(); // Pass control to the next handler\n});\n```\n\n"
                    "Whenever you call `next()`, Express forwards the request down the pipeline to the next middleware or route!"
                ),
                message_am=(
                    "🛡️ *የመካከለኛ አሰራሮች (Middleware) ሃይል* ⚙️\n\n"
                    "**ሚድልዌር (Middleware)** የኤክስፕረስ ዋነኛ አከርካሪ ነው። ጥያቄዎች ወደ መስመሮች ከመድረሳቸው በፊት "
                    "ተጠቃሚዎችን ለማረጋገጥ፣ መረጃዎችን ለመመዝገብ ወይም በ `req` ላይ አዳዲስ መረጃዎችን ለመጨመር ያገለግላል፦\n\n"
                    "```javascript\napp.use((req, res, next) => {\n  req.role = 'Admin';\n  next(); // ወደ ቀጣዩ እንዲያልፍ ያዛል\n});\n```\n\n"
                    "`next()` ሲጠራ ኤክስፕረስ ጥያቄውን ወደ ቀጣዩ ሚድልዌር ወይም ራውተር ያስተላልፋል!"
                ),
            ),
            TutorStep(
                id="express_ch5_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Attach `req.role = 'Admin'` in a middleware with `app.use()`, then return `Welcome ${req.role}!` in `/api/user`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use((req, res, next) => {\n  req.role = 'Admin';\n  next();\n});\n\napp.get('/api/user', (req, res) => {\n  res.send(`Welcome ${req.role}!`);\n});\n```"
                ),
                message_am=(
                    "በ `app.use()` ውስጥ `req.role = 'Admin'` አዘጋጅተው በ `/api/user` ላይ `Welcome ${req.role}!` የሚመልስ ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use((req, res, next) => {\n  req.role = 'Admin';\n  next();\n});\n\napp.get('/api/user', (req, res) => {\n  res.send(`Welcome ${req.role}!`);\n});\n```"
                ),
                expected_code_output="Welcome Admin!",
                hint_en="Use `app.use((req, res, next) => { req.role = 'Admin'; next(); });`.",
                hint_am="`app.use((req, res, next) => { req.role = 'Admin'; next(); });` ብለው ይጻፉ።",
                success_message_en=(
                    "🎉 *TERRIFIC!* The middleware enriched the request and passed control to the route handler with `next()`!"
                ),
                success_message_am=(
                    "🎉 *እጅግ ድንቅ!* ሚድልዌሩ መረጃውን ጨምሮ በ `next()` አማካኝነት ወደ ራውተሩ በተሳካ ሁኔታ አስተላልፏል!"
                ),
            ),
            TutorStep(
                id="express_ch5_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "What happens if an Express middleware does not call `next()` and does not send a response?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የኤክስፕረስ ሚድልዌር `next()` ካልጠራ እና ምላሽ ካልላከ በሰርቨሩ ላይ ምን ይከሰታል?"
                ),
                options_en=[
                    "The client request hangs and eventually times out",
                    "The database is deleted",
                    "The browser plays music",
                    "The operating system reboots",
                ],
                options_am=[
                    "ጥያቄው ሳይመለስ ተንጠልጥሎ በመቆየት ጊዜው ያልቃል (Timeout)",
                    "ዳታቤዙ ይሰረዛል",
                    "ብራውዘሩ ሙዚቃ ይከፍታል",
                    "ኦፕሬቲንግ ሲስተሙ ሪስታርት ያደርጋል",
                ],
                correct_option_index=0,
                hint_en="Without `next()` or `res.send()`, requests remain pending indefinitely!",
                hint_am="`next()` ወይም `res.send()` ካልተጠራ ጥያቄው ሳይመለስ ተንጠልጥሎ ይቀራል!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch6",
        order=6,
        title_en="Express Ch 6: Receiving POST Data with req.body",
        title_am="ኤክስፕረስ ምዕራፍ 6፦ አዳዲስ መረጃዎችን በ POST እና req.body መቀበል",
        description_en="Parse incoming JSON request bodies and create new resources.",
        description_am="የሚላኩ አዳዲስ የ JSON መረጃዎችን በ `express.json()` ማንበብ።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch6_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "📬 *Handling POST Requests & `express.json()`* 📥\n\n"
                    "While GET requests retrieve information, **POST requests** submit new data—such as user registrations or creating posts.\n\n"
                    "By default, Node.js delivers POST bodies as raw data streams. Express provides the `express.json()` middleware to parse JSON bodies automatically:\n\n"
                    "```javascript\napp.use(express.json()); // Essential body parser!\n\napp.post('/items', (req, res) => {\n  res.json({ created: req.body.title });\n});\n```\n\n"
                    "Now `req.body` contains the parsed JSON object sent by the client!"
                ),
                message_am=(
                    "📬 *የ POST ጥያቄዎችን በ `express.json()` ማስተናገድ* 📥\n\n"
                    "የ GET ጥያቄዎች መረጃዎችን ሲያመጡ፣ **የ POST ጥያቄዎች** ደግሞ አዳዲስ መረጃዎችን ለመፍጠር (ለምሳሌ መመዝገብ) ያገለግላሉ።\n\n"
                    "በተፈጥሮ ኖድ መረጃውን እንደ ጥሬ ፍሰት ነው የሚያመጣው። ኤክስፕረስ በቀላሉ በ `express.json()` መረጃውን ወደ ኦብጀክት ይለውጠዋል፦\n\n"
                    "```javascript\napp.use(express.json()); // የ JSON መፍቻ ሚድልዌር!\n\napp.post('/items', (req, res) => {\n  res.json({ created: req.body.title });\n});\n```\n\n"
                    "አሁን በ `req.body` ውስጥ የተጠቃሚውን መረጃ በቀላሉ ማግኘት ይቻላል!"
                ),
            ),
            TutorStep(
                id="express_ch6_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Set up `app.use(express.json())` and a `POST /items` route returning `{ created: req.body.title }`!\n\n"
                    "👇 *Type and send this code:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use(express.json());\n\napp.post('/items', (req, res) => {\n  res.json({ created: req.body.title });\n});\n```"
                ),
                message_am=(
                    "`app.use(express.json())` በመጠቀም በ `POST /items` ላይ `{ created: req.body.title }` የሚመልስ ኮድ ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use(express.json());\n\napp.post('/items', (req, res) => {\n  res.json({ created: req.body.title });\n});\n```"
                ),
                expected_code_output='{"created":"Express Mastery"}',
                hint_en="Add `app.use(express.json())` before your `app.post('/items', ...)` route.",
                hint_am="ከ `app.post('/items', ...)` በፊት `app.use(express.json())` ማካተትዎን ያረጋግጡ።",
                success_message_en=(
                    "🌟 *MAGNIFICENT!* You successfully parsed a JSON payload via POST and returned the created resource!"
                ),
                success_message_am=(
                    "🌟 *ድንቅ ስራ!* የ POST መረጃን በ `express.json()` አንብበው የተፈጠረውን እቃ በስኬት መልሰዋል!"
                ),
            ),
            TutorStep(
                id="express_ch6_s3",
                step_type=StepType.CONCEPT_CHECK,
                message_en=(
                    "🧠 *Brain Check:*\n\n"
                    "Which middleware in Express parses incoming JSON request bodies into `req.body`?"
                ),
                message_am=(
                    "🧠 *የእውቀት መፈተሻ ጥያቄ፦*\n\n"
                    "የሚላኩ የ JSON መረጃዎችን አንብቦ በ `req.body` ውስጥ የሚያዘጋጀው የኤክስፕረስ ሚድልዌር የትኛው ነው?"
                ),
                options_en=[
                    "express.json()",
                    "express.xml()",
                    "express.html()",
                    "express.style()",
                ],
                options_am=[
                    "express.json()",
                    "express.xml()",
                    "express.html()",
                    "express.style()",
                ],
                correct_option_index=0,
                hint_en="`express.json()` is the built-in JSON body parser in Express!",
                hint_am="`express.json()` በኤክስፕረስ ውስጥ አብሮ የተሰራ የ JSON ማንበቢያ ነው!",
            ),
        ],
    ),
    TutorChapter(
        id="express_ch7",
        order=7,
        title_en="Express Ch 7: Developer Profile Microservice Capstone",
        title_am="ኤክስፕረስ ምዕራፍ 7፦ የተሟላ የፕሮፋይል ማይክሮሰርቪስ ፕሮጀክት",
        description_en="Build a production REST microservice returning structured developer profile metadata.",
        description_am="የተሟላ የጀርባ ሰርቨር እና የፕሮፋይል REST API ማይክሮሰርቪስ መገንባት።",
        track="express",
        steps=[
            TutorStep(
                id="express_ch7_s1",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🏗️ *The Grand Capstone: Developer Profile Microservice!* 🌟\n\n"
                    "Let's combine everything you've mastered into a production-grade backend microservice:\n"
                    "1. Express server initialization\n"
                    "2. `express.json()` middleware\n"
                    "3. REST API endpoint `/api/profile`\n"
                    "4. Returning structured JSON metadata: `developer`, `stack`, and `role`!"
                ),
                message_am=(
                    "🏗️ *የመጨረሻው ታላቅ ፕሮጀክት፦ የተሟላ የፕሮፋይል ማይክሮሰርቪስ ሰርቨር!* 🌟\n\n"
                    "እስካሁን የተማርነውን በሙሉ በማጣመር እውነተኛ የጀርባ ሰርቨር (Microservice) እንገነባለን፦\n"
                    "1. የኤክስፕረስ ሰርቨር ዝግጅት\n"
                    "2. የ `express.json()` ሚድልዌር\n"
                    "3. የ REST API መስመር `/api/profile`\n"
                    "4. የተዋቀረ የ JSON መረጃ መላክ፦ `developer`፣ `stack`፣ እና `role`!"
                ),
            ),
            TutorStep(
                id="express_ch7_s2",
                step_type=StepType.CODE_PROMPT,
                message_en=(
                    "Write an Express app serving `/api/profile` returning `{ developer: 'Liya', stack: 'Node + Express', role: 'Backend Engineer' }`!\n\n"
                    "👇 *Type and send:*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use(express.json());\n\napp.get('/api/profile', (req, res) => {\n  res.json({\n    developer: 'Liya',\n    stack: 'Node + Express',\n    role: 'Backend Engineer'\n  });\n});\n```"
                ),
                message_am=(
                    "`/api/profile` ላይ የገንቢውን ፕሮፋይል JSON የሚመልስ የተሟላ ሰርቨር ጽፈው ይላኩ!\n\n"
                    "👇 *ይህንን ኮድ ጽፈው ይላኩ፦*\n"
                    "```javascript\nconst express = require('express');\nconst app = express();\n\napp.use(express.json());\n\napp.get('/api/profile', (req, res) => {\n  res.json({\n    developer: 'Liya',\n    stack: 'Node + Express',\n    role: 'Backend Engineer'\n  });\n});\n```"
                ),
                expected_code_output='{"developer":"Liya","stack":"Node + Express","role":"Backend Engineer"}',
                hint_en="Return the JSON object inside `app.get('/api/profile', (req, res) => res.json(...))`.",
                hint_am="በ `/api/profile` ውስጥ የ JSON መረጃውን በ `res.json(...)` መልሰው ይላኩ።",
                success_message_en=(
                    "🏆 *EXPRESS.JS MASTER!* You have officially built and deployed a production REST microservice with Express and Node.js!"
                ),
                success_message_am=(
                    "🏆 *የኤክስፕረስ (Express.js) ባለሙያ!* እውነተኛ ዘመናዊ የ REST API ማይክሮሰርቪስ ሰርቨር በስኬት ገንብተዋል!"
                ),
            ),
            TutorStep(
                id="express_ch7_s3",
                step_type=StepType.EXPLANATION,
                message_en=(
                    "🎓🌟 **CONGRATULATIONS! EXPRESS.JS GRADUATE!** 🌟🎓\n\n"
                    "You have mastered Node.js backend engineering with Express:\n"
                    "1. 🚂 HTTP Web Server initialization\n"
                    "2. 📦 REST APIs with structured `res.json()`\n"
                    "3. 🎯 Dynamic route parameters with `req.params`\n"
                    "4. 🔍 URL query string extraction with `req.query`\n"
                    "5. 🛡️ Middleware request pipelines with `app.use()` and `next()`\n"
                    "6. 📬 JSON body payload parsing for POST requests\n"
                    "7. 🏗️ Full microservice API architecture!\n\n"
                    "You can now build full-stack web and mobile backends from scratch! 🚀🔥"
                ),
                message_am=(
                    "🎓🌟 **እንኳን ደስ አለዎት! የኤክስፕረስ (Express.js) ተመራቂ ሆነዋል!** 🌟🎓\n\n"
                    "የኖድ (Node.js) የጀርባ ሰርቨር ግንባታን በሚገባ ተምረዋል፦\n"
                    "1. 🚂 የ HTTP ድህረ-ገጽ ሰርቨር መገንባት\n"
                    "2. 📦 የ REST API መረጃዎችን በ `res.json()` ማዘጋጀት\n"
                    "3. 🎯 ተለዋዋጭ የመስመር መለያዎች በ `req.params`\n"
                    "4. 🔍 የመፈለጊያ ቃላት በ `req.query`\n"
                    "5. 🛡️ የመካከለኛ አሰራሮች (Middleware) በ `app.use()` እና `next()`\n"
                    "6. 📬 የ POST አዳዲስ መረጃዎችን በ `express.json()` መቀበል\n"
                    "7. 🏗️ የተሟላ የማይክሮሰርቪስ ሰርቨር አሰራር!\n\n"
                    "አሁን የተሟሉ የድህረ-ገጽ እና የሞባይል ጀርባ ሰርቨሮችን ከዜሮ መገንባት ይችላሉ! 🚀🔥"
                ),
            ),
        ],
    ),
]


def get_all_express_chapters() -> List[TutorChapter]:
    """Return all Express tutor chapters ordered."""
    return sorted(EXPRESS_TUTOR_CHAPTERS, key=lambda c: c.order)


def get_express_tutor_chapter(chapter_id: str) -> Optional[TutorChapter]:
    """Retrieve Express tutor chapter by ID."""
    for ch in EXPRESS_TUTOR_CHAPTERS:
        if ch.id == chapter_id:
            return ch
    return None


def get_next_express_tutor_chapter_id(current_id: str) -> Optional[str]:
    """Return next Express chapter ID."""
    chapters = get_all_express_chapters()
    for idx, ch in enumerate(chapters):
        if ch.id == current_id:
            if idx + 1 < len(chapters):
                return chapters[idx + 1].id
            return None
    return None
