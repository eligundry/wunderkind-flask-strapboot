from flask import Blueprint, render_template, url_for, current_app, redirect, request, flash

from application.forms.users import *

blueprint = Blueprint('users', __name__)

@blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    return render_template('users/registration.html', form=form)
