# AI Ask Console (React + FastAPI)

A minimal React chat-style UI that talks to your existing FastAPI `/ask` endpoint.

## 1. Backend — run your FastAPI app

Your existing script (unchanged), assumed saved as `main.py`:

```bash
pip install fastapi uvicorn openai python-dotenv
uvicorn main:app --reload --port 8000
```

Confirm it's up: open `http://localhost:8000/` — you should see
`{"message":"welcome to FastAPI"}`.

Your `.env` file needs:
```
OPEN_API_KEY=sk-...
```
(Note: your code reads `OPEN_API_KEY`, not the more common `OPENAI_API_KEY` —
keep the name consistent between `.env` and `os.getenv(...)`.)

CORS is already open (`allow_origins=["*"]`) in your code, so the React dev
server can call it directly with no proxy needed.

## 2. Frontend — install and run

```bash
npm install
npm run dev
```

This starts Vite on `http://localhost:3000` and opens the console in your
browser. Type a question, press Enter (or click Ask), and it calls:

```
GET http://localhost:8000/ask?question=<your question>
```

and renders `response.answer` from the JSON your FastAPI endpoint returns.

## 3. Pointing at a different backend URL

By default the app calls `http://localhost:8000`. To point somewhere else
(e.g. your API running on a different host/port), create a `.env` file next
to `package.json`:

```
VITE_API_BASE_URL=http://localhost:9000
```

Vite only picks up `.env` changes on restart, so stop and re-run `npm run dev`
after adding it.

## 4. Production build

```bash
npm run build     # outputs static files to dist/
npm run preview   # serve the built app locally to sanity-check it
```

Deploy the contents of `dist/` behind any static file server (nginx, S3 +
CloudFront, GitHub Pages, etc). Just make sure `VITE_API_BASE_URL` is set to
wherever your FastAPI service is actually reachable at build time, since Vite
bakes env vars into the build.

## Project structure

```
ai-chat-app/
├── index.html
├── package.json
├── vite.config.js
├── README.md
└── src/
    ├── main.jsx     # React entry point
    ├── App.jsx      # UI + fetch logic for /ask
    └── App.css      # styling
```

## How the request/response mapping works

- Input field → `question` state → sent as a query param to `GET /ask`
- FastAPI: `ask_ai(question: str)` receives it, calls
  `client.responses.create(model="gpt-5", input=question)`, and returns
  `{"answer": response.output_text}`
- React reads `data.answer` and appends it to the on-screen transcript

## Notes / things worth tightening later

- Right now every question is a fresh, stateless call — your FastAPI endpoint
  doesn't carry conversation history, so the model has no memory of earlier
  questions in the session. If you want follow-up questions to have context,
  you'd need to pass prior turns into the `input` on the backend.
- Consider switching `/ask` to a `POST` with a JSON body instead of a query
  param — safer for long questions and avoids URL-encoding/length limits.
- No loading timeout/retry is implemented; a slow or hung OpenAI call will
  just show the typing indicator until it resolves or errors.
