from flourish_app import create_app

def test_index(client):
    response = client.get("/")
    assert  response.status == "200 OK"
    assert response.data == b"Hello World!"

