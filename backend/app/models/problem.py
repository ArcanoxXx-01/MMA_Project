from . import db
from datetime import datetime

class Problem(db.Model):
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
        return f"<Problem #{self.id}: titulo:{self.titulo}\n tema:{self.tema} tipo:{self.tipo}>"