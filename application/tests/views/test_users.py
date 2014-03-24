from application.tests.helpers import ApplicationTestCase, ApplicationDBTestCase, PageMixin

class UserTests(ApplicationDBTestCase, PageMixin):
    def test_user_register(self):
        self.assert_page('/sign-up', 'users/registration.html')

    def test_user_login(self):
        self.assert_page('/login', 'users/login.html')
