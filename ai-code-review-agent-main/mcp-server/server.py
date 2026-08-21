"""
MCP Server — exposes two deterministic code-analysis tools over the Model
Context Protocol (streamable-http transport, so any MCP client can call
them over plain HTTP on port 8002).

These tools do NOT use an LLM. They are simple, rule-based checks. The
LLM's job (readability, bugs, security judgement) happens later, in the
Code Review Agent — these tools just hand it a few hard facts to work with.
"""
import os
import re
from typing import Any

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

MCP_PORT = int(os.getenv("MCP_SERVER_PORT", "8002"))
LARGE_FILE_LINE_THRESHOLD = 500

mcp = FastMCP("code-review-tools", host="0.0.0.0", port=MCP_PORT)

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".jsx": "JavaScript (React)",
    ".tsx": "TypeScript (React)",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".go": "Go",
}

# Best-effort regexes for a rough function count per language family.
# These are heuristics, not a real parser — good enough for a quick signal.
FUNCTION_PATTERNS = {
    ".py": r"^\s*def\s+\w+\s*\(",
    ".js": r"\bfunction\s+\w*\s*\(|\b\w+\s*=\s*(\([^)]*\)|\w+)\s*=>",
    ".ts": r"\bfunction\s+\w*\s*\(|\b\w+\s*=\s*(\([^)]*\)|\w+)\s*=>",
    ".jsx": r"\bfunction\s+\w*\s*\(|\b\w+\s*=\s*(\([^)]*\)|\w+)\s*=>",
    ".tsx": r"\bfunction\s+\w*\s*\(|\b\w+\s*=\s*(\([^)]*\)|\w+)\s*=>",
    ".java": r"\b(public|private|protected|static)[\w\s<>\[\],]*\s+\w+\s*\([^;{}]*\)\s*\{",
    ".cs": r"\b(public|private|protected|static)[\w\s<>\[\],]*\s+\w+\s*\([^;{}]*\)\s*\{",
    ".cpp": r"\b\w[\w:<>&*\s]*\s+\w+\s*\([^;{}]*\)\s*\{",
    ".c": r"\b\w[\w\s*]*\s+\w+\s*\([^;{}]*\)\s*\{",
    ".go": r"\bfunc\s+\w+\s*\(",
}

CLASS_PATTERNS = {
    ".py": r"^\s*class\s+\w+",
    ".java": r"\bclass\s+\w+",
    ".cs": r"\bclass\s+\w+",
    ".cpp": r"\bclass\s+\w+",
    ".ts": r"\bclass\s+\w+",
    ".tsx": r"\bclass\s+\w+",
    ".js": r"\bclass\s+\w+",
    ".jsx": r"\bclass\s+\w+",
}


def _normalize_ext(file_extension: str) -> str:
    return file_extension if file_extension.startswith(".") else f".{file_extension}"


@mcp.tool()
def code_metadata(file_name: str, file_extension: str, code_content: str) -> dict[str, Any]:
    """Return basic metadata about a source file: detected language, line count, character count."""
    ext = _normalize_ext(file_extension)
    return {
        "file_name": file_name,
        "language": LANGUAGE_MAP.get(ext, "Unknown"),
        "number_of_lines": len(code_content.splitlines()),
        "number_of_characters": len(code_content),
    }


@mcp.tool()
def code_analysis(file_name: str, file_extension: str, code_content: str) -> dict[str, Any]:
    """Run simple deterministic checks: empty file, oversized file, rough function/class counts."""
    ext = _normalize_ext(file_extension)
    lines = code_content.splitlines()

    function_pattern = FUNCTION_PATTERNS.get(ext)
    class_pattern = CLASS_PATTERNS.get(ext)

    return {
        "file_name": file_name,
        "is_empty": len(code_content.strip()) == 0,
        "is_large_file": len(lines) > LARGE_FILE_LINE_THRESHOLD,
        "line_count": len(lines),
        "function_count": len(re.findall(function_pattern, code_content, re.MULTILINE)) if function_pattern else None,
        "class_count": len(re.findall(class_pattern, code_content, re.MULTILINE)) if class_pattern else None,
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
