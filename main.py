from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(message: Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.prompt}]
    )
    return {"response": response.choices[0].message["content"]}
