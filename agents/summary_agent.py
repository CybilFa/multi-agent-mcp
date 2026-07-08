from mcp_client.client import MCPClient
from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger


class SummaryAgent:
    """
    Summary Agent delegates summarization to the MCP Server.
    """

    def __init__(self, client: MCPClient):
        self.client = client

    async def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info("Summary Agent started.")

        result = await self.client.summarize(request.content)

        logger.info("Summary Agent completed.")

        return TaskResponse(
            status="success",
            result=result.structuredContent["result"]
        )
    