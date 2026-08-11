# tests/test_supervisor.py

import pytest
from unittest.mock import AsyncMock

from agents.supervisor import Supervisor
from models.schemas import TaskRequest, TaskResponse


@pytest.mark.asyncio
async def test_invalid_task():

    supervisor = Supervisor()

    supervisor.client.connect = AsyncMock()
    supervisor.client.close = AsyncMock()

    request = TaskRequest(
        task="translate",
        content="Hello World"
    )

    response = await supervisor.execute(request)

    assert response.status == "error"


@pytest.mark.asyncio
async def test_summary_routing():

    supervisor = Supervisor()

    supervisor.client.connect = AsyncMock()
    supervisor.client.close = AsyncMock()

    fake_agent = AsyncMock()

    fake_agent.execute.return_value = TaskResponse(
        status="success",
        result="summary"
    )

    supervisor.agents = {
        "summarize": fake_agent
    }

    request = TaskRequest(
        task="summarize",
        content="Artificial Intelligence."
    )

    response = await supervisor.execute(request)

    assert response.status == "success"
    