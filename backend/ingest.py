import os
from dotenv import load_dotenv
from backend.rag.loader import load_pdf

load_dotenv("backend/.env")
from backend.rag.chunker import chunk_docs
from backend.rag.vectorstore import create_vectorstore

docs = load_pdf("backend/data/sample.pdf")
chunks = chunk_docs(docs)
create_vectorstore(chunks)

print("PDF added to vector DB successfully")
