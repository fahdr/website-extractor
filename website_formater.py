from selenium.webdriver.remote.utils import format_json


def kpophearts(product):
    item_category=['lomo','neklace','tshirt']
    team_names=['bts','twice', 'red velvet']
    sku_type=['color','team','singer','none','quantity']
    #todo: clean up all dict items


    #splitting sku into each item
    team='set'
    title='title'
    pic='pic'
    price='price'
    category='category'

    formatted_product=dict(title=title,team=team,pic=pic,price=price,category=category)
    return formatted_product
