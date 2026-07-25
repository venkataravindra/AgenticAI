# #OpenAi - used to connect to ChatGpt
# from anthropic import Anthropic
# from openai import OpenAI

# #load_dotenv() - used to load environemntal file
# from dotenv import load_dotenv

# #import os module
# import os
# #loading environmental file
# load_dotenv()

# #connect to chatgpt
# client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

# question = input("enter your question")

# response = client.responses.create(
#     model = "gpt-5",
#     input = question
# )

# print(response.output_text)

# from ANTHROPIC--used to connect to Claude
from anthropic import Anthropic

#used to load environtmental file
from dotenv import load_dotenv


import os
#loading environment file
load_dotenv()

client=Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

question =input("enter your question")

response=client.messages.create(
    model="claude-opus-4-8",
    max_tokens=50,
    messages=[{"role":"user","content":question}]
)
answer=next((block.text for block in response.content if block.type=="text"),"")
print(answer)