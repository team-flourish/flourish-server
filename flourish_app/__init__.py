from flask import Flask, current_app
from flask_login import LoginManager
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token

from .extensions import db
from .main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    JWTManager(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = "login"
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)

    return app
