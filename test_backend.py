import requests

try:
    res = requests.post("http://127.0.0.1:8000/chat", json={"message": "What is in the sample document?"})
    print(f"Status Code: {res.status_code}")
    print(f"Response: {res.json()}")
except Exception as e:
    print(f"Error: {e}")
    if 'res' in locals():
        print(f"Raw Response: {res.text}")
