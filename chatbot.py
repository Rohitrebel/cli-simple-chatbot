import random
from datetime import datetime

def chatbot():
    print("Hello! I am ChatBot 🤖. How can i help you today\n")

    user_name = None 

    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input == "exit" or "bye" in user_input:
            print("ChatBot: Goodbye! Have a great day")
            break

        # Asking for name
        elif "my name is" in user_input:
            user_name = user_input.split("is")[-1].strip().capitalize()
            print(f"ChatBot: Nice to meet you, {user_name}!")

        elif "what is my name" in user_input and user_name:
            print(f"ChatBot: Your name is {user_name}, of course!")

        # Greetings
        elif any(word in user_input for word in ["hello", "hi", "hey"]):
            if user_name:
                print(f"ChatBot: Hello {user_name}! How can I help you today?")
            else:
                print("ChatBot: Hi there! What's your name?")

        # Small talk
        elif "how are you" in user_input:
            print("ChatBot: I’m doing great, thanks for asking! How about you?")

        elif "i am fine" in user_input or "i am good" in user_input:
            print("ChatBot: Glad to hear that!")

        # Time
        elif "time" in user_input:
            print("ChatBot: The current time is", datetime.now().strftime("%H:%M:%S"))

        # Date
        elif "date" in user_input:
            print("ChatBot: Today's date is", datetime.now().strftime("%Y-%m-%d"))

        # Calculator
        elif any(op in user_input for op in ["+", "-", "*", "/"]):
            try:
                result = eval(user_input)
                print("ChatBot: The answer is", result)
            except:
                print("ChatBot: Hmm, that doesn’t look like a valid math expression.")

        # Jokes
        elif "joke" in user_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why was the math book sad? Because it had too many problems.",
                "Why don’t programmers scared of python? Because it could bite them!"
            ]
            print("ChatBot:", random.choice(jokes))

        # About chatbot
        elif "what is a chatbot" in user_input:
            print("ChatBot: A chatbot is a program that can talk with users using rules or AI.")

        # Help
        elif "help" in user_input:
            print("ChatBot: You can ask me about time, date, math, jokes, or just chat with me!")

        # Default response
        else:
            print("ChatBot: Sorry, I don’t understand that yet.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
