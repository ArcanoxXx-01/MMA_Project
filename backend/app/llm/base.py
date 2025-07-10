import abc
from typing import Any, Dict

class BaseLLM(abc.ABC):
    """
    Clase base abstracta para modelos de lenguaje (LLM).

    Define la interfaz que deben implementar todos los modelos concretos, ya sea Fireworks,
    OpenAI, Cohere, etc. Establece métodos abstractos para generar y evaluar respuestas.
    """

    def __init__(self, api_key: str):
        """
        Inicializa la clase base con una clave de API.

        Args:
            api_key (str): Clave de autenticación para el proveedor del modelo de lenguaje.
        """
        self.api_key = api_key

    @abc.abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Genera una respuesta textual a partir de un prompt.

        Este método debe ser implementado por cualquier clase derivada.

        Args:
            prompt (str): Texto de entrada.
            **kwargs: Parámetros adicionales según el modelo (ej. temperatura, tokens...).

        Returns:
            str: Respuesta generada por el modelo.
        """
        pass

    @abc.abstractmethod
    def evaluate(self, prompt: str, reference: str, **kwargs) -> Dict[str, Any]:
        """
        Evalúa una respuesta generada a partir de un prompt y una referencia.

        Este método debe ser implementado por cualquier clase derivada.

        Args:
            prompt (str): Prompt con información sobre la pregunta/respuesta.
            reference (str): Texto de referencia o solución esperada.
            **kwargs: Parámetros adicionales según el modelo.

        Returns:
            Dict[str, Any]: Diccionario con resultados de evaluación (razonamiento, score, etc).
        """
        pass
