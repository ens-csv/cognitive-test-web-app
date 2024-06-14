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

def test_submit_answers(client):
    rv = client.post('/test', data={
        'q1': 'C',
        'q2': 'A',
        'q3': 'B',
        'q4': 'C'
    })
    assert b'You scored 4 out of 4.' in rv.data

def test_submit_wrong_answers(client):
    rv = client.post('/test', data={
        'q1': 'A',
        'q2': 'B',
        'q3': 'C',
        'q4': 'D'
    })
    assert b'You scored 0 out of 4.' in rv.data
