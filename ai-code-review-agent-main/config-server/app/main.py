"""
Config Server — a standalone FastAPI app that is the single source of truth
for LLM / RAG / MCP settings. The backend calls GET /config/application on
every review request instead of hardcoding these values itself.

Why a separate service instead of just a shared .env?
Because in a real system, config (model name, temperature, feature flags)
changes independently of code deploys, and often needs to be shared by
multiple backend instances. A tiny FastAPI service demonstrates that
pattern without needing a real config-management product.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.schemas import ApplicationConfig, LLMConfig, RAGConfig, MCPConfig

app = FastAPI(title="AI Code Review Agent - Config Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/config/application", response_model=ApplicationConfig)
def get_application_config():
    """
    Returns the active, non-secret configuration for the whole application.
    The real OPENAI_API_KEY never leaves this service in this response —
    each downstream service reads the actual secret from its own .env.
    See README "Configuration & Secrets" section for why.
    """
    return ApplicationConfig(
        llm=LLMConfig(
            provider=settings.llm_provider,
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            max_tokens=settings.llm_max_tokens,
            api_key_configured=bool(settings.openai_api_key and settings.openai_api_key != "sk-your-key-here"),
        ),
        rag=RAGConfig(
            embedding_provider=settings.embedding_provider,
            embedding_model=settings.embedding_model,
            chroma_db_path=settings.chroma_db_path,
            chroma_collection_name=settings.chroma_collection_name,
        ),
        mcp=MCPConfig(server_url=settings.mcp_server_url),
    )
