import pytest

from route import combat_bp
from flask import Flask
from app import create_app

# Import the testing ability of python 
@pytest.fixture

def client():
    """A function called client that associates app with the create_app() function"""
    app = create_app()
    
    with app.app_context():
        with app.test_client() as client:
            yield client

def test_status(client):
    """Tests that the status code of the of the endpoint returns OK"""
    response = client.get('/endpoint')
    assert response.status_code == 200

