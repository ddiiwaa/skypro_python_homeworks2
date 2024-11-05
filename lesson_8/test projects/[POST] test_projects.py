import pytest
import requests

class TestYougileAPI:

    base_url = "https://ru.yougile.com/api-v2"
project_data = {
    "name": "Test Project",
    "description": "This is a test project"
}

def test_create_project_positive(self):
    response = requests.post(f"{self.base_url}/projects", json=self.project_data)
    assert response.status_code == 200
    assert response.json()["name"] == self.project_data["name"]
    assert response.json()["description"] == self.project_data["description"]

def test_create_project_missing_required_fields(self):
    invalid_project_data = {
        "description": "This is a test project"
    }
    response = requests.post(f"{self.base_url}/projects", json=invalid_project_data)
    assert response.status_code == 400
    assert response.json()["error"] == "Name is required"