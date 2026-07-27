from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
prompt = input("Enter Image Description:")

response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"  # Correct format: no spaces, use 'x'
)

with open("output.png", "wb") as f:
    f.write(base64.b64decode(response.data[0].b64_json))  # Fixed: added b64decode

print("Image Generated Successfully !!")