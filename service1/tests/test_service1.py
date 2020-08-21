from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

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