from models.schemas import TaskRequest, TaskResponse
from tracing.logger import logger

# Create a sample request
request = TaskRequest(
    task="summarize",
    content="Artificial Intelligence is transforming software."
)

logger.info("Created TaskRequest")

# Create a sample response
response = TaskResponse(
    status="success",
    result="AI is transforming software."
)

logger.info("Created TaskResponse")

print("\nRequest")
print(request.model_dump())

print("\nResponse")
print(response.model_dump())
