"""
Simple retriever used by the LangGraph `retrieve_context` node.
No query rewriting, no reranking — just a similarity search against
ChromaDB, joined into one context string for the prompt.
"""
from app.rag.vector_store import get_vector_store

DEFAULT_K = 3


def retrieve_context(query: str, k: int = DEFAULT_K) -> str:
    """Return the top-k most relevant knowledge chunks, joined into one string."""
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query, k=k)
    if not results:
        return ""
    return "\n\n---\n\n".join(doc.page_content for doc in results)
