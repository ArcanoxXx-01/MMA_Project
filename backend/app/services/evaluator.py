from flask import current_app
from app.llm.fireworks_models import FireworksModel
from app.llm.prompts import EVALUATION_TEMPLATE, DEFAULT_PARAMS

class EvaluatorService:
    """
    Servicio encargado de evaluar respuestas estudiantiles usando un modelo de lenguaje (LLM).

    Este servicio utiliza un modelo Fireworks configurado a través de la clave API definida en la
    aplicación Flask. Se encarga de construir el prompt de evaluación, invocar el modelo y procesar la salida.
    """
    
    def __init__(self):
        """
        Inicializa el servicio de evaluación.

        Obtiene la clave de API desde la configuración de Flask y crea una instancia del modelo Fireworks.
        """
        api_key = current_app.config['FIREWORKS_API_KEY']
        self.llm = FireworksModel(api_key)

    def evaluate(self, problema, respuesta_est):
        """
        Evalúa una respuesta del estudiante.

        Args:
            problema (Problem): Instancia del problema a evaluar.
            respuesta_est (str): Respuesta del estudiante.

        Returns:
            dict: Contiene el razonamiento y la evaluación generada por el modelo.
        """
        prompt = EVALUATION_TEMPLATE.format(
            tema=problema.tema,
            tipo=problema.tipo,
            enunciado=problema.enunciado,
            respuesta=respuesta_est,
            solucion=problema.solucion,
            criterio=problema.criterio
        )

        razonamiento = self.llm.generate(prompt, **DEFAULT_PARAMS)
        evaluacion = self.llm.evaluate(prompt, problema.solucion, razonamiento=razonamiento, **DEFAULT_PARAMS)

        return {
            'razonamiento': razonamiento,
            'evaluacion': evaluacion
        }