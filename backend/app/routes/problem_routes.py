from flask import Blueprint, request, jsonify
from app.models.problem import Problem
from app.models import db
from app.services.evaluator import EvaluatorService

bp = Blueprint('problems', __name__)
"""
Blueprint para manejar rutas relacionadas con problemas académicos.

Incluye endpoints para listar, crear y evaluar problemas usando modelos de lenguaje.
"""

def get_evaluator():
    """
    Crea una instancia del servicio de evaluación.

    Returns:
        EvaluatorService: Servicio para evaluar respuestas estudiantiles.
    """
    return EvaluatorService()

@bp.route('/problems', methods=['GET'])
def list_problems():
    """
    Lista todos los problemas almacenados en la base de datos.

    Returns:
        Response: JSON con una lista de problemas y sus metadatos.
    """
    problemas = Problem.query.all()
    return jsonify([{
        'id': p.id,
        'titulo': p.titulo,
        'enunciado': p.enunciado,
        'creditos': p.creditos,
        'tema': p.tema,
        'tipo': p.tipo,
        'criterio': p.criterio
    } for p in problemas]), 200

@bp.route('/problems', methods=['POST'])
def create_problem():
    """
    Crea un nuevo problema académico a partir de los datos recibidos en formato JSON.

    Requiere los campos: titulo, enunciado, solucion, tema, tipo, creditos, criterio.

    Returns:
        Response: JSON con el ID del nuevo problema creado.
    """
    data = request.json
    p = Problem(
        titulo=data['titulo'],
        enunciado=data['enunciado'],
        solucion=data['solucion'],
        tema=data['tema'],
        tipo=data['tipo'], 
        creditos=data['creditos'],
        criterio=data['criterio']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({'id': p.id}), 201

@bp.route('/evaluate/<int:problem_id>', methods=['POST'])
def evaluate_problem(problem_id):
    """
    Evalúa una respuesta estudiantil para un problema específico.

    Args:
        problem_id (int): ID del problema a evaluar.

    JSON esperado:
        {
            "respuesta": "Texto de la respuesta del estudiante"
        }
        
    Returns:
        Response: JSON con el razonameinto del modelo y una nota (o mensaje de error).
    """
    evaluator = EvaluatorService()
    # 1. Busca el problema en la DB
    problem = Problem.query.get_or_404(problem_id)

    # 2. Toma la respuesta del estudiante 
    data: dict = request.json
    student_answer = data.get('respuesta', '')
    if not student_answer:
        return jsonify({'error': 'Falta el campo "respuesta"'}), 400

    # 3. Llama al servicio de evaluación
    result = evaluator.evaluate(problem, student_answer)

    # 4. Devuelve directamente el JSON con razonamiento y evaluación
    return jsonify(result)
