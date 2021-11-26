from flask_testing import TestCase
from application import app
from flask import url_for

class TestBase(TestCase):

    def create_app(self): #define flask object's configuration for unit tests
        app.config.update(
            SQLALCHEMY_DATABASEURI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self): #called before every test
        pass

    def tearDown(self): #called after every day
        pass 


#unit tests below inherit from TestBase.

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
