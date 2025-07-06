import abc
from typing import Any, Dict

class BaseLLM(abc.ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abc.abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

    @abc.abstractmethod
    def evaluate(self, prompt: str, reference: str, **kwargs) -> Dict[str, Any]:
        pass
