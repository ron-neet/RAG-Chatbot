from backend.rag.vectorstore import load_vectorstore

def get_retriever():
    vectordb = load_vectorstore()
    return vectordb.as_retriever(search_kwargs={"k": 3})
