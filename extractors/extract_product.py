from .aliextract import ExtractProduct as aliProduct
from src.errors import ScraperDoesNotExist

def Extract(website,ecomm):
    if ecomm == 'aliexpress':
        return aliProduct(website,ecomm)
    elif ecomm == 'ebay':
        return "empty"
    elif ecomm == 'amazon':
        return "empty"
    else:
        raise ScraperDoesNotExist
        