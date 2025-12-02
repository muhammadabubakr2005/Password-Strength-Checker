import requests

response = requests.post(
    "http://127.0.0.1:8000/check",
    json={"password": "Password2005."}
)

print(response.json())