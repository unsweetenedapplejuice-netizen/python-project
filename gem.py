#import google.generativeai as genai
#import os
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()

# Configure the API
#genai.configure(api_key=os.getenv('API_KEY'))

# System message to define the persona
#pirate_instructions = "You are a pirate chatbot. Respond only in pirate speak, using pirate slang and nautical terms. Do not reply in normal English."

# Initialize the model with system instructions
#model = genai.GenerativeModel(
#    model_name="gemini-3-flash-preview",
#    system_instruction=pirate_instructions
#)

#def start_chat():
    # Start a chat session to maintain context (optional but recommended)
#    chat_session = model.start_chat(history=[])
    
#    print("Ahoy! The salty dog is ready to chat. (Type 'exit' to abandon ship)")
    
#    while True:
#        user_input = input("You: ")
        
#        if user_input.lower() == 'exit':
#            print("Fair winds and following seas, matey!")
#            break
        
#        try:
            # Send message to the model
#            response = chat_session.send_message(user_input)
#            print(f"\nPirate: {response.text}\n")
#        except Exception as e:
#            print(f"Blimey! An error occurred: {e}")

#if __name__ == "__main__":
#    start_chat()

#from google import genai
import google.genai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Ensure your API Key is set in your environment variables or pass it here
client = genai.Client(api_key=os.getenv("API_KEY"))
#for m in client.models.list():
    # Only show models that support generating content
#    if 'generateContent' in m.supported_actions:
#        print(m.name)
file_path = input("Drag and drop your image here and press Enter: ").strip("'\" ")

try:
    with Image.open(file_path) as img:
        print(f"Successfully loaded {file_path}!")
        print(f"Format: {img.format}, Size: {img.size}")
except Exception as e:
    print(f"Could not read the image: {e}")
# 1. Upload the file
# Note: Ensure the path to your image is correct relative to this script
my_file = client.files.upload(file=file_path) 

# 2. Generate content
# We pass the file object directly in the list
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Describe the food in this image in a single paragraph while speaking like a medical professional. If the food is an apple, only state that the apple is delicious. If the image doesn't include food, refuse to give any information about the image in a flabberghasted manner. Otherwise, use medical jargon and technical scientific terms such as vitamins, antioxidants, and phytochemicals to describe the food in this image. Make sure to go over what is in the food. Do not speak in normal english." ]
)
print(response.text)
#next goal: set up means of user input into terminal so that user can upload their own images to get descriptions