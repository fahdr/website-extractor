from flask import Response, request
from database.models import DraftAliExProduct
from flask_restful import Resource
from database.db import client
from .aliextract import ExtractProduct
from .website_formatter import formatter

class Extract(Resource):
    def get(self,product,website):
        extractedProduct=DraftAliExProduct(**(ExtractProduct(product))).save()

        #save draft
        #format for website
        #formatter(website,extractedProduct)
        #return info
        return()
    
    def put(self):
        #get info
        #save draft
        return()