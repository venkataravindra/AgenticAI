"""
Orchestrates one review request: fetches active config from the Config
Server, loads the selected uploaded files from disk, runs the LangGraph
workflow, and keeps the structured result in memory so it can be fetched
again by review_id. In-memory only — a real deployment would use a
database table instead; that's an intentional simplification here.
"""
import uuid
from pathlib import Path

from app.agent.graph import build_review_graph
from app.config.client import get_application_config
from app.models.review import ReviewResponse
from app.services.file_service import UPLOAD_DIR

_review_store: dict[str, ReviewResponse] = {}
_review_graph = build_review_graph()


async def run_review(upload_id: str, file_names: list[str], review_focus: str) -> ReviewResponse:
    upload_path = UPLOAD_DIR / upload_id
    files = []
    for name in file_names:
        file_path = upload_path / name
        if not file_path.exists():
            raise FileNotFoundError(f"File '{name}' not found in upload '{upload_id}'.")
        files.append({
            "file_name": name,
            "file_extension": Path(name).suffix,
            "content": file_path.read_text(encoding="utf-8", errors="replace"),
        })

    config = get_application_config()

    initial_state = {
        "files": files,
        "review_focus": review_focus,
        "llm_config": config["llm"],
        "mcp_server_url": config["mcp"]["server_url"],
    }

    final_state = await _review_graph.ainvoke(initial_state)

    review_id = str(uuid.uuid4())
    review = ReviewResponse(review_id=review_id, **final_state["review_result"])
    _review_store[review_id] = review
    return review


def get_review(review_id: str) -> ReviewResponse:
    if review_id not in _review_store:
        raise KeyError(f"Review '{review_id}' not found.")
    return _review_store[review_id]
