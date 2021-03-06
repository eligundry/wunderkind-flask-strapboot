from flask.ext.testing import TestCase

from application import create_app, db

class ApplicationTestCase(TestCase):
    def create_app(self):
        return create_app(['application.settings.site', 'application.settings.test'])

class ApplicationDBTestCase(ApplicationTestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class PageMixin(object):
    def assert_page(self, url, template):
        response = self.client.get(url)
        self.assert_200(response)
        self.assert_template_used(template)
