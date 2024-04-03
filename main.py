from anthropic import Anthropic
import dotenv
import os

dotenv.load_dotenv()

# Setup API key
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)
# print(client._version)

# Create a chat instance:
response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=265,
    system="Respond only in Bengali.", # <-- system prompt
    messages=[
        {"role": "user", "content": "Hello, Claude!"} # <-- user prompt
    ]
)

# Send messages and get responses:
print(response.content[0].text)