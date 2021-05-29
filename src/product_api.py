from flask import Response, request
from flask_restful import Resource
from database.models import AliExProduct

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
    def get(self,website):
        #retrieve all products
        
        proudcts=AliExProduct.objects.to_json()
        return Response(proudcts, mimetype="application/json", status=200)

 