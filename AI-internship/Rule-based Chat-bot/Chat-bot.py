import random
import re

# Defining arrays of predefined responses
responses = {
    "greeting": [
        "Hello! I'm here to help. What can I assist you with today?",
        "Hi there! How can I be of service?",
        "Hey! What's on your mind?",
        "Greetings! How may I assist you?",
        "Good day! How can I assist you today?"
    ],
    "name": [
        "I'm just a chatbot, but you can call me Chatting_ai.",
        "I don't have a name, but you can call me anything you like.",
        "Names aren't really my thing, but you can address me as Chatbot."
    ],
    "joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the computer keep freezing? Because it left its Windows open!",
        "Here's one: Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How about this: Parallel lines have so much in common. It's a shame they'll never meet."
    ],
    "calculation": ["Sure, I can help with calculations. Please enter a mathematical expression to calculate:"],
    "search": [
        "Sure, I can search for information. What topic would you like me to look up?",
        "I'm here to assist you in finding information. What should I search for?",
        "Feel free to tell me what you'd like to know more about, and I'll find the information for you."
    ],
    "help": [
        "You can interact with me in the following ways:",
        "- Say 'hello' to greet me.",
        "- Ask me for a joke by saying 'tell me a joke.'",
        "- Request calculations by typing 'calculate' followed by a mathematical expression (e.g., 'calculate 2+2').",
        "- Ask me to search for information by typing 'search' followed by your query (e.g., 'search for cats').",
        "- If you want to end our conversation, simply type 'bye.'",
        "Feel free to ask anything else or use these commands to make the most of our conversation!",
        "I'm here to assist you in various ways. Just let me know how I can help."
    ],
    "unknown": [
        "I didn't quite get that. Could you rephrase or clarify your question?",
        "I'm having trouble understanding your question. Could you ask in a different way?",
        "I'm not sure I follow. Can you provide more details or rephrase your question?"
    ],
    "advice": [
        "If I were you, I would go to the internet and type exactly what you wrote there!",
        "For advice, it's often helpful to consult online resources. You can find valuable information there."
    ]
}

# ... (the rest of your code remains the same)

# Defining a function to perform calculations
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

# Defining a function to generate a response
def generate_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Checking if the user input matches any predefined patterns
    if any(keyword in user_input for keyword in ["hello", "hi", "hey", "hola", "namaste"]):
        return random.choice(responses["greeting"])
    elif "name" in user_input:
        return random.choice(responses["name"])
    elif "joke" in user_input:
        return random.choice(responses["joke"])
    elif "calculate" in user_input:
        # Using regular expressions to extract and calculate expressions
        match = re.search(r'calculate[^\d]*(.*)', user_input)
        if match:
            expression = match.group(1)
            result = calculate_expression(expression)
            if result is not None:
                return f"The result of {expression} is {result}."
            else:
                return "I couldn't perform the calculation. Please check the expression."
    elif "search" in user_input:
        return random.choice(responses["search"])
    elif "help" in user_input:
        return "\n".join(responses["help"])
    elif "advice" in user_input:
        return random.choice(responses["advice"])
    else:
        return random.choice(responses["unknown"])

# Main chat loop
print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit. Type 'help' for assistance.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break
    
    response = generate_response(user_input)
    print("Chatbot:", response)
