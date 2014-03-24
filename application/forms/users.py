from flask import current_app
from flask.ext.wtf import Form
from wtforms import (Field, TextField, TextAreaField, PasswordField,
                     BooleanField, SelectField, DateTimeField, ValidationError)
from wtforms.validators import Required, Length, Email, EqualTo

class RegistrationForm(Form):
    first_name = TextField(u'First Name', validators=[Required()])
    last_name = TextField(u'Last Name', [Required()])
    email = TextField(u'Email', [Required(), Email()])
    password = PasswordField(u'Password', [Required(), EqualTo('confirm_password')])
    confirm_password = PasswordField(u'Confirm Password', [Required()])

class LoginForm(Form):
    email = TextField(u'Email', [Required(), Email()])
    password = PasswordField(u'Password', [Required()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None
        self.auth_failed = False
