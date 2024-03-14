import re

def perform_math_operation(input_text):
    # Regular expression to match mathematical expressions
    math_pattern = r'(\d+)\s*([\+\-\*/])\s*(\d+)'

    match = re.match(math_pattern, input_text)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Division by zero is not allowed."
    else:
        return None

def respond(input_text):
    input_text = input_text.lower()
    
    if "hello" in input_text:
        return "Hello!"
    elif "how are you" in input_text:
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in input_text:
        return "Goodbye! Have a great day!"
    elif "what is your name" in input_text:
        return "My name is Chitti."
    elif "how old are you" in input_text:
        return "I'm as new as the new iPhone. Hahaha, sorry, chatbots don't age."
    elif "tell me a joke" in input_text:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "tell me about yourself" in input_text:
        return "I'm a simple chatbot created using if else statements in Python. It's a pretty cool language."
    elif "thank you" in input_text:
        return "What can i say except you're welcome!"
    elif "bye" in input_text:
        return "Goodbye! Have a great day!"
    else:
        math_result = perform_math_operation(input_text)
        if math_result is not None:
            return "The result of the operation is: {}".format(math_result)
        else:
            return "I'm sorry, I didn't understand that."

def main():
    print("Hey,This is Chatbot Chitti. When you want to exit, type bye")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            response = respond(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    main()
