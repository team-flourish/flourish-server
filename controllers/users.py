
users = [
    {'id': 1, 'username': 'Zelda', 'email': 'Zelda@gmail.com', 'password': 'FDSFDSFDS', 'rating': 4.5, 'num_of_rating': 2, 'location': "CR4 9TT", 'radius': 1.3 },
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
        raise BadRequest(f"We don't have that user with id {uid}!")

def createRating(req, uid):
    user = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        rating[key] = val
    return rating, 200

def get_products(req, uid):
    user = find_by_uid(uid)
    return user, 200


def update_radius(req, uid):
    user = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        radius[key] = val
    return radius, 200





