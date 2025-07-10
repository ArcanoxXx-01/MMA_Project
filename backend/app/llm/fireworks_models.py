import requests
from .base import BaseLLM
from typing import Any, Dict, Optional

class FireworksModel(BaseLLM):
    """
    Implementación concreta de un modelo de lenguaje basado en Fireworks.ai.

    Esta clase hereda de BaseLLM y utiliza la API de Fireworks para generar y evaluar
    respuestas a partir de prompts en lenguaje natural.
    """
    def __init__(self, api_key: str, model: str = "accounts/fireworks/models/llama-v3p1-8b-instruct"):
        """
        Inicializa una instancia del modelo Fireworks.

        Args:
            api_key (str): Clave de API para autenticar con Fireworks.ai.
            model (str): Nombre o ruta del modelo Fireworks a utilizar.
        """
        super().__init__(api_key)
        self.model = model
        self.api_url = "https://api.fireworks.ai/inference/v1/chat/completions"

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Genera una respuesta textual a partir de un prompt utilizando el modelo Fireworks.

        Args:
            prompt (str): Texto de entrada que describe la tarea o pregunta.
            **kwargs: Parámetros adicionales compatibles con la API (por ejemplo, temperatura, max_tokens...).

        Returns:
            str: Respuesta generada por el modelo.
        """
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


    def evaluate(self, prompt: str, reference: str, razonamiento: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Evalúa una respuesta generando o utilizando un razonamiento previo.

        Args:
            prompt (str): Prompt usado para generar la evaluación.
            reference (str): Solución esperada (no se usa en este modelo).
            razonamiento (str, optional): Si ya se generó el razonamiento, se puede reutilizar.
            **kwargs: Parámetros adicionales para el modelo.

        Returns:
            Dict[str, Any]: Resultado con razonamiento y metadatos de evaluación.
        """
        if razonamiento is None:
            razonamiento = self.generate(prompt, **kwargs)

        return {
            "razonamiento": razonamiento,
            "score": None,
            "nota": "Evaluación generada con modelo instructivo"
        }