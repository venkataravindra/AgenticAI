# from openai import OpenAI
# from dotenv import load_dotenv
# import os 
# from fastapi import FastAPI
# #wants to connect to other applications - React, Angular,VueJs, Java(8080), dotnet,......
# from fastapi.middleware.cors import CORSMiddleware

# load_dotenv()

# client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

# app = FastAPI()

# app.add_middleware(CORSMiddleware, 
#                    allow_origins= ["*"],
#                    allow_credentials=True,
#                    allow_methods=["*"],
#                    allow_headers=["*"])

# @app.get("/")
# def home( ):
#     return {"message":"welcome to FastAPI"}

# @app.get("/ask")
# def ask_ai(question : str):
#     response = client.responses.create(
#     model = "gpt-5",
#     input = question
#     )
#     return {"answer":response.output_text}

from anthropic import Anthropic
from dotenv import load_dotenv
import os
from fastapi import FastAPI

#want to connect other application like React,Angular,Java,Vuejs,dotnet....etc
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
client=Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
app=FastAPI()

#conneccting the code with other technology
app.add_middleware(CORSMiddleware,allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/")
def home():
    return {"mesage":"Welcome FATAPI"}

@app.get("/ask")
def ask_ai(question:str):
    response=client.messages.create(
        model="claude-opus-4-8",
        max_tokens=500,
        messages=[{"role":"user","content":question}]
    )
    answer=next((block.text for block in response.content if block.type=="text"),"")
    return {"answer":answer}

