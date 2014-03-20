from flask import current_app
from flask.ext.wtf import Form
from wtforms import (Field, TextField, TextAreaField, PasswordField,
                     BooleanField, SelectField, DateTimeField, ValidationError)
from wtforms.validators import Required, Length, Email

class RegistrationForm(Form):
    first_name = TextField(u'First Name', [Required()])
    last_name = TextField(u'Last Name', [Required()])
    email = TextField(u'Email', [Required(), Email()])
