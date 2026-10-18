---
name: chatbot-feature
description: Implement interactive chatbot features including conversation memory and streaming.
---

### Chatbot Implementation Standard

**1. Interactive Loop**
- Use a `while True:` loop to handle continuous user input.
- Include exit keywords: `exit`, `quit`, `bye`.

**2. Memory Management**
- Maintain a conversation state using a list of messages.
- Format: `[{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]`.
- Ensure the bot's response is appended back to the history.

**3. Real-time Streaming**
- Use the `.stream()` method of the LangChain LLM.
- Print chunks using `end="", flush=True` to avoid line breaks between tokens.

**4. LangChain Integration**
- Use `init_chat_model` or `ChatOllama` for the LLM backend.
- Pass the entire history list to the LLM on every call to maintain context.

### Verification Steps
1. Start the chatbot.
2. Provide a piece of information (e.g., "My name is Ali").
3. Ask a follow-up question (e.g., "What is my name?").
4. Verify the response is correct and streamed in real-time.
