---
name: migrate-ollama-to-langchain
description: Migrate AI logic from Ollama SDK to LangChain with chatbot features (memory & streaming).
---

### Migration Guidelines

**1. Library Swap**
- Replace `import ollama` with `from langchain_ollama import ChatOllama` or `from langchain.chat_models import init_chat_model`.

**2. Implementation Pattern**
- **Ollama SDK:** `ollama.chat(model='...', messages=...)` $\rightarrow$ **LangChain:** `llm = ChatOllama(model='...')` followed by `llm.invoke(...)` or `llm.stream(...)`.

**3. Chatbot Feature Requirements**
- **Memory:** Implement a list-based history `history = []` and append both `HumanMessage` and `AIMessage`.
- **Loop:** Wrap the logic in a `while True:` loop with `input("you: ")`.
- **Streaming:** Use `.stream(messages)` to provide a real-time typing effect.

**4. Verification**
- Run the script and verify that:
  - The bot remembers the user's name from a previous turn.
  - The output streams chunk-by-chunk.
  - The model used is `gemma4:31-cloud` (or the specified Ollama model).

### Execution Command
`python code/<filename>.py`
