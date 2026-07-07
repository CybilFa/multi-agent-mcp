from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger


class WorkerB:
    """
    Worker B extracts keywords.
    """

    def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info("Worker B started.")

        words = request.content.split()

        keywords = words[:5]

        logger.info("Worker B completed.")

        return TaskResponse(
            status="success",
            result=", ".join(keywords)
        )