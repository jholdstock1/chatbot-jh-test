import random

def get_response(question):
    knowledge_bank = {
        "What is your name?": "I am a chatbot.",
        "How are you?": "I don't have feelings, but I'm here to help!",
        "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
        "Who is the president of the United States?": "As of my last knowledge update in January 2022, it was Joe Biden.",
        "What is a text link?": "A text link is a customer facing link that appears on a publishers site."
        # Add more questions and answers as needed
    }

    # Check if the question is in the knowledge bank
    if question in knowledge_bank:
        return knowledge_bank[question]
    else:
        # If the question is not in the knowledge bank, provide a default response
        return "I'm sorry, I don't have information on that."

def main():
    print("Chatbot: Hello! Ask me anything or type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Get the response from the chatbot
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
