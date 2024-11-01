import requests
import unittest

class TestYougileApi(unittest.TestCase):
    base_url = "https://ru.yougile.com/api-v2"

def test_get_projects(self):
    response = requests.get(f"{self.base_url}/projects")
    self.assertEqual(response.status_code, 200)
    self.assertTrue("projects" in response.json())

def test_create_project(self):
    data = {
        "name": "Test Project",
        "description": "This is a test project"
    }
    response = requests.post(f"{self.base_url}/projects", json=data)
    self.assertEqual(response.status_code, 201)
    self.assertTrue("id" in response.json())
    self.assertEqual(response.json()["name"], "Test Project")

def test_update_project(self):
    project_id = 1  # replace with actual project ID
    data = {
        "description": "Updated description"
    }
    response = requests.put(f"{self.base_url}/projects/{project_id}", json=data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()["description"], "Updated description")

def test_delete_project(self):
    project_id = 1  # replace with actual project ID
    response = requests.delete(f"{self.base_url}/projects/{project_id}")
    self.assertEqual(response.status_code, 204)