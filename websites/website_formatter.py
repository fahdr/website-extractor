from selenium.webdriver.remote.utils import format_json
from database.models import WebsiteProducts


def formatter(product):

    formatted_product_list=[]
    #splitting sku into each item
    for item in product.skuItems :
        wsProduct=WebsiteProducts()
        wsProduct.title=product.title
        wsProduct.pic=item['itemImgUrl']
        wsProduct.price=item['itemPrice']
        formatted_product_list.append(wsProduct)
    

    return formatted_product_list


