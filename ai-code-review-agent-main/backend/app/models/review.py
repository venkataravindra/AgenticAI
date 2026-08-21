"""
Pydantic models for the structured code review.

Issue / ReviewResult are what we ask the LLM to produce directly via
with_structured_output(). ReviewResponse adds the fields the LLM has no
way of knowing (review_id, whether RAG/MCP were actually used) — that's
the whole reason it's a separate model instead of one giant schema.
"""
from typing import Literal, Optional

from pydantic import BaseModel, Field


class Issue(BaseModel):
    severity: Literal["low", "medium", "high"]
    category: Literal["bug", "security", "performance", "quality", "best_practice"]
    file: str
    line: Optional[int] = None
    message: str
    suggestion: str


class ReviewResult(BaseModel):
    summary: str
    score: int = Field(ge=0, le=100)
    issues: list[Issue]
    improvements: list[str]


class ReviewResponse(ReviewResult):
    review_id: str
    rag_context_used: bool
    mcp_tools_used: list[str]
