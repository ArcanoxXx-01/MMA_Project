# backend/app/services/evaluator.py
from flask import current_app
from app.llm.fireworks_models import FireworksModel
from app.llm.prompts import EVALUATION_TEMPLATE, DEFAULT_PARAMS

class EvaluatorService:
    def __init__(self):
        api_key = current_app.config['FIREWORKS_API_KEY']
        self.llm = FireworksModel(api_key)

    def evaluate(self, problema, respuesta_est):
        prompt = EVALUATION_TEMPLATE.format(
            tema=problema.tema,
            tipo=problema.tipo,
            enunciado=problema.enunciado,
            respuesta=respuesta_est,
            solucion=problema.solucion,
            criterio=problema.criterio
        )
        razonamiento = self.llm.generate(prompt, **DEFAULT_PARAMS)
        evaluacion = self.llm.evaluate(prompt, problema.solucion, **DEFAULT_PARAMS)
        return {'razonamiento': razonamiento, 'evaluacion': evaluacion}