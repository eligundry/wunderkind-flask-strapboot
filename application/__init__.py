from flask import Flask, render_template
from flask.ext import restful
from flask.ext.assets import Environment, Bundle
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

api = restful
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_objects=['application.settings.site']):
    app = Flask(__name__)

    # Add the settings object to Flask
    for config_object in config_objects:
        app.config.from_object(config_object)

    # Initalize objects for the application
    api.Api(app)
    assets = Environment(app)
    bcrypt.init_app(app)
    db.init_app(app)
    db.configure_mappers()
    login_manager.init_app(app)

    # Load views
    from application.views import general, errors, users

    app.register_blueprint(general.blueprint)
    app.register_blueprint(errors.blueprint)
    app.register_blueprint(users.blueprint)

    # Configure Flask-Assets
    assets.config['less_bin'] = '/usr/bin/lessc'

    bootstrap_less = Bundle('css/bootstrap/bootstrap.less', filters='less,cssmin', output='compiled/css/main.css')
    bootstrap_js = Bundle('js/bootstrap/*', filters='rjsmin', output='compiled/js/main.js')

    assets.register('bootstrap_less', bootstrap_less)
    assets.register('bootstrap_js', bootstrap_js)

    # Error Pages
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500

    return app
