from anthropic import Anthropic
import dotenv
import os

dotenv.load_dotenv()


def chat_with_assistant(user_prompt: str, system_prompt: str = None) -> str:
    # Setup API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=api_key)
    # print(client._version)

    if system_prompt is None:
        system_prompt = """You are an AI assistant tasked with helping users with questions. 
        Your provide short answers with simple language that doesn't sounds like AI generated."""

    # Create a chat instance:
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=265,
        system=system_prompt,  # <-- system prompt
        messages=[
            {"role": "user", "content": user_prompt}  # <-- user prompt
        ]
    )

    # Send messages and get responses:
    return response.content[0].text.strip()
    # return response.content[0].text.replace("।", ".")
    # return response.content[0].text.replace("।", ".").replace("।", ".")
    # return response.content[0].text.replace("।", ".").replace("।", ".").replace("।", ".")
