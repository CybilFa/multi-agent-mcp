from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger


class WorkerA:
    """
    Worker A is responsible for summarizing text.
    """

    def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info("Worker A started.")

        summary = request.content.split(".")[0] + "."

        logger.info("Worker A completed.")

        return TaskResponse(
            status="success",
            result=summary
        )