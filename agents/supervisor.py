from mcp_client.client import MCPClient
from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger

from agents.summary_agent import SummaryAgent
from agents.keyword_agent import KeywordAgent


class Supervisor:
    """
    Supervisor Agent responsible for routing tasks
    to specialized agents.
    """

    def __init__(self):

        self.client = MCPClient()

        # Initialize agents once with the shared client
        self.agents = {
            "summarize": SummaryAgent(self.client),
            "keywords": KeywordAgent(self.client),
        }

    async def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info(f"Supervisor received task: {request.task}")

        try:

            # Open one shared MCP connection
            await self.client.connect()

            agent = self.agents.get(request.task.lower())

            if agent is None:

                logger.error(f"No agent registered for '{request.task}'")

                return TaskResponse(
                    status="error",
                    result=f"No agent found for task '{request.task}'"
                )

            logger.info(f"Routing to {agent.__class__.__name__}")

            response = await agent.execute(request)

            return response

        finally:  
              await self.client.close()
              