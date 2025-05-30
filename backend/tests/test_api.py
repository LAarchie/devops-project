import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_hello(client):
    res = client.get('/api/hello')
    assert res.get_json() == {"message": "Hello, World!"}

def test_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "healthy"}

def test_log(client):
    message = "Log test message"
    res = client.post('/api/log-test', json={"message": message})
    assert res.status_code == 200
    assert res.get_json() == {"status": "success", "message": message}


def test_log_fail(client):
    res = client.post('/api/log-test', json={})
    assert res.status_code == 400
    assert res.get_json() == {"status": "error", "message": "No message provided"}