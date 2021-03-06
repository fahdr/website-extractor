from selenium import webdriver

def ExtractProduct(product_id):
    DRIVER_PATH = '/Users/fahdrahman/Documents/ali-scrape-selenium/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://www.aliexpress.com/item/'+str(product_id)+'.html')
    title=driver.find_element_by_css_selector('h1.product-title-text').text
    reviews=driver.find_element_by_css_selector('span.product-reviewer-reviews').text
    orders=driver.find_element_by_css_selector('span.product-reviewer-sold').text
    rating=driver.find_element_by_css_selector('span.overview-rating-average').text

    sku_list=driver.find_elements_by_css_selector('li.sku-property-item')
    item_attr=[]

    for item in sku_list:
        #add code click only if element is clickable
        item.click()
        item_title=driver.find_element_by_css_selector('span.sku-title-value').text
        #add code to handle prices during flash sale
        item_price_sale=driver.find_element_by_css_selector('div.product-price-current span.product-price-value').text
        item_price=driver.find_element_by_css_selector('div.product-price-original span.product-price-value').text
        img_url=driver.find_element_by_css_selector('img.magnifier-image').get_attribute('src')
        item_attr.append({'itemTitle':item_title,'itemSalePrice':item_price_sale,'itemPrice':item_price,'itemImgUrl':img_url})

      
    shipping_price=driver.find_element_by_css_selector('div.product-shipping-price span.bold').text
    shipping_method=driver.find_element_by_css_selector('span.product-shipping-info').text
    delivery_date=driver.find_element_by_css_selector('span.product-shipping-delivery span').text
    newdict=dict(
    skuID=product_id,
    title=title,
    reviewCount=reviews,
    orders=orders,
    rating=rating,
    skuItems=item_attr,
    )

    return newdict





