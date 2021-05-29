from bson.json_util import loads
from flask import Response, request
from database.models import AliExProduct,KpopheartProducts,ScrapingSites
from flask_restful import Resource
from database.db import client
from .aliextract import ExtractProduct
from .website_formatter import formatter
from mongoengine.errors import DoesNotExist
from .errors import ScraperDoesNotExist
import json

class Extract(Resource):
    def get(self,product,website,ecomm):
        #check if the ecommerce site is supported
        try:
            scrape_site=ScrapingSites.objects().get(name=ecomm)
            extractedProduct=AliExProduct(**(ExtractProduct(product)))
            extractedProduct.website=website
            extractedProduct.websiteProducts=formatter(website,extractedProduct)
            extractedProduct.save()
            return(json.loads(extractedProduct.to_json()))
        except DoesNotExist:
            raise ScraperDoesNotExist

        
    
    def put(self):
        #get info
        #save draft
        return()

    