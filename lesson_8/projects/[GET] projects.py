import requests
import pytest

class YougileAPI:
    base_url = "https://ru.yougile.com/api-v2"

    def get_projects(self):
        url = f"{self.base_url}/projects"
        response = requests.get(url)
        return response

@pytest.fixture
def api():
    return YougileAPI()

def test_get_projects_positive(api):
    response = api.get_projects()
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "projects" in response.json()

def test_get_projects_negative(api):
    # Негативный тест проверяющий обязательные поля
    response = api.get_projects()
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "projects" in response.json()
    assert all(project.get("id") for project in response.json()["projects"])
    assert all(project.get("name") for project in response.json()["projects"])