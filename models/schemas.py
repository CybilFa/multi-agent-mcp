from pydantic import BaseModel, Field
from typing import Literal


class TaskRequest(BaseModel):
    """
    Represents a task sent by the user or supervisor.
    """

    task: str = Field(..., description="Task to perform")
    content: str = Field(..., description="Input content for the task")


class TaskResponse(BaseModel):
    """
    Standard response returned by workers or tools.
    """

    status: Literal["success", "error"]
    result: str


class ToolCall(BaseModel):
    """
    Represents one tool execution event.
    Used by the tracing layer.
    """

    tool_name: str
    status: Literal["started", "completed", "failed"]
    timestamp: str
    