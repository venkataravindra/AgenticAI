import os

from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel      # q : str   age : int       avilability : bool

from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.tools import create_retriever_tool
from langchain.agents import create_agent


# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

if not os.getenv("ANTHROPIC_API_KEY"):
    raise ValueError("ANTHROPIC_API_KEY is missing")


# --------------------------------------------------
# 2. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Agentic RAG API",
    description="Simple Agentic RAG application using Claude and ChromaDB",
    version="1.0"
)


# --------------------------------------------------
# 3. Load PDF
# --------------------------------------------------

loader = PyPDFLoader("company.pdf")

documents = loader.load()


# --------------------------------------------------
# 4. Split PDF
# --------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)


# --------------------------------------------------
# 5. Create embeddings
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 6. Create ChromaDB
# --------------------------------------------------

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="company_docs"
)


# --------------------------------------------------
# 7. Create retriever
# --------------------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# --------------------------------------------------
# 8. Create RAG tool
# --------------------------------------------------

search_company = create_retriever_tool(
    retriever,
    "search_company_documents",
    """
    Search the company documents for information about
    courses, training, technologies, workshops and
    company information.
    """
)


# --------------------------------------------------
# 9. Create Claude
# --------------------------------------------------

llm = ChatAnthropic(
    model="claude-sonnet-4-5",
    temperature=0
)


# --------------------------------------------------
# 10. Create Agent
# --------------------------------------------------

agent = create_agent(
    model=llm,
    tools=[search_company],
    system_prompt="""
    You are a company knowledge assistant.

    Use the company document search tool when the
    question requires company information.

    If the question does not require company
    information, answer directly.

    Do not invent company information.
    """
)


# --------------------------------------------------
# 11. Request model
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str


# --------------------------------------------------
# 12. Home API
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Agentic RAG API is running"
    }


# --------------------------------------------------
# 13. Ask Agent
# --------------------------------------------------

@app.post("/ask")
def ask_agent(request: QuestionRequest):

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.question
                }
            ]
        }
    )

    answer = response["messages"][-1].content

    return {
        "question": request.question,
        "answer": answer
    }