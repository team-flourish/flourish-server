from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug import exceptions
from controllers import users

app = Flask(__name__)
CORS(app)

# database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# database model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(100))
    password = db.Column(db.String(25))
    rating = db.Column(db.Float)
    num_of_rating = db.Column(db.Integer)
    location = db.Column(db.String(7))
    radius = db.Column(db.Float)

class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    is_Retail = db.Column(db.Boolean)
    location = db.Column(db.String(7))
    price = db.Column(db.Float)
    expiry = db.Column(db.String(15))
    description = db.Column(db.String(100))
    image = db.Column(db.String(500))

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name  = db.Column(db.String(100))

@app.get('/')
def index():
  return 'Hello, world!'

@app.route('/users/<int:user_id>/rating', methods=['POST'])
def rating_handler(user_id):
    fns = {
        'POST': users.createRating
    }
    resp, code = fns[request.method](request, user_id)
    return jsonify(resp), code

@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def user_handler(user_id):
    fns = {
        'GET': users.show_user_details,
        'DELETE': users.destroy_user
    }
    resp, code = fns[request.method](request, user_id)
    return jsonify(resp), code

@app.route('/users/<int:user_id>/location', methods=['PATCH'])
def location_handler(user_id):
    fns = {
        'PATCH': users.update_location,
    }
    resp, code = fns[request.method](request, user_id)
    return jsonify(resp), code

@app.route('/users/<int:user_id>/product', methods=['GET'])
def product_handler(user_id):
    fns = {
        'GET': users.get_products,
    }
    resp, code = fns[request.method](request, user_id)
    return jsonify(resp), code

@app.route('/users/<int:user_id>/radius', methods=['PATCH'])
def radius_handler(user_id):
    fns = {
        'PATCH': users.update_radius,
    }
    resp, code = fns[request.method](request, user_id)
    return jsonify(resp), code

# boiler plate
if __name__ == "__main__":
    app.run(debug=True)
