from flask import Flask
from flask_restful import Api
from config import api_config
from api.main.routes import register_routes


app = Flask(__name__)
app.config.from_object(api_config['development'])  # Change to 'production' for production
api = Api(app)

register_routes(api)

def create_app():
    return app