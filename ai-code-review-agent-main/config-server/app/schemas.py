"""
Pydantic response models for the Config Server.

Grouped into llm / rag / mcp because that's exactly how the backend
consumes them (three separate clients each need their own slice).
Note: NO api keys appear here. Only non-secret operational settings.
"""
from pydantic import BaseModel


class LLMConfig(BaseModel):
    provider: str
    model: str
    temperature: float
    max_tokens: int
    api_key_configured: bool  # tells the backend "yes a key is set", never the key itself


class RAGConfig(BaseModel):
    embedding_provider: str
    embedding_model: str
    chroma_db_path: str
    chroma_collection_name: str


class MCPConfig(BaseModel):
    server_url: str


class ApplicationConfig(BaseModel):
    llm: LLMConfig
    rag: RAGConfig
    mcp: MCPConfig
