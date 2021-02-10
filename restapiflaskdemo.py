# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:51:01 2021

@author: SATISHBIRLANGI


app = express()

app.get('',())

ap.post('',())
"""

import json

from flask import Flask,jsonify,request,Response,make_response

from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema

from marshmallow import fields

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:admin@localhost:3306/devops'

db = SQLAlchemy(app)

class Produc(db.Model) :
    __tablename__="pyproducts"
    productId = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(40))
    descriprion = db.Column(db.String(60))
    productCode = db.Column(db.String(40))
   # price = db.Column(db.float)
   # startRating = db.Column(db.float)
    imageUrl = db.Column(db.String(40))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self,productName,descriprion,productCode,price,startRating,imageUrl):
       
        self.productName = productName
        self.descriprion = descriprion
        self.productCode = productCode
        self.price = price
        self.startRating = startRating
        self.imageUrl = imageUrl
    def __repr__(self):
        return "% self.productId"
    
db.create_all()

class  ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model= Product
        sqla_session = db.session
    productId = fields.Number(dump_only=True)
    productName = fields.String(required=True)
    descriprion = fields.String(required=True)
    productCode = fields.String(required=True)    
    price = fields.Number(required=True)
    startRating = fields.Number(required=True)
    imageUrl = fields.String(required=True)
        
@app.route('/products',methods=['POST'])   
def createProduct():
    data = request.get_json()
    Product_schema = ProductSchema()
    Product = Product_schema.load(data)
    result = Product_schema.dump(product.create())
    return make_response(jsonify({"product":result}),201)
app.run(port=4000)

@app.route('/products/<int:productId>',methods=['GET'])   
def getProductId(productId):
    get_product = product.query.get(productId)
    Product_schema = ProductSchema()
    Product = Product_schema.load(data)
    return make_response(jsonify({"product":result}),202)
    
 @app.route('/products/<int:productId>',methods=['DELETE'])   
def getProductId(productId):
    get_product = product.query.get(productId)
    Product_schema = ProductSchema()
    Product = Product_schema.load(data)
    return make_response(jsonify({"product deleted"}),204)  

@app.route('/products/<int:productId>',methods=['PUT'])   
def getProductId(productId):
    get_product = product.query.get(productId)
    if data.get('price'):
        get_product.price = data['price']
    result = Product_schema.dump(get_products
    return make_response(jsonify({"product":result}),201)   
    


@app.route('/products/find/<productNmae>',methods=['GET'])   
def getProductId(productName):
    get_product = product.query.filter_by(productName=productName)
    ProductSchema = ProductSchema(many=True)
    Products= ProductSchema.dump(get_products)
    return make_response(jsonify({"product":result}),201)


app.run(port=4002)