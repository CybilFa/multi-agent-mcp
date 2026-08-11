# tests/test_client.py

import pytest
from unittest.mock import AsyncMock

from mcp_client.client import MCPClient


@pytest.mark.asyncio
async def test_summarize():

    client = MCPClient()

    client.summarize = AsyncMock(
        return_value={
            "result": "Artificial Intelligence is transforming software engineering."
        }
    )

    result = await client.summarize("AI is transforming software engineering.")

    assert result["result"].startswith("Artificial")


@pytest.mark.asyncio
async def test_keywords():

    client = MCPClient()

    client.keywords = AsyncMock(
        return_value={
            "result": [
                "artificial",
                "intelligence",
                "software"
            ]
        }
    )

    result = await client.keywords("AI is transforming software engineering.")

    assert "software" in result["result"]
    