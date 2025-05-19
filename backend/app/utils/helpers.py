# backend/app/utils/helpers.py
import re

def normalize_text(text: str) -> str:
    """
    Normaliza el texto para comparaciones:
    - Pasa a minúsculas
    - Elimina espacios extra
    - Quita puntuación innecesaria
    """
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[.,;:!?’'\"]", "", text)
    return text