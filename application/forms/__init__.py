import re

from flask import current_app
from flask.ext.wtf import Form
from wtforms import (Field, TextField, TextAreaField, PasswordField,
                     BooleanField, SelectField, DateTimeField, ValidationError)
from wtforms.validators import Required, Length, Email, EqualTo

from application import bcrypt, db

def unique(column, message=None):
    if message is None:
        message = u'{} is not unique'

    def validator(form, field):
        if (field.object_data != field.data and db.session.query(exists().where(column == field.data)).scalar()):
            label_text = re.sub(r'\([^)]*\)', '', field.label.text).strip()
            raise ValidationError(message.format(label_text))

    return validator
