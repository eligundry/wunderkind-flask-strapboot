from application.tests.helpers import ApplicationTestCase, ApplicationDBTestCase, PageMixin

class GeneralTests(ApplicationTestCase, PageMixin):
    def test_home(self):
        self.assert_page('/', 'general/index.html')
