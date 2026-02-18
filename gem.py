import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure your API Key is set in your environment variables or pass it here
client = genai.Client(api_key=os.getenv("API_KEY"))

# 1. Upload the file
# Note: Ensure the path to your image is correct relative to this script
my_file = client.files.upload(file="Strawberries-Header-OG.jpg") 

# 2. Generate content
# We pass the file object directly in the list
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Describe the food in this image in a single paragraph while speaking like a medical professional. If the food is an apple, only state that the apple is delicious. If the image doesn't include food, refuse to give any information about the image in a flabberghasted manner. Otherwise, use medical jargon and technical scientific terms such as vitamins, antioxidants, and phytochemicals to describe the food in this image. Make sure to go over what is in the food. Do not speak in normal english." ]
)
print(response.text)