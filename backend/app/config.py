import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

class Config:
    """
    Clase de configuración principal para la aplicación Flask.

    Esta clase define los parámetros clave utilizados durante la ejecución, como:
    - La URI de conexión a la base de datos
    - La clave de autenticación para el proveedor de LLMs (Fireworks)
    - Opciones adicionales de SQLAlchemy

    Las variables se pueden definir externamente en un archivo .env para mantener
    el código desacoplado de información sensible.
    """

    # URI para conectar a la base de datos (por defecto usa SQLite local)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///problems.db')

    # Desactiva el sistema de seguimiento de modificaciones de objetos de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave de API para acceder a los modelos de lenguaje de Fireworks.ai
    FIREWORKS_API_KEY = os.getenv('FIREWORKS_API_KEY', '')

    # (Opcional) Aquí podrían añadirse otras configuraciones, como logging, CORS, etc.
