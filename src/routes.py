from .extract_api import Extract
from .product_api import Product
def initialize_routes(api):
    api.add_resource(Extract, '/extract/<website>/<product>')
    api.add_resource(Product, '/product/<website>/<productid>')
