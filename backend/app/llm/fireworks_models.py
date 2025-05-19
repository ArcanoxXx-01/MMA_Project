# backend/app/llm/fireworks_model.py
import requests
from .base import BaseLLM
from typing import Any, Dict

class FireworksModel(BaseLLM):
    def __init__(self, api_key: str, model: str = "accounts/fireworks/models/llama-v3p1-8b-instruct"):
        super().__init__(api_key)
        self.model = model
        self.api_url = "https://api.fireworks.ai/inference/v1/chat/completions"

    def generate(self, prompt: str, **kwargs) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            **kwargs
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(self.api_url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

    def evaluate(self, prompt: str, reference: str, **kwargs) -> Dict[str, Any]:
        razonamiento = self.generate(prompt, **kwargs)
        return {
            "razonamiento": razonamiento,
            "score": None,
            "nota": "Evaluación generada con modelo instructivo"
        }