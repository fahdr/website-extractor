from flask import Flask
from flask_restful import Api
from src.routes import initialize_routes
from src.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)


initialize_routes(api)

app.run()


