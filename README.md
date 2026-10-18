# GenAI Foundations

A collection of foundational experiments and implementations exploring Generative AI, specifically focusing on Large Language Model (LLM) integration, chat interfaces, and agentic workflows using the LangChain framework.

## 🚀 Project Overview

This project serves as a learning ground for building AI-powered applications. It demonstrates the progression from a simple streaming chat interface to more complex agentic loops and tool-calling capabilities.

## 🛠️ Core Components

### 💬 Chat Interfaces
- `code/main.py`: A basic streaming chat implementation that maintains conversation history.
- `code/chat1.py`: An enhanced chat version with support for environment variable loading from specific paths and integration with `google_genai`.

### 🤖 Agentic Workflows
- `code/agent.py`: An interactive agent chat using `create_agent` and the configured model.

### 📚 RAG (Retrieval-Augmented Generation)
- `code/rag.py`: (Work in Progress) Dedicated space for implementing retrieval-augmented generation to provide LLMs with external data.

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.13+
- A `.env` file in the `code/` directory containing:
  - `MODEL_NAME`: The model to use, such as `ollama:gemma4:31b-cloud`, `openai:gpt-4o`, or `google_genai:gemini-pro`.
  - `API_KEY`: Your provider's API key (not needed for local Ollama models).

For Ollama, make sure Ollama is running and the model is available (`ollama list`).

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd genai-foundations
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## 📖 Usage

To start the basic chat interface:
```bash
python code/main.py
```

To run the agent experiment:
```bash
python code/agent.py
```

Both chat scripts keep conversation history. The model decides from meaning whether a message is a greeting or a question. For a greeting, it replies briefly in the same language and adds `Time: ...` on the next line. For questions, it answers directly without a greeting or time. Set `TIMEZONE` to an IANA time-zone name if needed; it defaults to `Asia/Karachi` and falls back to the computer's local time if Windows lacks time-zone data.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** [LangChain](https://python.langchain.com/)
- **Configuration:** `python-dotenv`
