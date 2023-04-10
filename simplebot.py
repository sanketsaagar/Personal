# import necessary libraries
import random

# define chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm good, how about you?"],
    "what's your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!"],
    "default": ["Sorry, I didn't understand what you said.", "Can you please repeat that?"]
}

# define function to return chatbot response based on user input
def get_response(user_input):
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# start chatbot conversation
print("Welcome to the chatbot!")
while True:
    user_input = input("You: ").lower()
    chatbot_response = get_response(user_input)
    print("Chatbot:", chatbot_response)
