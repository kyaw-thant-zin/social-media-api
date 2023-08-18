from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import api_config
from api.main.routes import register_routes

# app
app = Flask(__name__)

# CORS
CORS(app=app, origins=["*"])

# config
app.config.from_object(api_config['development'])  # Change to 'production' for production

# JWT
jwt = JWTManager(app=app)

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models
import api.main.model

# api
api = Api(app, prefix='/api')

# routes
register_routes(api)

def create_app():
    return app