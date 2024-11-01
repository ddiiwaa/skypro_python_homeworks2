import requests
import unittest

class TestYougileApi(unittest.TestCase):
    base_url = "https://ru.yougile.com/api-v2"

def test_create_project(self):
    url = f"{self.base_url}/projects"
    payload = {
        "name": "Test Project",
        "description": "This is a test project",
        "status": "active"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()["name"], "Test Project")
    self.assertEqual(response.json()["description"], "This is a test project")
    self.assertEqual(response.json()["status"], "active")

def test_create_project_invalid_payload(self):
    url = f"{self.base_url}/projects"
    payload = {
        "description": "This is a test project",
        "status": "active"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    self.assertEqual(response.status_code, 400)