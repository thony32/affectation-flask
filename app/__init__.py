from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()  # Initialize without passing the app


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Initialize SQLAlchemy with the app
    CORS(app, resources={r"/*": {"origins": "*"}})  # CORS setup

    JWTManager(app)
    # from app.api.affect_api import affect_api
    from app.api.employee_api import employee_api
    from app.api.place_api import place_api

    # app.register_blueprint(affect_api)
    app.register_blueprint(employee_api)
    app.register_blueprint(place_api)

    return app
