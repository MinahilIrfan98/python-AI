from datetime import datetime
from pydantic import BaseModel # data part pr data validation
# from typing import Optional

from langchain.agents import create_agent


# Agent tool(s)
def get_time() -> str:
    """Return the current local time"""
    return datetime.now().strftime("%H:%M")

# Agent response
class Reply(BaseModel):
    is_greeting: bool
    time: str | None = None
    answer: str

# Agent
agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[get_time],
    system_prompt=(
        "You are a helpful AI Agent! "
        "If the user is greeting you, set is_greeting=true, call get_time, "
        "fill in time, and greet them based on the time of day. "
        "Otherwise set is_greeting=false and just answer normally."
    ),
    response_format=Reply
)

query = input("Query: ")

result = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
)
response = result["structured_response"]

if response.is_greeting:
    print(f"Time: {response.time}")
    print(f"Greeting: {response.answer}")
else:
    print(response.answer)

# Hi
# Time: 10:19
# Greeting: Hi good morning ...
# What is NLP?
# NPL is ....