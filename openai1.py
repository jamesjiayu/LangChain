from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


model= init_chat_model("gpt-4.1-nano", model_provider="openai")
resp=model.invoke("who is Jesus Christ?")


if __name__ == "__main__":
    print(resp)
    
