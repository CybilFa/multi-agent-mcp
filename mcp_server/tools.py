# mcp_server/tools.py

def summarize_text(text: str) -> str:
    """
    Dummy summarization tool.

    Returns the first sentence of the input.
    """

    if not text.strip():
        return "No content provided."

    return text.split(".")[0] + "."