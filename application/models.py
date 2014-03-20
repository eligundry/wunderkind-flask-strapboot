from flask.ext.login import UserMixin
from sqlalchemy import types
from sqlalchemy.orm import subqueryload

from application import db, bcrypt

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128))
    is_active_user = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, **columns):
        password = columns.pop('password', None)

        if password is not None:
            pass

        super(User, self).__init__(**columns)

    def __repr__(self):
        return u'<User "{}">'.format(self.email).encode('utf-8')

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def is_active(self):
        return True if self.is_active_user is None else self.is_active_user
