from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

# Create video generation job
result = client.videos.create(
    model="sora-2",
    prompt="""
          Create a 5-second ultra-realistic cinematic video of a futuristic city at sunrise. 
          A lone person walks confidently through a neon-lit street while flying cars move overhead. 
          The camera starts with a low-angle tracking shot, then smoothly rises to reveal the skyline. 
          Volumetric lighting, realistic reflections on wet roads, subtle fog, dynamic shadows, 4K, HDR, shallow depth of field, highly detailed, natural character movement, movie-quality visuals, 24 fps.
    """
)

video_id = result.id

print(f"Video ID: {video_id}")

# Wait until generation completes
while True:
    status = client.videos.retrieve(video_id)

    print("Current Status:", status.status)

    if status.status == "completed":
        print("Video generation completed.")
        break

    if status.status == "failed":
        print("Video generation failed.")
        exit()

    time.sleep(5)

# Download video AFTER completion
video = client.videos.download_content(video_id)

with open("generated_video.mp4", "wb") as f:
    f.write(video.read())

print("Video downloaded successfully!")