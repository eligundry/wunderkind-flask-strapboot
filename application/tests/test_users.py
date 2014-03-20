from application import db
from application.models import User
from application.tests.helpers import ApplicationTestCase, ApplicationDBTestCase

class UserTests(ApplicationDBTestCase):
    def init_user(self, **kwargs):
        return User(email="eligundry@gmail.com", first_name="Eli", last_name="Gundry", **kwargs)

    def test_set_password(self):
        user = self.init_user()
        user.set_password('password')
        self.assertNotEqual(user.password, 'password')

    def test_active_user(self):
        user = self.init_user()
        self.assertTrue(user.is_active())

        user.is_active_user = False
        self.assertFalse(user.is_active())

    def test_admin_user(self):
        user = self.init_user()
        self.assertFalse(user.is_active_user)

        user.is_active_user = True
        self.assertTrue(user.is_active_user)

    def test_user_database(self):
        user = self.init_user()
        user.set_password('password')

        db.session.add(user)
        db.session.commit()
