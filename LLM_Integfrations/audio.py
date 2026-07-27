from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
prompt = input("Enter text to generate audio:")
#guru brahma guru vishnu guru devo maheswara guru sakshakth para brahma tasmai shri gurave namaha
with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input = prompt,
) as response:
    response.stream_to_file("output.mp3")
    print("Audio Generated Successfully!!")