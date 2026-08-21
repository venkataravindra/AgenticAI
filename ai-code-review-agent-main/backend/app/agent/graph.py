"""
The single-agent LangGraph workflow:

    START -> validate_code -> retrieve_context -> run_mcp_tools -> review_code -> format_response -> END

    (conditional edge: a validation failure at validate_code skips straight to
    format_response so the API still returns clean JSON instead of a 500 error)

There is only one AI agent here — review_code_node, which calls the LLM.
Every other node is plain deterministic Python (validation, a vector
search, two tool calls). LangGraph's job is just to sequence them and
carry state between steps.
"""
from langgraph.graph import END, START, StateGraph

from app.agent.reviewer import review_code_with_llm
from app.agent.state import CodeReviewState
from app.mcp.client import run_code_tools
from app.rag.retriever import retrieve_context as retrieve_rag_context

ALLOWED_EXTENSIONS = {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".cpp", ".c", ".cs", ".go"}


async def validate_code(state: CodeReviewState) -> CodeReviewState:
    files = state.get("files", [])
    if not files:
        return {**state, "error": "No files provided for review."}
    for f in files:
        if f["file_extension"] not in ALLOWED_EXTENSIONS:
            return {**state, "error": f"Unsupported file type: {f['file_extension']}"}
    return state


def route_after_validation(state: CodeReviewState) -> str:
    """If validation failed, skip RAG/MCP/LLM entirely and go straight to formatting."""
    return "format_response" if state.get("error") else "retrieve_context"


async def retrieve_context_node(state: CodeReviewState) -> CodeReviewState:
    languages = ", ".join(sorted({f["file_extension"] for f in state["files"]}))
    query = (
        f"Best practices, common bugs, and security guidance relevant to: "
        f"{state['review_focus']}. File types: {languages}"
    )
    return {**state, "rag_context": retrieve_rag_context(query)}


async def run_mcp_tools_node(state: CodeReviewState) -> CodeReviewState:
    mcp_results = {}
    for f in state["files"]:
        mcp_results[f["file_name"]] = await run_code_tools(
            state["mcp_server_url"], f["file_name"], f["file_extension"], f["content"]
        )
    return {**state, "mcp_results": mcp_results, "mcp_tools_used": ["code_metadata", "code_analysis"]}


async def review_code_node(state: CodeReviewState) -> CodeReviewState:
    code_files_text = "\n\n".join(
        f"### File: {f['file_name']}\n```{f['file_extension'].lstrip('.')}\n{f['content']}\n```"
        for f in state["files"]
    )
    result = review_code_with_llm(
        llm_config=state["llm_config"],
        code_files=code_files_text,
        review_focus=state["review_focus"],
        rag_context=state["rag_context"],
        mcp_results=state["mcp_results"],
    )
    return {**state, "review_result": result.model_dump()}


async def format_response_node(state: CodeReviewState) -> CodeReviewState:
    if state.get("error"):
        return {
            **state,
            "review_result": {
                "summary": f"Review could not be completed: {state['error']}",
                "score": 0,
                "issues": [],
                "improvements": [],
                "rag_context_used": False,
                "mcp_tools_used": [],
            },
        }
    review_result = state["review_result"]
    review_result["rag_context_used"] = bool(state.get("rag_context"))
    review_result["mcp_tools_used"] = state.get("mcp_tools_used", [])
    return {**state, "review_result": review_result}


def build_review_graph():
    graph = StateGraph(CodeReviewState)
    graph.add_node("validate_code", validate_code)
    graph.add_node("retrieve_context", retrieve_context_node)
    graph.add_node("run_mcp_tools", run_mcp_tools_node)
    graph.add_node("review_code", review_code_node)
    graph.add_node("format_response", format_response_node)

    graph.add_edge(START, "validate_code")
    graph.add_conditional_edges(
        "validate_code",
        route_after_validation,
        {"format_response": "format_response", "retrieve_context": "retrieve_context"},
    )
    graph.add_edge("retrieve_context", "run_mcp_tools")
    graph.add_edge("run_mcp_tools", "review_code")
    graph.add_edge("review_code", "format_response")
    graph.add_edge("format_response", END)

    return graph.compile()
