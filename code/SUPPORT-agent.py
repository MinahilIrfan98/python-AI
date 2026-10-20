from langchain.agents import create_agent
from pydantic import BaseModel
from typing import Literal


class Ticket(BaseModel):
    category: Literal["billing", "shipping", "technical", "general"]
    priority: Literal["low", "medium", "high"]
    summary: str


agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[],
    system_prompt="Classify the customer support messages.",
    response_format=Ticket,
)

msg = input("Customer message: ")
result = agent.invoke(
    {"messages": [{"role": "user", "content": msg}]}
)
print(result["structured_response"])

