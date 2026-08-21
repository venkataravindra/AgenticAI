"""
Shared state that flows through every node of the LangGraph workflow.
Only what the nodes actually need — no extra bookkeeping.
"""
from typing import Optional, TypedDict


class UploadedFile(TypedDict):
    file_name: str
    file_extension: str
    content: str


class CodeReviewState(TypedDict, total=False):
    # provided at graph invocation
    files: list[UploadedFile]
    review_focus: str
    llm_config: dict
    mcp_server_url: str

    # filled in by nodes as the graph runs
    rag_context: str
    mcp_results: dict
    mcp_tools_used: list[str]
    review_result: dict
    error: Optional[str]
