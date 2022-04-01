from werkzeug import exceptions

users = [
    {'id': 1, 'username': 'Zelda', 'email': 'Zelda@gmail.com', 'password': 'FDSFDSFDS', 'rating': 4.5, 'num_of_rating': 2, 'location': "BN9 9TT", 'radius': 1.3, 'rating': 0 },
    {'id': 2, 'username': 'Zelda2', 'email': 'Zeldaaaaa@gmail.com', 'password': 'ABCDEF', 'rating': 4.5, 'num_of_rating': 2, 'location': "BN9 9TT", 'radius': 1.3, 'rating': 0 },
]

products = [
    { "user_id": 1, "description": 'Chicken', "category_id": 1, "is_retail": True, "location":'CR4 9TT', 
    "price": 2.99, "expiry": '10/04/22', "image": 'IMAGE-LINK'},
]

categories = [
    {"category_name": 'Meat'},
    {"category_name": 'Veg'},
]

def get_products(req, id):
    try:
        return (products)
    except:
        raise exceptions.BadRequest(f"We don't have any products at the moment!")
    
