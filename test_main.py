from flourish_app import create_app
import json

def test_index(client):
    response = client.get("/")
    assert  response.status == "200 OK"
    assert response.data == b"Hello World!"

def test_getAllProducts(client):
    res = client.get("/products")
    assert res.status == '200 OK'
    assert len(res.json) == 3
    assert res.json[2]['description'] == 'Onion'

def test_getProductById(client):
    res = client.get("/products/1")
    assert res.status == '200 OK'
    assert len(res.json) == 1
    assert res.json[0]['description'] == 'Tomatoes'

def test_getProductByCategoryId(client):
    res = client.get("/products/category/2")
    assert res.status == '200 OK'
    assert len(res.json) == 3
    assert res.json[1]['description'] == 'Broccoli'

def test_getAllUsers(client):
    res = client.get("/users")
    assert res.status == '200 OK'
    assert len(res.json) == 4
    assert res.json[1]['email'] == 'test2@email.co.uk'

def test_getAllUsersProductsById(client):
    res = client.get("/users/3/products")
    assert res.status == '200 OK'
    assert len(res.json) == 2    
    assert res.json[1]['expiry'] == '03/04/2022'

def test_handleUserById(client):
    res = client.get("/users/3")
    assert res.status == '200 OK'
    assert len(res.json) == 1    
    assert res.json[0]['location'] == 'SE18'


def test_getAllRatings(client):
    res = client.get("/ratings")
    assert res.status == '200 OK'
    assert len(res.json) == 1    
    assert res.json[0]['rating'] == 1
