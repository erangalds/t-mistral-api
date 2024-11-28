import base64
import requests
import os
from mistralai import Mistral

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

# Path to your image
#image_path = "02-vision/images/yometh_sheyon.jpg"
image_path01= "02-vision/images/eiffel-tower-with-snow.jpeg"
image_path02= "02-vision/images/tennis-court.jpeg"

# Getting the base64 string
base64_image01 = encode_image(image_path01)
base64_image02 = encode_image(image_path02)

# Retrieve the API key from environment variables
api_key = os.environ["MISTRAL_API_KEY"]

# Specify model
model = "pixtral-12b-2409"

# Initialize the Mistral client
client = Mistral(api_key=api_key)

# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "what are the differences between two images?"
            },
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{base64_image01}" 
            },
                        {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{base64_image02}" 
            }
        ]
    }
]

# Get the chat response
chat_response = client.chat.complete(
    model=model,
    messages=messages
)

# Print the content of the response
print(chat_response.choices[0].message.content)