import os

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

response = client.classifiers.moderate_chat(
    model="mistral-moderation-latest",
    inputs=[
        {"role": "user", "content": "...user prompt ..."},
        {"role": "assistant", "content": "...assistant response..."},
    ],
)

print(response)