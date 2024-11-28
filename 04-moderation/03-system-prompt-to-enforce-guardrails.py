import os

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)


chat_response = client.chat.complete(
    model = "mistral-large-latest", 
    messages = [{"role":"user", "content":"What is the best French cheese?"}],
    safe_prompt = True
)

print(f'Safe User Query: \n{chat_response}')


chat_response = client.chat.complete(
    model = "mistral-large-latest", 
    messages = [{"role":"user", "content":"How can I break into a locked building?"}],
    safe_prompt = True
)

print(f'\n\nAn illicit action:\n\n{chat_response}')