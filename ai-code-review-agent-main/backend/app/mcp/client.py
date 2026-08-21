"""
MCP Client — the backend's connection to the MCP Server (mcp-server/server.py).

Flow: Code Review Agent -> MCP Client -> MCP Server -> Tools

This opens a fresh streamable-http session per call, which is the simplest
correct pattern for a request/response tool call (no long-lived connection
to manage across FastAPI requests).
"""
import json

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def call_mcp_tool(server_url: str, tool_name: str, arguments: dict) -> dict:
    """Call one MCP tool and return its structured (dict) result."""
    async with streamablehttp_client(f"{server_url}/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            if result.isError:
                raise RuntimeError(f"MCP tool '{tool_name}' failed: {result.content}")
            if result.structuredContent:
                return result.structuredContent
            # Fallback: some clients/tool signatures don't populate structuredContent,
            # but our tools always return JSON-serialized dicts as text content.
            if result.content:
                return json.loads(result.content[0].text)
            return {}


async def run_code_tools(server_url: str, file_name: str, file_extension: str, code_content: str) -> dict:
    """Call both MCP tools for one file and combine their results."""
    metadata = await call_mcp_tool(
        server_url, "code_metadata",
        {"file_name": file_name, "file_extension": file_extension, "code_content": code_content},
    )
    analysis = await call_mcp_tool(
        server_url, "code_analysis",
        {"file_name": file_name, "file_extension": file_extension, "code_content": code_content},
    )
    return {**metadata, **analysis}
