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
    from application.views import errors

    app.register_blueprint(general.blueprint)
    app.register_blueprint(errors.blueprint)

    # Error Pages
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500

    return app
