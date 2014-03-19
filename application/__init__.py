from flask import Flask, render_template

def create_app(config):
    app = Flask(__name__)
    return app
