from flask import Response, request
from flask_restful import Resource
from database.models import EcommProduct

class Product(Resource):
    def get(self,productid,website):
        product=EcommProduct.objects(skuID=productid,website=website).get().to_json()
        return Response(product, mimetype="application/json", status=200)
    def put(self):
        #get info
        #save to db for website product
        return ()

class Products(Resource):
    def get(self,website,ecomm):
        #retrieve all products
        products=EcommProduct.objects(website=website,ecomm=ecomm).to_json()
        return Response(products, mimetype="application/json", status=200)

 