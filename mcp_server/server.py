from mcp.server.fastmcp import FastMCP

from mcp_server.resources import SAMPLE_DOCUMENT
from mcp_server.tools import summarize_text, extract_keywords

mcp = FastMCP("MCP Demo")


@mcp.resource("document://demo")
def sample_document() -> str:
    """
    Exposes a sample document as an MCP Resource.
    """
    return SAMPLE_DOCUMENT


@mcp.tool()
def summarize(text: str) -> str:
    """
    Summarize the provided text.
    """
    return summarize_text(text)


@mcp.tool()
def keywords(text: str) -> list[str]:
    """
    Extract keywords from the provided text.
    """
    return extract_keywords(text)


if __name__ == "__main__":
    print("Starting MCP Server...")
    print("Waiting for MCP client connections...")

    mcp.run()
    