from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService4(TestBase):
    def test_outcome(self):
        response = self.client.get(url_for('outcome'))
        self.assertEqual(response.status_code, 200)

    def test_15(self):
        response = self.client.get(url_for('outcome'), data="Today")
        self.assertIn(b'15%', response.data)

    def test_20(self):
        response = self.client.get(url_for('outcome'), data="On this coming Friday")
        self.assertIn(b'20%', response.data)

    def test_25(self):
        response = self.client.get(url_for('outcome'), data="This month")
        self.assertIn(b'25%', response.data)

    def test_75(self):
        response = self.client.get(url_for('outcome'), data="This year")
        self.assertIn(b'75%', response.data)

    def test_40(self):
        response = self.client.get(url_for('outcome'), data="In a few months")
        self.assertIn(b'40%', response.data)

    def test_55(self):
        response = self.client.get(url_for('outcome'), data="Next spring")
        self.assertIn(b'55%', response.data)

    def test_unable(self):
        response = self.client.get(url_for('outcome'), data="Yesterday")
        self.assertIn(b'Unable to calculate', response.data)