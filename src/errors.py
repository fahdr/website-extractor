from werkzeug.exceptions import HTTPException

class ScraperDoesNotExist(HTTPException):
    pass

class WebsiteDoesNotExist(HTTPException):
    pass

class ProductExists(HTTPException):
    pass

errors = {
    "ScraperDoesNotExist": {
        "message": "The scraper for this ecommerce site does not exist. Make a request?",
        "status": 400
    },
    "WebsiteDoesNotExist": {
        "message": "You are not registered, or might not have logged in. Please consider registering",
        "status": 400
    },
    "ProductExists": {
        "message": "Product already exists. Try editing it instead",
        "status": 400
    },
}