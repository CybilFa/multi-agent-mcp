# tests/test_tools.py

from mcp_server.tools import summarize_text, extract_keywords


def test_summarize_returns_first_sentence():

    text = (
        "Artificial Intelligence is transforming software engineering. "
        "It is changing the future."
    )

    result = summarize_text(text)

    assert result == "Artificial Intelligence is transforming software engineering."


def test_summarize_empty_text():

    result = summarize_text("")

    assert result == "No content provided."


def test_extract_keywords():

    text = (
        "Artificial Intelligence is transforming modern software engineering."
    )

    result = extract_keywords(text)

    assert isinstance(result, list)

    assert "artificial" in result
    assert "intelligence" in result
    assert "software" in result
    assert "engineering" in result


def test_extract_keywords_empty():

    result = extract_keywords("")

    assert result == []
    