import os
from dotenv import load_dotenv

# Load .env from backend directory or project root
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if not load_dotenv(dotenv_path):
    load_dotenv() # Fallback to default search

from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.chatbot import rag_answer

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply = rag_answer(req.message)
    return {"reply": reply}
