import requests
import unittest

class TestYougileMethods(unittest.TestCase):
    
    base_url = 'https://ru.yougile.com/api-v2'
project_id = 123  # Replace with actual project ID

def test_get_project(self):
    url = f'{self.base_url}/projects/{self.project_id}'
    response = requests.get(url)

    self.assertEqual(response.status_code, 200)
    self.assertTrue('project_name' in response.json())
    self.assertTrue('created_at' in response.json())
    self.assertTrue('updated_at' in response.json())