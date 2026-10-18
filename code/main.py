import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
# from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model_name = os.getenv("MODEL_NAME")
if not model_name:
    raise SystemError("MODEL_NAME is not set in .env ('e.g. openai:gpt-6')")

llm = init_chat_model(
    model=os.getenv("MODEL_NAME"),
    # temperature=os.getenv("TEMPERATURE"),
    api_key=os.getenv("API_KEY")
)

SYSTEM_PROMPT = "You are a helpful AI assistant!"

history = [
    {"role": "system", "content": SYSTEM_PROMPT}  # System Message
]

print("Welcome to Cue chat!")
while True:
    try:
        question = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if not question:
        continue

    if question.lower() in ("exit", "quit", "bye"):
        print("Goodbye!")
        break

    history.append({"role": "user", "content": question})  # User Message
    print("Bot: ", end="", flush=True)

    full = None
    for chunk in llm.stream(history):
        print(chunk.text, end="", flush=True)
        full = chunk if full is None else full + chunk
    print()

    history.append(full)