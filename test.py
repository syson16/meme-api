import pytest
from main import create_app

@pytest.fixture()
def app():
    app = create_app()
    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_example(client):
    response = client.get("/")
    assert b"<p>Hello, World!</p>" in response.data

def test_json_data(client):
    response = client.get("/memes")
    assert response.json["token"] == "dummy-token-1" and response.json["remaining-calls"] == 9

def test_json_data_second_call(client):
    client.get("/memes")
    response2 = client.get("/memes")
    assert response2.json["token"] == "dummy-token-1" and response2.json["remaining-calls"] == 8