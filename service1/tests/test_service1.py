from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        fortuneData = ToldFortunes(
            timeframe = "Today",
            fortune = "an acquaintance of the past will positively affect you",
            percentage = "15%"
        )

        db.session.add(fortuneData)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_fortuneteller(self):
        with patch('requests.get') as t:
            with patch('requests.get') as f:
                with patch('requests.post') as p:
                    t.return_value.text = "Today"
                    f.return_value.text = "you will face great uncertainty"
                    p.return_value.text = "15%"

                    response = self.client.get(url_for('fortuneteller'))
                    self.assertEqual(response.status_code, 200)