import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///problems.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FIREWORKS_API_KEY = os.getenv('FIREWORKS_API_KEY', '')
    # Opcionales: settings de logging, CORS, etc.
# backend/app/config.py
