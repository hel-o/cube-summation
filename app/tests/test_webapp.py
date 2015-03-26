import unittest

from app import app


class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert 200 == response.status_code
