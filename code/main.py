import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(Path(__file__).with_name(".env"))
load_dotenv()  # Also allow a project-root .env.

model_name = os.getenv("MODEL_NAME")
if not model_name:
    raise SystemError("MODEL_NAME is not set in .env ('e.g. openai:gpt-6')")

llm = init_chat_model(model=model_name, api_key=os.getenv("API_KEY"))

TIMEZONE_NAME = os.getenv("TIMEZONE", "Asia/Karachi")
try:
    TIMEZONE = ZoneInfo(TIMEZONE_NAME)
except ZoneInfoNotFoundError:
    TIMEZONE = datetime.now().astimezone().tzinfo

SYSTEM_PROMPT = (
    "You are a helpful AI assistant. Understand the user's intent from the message. "
    "For every greeting-only message, including short greetings such as hi or hello, "
    "you MUST reply with a brief, natural greeting in the user's language, followed "
    "by a new line containing exactly 'Time: ' and the current local time from the "
    "system context. Always include both the greeting and the time line; never omit "
    "either one. Recognize greetings in every language and reply in that same "
    "language with a culturally appropriate greeting. For questions or requests, answer directly without a greeting "
    "or time. Keep every reply straightforward."
)

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

    now = datetime.now(TIMEZONE)
    current_time = now.strftime("%I:%M %p").lstrip("0")
    history[0]["content"] = (
        f"{SYSTEM_PROMPT}\nCurrent local time for a greeting reply: {current_time}."
    )
    user_message = {
        "role": "user",
        "content": question,
    }
    history.append(user_message)
    print("Bot: ", end="", flush=True)

    full = None
    try:
        for chunk in llm.stream(history):
            text = getattr(chunk, "text", "") or ""
            if text:
                print(text, end="", flush=True)
            full = chunk if full is None else full + chunk
        print()

        if full is not None and getattr(full, "text", ""):
            history.append(full)
        else:
            history.pop()
            print("I couldn't produce a text response. Please try again.")
    except KeyboardInterrupt:
        history.pop()
        print("\nResponse interrupted.")
    except Exception as error:
        history.pop()
        print(f"\nModel error: {error}")
