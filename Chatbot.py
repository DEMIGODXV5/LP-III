import re
import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        # Greetings
        r"\b(hello|hi|hey)\b": [
            "Hello. Welcome to our grocery store.",
            "Hi there. How can I help you today?"
        ],

        # Specific products FIRST (important)
        r"\b(milk)\b": [
            "Milk costs 30 rupees per liter."
        ],
        r"\b(eggs)\b": [
            "A dozen eggs cost 80 rupees."
        ],
        r"\b(rice)\b": [
            "Rice costs 50 rupees per kilogram."
        ],

        # Product categories
        r"\b(fruits)\b": [
            "We have apples, bananas, and oranges."
        ],
        r"\b(vegetables|veggies)\b": [
            "We have fresh vegetables available. What would you like?"
        ],
        r"\b(snacks)\b": [
            "We have chips, biscuits, and chocolates."
        ],
        r"\b(beverages|drinks)\b": [
            "We have juices, soft drinks, and bottled water."
        ],

        # General queries
        r"\b(price|cost)\b": [
            "Please tell me the product name to check its price."
        ],
        r"\b(order status|track order)\b": [
            "Please provide your order ID to check the status."
        ],
        r"\b(shipping time|delivery time)\b": [
            "We offer same-day delivery and standard delivery in 3 to 5 days."
        ],
        r"\b(return policy)\b": [
            "You can return items within 7 days if they are unopened."
        ],
        r"\b(payment methods)\b": [
            "We accept UPI, debit cards, credit cards, and cash."
        ],
        r"\b(store hours|timing)\b": [
            "Our store is open from 8 AM to 10 PM every day."
        ],
        r"\b(location|address)\b": [
            "We are located at XYZ Market, Main Street."
        ],
        r"\b(buy|order)\b": [
            "You can place an order online or visit our store."
        ],

        # Politeness
        r"\b(thank you|thanks)\b": [
            "You are welcome."
        ]
    }

    # Pattern matching
    for pattern, reply_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(reply_list)

    return "Sorry, I didn’t understand that. Please ask about products, prices, or delivery."


# -------- Chat Loop --------
print("Grocery Chatbot (type 'bye' or 'exit' to stop)\n")

while True:
    user_message = input("You: ")

    if user_message.lower() in ["bye", "exit"]:
        print("Bot: Goodbye. Have a nice day.")
        break

    response = chatbot_response(user_message)
    print("Bot:", response)
