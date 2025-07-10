from . import db
from datetime import datetime

class Problem(db.Model):
    """
    Modelo que representa un problema académico en la base de datos.

    Cada instancia corresponde a una pregunta o ejercicio que puede ser evaluado
    automáticamente. Contiene metadatos relevantes como el tema, tipo de pregunta,
    solución esperada, créditos asignados y criterios de evaluación.

    Atributos:
        id (int): Identificador único del problema.
        titulo (str): Título breve del problema.
        enunciado (str): Descripción completa o pregunta que ve el estudiante.
        solucion (str): Solución esperada que será usada como referencia.
        tema (str): Tema académico al que pertenece (ej. Lógica, Álgebra...).
        tipo (str): Tipo de pregunta (abierta, opción múltiple, V/F...).
        creditos (int): Cantidad de créditos asignados al problema.
        criterio (str): Criterio bajo el cual se debe evaluar (ej. exactitud, claridad).
    """
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True) 
    titulo  = db.Column(db.Text, nullable=False)
    enunciado = db.Column(db.Text, nullable=False)
    solucion  = db.Column(db.Text, nullable=False)
    tema = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    creditos = db.Column(db.Integer, nullable=False)
    criterio  = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """
        Retorna una representación legible del objeto Problem.

        Returns:
            str: Representación en formato "<Problem #ID: titulo:..., tema:..., tipo:...>"
        """
        return f"<Problem #{self.id}: titulo:{self.titulo}\n tema:{self.tema} tipo:{self.tipo}>"