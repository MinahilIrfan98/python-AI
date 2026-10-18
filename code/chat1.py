import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from datetime import datetime


# load code/.env no matter which folder you run the script from
load_dotenv(Path(__file__).parent / ".env")

llm = init_chat_model(
    model=os.getenv("MODEL_NAME"),
    model_provider="google_genai",
)

# memory: the whole conversation is sent on every call
history = [{"role": "system", "content": "You are a helpful assistant!"}]

@tool
def get_time():
    """Get the current time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#tool bind
#agentic loop+tool streaming

#conversation loop:chat + history + stream
print("Welcome! Type 'exit', 'quit' or 'bye' to leave.")
while True:
    question = input("you: ").strip()

    if not question:
        continue

    if question.lower() in ("exit", "quit", "bye"):
        print("bye")
        break
    history.append({"role": "user", "content": question})
    print("Bot: ", end="", flush=True)

    full = None  # the whole AI message, built up chunk by chunk
    completed=True
    try:
        for chunk in llm.stream(history):
            print(chunk.text, end="", flush=True)  # print only the NEW piece
            full = chunk if full is None else full + chunk
        completed=True
        print()
    except KeyboardInterrupt:
        print("\n[interrupted]")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        

    if full is not None and full.text:
        history.append(full)  # remember the reply
    else:
        history.pop()  # no reply, so remove the last user message