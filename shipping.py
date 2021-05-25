from selenium import webdriver

DRIVER_PATH = '/Users/fahdrahman/Documents/ali-scrape-selenium/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.aliexpress.com/item/1005001850098429.html')

shipping_price=driver.find_element_by_css_selector('div.product-shipping-price span.bold').text
shipping_method=driver.find_element_by_css_selector('span.product-shipping-info').text
delivery_date=driver.find_element_by_css_selector('span.product-shipping-delivery span').text

print(dict(shipping_price=shipping_price,shipping_method=shipping_method,delivery_date=delivery_date))


