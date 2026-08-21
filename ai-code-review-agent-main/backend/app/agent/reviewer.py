"""
The Code Review Agent's core LLM call.

This is the one place that talks to OpenAI's chat model. It builds a
ChatOpenAI instance from the Config Server's llm settings, assembles a
prompt out of the uploaded code + RAG context + MCP analysis, and asks
the model for a structured ReviewResult (no manual JSON parsing needed —
with_structured_output handles that).
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.config.client import get_openai_api_key
from app.models.review import ReviewResult

SYSTEM_PROMPT = """You are an experienced senior software engineer performing a code review.

Review the provided source file(s) for:
- Code quality: readability, naming, duplication, structure, unnecessary complexity
- Bugs: logical errors, None/null handling, incorrect conditions, edge cases
- Security: hardcoded secrets, unsafe input handling, dangerous operations \
(present these as AI-assisted findings, not a complete security audit)
- Performance: unnecessary loops, repeated calculations, inefficient data handling
- Best practices, using the reference knowledge below where relevant

Requested review focus: {review_focus}

Reference knowledge retrieved from the best-practices library:
{rag_context}

Deterministic file analysis from MCP tools (line/char counts, function/class counts, \
empty/oversized flags):
{mcp_results}

Give a score from 0-100 (100 = excellent), a short overall summary, a list of specific
issues (each with file, line if known, severity, category, message, suggestion), and a
list of general improvement suggestions. Only cite line numbers you can actually see in
the provided code."""

USER_PROMPT = "Here is the code to review:\n\n{code_files}"

_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", USER_PROMPT),
])


def build_llm(llm_config: dict) -> ChatOpenAI:
    """Create a ChatOpenAI client from Config Server settings + the locally-held API key."""
    return ChatOpenAI(
        model=llm_config["model"],
        temperature=llm_config["temperature"],
        max_tokens=llm_config["max_tokens"],
        api_key=get_openai_api_key(),
    )


def review_code_with_llm(
    llm_config: dict,
    code_files: str,
    review_focus: str,
    rag_context: str,
    mcp_results: dict,
) -> ReviewResult:
    llm = build_llm(llm_config)
    structured_llm = llm.with_structured_output(ReviewResult)
    chain = _prompt | structured_llm

    return chain.invoke({
        "review_focus": review_focus,
        "rag_context": rag_context or "No additional context retrieved.",
        "mcp_results": mcp_results or {},
        "code_files": code_files,
    })
