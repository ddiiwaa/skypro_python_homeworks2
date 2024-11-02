import requests
import pytest

class TestYougileAPI:

    base_url = "https://ru.yougile.com/api-v2"

    def test_get_project_info_positive(self):
        project_id = 1
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url)
        assert response.status_code == 200
        project_data = response.json()
        assert "name" in project_data
        assert "description" in project_data
        assert "created_at" in project_data

    def test_get_project_info_negative(self):
        project_id = 9999999  # assuming this project ID does not exist
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url)
        assert response.status_code == 404