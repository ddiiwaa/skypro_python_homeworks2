import requests
import unittest

class YougileApiTests(unittest.TestCase):
    base_url = "https://ru.yougile.com/api-v2/projects/{id}"
project_id = 123  # Replace with actual project ID

def test_update_project(self):
    url = self.base_url.format(id=self.project_id)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_token_here"  # Replace with actual token
    }
    
    data = {
        "name": "Updated Project Name",
        "description": "Updated project description"
        # Add more fields to update as needed
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    self.assertEqual(response.status_code, 200)
    # Add more assertions to check if the project was updated successfully