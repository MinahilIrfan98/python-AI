  if question.lower() in ("exit", "quit", "bye"):
        print("Goodbye!")
        break

    history.append({"role": "user", "content": question})  # usermessage
print("Bot:", end="", flush=True)


full = None  # None | AIMessageChunk
for chunk in model.stream("What color is the sky?"):
    full = chunk if full is None else full + chunk
    print()
    completed=True
    except KeyboardInterrupt:
print("\n[interrupted]")
except Exception as e:
    print(f"\n[error] {e}")

is full and full.text:
history.append(full)
else:
history.pop()