#OpenAi - used to connect to ChatGpt

from openai import OpenAI

#load_dotenv() - used to load environemntal file
from dotenv import load_dotenv

#import os module
import os
#loading environmental file
load_dotenv()

#connect to chatgpt
client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

question = input("enter your question")

response = client.responses.create(
    model = "gpt-5",
    input = question
)

print(response.output_text)