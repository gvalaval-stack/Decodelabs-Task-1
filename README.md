# Rule-Based AI Chatbot

A simple rule-based chatbot using Python if-else logic and keyword matching.

## How to Run
```bash
python chatbot.py
```
No external libraries required — pure Python.

## Features
- Greetings & farewells
- Basic Q&A (name, capabilities, jokes, weather, time)
- Continuous conversation loop
- Graceful exit on `quit` / `bye`

## Sample Conversation
```
You: hello
Chatbot: Hello! How can I help you?

You: tell me a joke
Chatbot: Why did the programmer quit? Because he didn't get arrays! 😄

You: bye
Chatbot: Goodbye! Have a great day!
```

## How to Extend
Add new entries to the `responses` dictionary in this format:
```python
("keyword1", "keyword2"): "Your response here",
```

## Concepts Covered
- Control flow (`while`, `if-else`)
- Dictionary-based rule matching
- String handling (`.lower()`, `.strip()`)
- Basic AI concept: rule-based / pattern-matching systems
