import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
messages = [
    {
        "role": "user",
        "content": "What is the best French meal? Return the name and the ingredients in short JSON object.",
    }
]
chat_response = client.chat.complete(
      model = model,
      messages = messages,
)

print(f'Asking for JSON output in the Prompt.\n {chat_response.choices[0].message.content}')

chat_response = client.chat.complete(
      model = model,
      messages = messages,
      response_format = {
          "type": "json_object",
      }
)

print(f'\nSetting the response_foramt parameter to json_object. \n {chat_response.choices[0].message.content}')

