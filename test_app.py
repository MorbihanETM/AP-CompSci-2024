
import pytest

from route import combat_bp
from flask import Flask
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.register_blueprint(combat_bp, url_prefix='/endpoint')
    # app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_status(client):
    response = client.get('/endpoint')
    assert response.status_code == 200

