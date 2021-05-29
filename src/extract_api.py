from bson.json_util import loads
from flask import Response, request
from database.models import ScrapingSites,Websites
from flask_restful import Resource
from database.db import client
from extractors.extract_product import ProductExtractor
from websites.website_formatter import formatter
from mongoengine.errors import DoesNotExist
from .errors import ScraperDoesNotExist, WebsiteDoesNotExist
import json

class Extract(Resource):
    def get(self,product,website,ecomm):

        #check if website exists
        try:
            Websites.objects().get(name=website)
        except DoesNotExist:
            raise WebsiteDoesNotExist
        #check if the ecommerce site is supported
        try:
            ScrapingSites.objects().get(name=ecomm)
        except DoesNotExist:
            raise ScraperDoesNotExist
        

        extractedProduct=ProductExtractor(product,ecomm)
        extractedProduct.website=website
        extractedProduct.ecomm=ecomm
        extractedProduct.websiteProducts=formatter(website,extractedProduct)
        extractedProduct.save()
        return(json.loads(extractedProduct.to_json()))
        

        
    
    def put(self):
        #get info
        #save draft
        return()

    