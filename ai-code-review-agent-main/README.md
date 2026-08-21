# AI Code Review Agent

A student-friendly, end-to-end **single-agent** code review application built with
FastAPI, LangChain, LangGraph, ChromaDB (RAG), MCP, and a React (Vite) frontend.

Upload source files, pick a review focus, and get a structured AI code review —
backed by retrieved best-practices knowledge (RAG) and deterministic file
analysis (MCP tools), all orchestrated by one LangGraph workflow around one
LLM agent.

---

## 1. Architecture

```
                         React Frontend (Vite, :5173)
                                    |
                                    | HTTP (fetch)
                                    v
                    FastAPI Code Review Backend (:8000)
                                    |
              +---------------------+----------------------+
              |                     |                       |
              v                     v                       v
      Config Client         LangGraph Workflow         Local File Storage
              |                     |                     (backend/uploads)
              v                     |
      Config Server (:8001)        |
      (LLM / RAG / MCP settings)   |
                                    |
                       +------------+------------+
                       |                         |
                       v                         v
                 RAG (ChromaDB)            MCP Client -> MCP Server (:8002)
                       |                         |
                       v                         v
                 OpenAI Embeddings         code_metadata / code_analysis tools
                       |
                       v
                 OpenAI Chat Model (gpt-4o-mini)
```

Four independent services, each with its own venv/deps:

| Service | Folder | Port | Purpose |
|---|---|---|---|
| Config Server | `config-server/` | 8001 | Single source of truth for LLM/RAG/MCP settings |
| MCP Server | `mcp-server/` | 8002 | Exposes `code_metadata` + `code_analysis` tools |
| Backend | `backend/` | 8000 | FastAPI + LangGraph + RAG + MCP client + LLM |
| Frontend | `frontend/` | 5173 | React + Vite UI |

---

## 2. Technologies

- **FastAPI + Uvicorn** — all three backend-side services
- **LangChain** — LLM client, prompt templates, document loading/splitting, embeddings, Chroma vector store
- **LangGraph** — orchestrates the 5-step single-agent workflow
- **ChromaDB** — local vector store for the RAG knowledge base
- **MCP (Model Context Protocol)** — `mcp[cli]==1.29.0`, streamable-HTTP transport
- **OpenAI** — `gpt-4o-mini` (chat) + `text-embedding-3-small` (embeddings)
- **React + Vite** — frontend, no UI framework, plain CSS

---

## 3. Prerequisites

- Python 3.12+ (tested with 3.12.7)
- Node.js 20+ / npm 11+ (tested with 20.20.2 / 11.18.0)
- An OpenAI API key with access to `gpt-4o-mini` and `text-embedding-3-small`

---

## 4. Installation

Already done if you're reading this after the initial build, but for a fresh
clone:

```bash
# Config Server
cd config-server
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cp .env.example .env   # then edit .env

# MCP Server
cd ../mcp-server
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cp .env.example .env

# Backend
cd ../backend
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
cp .env.example .env   # then edit .env

# Frontend
cd ../frontend
npm install
```

---

## 5. Environment variables

### `config-server/.env`
```
OPENAI_API_KEY=sk-your-key-here     # used only to report api_key_configured, never returned over HTTP
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
LLM_TEMPERATURE=0.2
LLM_MAX_TOKENS=2000
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small
CHROMA_DB_PATH=../backend/chroma_db
CHROMA_COLLECTION_NAME=coding_knowledge
MCP_SERVER_URL=http://localhost:8002
CONFIG_SERVER_PORT=8001
```

### `backend/.env`
```
OPENAI_API_KEY=sk-your-key-here     # the REAL secret the backend actually uses
CONFIG_SERVER_URL=http://localhost:8001
MCP_SERVER_URL=http://localhost:8002
MAX_UPLOAD_SIZE_MB=2
UPLOAD_DIR=uploads
```

### `mcp-server/.env`
```
MCP_SERVER_PORT=8002
```

**Why does `OPENAI_API_KEY` appear in two places?** The Config Server centralizes
*non-secret* settings (model name, temperature, embedding model, URLs) — but it
never echoes the real API key back over HTTP (see `config-server/app/main.py`,
`api_key_configured` is a boolean, not the key). The backend reads its own copy
of the key locally to actually call OpenAI. In production, both services would
instead pull the same secret from a real Secret Manager (AWS Secrets Manager,
Vault, etc.) rather than each having their own `.env` — that's a deployment
concern, intentionally out of scope here.

---

## 6. Running everything (4 terminals)

```bash
# Terminal 1 — Config Server
cd config-server && ./.venv/bin/uvicorn app.main:app --reload --port 8001

# Terminal 2 — MCP Server
cd mcp-server && ./.venv/bin/python server.py

# Terminal 3 — Backend (run RAG ingestion once first)
cd backend && ./.venv/bin/python -m app.rag.ingest
cd backend && ./.venv/bin/uvicorn app.main:app --reload --port 8000

# Terminal 4 — Frontend
cd frontend && npm run dev
```

Then open **http://localhost:5173**.

Start order matters a little: Config Server and MCP Server should be up
*before* you hit the backend's `/api/review` endpoint, since that's when the
backend calls out to both.

---

## 7. API endpoints (backend, :8000)

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/files/upload` | Upload one or more code files (multipart `files[]`) |
| GET | `/api/files/{upload_id}` | List files stored under an upload |
| POST | `/api/review` | Run the LangGraph review workflow on selected files |
| GET | `/api/review/{review_id}` | Re-fetch a past review result |
| GET | `/health` | Liveness check |

Config Server (:8001): `GET /config/application`, `GET /health`.

---

## 8. Real-time request flow (what happens on "Review My Code")

1. User selects files and a review focus in React.
2. React `POST`s the files to `/api/files/upload` → backend validates
   extension/size/non-empty, stores them under `backend/uploads/{upload_id}/`.
3. React `POST`s `/api/review` with `upload_id`, `file_names`, `review_focus`.
4. Backend (`app/services/review_service.py`) calls the Config Server:
   `GET /config/application`.
5. Backend builds the initial LangGraph state and runs the graph
   (`app/agent/graph.py`):
   - `validate_code` — checks file types are supported.
   - `retrieve_context` — queries ChromaDB (`app/rag/retriever.py`) for
     relevant best-practices chunks.
   - `run_mcp_tools` — MCP Client (`app/mcp/client.py`) calls `code_metadata`
     and `code_analysis` on the MCP Server for each file.
   - `review_code` — the single Code Review Agent: builds a prompt from the
     code + RAG context + MCP results + review focus, calls the OpenAI chat
     model via LangChain (`app/agent/reviewer.py`) with structured output.
   - `format_response` — attaches `rag_context_used` / `mcp_tools_used` flags.
6. Backend wraps the result in a `ReviewResponse` (adds `review_id`), stores
   it in memory, and returns JSON.
7. React renders score, summary, issues, improvements, and RAG/MCP usage.

---

## 9. Project structure

```
Code-Review-Agent/
├── config-server/        # FastAPI, GET /config/application
├── mcp-server/            # FastMCP server: code_metadata, code_analysis
├── backend/
│   └── app/
│       ├── api/           # files.py, review.py (route handlers)
│       ├── agent/         # state.py, graph.py, reviewer.py (LangGraph + LLM)
│       ├── rag/           # documents/, ingest.py, vector_store.py, retriever.py
│       ├── mcp/           # client.py (MCP client)
│       ├── config/        # client.py (Config Server client)
│       ├── services/      # file_service.py, review_service.py
│       └── models/        # review.py (Pydantic schemas)
└── frontend/
    └── src/
        ├── components/    # FileUpload, ReviewOptions, ReviewResult
        └── services/      # api.js
```

---

## 10. Troubleshooting

- **`RuntimeError: OPENAI_API_KEY is not set`** — edit `backend/.env`
  (and `config-server/.env`) with a real key.
- **Review request hangs/fails with a connection error** — make sure the
  Config Server (8001) and MCP Server (8002) are both running before hitting
  `/api/review`.
- **RAG context is always empty** — you need to run
  `python -m app.rag.ingest` from `backend/` at least once (with a real API
  key set, since ingestion calls the OpenAI embeddings API).
- **CORS errors in the browser console** — confirm the frontend is running on
  port 5173 (backend only allows that origin); change
  `backend/app/main.py`'s `allow_origins` if you use a different port.
- **Port already in use** — another process is bound to 8000/8001/8002/5173;
  stop it or change the port in the relevant `.env` / `uvicorn --port`.

---

## 11. Explicitly out of scope (by design)

Authentication, user accounts, databases, Docker, CI/CD, cloud deployment,
multi-agent orchestration, advanced/agentic RAG, and reranking are all
intentionally excluded — this project is scoped to teach the core
integration of a single agent + LangGraph + LangChain + RAG + MCP + a
Config Server, end to end, without extra moving parts.
