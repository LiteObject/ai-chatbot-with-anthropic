import ai_assistant as ai
from colorama import Fore, Back, Style

def print_system_message(message):
    print(Fore.LIGHTRED_EX + "Chatbot: " + message + Fore.RESET + "\n")

if __name__ == "__main__":
    try:

        while True:
            Style.RESET_ALL

            user_input = input("You: ").strip()

            if len(user_input) > 0:
                if user_input.lower() in ["quit", "exit", "bye", "qq"]:
                    print_system_message("Goodbye!")                             
                    break

                response =  ai.chat_with_assistant(user_input)
                print_system_message(response)                

    except Exception as e:
        print(f"Error: {e}")