"""
Builds the ChromaDB vector store via LangChain's Chroma wrapper.

Configuration (embedding model, collection name, storage path) comes from
the Config Server so it can be changed in one place; only the OpenAI API
key is read locally, per app/config/client.py's secret-handling rule.
"""
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config.client import get_application_config, get_openai_api_key


def get_vector_store() -> Chroma:
    config = get_application_config()
    rag_config = config["rag"]

    embeddings = OpenAIEmbeddings(
        model=rag_config["embedding_model"],
        api_key=get_openai_api_key(),
    )

    return Chroma(
        collection_name=rag_config["chroma_collection_name"],
        embedding_function=embeddings,
        persist_directory=rag_config["chroma_db_path"],
    )
