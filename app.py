import ai_assistant as ai
from colorama import Fore, Back, Style
import gradio as gr

if __name__ == "__main__":
    try:

        while True:
            user_input = input("You: ").strip()

            if len(user_input) > 0:
                if user_input.lower() in ["quit", "exit", "bye", "qq"]:
                    print(Fore.LIGHTRED_EX + "Chatbot: Goodbye!")                             
                    break

                response =  ai.chat_with_assistant(user_input)
                print(Fore.LIGHTRED_EX + "Chatbot: ", response, "\n")

    except Exception as e:
        print(f"Error: {e}")