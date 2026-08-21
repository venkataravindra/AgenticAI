"""
Loads all runtime configuration from environment variables (.env file).

This is the ONLY place in the whole project that reads raw environment
variables for LLM/RAG/MCP settings. Every other service asks the Config
Server for values instead of reading its own .env — that's the whole point
of having a Config Server.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # LLM
    openai_api_key: str = ""
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o-mini"
    llm_temperature: float = 0.2
    llm_max_tokens: int = 2000

    # RAG / embeddings
    embedding_provider: str = "openai"
    embedding_model: str = "text-embedding-3-small"
    chroma_db_path: str = "../backend/chroma_db"
    chroma_collection_name: str = "coding_knowledge"

    # MCP
    mcp_server_url: str = "http://localhost:8002"

    # Config server
    config_server_port: int = 8001


settings = Settings()
