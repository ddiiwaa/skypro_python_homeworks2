# test_yougile_api.py

import requests
import pytest

class YougileAPI:
    base_url = "https://ru.yougile.com/api-v2"

    def __init__(self, project_id):
        self.project_id = project_id

    def update_project(self, payload):
        url = f"{self.base_url}/projects/{self.project_id}"
        response = requests.put(url, json=payload)
        return response


class TestYougileAPI:

    @pytest.fixture
    def project_id(self):
        return "123"  # Замените на реальный project id

    @pytest.fixture
    def yougile_api(self, project_id):
        return YougileAPI(project_id)

    def test_update_project_positive(self, yougile_api):
        payload = {
            "name": "New Project Name"
        }
        response = yougile_api.update_project(payload)
        assert response.status_code == 200
        assert response.json()["name"] == "New Project Name"  # Проверяем, что имя проекта изменилось

    def test_update_project_missing_required_field(self, yougile_api):
        payload = {}  # Не указываем обязательное поле
        response = yougile_api.update_project(payload)
        assert response.status_code == 400
        assert "error" in response.json()  # Проверяем, что в ответе есть информация об ошибке

    # Для тестов с другими негативными сценариями можно добавить дополнительные методы