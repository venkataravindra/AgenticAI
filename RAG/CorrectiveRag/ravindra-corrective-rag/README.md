# Ravindra Corrective Rag — Frontend

A React (Vite) UI for your Corrective RAG FastAPI backend (`/health`, `/ask`).

## What's inside

```
ravindra-corrective-rag/
├── index.html
├── package.json
├── vite.config.js
├── .env.example
└── src/
    ├── main.jsx
    ├── App.jsx      # UI + API calls
    ├── App.css
    └── index.css    # design tokens (colors, fonts)
```

The UI shows:
- A live API health indicator (polls `GET /health` every 15s)
- A "correction pipeline" visual (Retrieve → Grade → Correct → Answer) that animates while a question is in flight, and flags the **Correct** stage in amber with the `correction_count` returned by `/ask`
- A running conversation panel with each question, its answer, and whether a correction was applied

## 1. Backend: enable CORS

Your FastAPI app doesn't currently allow cross-origin requests, which the browser will block once the frontend (port 5173) calls it (port 8000). Add this to your FastAPI file, right after `app = FastAPI(...)`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then run your backend as usual, e.g.:

```bash
uvicorn app:app --reload --port 8000
```

(adjust `app:app` to match your actual filename/module — the one containing `app = FastAPI(...)`).

## 2. Frontend: install and run

Requires Node.js 18+.

```bash
cd ravindra-corrective-rag
npm install
```

Copy the env file and point it at your backend (defaults to `http://localhost:8000` if you skip this):

```bash
cp .env.example .env
```

Start the dev server:

```bash
npm run dev
```

Open **http://localhost:5173** — you should see "Ravindra Corrective Rag" with a green "api online" indicator if the backend is reachable.

## 3. Build for production (optional)

```bash
npm run build
npm run preview   # serves the production build locally to sanity-check it
```

The static output lands in `dist/`. Serve that folder from any static host (Nginx, S3, Vercel, etc.), and point `VITE_API_URL` (set at build time) at your deployed FastAPI URL.

## Troubleshooting

- **"api offline" badge / network error on ask** — check the backend is running on the URL in `.env`, and that CORS is enabled as shown above.
- **CORS error in browser console** — the `allow_origins` list in your FastAPI CORS middleware must include the exact origin the frontend is served from (e.g. add your deployed frontend's URL later, not just `localhost:5173`).
- **Port already in use** — change `server.port` in `vite.config.js`, or run `npm run dev -- --port 5174`.
