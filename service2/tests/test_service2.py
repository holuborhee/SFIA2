from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_timeframe_view(self):
        response = self.client.get(url_for('timeframe'))
        self.assertEqual(response.status_code, 200)
    
    def test_timeframe(self):
        with patch('requests.get') as t:
            t.return_value.text = "Today"

            response = self.client.get(url_for('timeframe'))
            self.assertIn(b'Today', response.data)