from langchain_google_genai import ChatGoogleGenerativeAI
from configs.config import get_google_api_key

def get_gemini_llm(model_name="gemini-2.0-flash", temperature=0):
    api_key = get_google_api_key()
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        api_key=api_key,
        temperature=temperature
    )
    return llm


