import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b'Welcome to the Cognitive Test' in rv.data

def test_test_page(client):
    rv = client.get('/test')
    assert rv.status_code == 200
