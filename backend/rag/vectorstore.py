from langchain_chroma import Chroma
from backend.rag.embeddings import get_embeddings

def create_vectorstore(chunks, persist_dir="db"):
    embeddings = get_embeddings()
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    # Note: langchain-chroma persists automatically or doesn't need explicit persist()
    return vectordb

def load_vectorstore(persist_dir="db"):
    embeddings = get_embeddings()
    return Chroma(persist_directory=persist_dir, embedding_function=embeddings)
