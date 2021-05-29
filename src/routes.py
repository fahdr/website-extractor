from .extract_api import Extract
from .product_api import Product,Products
def initialize_routes(api):
    api.add_resource(Extract, '/<website>/extract/<ecomm>/<product>/')
    api.add_resource(Product, '/<website>/product/<productid>/')
    api.add_resource(Products, '/<website>/<ecomm>/products/')
