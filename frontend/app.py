import streamlit as st
import requests

st.title("RAG Chatbot")

msg = st.text_input("Ask a question:")

if st.button("Send"):
    try:
        res = requests.post("http://127.0.0.1:8000/chat", json={"message": msg})
        res.raise_for_status() # Check for HTTP errors
        st.write(res.json()["reply"])
    except requests.exceptions.HTTPError as e:
        st.error(f"Backend error: {e}")
    except requests.exceptions.JSONDecodeError:
        st.error("Failed to decode response from backend. Raw response:")
        st.code(res.text)
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
