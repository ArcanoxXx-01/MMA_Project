import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('FIREWORKS_API_KEY')

url = "https://api.fireworks.ai/inference/v1/chat/completions"
payload = {
  "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
  "max_tokens": 10,
  "top_p": 1,
  "top_k": 40,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "temperature": 0.6,
  "messages": [
    {
      "role": "user",
      "content": "Hola, que tal?"
    }
  ]
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}
response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)