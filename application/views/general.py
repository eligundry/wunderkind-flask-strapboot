from flask import Blueprint, render_template, url_for, current_app, redirect, request, flash

blueprint = Blueprint('general', __name__)

@blueprint.route('/')
def index():
    return render_template('general/index.html')
