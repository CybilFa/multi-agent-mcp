# tests/test_agents.py

import pytest
from unittest.mock import AsyncMock

from agents.summary_agent import SummaryAgent
from agents.keyword_agent import KeywordAgent
from models.schemas import TaskRequest


@pytest.mark.asyncio
async def test_summary_agent():

    client = AsyncMock()

    client.summarize.return_value.structuredContent = {
        "result": "Artificial Intelligence."
    }

    agent = SummaryAgent(client)

    request = TaskRequest(
        task="summarize",
        content="Artificial Intelligence is transforming software engineering."
    )

    response = await agent.execute(request)

    assert response.status == "success"
    assert response.result == "Artificial Intelligence."


@pytest.mark.asyncio
async def test_keyword_agent():

    client = AsyncMock()

    client.keywords.return_value.structuredContent = {
        "result": [
            "artificial",
            "intelligence",
            "software"
        ]
    }

    agent = KeywordAgent(client)

    request = TaskRequest(
        task="keywords",
        content="Artificial Intelligence is transforming software engineering."
    )

    response = await agent.execute(request)

    assert response.status == "success"

    assert response.result == "artificial, intelligence, software"
    