from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os #to pinpoint where database is setup

# Initialize app with flask
app = Flask(__name__)

# Set up alchemy db
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #stop the console from complaining

# Initialize Database
db = SQLAlchemy(app)
#Initialize marshmallow
ma = Marshmallow(app)

# Product Class/Model (Model gives predefined methods)
class Product(db.Model) :
    #Add fields
    id = db.Column(db.Integer, primary_key=True) #Autoincrements by default
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True) #many indicates we are dealing with more than one product

#Create a product
@app.route('/product', methods= ['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty) #product class taking params

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product) #new_product is returned to client


# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  print(result)
  return jsonify(result)
  

# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({'msg': 'Hello World'})

# Get a product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

#Update a product
@app.route('/product/<id>', methods= ['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit

    return product_schema.jsonify(product)


# Run the server
if __name__ == '__main__':
    app.run(debug=True)