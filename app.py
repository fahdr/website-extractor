import flask
from flask import request, jsonify
from selenium.webdriver.remote.utils import format_json
from extract_product import extract_product
from website_formatter import kpophearts,case10

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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


app.run()