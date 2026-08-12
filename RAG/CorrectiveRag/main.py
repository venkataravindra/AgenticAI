import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import StateGraph, START, END

from typing import TypedDict

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set in .env file")


# ============================================================
# 2. CREATE LLM
# ============================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# ============================================================
# 3. CREATE DOCUMENTS
# ============================================================

# documents = [

#     Document(
#         page_content="""
#         Python is a high-level programming language.
#         Python is easy to learn and supports object-oriented programming.
#         Python is commonly used for web development, data science,
#         machine learning and artificial intelligence.
#         """,
#         metadata={"source": "python.txt"}
#     ),

#     Document(
#         page_content="""
#         FastAPI is a modern Python web framework.
#         FastAPI is commonly used to build REST APIs.
#         It provides automatic API documentation and supports
#         asynchronous programming.
#         """,
#         metadata={"source": "fastapi.txt"}
#     ),

#     Document(
#         page_content="""
#         MongoDB is a NoSQL database.
#         MongoDB stores data in documents using a JSON-like structure.
#         MongoDB is commonly used with modern web applications.
#         """,
#         metadata={"source": "mongodb.txt"}
#     ),

#     Document(
#         page_content="""
#         React is a JavaScript library used for building user interfaces.
#         React applications are created using components.
#         React supports reusable UI components.
#         """,
#         metadata={"source": "react.txt"}
#     )
# ]
# ============================================================
# 3. LOAD PDF DOCUMENT
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_PATH = os.path.join(
    BASE_DIR,
    "data",
    "Resume.pdf"
)

print("\n==============================")
print("PDF PATH")
print("==============================")

print("Looking for PDF at:")
print(PDF_PATH)

if not os.path.isfile(PDF_PATH):
    raise FileNotFoundError(
        f"PDF file not found: {PDF_PATH}\n"
        f"Please make sure Resume.pdf exists inside the data folder."
    )

loader = PyPDFLoader(PDF_PATH)

pdf_documents = loader.load()

print("\n==============================")
print("PDF LOADING")
print("==============================")

print(f"PDF: {PDF_PATH}")
print(f"Pages loaded: {len(pdf_documents)}")

for i, doc in enumerate(pdf_documents, start=1):
    print(f"\nPage {i}")
    print(doc.page_content[:500])

documents = loader.load()

print("\n==============================")
print("PDF LOADING")
print("==============================")

print(f"PDF: {PDF_PATH}")
print(f"Pages loaded: {len(documents)}")

for i, doc in enumerate(documents, start=1):
    print(f"\nPage {i}")
    print(doc.page_content[:500])

# ============================================================
# 4. LOAD WEBSITE
# ============================================================

WEBSITE_URL = "https://fastapi.tiangolo.com/"

web_loader = WebBaseLoader(
    WEBSITE_URL
)

web_documents = web_loader.load()

print("\n==============================")
print("WEBSITE LOADING")
print("==============================")

print(f"Website: {WEBSITE_URL}")
print(f"Web documents loaded: {len(web_documents)}")

for i, doc in enumerate(web_documents, start=1):
    print(f"\nWebsite Document {i}:")
    print(doc.page_content[:500])


# ============================================================
# 4. SPLIT PDF INTO CHUNKS
# ============================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = text_splitter.split_documents(documents)

print("\n==============================")
print("DOCUMENT CHUNKING")
print("==============================")

print(f"Total chunks created: {len(documents)}")

for i, doc in enumerate(documents[:5], start=1):
    print(f"\nChunk {i}")
    print("Source Type:", doc.metadata.get("source_type"))
    print("Source:", doc.metadata.get("source_name"))
    print("Content:")
    print(doc.page_content[:500])

documents = pdf_documents + web_documents

print("\n==============================")
print("ALL DOCUMENTS")
print("==============================")

print(f"PDF documents: {len(pdf_documents)}")
print(f"Website documents: {len(web_documents)}")
print(f"Total documents: {len(documents)}")

# ============================================================
# ADD SOURCE METADATA
# ============================================================

for doc in pdf_documents:
    doc.metadata["source_type"] = "pdf"
    doc.metadata["source_name"] = "Resume.pdf"

for doc in web_documents:
    doc.metadata["source_type"] = "website"
    doc.metadata["source_name"] = WEBSITE_URL

# ============================================================
# 4.1 CREATE VECTOR DATABASE
# ============================================================

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="corrective_rag_demo"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# ============================================================
# 5. DEFINE GRAPH STATE
# ============================================================

class RAGState(TypedDict):

    question: str

    documents: list

    relevance: str

    final_answer: str

    correction_count: int


# ============================================================
# 6. RETRIEVE DOCUMENTS
# ============================================================

# def retrieve_documents(state: RAGState):

#     print("\n==============================")
#     print("STEP 1: RETRIEVING DOCUMENTS")
#     print("==============================")

#     question = state["question"]

#     docs = retriever.invoke(question)

#     print(f"\nQuestion: {question}")

#     print("\nRetrieved Documents:")

#     for i, doc in enumerate(docs, start=1):

#         print(f"\nDocument {i}:")
#         print(doc.page_content.strip())

#     return {
#         "documents": docs
#     }

def retrieve_documents(state: RAGState):

    print("\n==============================")
    print("STEP 1: RETRIEVING DOCUMENTS")
    print("==============================")

    question = state["question"]

    docs = retriever.invoke(question)

    print(f"\nQuestion: {question}")

    print("\nRetrieved Documents:")

    for i, doc in enumerate(docs, start=1):

        print(f"\nDocument {i}:")

        print(
            "Source Type:",
            doc.metadata.get("source_type")
        )

        print(
            "Source:",
            doc.metadata.get("source_name")
        )

        print(
            "Page:",
            doc.metadata.get("page", "N/A")
        )

        print("\nContent:")
        print(doc.page_content.strip())

    return {
        "documents": docs
    }
# ============================================================
# 7. EVALUATE RETRIEVED DOCUMENTS
# ============================================================

def evaluate_documents(state: RAGState):

    print("\n==============================")
    print("STEP 2: EVALUATING DOCUMENTS")
    print("==============================")

    question = state["question"]

    documents = state["documents"]

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = ChatPromptTemplate.from_template(
    """
    You are a document relevance evaluator.

    Determine whether the retrieved context contains information
    that can directly help answer the user's question.

    Question:
    {question}

    Retrieved Documents:
    {context}

    Return exactly one of these values:

    RELEVANT
    NOT_RELEVANT

    Do not return any explanation.
    """
 )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "context": context
        }
    )

    result = response.content.strip().upper()

    print("\nEvaluator Result:", result)

    if "RELEVANT" in result and "NOT_RELEVANT" not in result:
        relevance = "relevant"
    else:
        relevance = "not_relevant"

    return {
        "relevance": relevance
    }


# ============================================================
# 8. CORRECT RETRIEVAL
# ============================================================

# def correct_retrieval(state: RAGState):

#     print("\n==============================")
#     print("STEP 3: CORRECTING RETRIEVAL")
#     print("==============================")

#     question = state["question"]

#     print("\nOriginal question:")
#     print(question)

#     # --------------------------------------------------------
#     # Simple classroom correction:
#     # Ask the LLM to rewrite the query into better search terms.
#     # --------------------------------------------------------

#     prompt = ChatPromptTemplate.from_template(
#         """
#         Improve the following search query.

#         Original Question:
#         {question}

#         Return only a better search query.
#         Do not explain anything.
#         """
#     )

#     chain = prompt | llm

#     response = chain.invoke(
#         {
#             "question": question
#         }
#     )

#     improved_query = response.content.strip()

#     print("\nImproved Query:")
#     print(improved_query)

#     # --------------------------------------------------------
#     # Search again using the improved query
#     # --------------------------------------------------------

#     new_docs = retriever.invoke(improved_query)

#     print("\nCorrected Retrieval Results:")

#     for i, doc in enumerate(new_docs, start=1):

#         print(f"\nDocument {i}:")
#         print(doc.page_content.strip())

#     return {
#         "documents": new_docs
#     }

def correct_retrieval(state: RAGState):

    print("\n==============================")
    print("STEP 3: CORRECTING RETRIEVAL")
    print("==============================")

    question = state["question"]

    correction_count = state["correction_count"] + 1

    print("\nCorrection Iteration:", correction_count)

    print("\nOriginal question:")
    print(question)

    # --------------------------------------------------------
    # Improve search query
    # --------------------------------------------------------

    prompt = ChatPromptTemplate.from_template(
        """
        Improve the following search query for semantic retrieval.

        Original Question:
        {question}

        Return only the improved search query.
        Do not explain anything.
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    improved_query = response.content.strip()

    print("\nImproved Query:")
    print(improved_query)

    # --------------------------------------------------------
    # Retrieve again
    # --------------------------------------------------------

    new_docs = retriever.invoke(improved_query)

    print("\nCorrected Retrieval Results:")

    for i, doc in enumerate(new_docs, start=1):

        print(f"\nDocument {i}:")

        print(
            "Source Type:",
            doc.metadata.get("source_type")
        )

        print(
            "Source:",
            doc.metadata.get("source_name")
        )

        print(
            "Page:",
            doc.metadata.get("page", "N/A")
        )

        print("\nContent:")
        print(doc.page_content.strip())

    return {
        "documents": new_docs,
        "correction_count": correction_count
    }


# ============================================================
# 9. GENERATE FINAL ANSWER
# ============================================================

def generate_answer(state: RAGState):

    print("\n==============================")
    print("STEP 4: GENERATING ANSWER")
    print("==============================")

    question = state["question"]

    documents = state["documents"]

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful teacher.

        Answer the question using ONLY the provided context.

        If the answer is not available in the context,
        say that the information is not available.

        Explain the answer in simple English.

        Question:
        {question}

        Context:
        {context}

        Answer:
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "context": context
        }
    )

    answer = response.content

    print("\nFINAL ANSWER:")
    print(answer)

    return {
        "final_answer": answer
    }


# ============================================================
# 10. ROUTER
# ============================================================

# def check_relevance(state: RAGState):

#     if state["relevance"] == "relevant":

#         print("\nDocuments are useful.")
#         print("Going directly to answer generation.")

#         return "generate"

#     else:

#         print("\nDocuments are NOT useful.")
#         print("Going to corrective retrieval.")

#         return "correct"

def check_relevance(state: RAGState):

    relevance = state["relevance"]
    correction_count = state["correction_count"]

    print("\n==============================")
    print("ROUTER")
    print("==============================")

    print("Relevance:", relevance)
    print(f"Correction count: {correction_count}/2")

    # --------------------------------------------------------
    # CASE 1: Documents are relevant
    # --------------------------------------------------------

    if relevance == "relevant":

        print("\nDocuments are useful.")
        print("Going to answer generation.")

        return "generate"

    # --------------------------------------------------------
    # CASE 2: Documents are NOT relevant
    # --------------------------------------------------------

    if relevance == "not_relevant":

        # We have not yet performed 2 corrections
        if correction_count < 2:

            print("\nDocuments are NOT useful.")

            print(
                f"Correction {correction_count + 1}/2 "
                "will be performed."
            )

            return "correct"

        # ----------------------------------------------------
        # Maximum 2 corrections reached
        # ----------------------------------------------------

        print("\nDocuments are still NOT relevant.")

        print(
            "Maximum 2 correction iterations reached."
        )

        print(
            "Stopping corrective loop."
        )

        print(
            "Going to final answer generation."
        )

        return "generate"

    # --------------------------------------------------------
    # Safety fallback
    # --------------------------------------------------------

    print("\nUnknown relevance value.")
    print("Stopping corrective loop.")

    return "generate"
# ============================================================
# 11. BUILD LANGGRAPH
# ============================================================

graph = StateGraph(RAGState)


# Add nodes

graph.add_node(
    "retrieve",
    retrieve_documents
)

graph.add_node(
    "evaluate",
    evaluate_documents
)

graph.add_node(
    "correct",
    correct_retrieval
)

graph.add_node(
    "generate",
    generate_answer
)


# Start

graph.add_edge(
    START,
    "retrieve"
)


# Retrieve → Evaluate

graph.add_edge(
    "retrieve",
    "evaluate"
)


# Evaluate → Relevant / Not Relevant

graph.add_conditional_edges(
    "evaluate",
    check_relevance,
    {
        "generate": "generate",
        "correct": "correct"
    }
)


# Correct → Generate

# graph.add_edge(
#     "correct",
#     "generate"
# )

graph.add_edge(
    "correct",
    "evaluate"
)

# Generate → End

graph.add_edge(
    "generate",
    END
)


# Compile graph

app = graph.compile()


# ============================================================
# 12. USER INPUT
# ============================================================

print("\n======================================")
print("       CORRECTIVE RAG DEMO")
print("======================================")

question = input(
    "\nAsk your question: "
)


# ============================================================
# 13. RUN GRAPH
# ============================================================

# result = app.invoke(
#     {
#         "question": question,
#         "documents": [],
#         "relevance": "",
#         "final_answer": "",
#         "correction_count": 0
#     }
# )

def ask_rag(question: str):

    result = app.invoke(
        {
            "question": question,
            "documents": [],
            "relevance": "",
            "final_answer": "",
            "correction_count": 0
        }
    )

    return result
# ============================================================
# 14. FINAL OUTPUT
# ============================================================

print("\n======================================")
print("             FINAL RESULT")
print("======================================")

# print(result["final_answer"])

#1.read data from pdf 
#2. read data from website
#3.negative flow is executing 1 time , check and improve to make it 2 iteration 
#4. build fastapi and link to UI