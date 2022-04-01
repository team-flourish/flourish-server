from werkzeug import exceptions

users = [
    {'id': 1, 'username': 'Zelda', 'email': 'Zelda@gmail.com', 'password': 'FDSFDSFDS', 'rating': 4.5, 'num_of_rating': 2, 'location': "BN9 9TT", 'radius': 1.3, 'rating': 0 },
    {'id': 2, 'username': 'Zelda2', 'email': 'Zeldaaaaa@gmail.com', 'password': 'ABCDEF', 'rating': 4.5, 'num_of_rating': 2, 'location': "BN9 9TT", 'radius': 1.3, 'rating': 0 },
]

products = [
    { "user_id": 1, "description": 'Chicken', "category_id": 1, "is_retail": True, "location":'CR4 9TT', 
    "price": 2.99, "expiry": '10/04/22', "image": 'IMAGE-LINK'},
]

def show_user_details(req, uid):
    return find_by_uid(uid), 200

def destroy_user(req, uid):
    user = find_by_uid(uid)
    users.remove(user)
    return user, 204

def find_by_uid(uid):
    try:
        return next(user for user in users if user['id'] == uid)
    except:
        raise exceptions.BadRequest(f"We don't have that user with id {uid}!")

def find_product_by_uid(uid):
    try:
        return next(product for product in products if product['user_id'] == uid)
    except:
        raise exceptions.BadRequest(f"We don't have any product with user {uid}!")

def createRating(req, uid):
    user = find_by_uid(uid)
    req = req.get_json()
    user['rating'] = req['rating']
    return user, 200

def get_products(req, uid):
    product = find_product_by_uid(uid)
    return product, 200


def update_radius(req, uid):
    user = find_by_uid(uid)
    req = req.get_json()
    user['radius'] = req['radius']
    return user, 200





