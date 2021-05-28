from selenium.webdriver.remote.utils import format_json
from database.models import KpopheartProducts


def formatter(websiteName,product):
    return websites[websiteName](product)

def kpophearts(product):
    item_category=['lomo','neklace','tshirt']
    team_names=['bts','twice', 'red velvet']
    sku_type=['color','team','singer','none','quantity']
    #todo: clean up all dict items

    formatted_product_list=[]
    #splitting sku into each item
    for item in product.skuItems :
        wsProduct=KpopheartProducts()
        wsProduct.team=item['itemTitle']
        wsProduct.title=product.title
        wsProduct.pic=item['itemImgUrl']
        wsProduct.price=item['itemPrice']
        formatted_product_list.append(wsProduct)
    

    return formatted_product_list

websites={'kpophearts':kpophearts,}
