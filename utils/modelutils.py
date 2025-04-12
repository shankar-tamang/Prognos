import os
from dotenv import load_dotenv
import google.generativeai as genai



class ModelIO():
    def __init__(self, model_name="gemini-2.0-flash"):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")
        genai.configure(api_key=api_key)
        self.model_name=model_name
        self.model = genai.GenerationConfig(model_name)

    def generate(self, prompt):
        try:
            response = self.model.generate_response(prompt)
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None