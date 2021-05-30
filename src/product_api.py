from flask import Response, request
from flask_restful import Resource
from database.models import EcommProduct
from errors import UpdateProductError,SchemaValidationError,InternalServerError
from mongoengine.errors import InvalidQueryError,DoesNotExist

class Product(Resource):
    def get(self,productid,website):
        product=EcommProduct.objects(skuID=productid,website=website).get().to_json()
        return Response(product, mimetype="application/json", status=200)

    def put(self,productid,website):
        #get info
        try:
            product = EcommProduct.objects.get(skuID=productid, website=website)
            #save to db for website product
        
            body = request.get_json()
            product.update(**body)
            return '', 200

        except InvalidQueryError:
            raise SchemaValidationError

        except DoesNotExist:
            raise UpdateProductError

        except Exception:
            raise InternalServerError  
 

class Products(Resource):
    def get(self,website,ecomm):
        #retrieve all products
        products=EcommProduct.objects(website=website,ecomm=ecomm).to_json()
        return Response(products, mimetype="application/json", status=200)

 