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

load_dotenv()

# Ensure your API Key is set in your environment variables or pass it here
client = genai.Client(api_key=os.getenv("API_KEY"))

# 1. Upload the file
# Note: Ensure the path to your image is correct relative to this script
my_file = client.files.upload(path="Strawberries-Header-OG.jpg") 

# 2. Generate content
# We pass the file object directly in the list
response = client.models.generate_content(
    model="gemini-2.0-flash-exp", # Using the latest 2.0 Flash for best results
    contents=[my_file, "Caption this image."]
)

print(response.text)