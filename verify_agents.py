from agents.supervisor import Supervisor
from models.schemas import TaskRequest

supervisor = Supervisor()

print("\n----- SUMMARY -----")

response = supervisor.execute(
    TaskRequest(
        task="summarize",
        content="Artificial Intelligence is changing the world. It helps automate tasks."
    )
)

print(response.model_dump())


print("\n----- KEYWORDS -----")

response = supervisor.execute(
    TaskRequest(
        task="keywords",
        content="Artificial Intelligence enables machine learning and natural language processing."
    )
)

print(response.model_dump())
