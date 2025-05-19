<!-- backend/README.md -->
# Backend Flask para Evaluación Automática

Esta aplicación provee endpoints para gestionar problemas académicos y evaluarlos automáticamente usando LLMs a través de fireworks.ai.

## Estructura
- `app/models`: modelos de la base de datos
- `app/llm`: cliente genérico y específico para LLM
- `app/services`: lógica de evaluación
- `app/routes`: endpoints REST
- `app/utils`: helpers

## Uso
1. Configura `.env` con `DATABASE_URI` y `FIREWORKS_API_KEY`.
2. Instala dependencias: `pip install -r requirements.txt`.
3. Corre la app: `python run.py`.
4. Usa `/api/problems` y `/api/evaluate/<id>`.