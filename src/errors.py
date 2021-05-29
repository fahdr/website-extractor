from werkzeug.exceptions import HTTPException

class ScraperDoesNotExist(HTTPException):
    pass

errors = {
    "ScraperDoesNotExist": {
        "message": "The scraper for this ecommerce site does not exist. Make a request?",
        "status": 400
    },
}