import unittest
import alchemy
from flask import json

class AlchemyTests(unittest.TestCase):

    def setUp(self):
        self.app = alchemy.create_app().test_client()
    
    def test_create_address(self):
        resp = self.app.post(
            "/api/addresses",
            data = json.dumps({
                "line1": "32 avenue du system",
                "zipcode": "91758",
                "city": "Windows-sur-seine"
            }),
            content_type = "application/json"
        )

        self.assertEqual(resp.status_code, 200)