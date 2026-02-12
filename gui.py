import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Gemini 2.5 Medical Analyst")
        self.geometry("600x500")
        
        # Initialize Gemini Client
        self.client = genai.Client(api_key=os.getenv("API_KEY"))
        self.selected_file_path = None

        # --- UI Elements ---
        self.label = ctk.CTkLabel(self, text="Upload an image for medical analysis", font=("Arial", 16))
        self.label.pack(pady=20)

        self.upload_btn = ctk.CTkButton(self, text="Select Image", command=self.select_file)
        self.upload_btn.pack(pady=10)

        self.analyze_btn = ctk.CTkButton(self, text="Run Analysis", command=self.run_analysis, state="disabled")
        self.analyze_btn.pack(pady=10)

        self.result_text = ctk.CTkTextbox(self, width=500, height=200, wrap="word")
        self.result_text.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.selected_file_path = file_path
            self.label.configure(text=f"Selected: {os.path.basename(file_path)}")
            self.analyze_btn.configure(state="normal")

    def run_analysis(self):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("insert", "Analyzing... please wait medical professional.")
        
        # We update the UI to show it's working
        self.update_idletasks()

        try:
            # 1. Upload the file
            my_file = self.client.files.upload(file=self.selected_file_path)

            # 2. Generate content (using your specific prompt)
            prompt = ("Describe the food in this image in a single paragraph while speaking like a medical professional. "
                      "If the food is an apple, only state that the apple is delicious. "
                      "If the image doesn't include food, refuse to give any information about the image in a flabberghasted manner. "
                      "Otherwise, use medical jargon and technical scientific terms such as vitamins, antioxidants, and phytochemicals.")

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[my_file, prompt]
            )

            self.result_text.delete("1.0", "end")
            self.result_text.insert("insert", response.text)
            
        except Exception as e:
            self.result_text.insert("insert", f"Error: {str(e)}")

if __name__ == "__main__":
    app = GeminiApp()
    app.mainloop()