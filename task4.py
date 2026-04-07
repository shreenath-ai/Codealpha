# ============================================
#   BASIC CHATBOT
#   CodeAlpha Internship Task 4
#   Author: Python Intern
# ============================================


# ─────────────────────────────────────────
#  Predefined responses dictionary
# ─────────────────────────────────────────
RESPONSES = {
    # Greetings
    "hello": "Hi there! 👋 How can I help you today?",
    "hi": "Hello! 😊 Nice to meet you!",
    "hey": "Hey! What's up? 😄",

    # How are you
    "how are you": "I'm doing great, thanks for asking! 😊 How about you?",
    "how are you doing": "I'm fantastic! Ready to chat. 🤖",
    "what's up": "Not much, just here to help you! 😄",
    "whats up": "All good! What can I do for you?",

    # About the bot
    "what is your name": "I'm ChatBot 🤖, your friendly Python assistant!",
    "what's your name": "My name is ChatBot! Built with Python 🐍",
    "who are you": "I'm a simple rule-based chatbot made for CodeAlpha Task 4! 🤖",
    "are you a bot": "Yes, I'm a bot! 🤖 But I'm here to help!",
    "are you human": "Nope! I'm a Python-powered chatbot 🐍",

    # Help
    "help": "I can chat with you! Try saying: hello, how are you, what is your name, joke, time, bye 😊",
    "what can you do": "I can greet you, answer questions, tell jokes, and more! Try 'help' for hints.",

    # Jokes
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
    "joke": "Why did the Python programmer break up with Java? Too much class drama! 😂",
    "funny": "Here's one: I told my computer I needed a break... now it won't stop sending me Kit-Kat ads 😄",

    # Python related
    "i love python": "Python is awesome! 🐍 Great choice for programming!",
    "python": "Python is one of the best programming languages! 🐍 Keep coding!",
    "codealpha": "CodeAlpha is a great internship program! Keep up the good work 💪",

    # Time / Date
    "what time is it": "__TIME__",
    "time": "__TIME__",
    "what is today": "__DATE__",
    "today": "__DATE__",

    # Goodbye
    "bye": "Goodbye! 👋 Have a great day!",
    "goodbye": "See you later! Take care 😊",
    "exit": "Bye bye! 👋",
    "quit": "Quitting chat... Goodbye! 👋",

    # Thanks
    "thank you": "You're welcome! 😊",
    "thanks": "No problem at all! 😊",
    "thanks a lot": "Happy to help! 😄",

    # Default
    "default": "Hmm, I'm not sure about that 🤔 Try asking something else or type 'help'."
}


# ─────────────────────────────────────────
#  Get chatbot response
# ─────────────────────────────────────────
def get_response(user_input):
    """Return a response based on user input."""
    from datetime import datetime

    text = user_input.lower().strip()

    # Check for exit commands
    if text in ("bye", "goodbye", "exit", "quit"):
        return RESPONSES.get(text), True  # True = exit flag

    # Check for exact or partial matches
    for key, response in RESPONSES.items():
        if key in text:
            # Handle dynamic time/date responses
            if response == "__TIME__":
                return f"The current time is: {datetime.now().strftime('%H:%M:%S')} ⏰", False
            elif response == "__DATE__":
                return f"Today is: {datetime.now().strftime('%A, %B %d, %Y')} 📅", False
            return response, False

    return RESPONSES["default"], False


# ─────────────────────────────────────────
#  Main chatbot loop
# ─────────────────────────────────────────
def chatbot():
    """Main chatbot function."""
    print("=" * 50)
    print("   🤖 CHATBOT — CodeAlpha Internship Task 4")
    print("=" * 50)
    print("  Hi! I'm ChatBot 🤖 Type 'help' for hints.")
    print("  Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("\n  You: ").strip()

        if not user_input:
            print("  Bot: Please say something! 😊")
            continue

        response, should_exit = get_response(user_input)
        print(f"  Bot: {response}")

        if should_exit:
            break


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────
if __name__ == "__main__":
    chatbot()