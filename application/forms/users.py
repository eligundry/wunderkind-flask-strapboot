from application.forms import *
from application.models.user import *

class RegistrationForm(Form):
    first_name = TextField(u'First Name', validators=[Required()])
    last_name = TextField(u'Last Name', [Required()])
    email = TextField(u'Email', [Required(), Email(), unique(User.email)])
    password = PasswordField(u'Password', [Required(), EqualTo('confirm_password')])
    confirm_password = PasswordField(u'Confirm Password', [Required()])

class LoginForm(Form):
    email = TextField(u'Email', [Required(), Email()])
    password = PasswordField(u'Password', [Required()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None
        self.auth_failed = False

    def validate(self, *args, **kwargs):
        success = super(LoginForm, self).validate(*args, **kwargs)
        if not success:
            return success

        user = User.query.filter_by(email=self.email.data, is_active_user=True).first()

        if (user is not None and bcrypt.check_password_hash(user.password, self.password.data)):
            self.user = user
            return True

        self.auth_failed = True
        return False
