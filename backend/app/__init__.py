from flask import Flask
from .models import db
from app.routes import problem_routes
from app.config import Config
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(problem_routes.bp, url_prefix='/api')
    return app
    