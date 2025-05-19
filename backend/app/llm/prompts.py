# backend/app/llm/prompts.py
EVALUATION_TEMPLATE = """
Eres un asistente experto en el área de {tema} y en evaluación académica universitaria.

Tu tarea es analizar la respuesta de un estudiante a una pregunta de tipo {tipo}, comparándola con la solución esperada. Debes aplicar el siguiente criterio de evaluación:

CRITERIO DE EVALUACIÓN: {criterio}

A continuación se presentan los elementos relevantes:

---
🧩 ENUNCIADO DE LA PREGUNTA:
{enunciado}

✅ SOLUCIÓN ESPERADA:
{solucion}

📝 RESPUESTA DEL ESTUDIANTE:
{respuesta}
---

🔍 PASO 1 — ANÁLISIS:
Explica detalladamente si la respuesta del estudiante es correcta, incorrecta o parcialmente correcta. Justifica en qué coincide o difiere con la solución esperada, y si cumple con el criterio de evaluación.

📊 PASO 2 — EVALUACIÓN FINAL:
Proporciona una puntuación del 0 al 100 y una breve justificación. La puntuación debe reflejar el grado de cumplimiento con la solución y el criterio indicado.
"""

DEFAULT_PARAMS = {
    'temperature': 0.2,
    'max_tokens': 500
}