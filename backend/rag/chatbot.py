from backend.rag.retriever import get_retriever
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def rag_answer(question: str):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    Answer the question using ONLY the context below.
    If answer is not in context, say: "I don't know."

    Context:
    {context}

    Question:
    {question}
    """

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
