from datetime import datetime
from langchain.agents import create_agent

def get_time()-> str:
    """ Retur current local time"""
    return datetime.now().strftime(format="%H:%T")

agent=create_agent(
    model="ollama:gemma4:31-cloud",
    tools=[],
    system_prompt="You are a helpful assistant!",

)

response=agent.invoke(
    input={"messages": [{"role": "user", "content": "Hello, how are you?"}]}
)

print(result["messages"][-1].text)