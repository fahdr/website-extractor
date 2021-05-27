from flask import Response, request
from flask_restful import Resource

class Product(Resource):
    def get(self,productid):
        #retrieve product from db
        #return info
        return {'hello': 'world'}
    def put(self):
        #get info
        #save to db for website product
        return ()

 