import unittest
import requests
from django.test import Client

HOST = 'http://127.0.0.1:8000/'


class TestClient(unittest.TestCase):

    def test_api(self):
        response = requests.get(f'{HOST}health')
        self.assertEqual(response.status_code, 200)
        
    # def test_bd(self):
    #     response = requests.get(f'{HOST}health/bd')
    #     self.assertAlmostEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()