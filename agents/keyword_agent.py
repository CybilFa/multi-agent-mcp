from mcp_client.client import MCPClient
from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger


class KeywordAgent:
    """
    Keyword Agent delegates keyword extraction to the MCP Server.
    """

    def __init__(self, client: MCPClient):
        self.client = client

    async def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info("Keyword Agent started.")

        result = await self.client.keywords(request.content)

        logger.info("Keyword Agent completed.")

        keywords = result.structuredContent["result"]

        return TaskResponse(
             status="success",
             result=", ".join(keywords)
        )
    