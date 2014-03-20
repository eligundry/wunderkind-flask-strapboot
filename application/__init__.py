from flask import Flask, render_template
from flask.ext import restful
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

api = restful
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_objects):
    app = Flask(__name__)

    # Add the settings object to Flask
    for config_object in config_objects:
        app.config.from_object(config_object)

    # Initalize objects for the application
    api.Api(app)
    bcrypt.init_app(app)
    db.init_app(app)
    db.configure_mappers()
    login_manager.init_app(app)

    # Load views
    from application.views import general

    app.register_blueprint(general.blueprint)

    return app
