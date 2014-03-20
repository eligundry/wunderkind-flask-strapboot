from application.tests.helpers import ApplicationTestCase, ApplicationDBTestCase, PageMixin

class ErrorTest(ApplicationTestCase, PageMixin):
    def test_404(self):
        response = self.client.get('/blah')
        self.assert_404(response)
        self.assert_template_used('errors/404.html')
