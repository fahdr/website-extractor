from .aliextract import ExtractProduct as aliProduct
from src.errors import ScraperDoesNotExist
from database.models import AliExProduct

def Extract(product,ecomm):
    if ecomm == 'aliexpress':
        return AliExProduct(**aliProduct(product,ecomm))
    elif ecomm == 'ebay':
        return "empty"
    elif ecomm == 'amazon':
        return "empty"
    else:
        raise ScraperDoesNotExist
        