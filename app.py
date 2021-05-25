import flask
from flask import request, jsonify
from selenium.webdriver.remote.utils import format_json
from extract_product import extract_product
from website_formater import kpophearts,case10

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/<website>/extract/<product>', methods=['GET'])
def extract(website,product):
    product_json=extract_product(product)
    if product=='kpophearts':
        formatted_product=kpophearts(product_json)
    elif product=='case10':
        formatted_product=case10(product_json)
    else:
        formatted_product=product_json

    return formatted_product


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()