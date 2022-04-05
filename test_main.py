from flourish_app import create_app
import json

def test_index(client):
    response = client.get("/")
    assert  response.status == "200 OK"
    assert response.data == b"Hello World!"

def test_getAllProducts(client):
    mock_data = json.dumps(
        {
        "category_id": 2,
        "date_time": "Tue, 05 Apr 2022 00:00:00 GMT",
        "description": 'Tomatoes',
        "expiry": "03/04/2022",
        "image": "LINK",
        "is_retail": 1,
        "location": "SE18",
        "price": 2.99,
        #"product_id": 1,
        "user_id": 1
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/products', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'
    res = client.get("/products")
    assert res.status == '200 OK'
    #assert len(res.json) == 14
    assert res.json[1]['description'] == 'Carrots'

def test_getProductById(client):

    res = client.get("/products/1")
    assert res.status == '200 OK'
    assert len(res.json) == 1
    assert res.json[0]['description'] == 'Tomatoes'

def test_getProductByCategoryId(client):
    res = client.get("/products/category/2")
    assert res.status == '200 OK'
    assert res.json[1]['description'] == 'Carrots'

def test_getAllUsers(client):
    res = client.get("/users")
    assert res.status == '200 OK'
    assert res.json[0]['email'] == 'zahra@email.co.uk'

def test_getAllUsersProductsById(client):
    res = client.get("/users/1/products")
    assert res.status == '200 OK'   
    assert res.json[0]['expiry'] == '03/04/2022'

def test_handleUserById(client):
    res = client.get("/users/1")
    assert res.status == '200 OK'  
    assert res.json[0]['location'] == 'BN9'

    res = client.delete("/users/5")
    assert res.status == '204 NO CONTENT'  

def test_vote(client):
    mock_data = json.dumps(
        {    
            "product_id": 1,
            "user_id": 1,
            "rating": 4.0
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/rating/vote', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'


def test_getAllRatings(client):
    res = client.get("/ratings")
    assert res.status == '200 OK'  
    assert res.json[0]['rating'] == 4

def test_getRatingByUserId(client):
    res = client.get("/ratings/users/1")
    assert res.status == '200 OK'  
    assert res.json[0]['rating'] == 4

def test_getRatingById(client):
    res = client.get("/ratings/users/1/products/1")
    assert res.status == '200 OK'  
    assert res.json[0]['rating'] == 4

def test_updateLocation(client):
    mock_data = json.dumps(
        {
        "updated_location": "BN9"
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.patch('/users/1/location', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'

def test_updateRadius(client):
    mock_data = json.dumps(
        {
        "updated_radius": 3.0
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.patch('/users/1/radius', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'



