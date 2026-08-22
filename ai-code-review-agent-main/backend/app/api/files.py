"""
File upload endpoints. POST validates and stores files under a new
upload_id directory; GET lists what's stored so the frontend can show
the user what's available to select for review. POST /from-url stages
files the same way but sources them by cloning a public GitHub/Bitbucket
repo instead of accepting a direct upload.
"""
from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.services.file_service import FileValidationError, list_uploaded_files, save_uploaded_files
from app.services.repo_service import RepoFetchError, fetch_repo_files

router = APIRouter(prefix="/api/files", tags=["files"])


class RepoUrlRequest(BaseModel):
    repo_url: str
    branch: str | None = None


@router.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    try:
        return await save_uploaded_files(files)
    except FileValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/from-url")
def fetch_files_from_url(request: RepoUrlRequest):
    try:
        return fetch_repo_files(request.repo_url, request.branch)
    except RepoFetchError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{upload_id}")
def get_uploaded_files(upload_id: str):
    try:
        return {"upload_id": upload_id, "files": list_uploaded_files(upload_id)}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
