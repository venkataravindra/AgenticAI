from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from main import ask_rag

from fastapi.middleware.cors import CORSMiddleware
# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Corrective RAG API",
    description="FastAPI application for PDF + Website Corrective RAG",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# REQUEST MODEL
# ============================================================

class QuestionRequest(BaseModel):

    question: str


# ============================================================
# RESPONSE MODEL
# ============================================================

class QuestionResponse(BaseModel):

    question: str

    answer: str

    correction_count: int


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
def root():

    return {
        "message": "Corrective RAG API is running"
    }


@app.get("/health")
def health():

    return {
        "status": "UP"
    }


# ============================================================
# ASK RAG
# ============================================================

@app.post(
    "/ask",
    response_model=QuestionResponse
)
def ask_question(request: QuestionRequest):

    try:

        # Validate question
        if not request.question.strip():

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )

        # Call Corrective RAG
        result = ask_rag(
            request.question
        )

        return QuestionResponse(

            question=request.question,

            answer=result["final_answer"],

            correction_count=result["correction_count"]

        )

    except HTTPException:

        raise

    except Exception as e:

        print("RAG ERROR:", str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )