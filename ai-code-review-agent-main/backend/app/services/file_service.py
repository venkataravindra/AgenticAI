"""
Saves uploaded files to disk under uploads/{upload_id}/ and reads them
back. No database — the upload_id directory on disk IS the record, which
is enough for a student project (see README for the production caveat).
"""
import os
import uuid
from pathlib import Path

from fastapi import UploadFile

ALLOWED_EXTENSIONS = {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".cpp", ".c", ".cs", ".go"}
MAX_UPLOAD_SIZE_BYTES = int(os.getenv("MAX_UPLOAD_SIZE_MB", "2")) * 1024 * 1024
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads"))


class FileValidationError(Exception):
    pass


def _validate_file(filename: str, content: bytes) -> None:
    extension = Path(filename).suffix
    if extension not in ALLOWED_EXTENSIONS:
        raise FileValidationError(f"'{filename}': unsupported file type '{extension}'.")
    if len(content) == 0:
        raise FileValidationError(f"'{filename}': file is empty.")
    if len(content) > MAX_UPLOAD_SIZE_BYTES:
        max_mb = MAX_UPLOAD_SIZE_BYTES // (1024 * 1024)
        raise FileValidationError(f"'{filename}': exceeds max size of {max_mb}MB.")


async def save_uploaded_files(files: list[UploadFile]) -> dict:
    """Validate every file first, then persist all of them together (all-or-nothing)."""
    contents = []
    for file in files:
        content = await file.read()
        _validate_file(file.filename, content)
        contents.append((file.filename, content))

    upload_id = str(uuid.uuid4())
    upload_path = UPLOAD_DIR / upload_id
    upload_path.mkdir(parents=True, exist_ok=True)

    saved_files = []
    for filename, content in contents:
        (upload_path / filename).write_bytes(content)
        saved_files.append(filename)

    return {"upload_id": upload_id, "files": saved_files}


def list_uploaded_files(upload_id: str) -> list[str]:
    upload_path = UPLOAD_DIR / upload_id
    if not upload_path.exists():
        raise FileNotFoundError(f"Upload '{upload_id}' not found.")
    return sorted(p.name for p in upload_path.iterdir() if p.is_file())


def read_uploaded_file(upload_id: str, filename: str) -> str:
    file_path = UPLOAD_DIR / upload_id / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File '{filename}' not found in upload '{upload_id}'.")
    return file_path.read_text(encoding="utf-8", errors="replace")
