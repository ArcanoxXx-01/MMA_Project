# backend/tests/test_problems.py
import pytest
from app import create_app
from app.models import db, Problem

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_and_list(client):
    # Crear un problema
    res = client.post('/api/problems', json={
        'tema': 'optimización',
        'tipo': 'VF',
        'solucion': 'True',
        'criterio': 'estricto'
    })
    assert res.status_code == 201

    # Listar problemas
    res = client.get('/api/problems')
    data = res.get_json()
    assert len(data) == 1
    assert data[0]['tema'] == 'optimización'