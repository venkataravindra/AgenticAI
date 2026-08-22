"""
Fetches a public GitHub/Bitbucket repository via `git clone` and stages its
reviewable source files under uploads/{upload_id}/, mirroring exactly what
save_uploaded_files() produces for direct uploads. That means a repo URL
flows through the same review_service/run_review path an upload does --
no changes needed downstream of fetch_repo_files().
"""
import os
import shutil
import stat
import subprocess
import tempfile
import uuid
from pathlib import Path
from urllib.parse import urlparse

from app.services.file_service import ALLOWED_EXTENSIONS, MAX_UPLOAD_SIZE_BYTES, UPLOAD_DIR

# Restricting to these hosts (rather than allowing any http(s) URL) closes off
# SSRF-via-clone against arbitrary internal/external hosts.
ALLOWED_HOSTS = {"github.com", "www.github.com", "bitbucket.org", "www.bitbucket.org"}

IGNORED_DIRS = {
    ".git", "node_modules", "vendor", "venv", ".venv", "__pycache__",
    "dist", "build", ".next", "target", ".idea", ".vscode",
}

MAX_REPO_FILES = int(os.getenv("REPO_MAX_FILES", "30"))
CLONE_TIMEOUT_SECONDS = int(os.getenv("REPO_CLONE_TIMEOUT_SECONDS", "30"))


class RepoFetchError(Exception):
    pass


def _validate_repo_url(repo_url: str) -> str:
    parsed = urlparse(repo_url.strip())
    if parsed.scheme not in ("http", "https"):
        raise RepoFetchError("Only http:// or https:// repository URLs are supported.")
    if parsed.username or parsed.password:
        raise RepoFetchError("Repository URLs with embedded credentials are not supported.")
    if parsed.hostname not in ALLOWED_HOSTS:
        raise RepoFetchError(
            f"Unsupported host '{parsed.hostname}'. Only GitHub and Bitbucket URLs are supported."
        )
    return parsed.geturl()


def _force_remove_readonly(func, path, _exc_info):
    """git leaves some objects read-only; shutil.rmtree needs this to clean them up on Windows."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def _clone(repo_url: str, branch: str | None, dest: Path) -> None:
    command = ["git", "clone", "--depth", "1", "--single-branch"]
    if branch:
        command += ["--branch", branch]
    command += [repo_url, str(dest)]

    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=CLONE_TIMEOUT_SECONDS,
            env=env,
        )
    except FileNotFoundError as e:
        raise RepoFetchError("git is not installed on the server.") from e
    except subprocess.TimeoutExpired as e:
        raise RepoFetchError("Cloning the repository timed out.") from e

    if result.returncode != 0:
        stderr = result.stderr.strip()
        stderr_tail = stderr.splitlines()[-1] if stderr else "unknown error"
        raise RepoFetchError(f"Could not clone repository: {stderr_tail}")


def fetch_repo_files(repo_url: str, branch: str | None = None) -> dict:
    """Clone repo_url, copy its reviewable source files into a new upload_id
    directory, and return the same {upload_id, files} shape save_uploaded_files() does."""
    validated_url = _validate_repo_url(repo_url)

    tmp_dir = tempfile.mkdtemp(prefix="repo_clone_")
    try:
        clone_path = Path(tmp_dir) / "repo"
        _clone(validated_url, branch, clone_path)

        candidates = sorted(
            p for p in clone_path.rglob("*")
            if p.is_file()
            and p.suffix in ALLOWED_EXTENSIONS
            and not IGNORED_DIRS.intersection(p.relative_to(clone_path).parts)
            and 0 < p.stat().st_size <= MAX_UPLOAD_SIZE_BYTES
        )

        if not candidates:
            raise RepoFetchError("No reviewable source files found in this repository.")

        truncated = len(candidates) > MAX_REPO_FILES
        candidates = candidates[:MAX_REPO_FILES]

        upload_id = str(uuid.uuid4())
        upload_path = UPLOAD_DIR / upload_id
        upload_path.mkdir(parents=True, exist_ok=True)

        saved_files = []
        for file_path in candidates:
            relative_name = file_path.relative_to(clone_path).as_posix()
            destination = upload_path / relative_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file_path, destination)
            saved_files.append(relative_name)

        return {"upload_id": upload_id, "files": saved_files, "truncated": truncated}
    finally:
        shutil.rmtree(tmp_dir, onerror=_force_remove_readonly)