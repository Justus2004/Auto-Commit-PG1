
import random



# Predefined responses

responses = {

    "hi": ["Hello!", "Hi there!", "Hey!"],

    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good, thanks!"],

    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],

    "default": ["Sorry, I didn't understand that.", "I'm not sure what you mean."],

}



def chatbot_response(user_input):

    # Convert user input to lowercase for case-insensitive matching

    user_input = user_input.lower()



    # Check if user input matches any predefined responses

    for key in responses:

        if user_input in key:

            return random.choice(responses[key])



    # If no predefined response matches, return a default response

    return random.choice(responses["default"])



# Main function to interact with the chatbot

def main():

    print("Welcome to the Chatbot!")

    print("Type 'bye' to exit.")



    while True:

        user_input = input("You: ")

        if user_input.lower() == 'bye':

            print(chatbot_response(user_input))

            break

        else:

            print("Bot:", chatbot_response(user_input))



if __name__ == "__main__":

    main()



