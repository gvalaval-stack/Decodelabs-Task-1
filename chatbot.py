def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'quit' to exit.")

    responses = {
        ("hi", "hello", "hey", "howdy"): "Hello! How can I help you?",
        ("how are you", "how r u", "how are u"): "I'm doing great, thanks for asking!",
        ("what is your name", "who are you", "your name"): "I'm RuleBot, a simple rule-based chatbot!",
        ("what can you do", "help", "capabilities"): "I can respond to greetings, answer basic questions, and tell jokes!",
        ("joke", "tell me a joke", "funny"): "Why did the programmer quit? Because he didn't get arrays! 😄",
        ("bye", "goodbye", "see you", "quit", "exit"): "Goodbye! Have a great day!",
        ("thanks", "thank you", "thx"): "You're welcome! 😊",
        ("time", "what time is it"): "I don't have a clock, but your device does! 😄",
        ("weather", "how is the weather"): "I can't check the weather, but I hope it's sunny where you are!",
    }

    while True:
        user_input = input("You: ").strip().lower()

        if not user_input:
            print("Chatbot: Please say something!")
            continue

        matched = False
        for keywords, reply in responses.items():
            if any(kw in user_input for kw in keywords):
                print(f"Chatbot: {reply}")
                matched = True
                if any(kw in user_input for kw in ("bye", "goodbye", "see you", "quit", "exit")):
                    return
                break

        if not matched:
            print("Chatbot: I don't understand that. Try saying 'help' to see what I can do!")

if __name__ == "__main__":
    chatbot()
