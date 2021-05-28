from bson.json_util import loads
from flask import Response, request
from database.models import AliExProduct,KpopheartProducts
from flask_restful import Resource
from database.db import client
from .aliextract import ExtractProduct
from .website_formatter import formatter
import json

class Extract(Resource):
    def get(self,product,website):
        extractedProduct=AliExProduct(**(ExtractProduct(product)))

        #save draft
        #format for website
        extractedProduct.websiteProducts=formatter(website,extractedProduct)
        extractedProduct.save()
        #return info
        return(json.loads(extractedProduct.to_json()))
    
    def put(self):
        #get info
        #save draft
        return()