from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger

from agents.worker_a import WorkerA
from agents.worker_b import WorkerB


class Supervisor:
    """
    Routes tasks to the correct worker.
    """

    def __init__(self):

        self.worker_a = WorkerA()
        self.worker_b = WorkerB()

    def execute(self, request: TaskRequest) -> TaskResponse:

        logger.info(f"Supervisor received task: {request.task}")

        if request.task.lower() == "summarize":

            logger.info("Routing to Worker A")

            return self.worker_a.execute(request)

        elif request.task.lower() == "keywords":

            logger.info("Routing to Worker B")

            return self.worker_b.execute(request)

        logger.error("Unknown task")

        return TaskResponse(
            status="error",
            result="Unknown task."
        )