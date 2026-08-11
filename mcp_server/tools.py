# mcp_server/tools.py

from typing import List


def summarize_text(text: str) -> str:
    """
    Dummy summarization tool.

    Returns the first sentence of the input.
    """

    if not text.strip():
        return "No content provided."

    return text.split(".")[0].strip() + "."


def extract_keywords(text: str) -> List[str]:
    """
    Dummy keyword extraction tool.

    Returns unique keywords after removing common stop words.
    """

    if not text.strip():
        return []

    stop_words = {
        "the", "is", "a", "an", "and", "or", "to",
        "of", "for", "in", "on", "with", "this",
        "that", "it", "are", "was", "be", "as",
        "by", "at", "from", "into", "their"
    }

    words = (
        text.lower()
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .replace("?", "")
        .split()
    )

    keywords = []

    for word in words:
        if len(word) > 3 and word not in stop_words:
            if word not in keywords:
                keywords.append(word)

    return keywords
