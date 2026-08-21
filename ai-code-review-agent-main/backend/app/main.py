"""
FastAPI entrypoint. Wires together the files and review routers and
enables CORS for the frontend's origin(s).
"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.files import router as files_router
from app.api.review import router as review_router

app = FastAPI(title="AI Code Review Agent - Backend")

# Comma-separated list, e.g. "http://localhost:5173,http://<ec2-public-ip>"
allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files_router)
app.include_router(review_router)


@app.get("/health")
def health():
    return {"status": "ok"}
