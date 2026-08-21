"""
Review endpoints. POST kicks off the LangGraph workflow for a set of
already-uploaded files; GET re-fetches a past result by review_id.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.review import ReviewResponse
from app.services.review_service import get_review, run_review

router = APIRouter(prefix="/api/review", tags=["review"])


class ReviewRequest(BaseModel):
    upload_id: str
    file_names: list[str]
    review_focus: str = "general"


@router.post("", response_model=ReviewResponse)
async def create_review(request: ReviewRequest):
    try:
        return await run_review(request.upload_id, request.file_names, request.review_focus)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{review_id}", response_model=ReviewResponse)
def fetch_review(review_id: str):
    try:
        return get_review(review_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
