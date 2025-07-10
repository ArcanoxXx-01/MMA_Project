from flask import Flask
from .models import db
from app.routes import problem_routes
from app.config import Config
from flask_cors import CORS

def create_app():
    """
    Crea e inicializa una instancia de la aplicación Flask.

    Configura la aplicación con:
    - CORS habilitado para rutas que comiencen con /api/*
    - Configuración general desde el objeto Config
    - Inicialización de la base de datos SQLAlchemy
    - Creación de tablas en la base de datos
    - Registro del Blueprint de rutas relacionadas con problemas académicos

    Returns:
        Flask: Instancia configurada de la aplicación.
    """
    app = Flask(__name__)
    
    # Permite CORS para el frontend u otras apps externas
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Carga la configuración (por ejemplo, clave API, URI de la base de datos, etc.)
    app.config.from_object(Config)

    # Inicializa SQLAlchemy con la app
    db.init_app(app)

    # Crea las tablas si no existen aún
    with app.app_context():
        db.create_all()

    # Registra el blueprint de rutas de problemas con prefijo /api
    app.register_blueprint(problem_routes.bp, url_prefix='/api')

    return app
