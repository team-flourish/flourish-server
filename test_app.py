from flourish_app import create_app

def test_index(client):
    response = client.get("/")
    assert response.data == b"Hello World!"

