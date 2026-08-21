"""
Config Client — the backend's only door into the Config Server.

Every other backend module (LLM layer, RAG layer, MCP layer) gets its
settings by calling get_application_config() instead of reading .env
directly. That's what makes the Config Server the single source of truth:
change LLM_MODEL in config-server/.env, restart just that service, and
every backend request picks up the new value on its next call.

The one exception is the OpenAI API key: the Config Server's HTTP response
never contains it (see config-server/app/main.py). The backend reads its
OWN copy of OPENAI_API_KEY from its own .env — this mirrors how a real
Secret Manager would hand the same secret to multiple services without
ever putting it on the wire between them.
"""
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

CONFIG_SERVER_URL = os.getenv("CONFIG_SERVER_URL", "http://localhost:8001")


def get_application_config() -> dict:
    """Fetch the active llm/rag/mcp settings from the Config Server."""
    response = httpx.get(f"{CONFIG_SERVER_URL}/config/application", timeout=5.0)
    response.raise_for_status()
    return response.json()


def get_openai_api_key() -> str:
    """Read the real secret locally — never fetched over HTTP from the Config Server."""
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set in backend/.env. Copy backend/.env.example "
            "to backend/.env and fill in a real key."
        )
    return api_key
