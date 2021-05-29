from flask import Response, request
from flask_restful import Resource
from database.models import EcommProduct

class Product(Resource):
    def get(self,productid,website):
        #retrieve product from db
        #return info
        return {'hello': 'world'}
    def put(self):
        #get info
        #save to db for website product
        return ()

class Products(Resource):
    def get(self,website,ecomm):
        #retrieve all products
        proudcts=EcommProduct.objects(website=website,ecomm=ecomm).to_json()
        return Response(proudcts.to_json(), mimetype="application/json", status=200)

 