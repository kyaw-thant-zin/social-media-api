from flask import Flask
from flask_restful import Api
from config import api_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.main.routes import register_routes

# app
app = Flask(__name__)

# config
app.config.from_object(api_config['development'])  # Change to 'production' for production

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models
import api.main.model

# api
api = Api(app)

# routes
register_routes(api)

def create_app():
    return app