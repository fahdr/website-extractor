from werkzeug.exceptions import HTTPException

class ScraperDoesNotExist(HTTPException):
    pass

class WebsiteDoesNotExist(HTTPException):
    pass

class ProductExists(HTTPException):
    pass

class UpdateProductError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class InternalServerError(HTTPException):
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
    "UpdateProductError": {
        "message": "Either the product does not exist, or you have not logged in",
        "status": 400
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
}