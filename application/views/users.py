from application.views import *
from application.forms.users import *

blueprint = Blueprint('users', __name__)

@blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        message = u'User "{}" successfully added.'.format(user.email)
        flash(message, 'success')
        return redirect(url_for('general.index'))

    return render_template('users/registration.html', form=form)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(form.user)
        return redirect(url_for('general.index'))

    return render_template('users/login.html', form=form)
