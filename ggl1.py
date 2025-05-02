from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
load_dotenv()
api_key = os.getenv("GGL_API_KEY")


model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
resp=model.invoke("who is Jesus Christ?")
print(resp)

