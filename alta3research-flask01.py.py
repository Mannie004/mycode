from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os #to pinpoint where database is setup

# Initialize app with flask
app = Flask(__name__)

# Set up alchemy db
basedir = os.path.abspath(os.path.dirname(__file__))

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite: ////home/student/mycode/db.sqlite' #sqlite: **///' + os.path.join(basedir, 'db.sqlite
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
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True) #many indicates we are dealing with more than one product

# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({'msg': 'Hello World'})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)