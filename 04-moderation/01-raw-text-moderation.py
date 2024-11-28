import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

response = client.classifiers.moderate(
    model = "mistral-moderation-latest",  
    inputs=["I want to get into my car and go on a trip."]
)

print(f'A safe sentence. \n{response}')


response = client.classifiers.moderate(
    model = "mistral-moderation-latest",  
    inputs=["I want to break into my neighbors car and go on a trip."]
)

print(f'\n\nA illicit action\n{response}')
