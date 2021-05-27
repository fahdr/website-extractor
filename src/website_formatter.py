from selenium.webdriver.remote.utils import format_json


def formatter(websiteName,product):
    websites[websiteName](product)

def kpophearts(product):
    item_category=['lomo','neklace','tshirt']
    team_names=['bts','twice', 'red velvet']
    sku_type=['color','team','singer','none','quantity']
    #todo: clean up all dict items

    formatted_product_list=[]
    #splitting sku into each item
    for item in product[items]:

        team=item['item_title']
        title=item['title']
        pic=item['img_url']
        price=item['item_price']
        category=item['category']
        formatted_product_list.append(title=title,team=team,pic=pic,price=price,category=category)
        
    return formatted_product_list

websites={'kpophearts':kpophearts,}
