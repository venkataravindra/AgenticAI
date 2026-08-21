"""
One-time ingestion script: loads the markdown knowledge documents, splits
them into chunks, embeds them with OpenAI, and stores them in ChromaDB.

Run from the backend/ directory (with its venv active):
    python -m app.rag.ingest

Safe to re-run — Chroma will just add duplicate chunks, so only run it
again after clearing backend/chroma_db/ if you want a clean rebuild.
"""
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.vector_store import get_vector_store

DOCUMENTS_DIR = Path(__file__).parent / "documents"


def ingest_documents() -> None:
    documents = []
    for file_path in sorted(DOCUMENTS_DIR.glob("*.md")):
        documents.extend(TextLoader(str(file_path)).load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    vector_store = get_vector_store()
    vector_store.add_documents(chunks)

    print(f"Ingested {len(documents)} documents -> {len(chunks)} chunks into ChromaDB.")


if __name__ == "__main__":
    ingest_documents()
