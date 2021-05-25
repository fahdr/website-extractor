from selenium import webdriver

DRIVER_PATH = '/Users/fahdrahman/Documents/ali-scrape-selenium/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.aliexpress.com/item/1005001850098429.html')
title=driver.find_element_by_css_selector('h1.product-title-text').text
reviews=driver.find_element_by_css_selector('span.product-reviewer-reviews').text
orders=driver.find_element_by_css_selector('span.product-reviewer-sold').text
rating=driver.find_element_by_css_selector('span.overview-rating-average').text


sku_list=driver.find_elements_by_css_selector('li.sku-property-item')
item_attr=[]

for item in sku_list:
    item.click()
    item_title=driver.find_element_by_css_selector('span.sku-title-value').text
    item_price_sale=driver.find_element_by_css_selector('div.product-price-current span.product-price-value').text
    item_price=driver.find_element_by_css_selector('div.product-price-original span.product-price-value').text
    img_url=driver.find_element_by_css_selector('img.magnifier-image').get_attribute('src')
    item_attr.append({'item_title':item_title,'item_price_sale':item_price_sale,'item_price':item_price,'img_url':img_url})

#shipping=driver.find_element_by_css_selector

print(dict(title=title,reviews=reviews,orders=orders,rating=rating,items=item_attr))
    





