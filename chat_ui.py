from anthropic import Anthropic
import dotenv
import os
import gradio as gr
import ai_assistant as ai

dotenv.load_dotenv()

def greet(name: str) -> str:
    return f"Hello {name}!"

user_input = gr.Textbox(label="Your Input:", placeholder="Enter your question here")
system_output = gr.Textbox(label="System Output:")
chatbot_ui = gr.Interface(fn=ai.chat_with_assistant, inputs=[user_input], outputs=[system_output])

#demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# demo.launch(share=True)  # Share your demo with just 1 extra parameter 🚀
# 👉   https://a23dsf231adb.gradio.live

chatbot_ui.launch()