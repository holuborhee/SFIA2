from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_fortune_view(self):
        response = self.client.get(url_for('fortune'))
        self.assertEqual(response.status_code, 200)