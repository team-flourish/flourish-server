from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug import exceptions

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


@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':

        try: 
            allProducts = Products.query.all()
            return jsonify(allProducts), 200

        except exceptions.NotFound:
            raise exceptions.NotFound("There are no products in the database currently!")

        except:
            raise exceptions.InternalServerError()


    elif request.method == 'POST':
    # format of request { description, category_id, is_retail, location, price, expiry, image} 
    # { "user_id": 1, "description": "Tomatoes", "category_id": 2, "is_retail": "True", "location": "SE18", 
    # "price": 2.99, "expiry": "02/04/2022", "image": "LINK"}
        
        req = request.json
        try:
            new_product = Products(
                user_id = req.user_id, 
                description = req.description, 
                category_id = req.category_id,
                is_retail = req.is_retail, 
                location = req.location, 
                price = req.price, 
                expiry = req.expiry, 
                image = req.image
            )

            db.session.add(new_product)
            db.session.commit()
            return f"New product was added!", 201

        except: 
            raise exceptions.InternalServerError()
