import requests


class ProjectPage:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer itda9Qq1nsn4T5iVGEPDR6JeoiMdXuFEzptbB6PoMDNupkE0I5v1pwgpIe1aoM7k"
    }

    def create_project(self, title="Тестовое питон", users=None):
        if users is None:
            users = {
                "ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8": "worker"
            }
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(
            self.BASE_URL, json=payload, headers=self.HEADERS)
        response.raise_for_status()  # Выдает ошибку для статусов 4xx и 5xx
        return response.json()['id']

    def get_projects(self):
        response = requests.get(self.BASE_URL, headers=self.HEADERS)
        response.raise_for_status()
        return response.json()

    def update_project(
            self, project_id, title="Тестовое питон измененное", users=None):
        if users is None:
            users = {
                "ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8": "worker"
            }
        update_url = f"{self.BASE_URL}/{project_id}"
        payload = {
            "deleted": False,
            "title": title,
            "users": users
        }
        response = requests.put(update_url, json=payload, headers=self.HEADERS)
        response.raise_for_status()
        return self.get_project_by_id(project_id)

    def get_project_by_id(self, project_id):
        response = requests.get(
            f"{self.BASE_URL}/{project_id}", headers=self.HEADERS)
        response.raise_for_status()
        return response.json()

    def create_project_without_title(self):
        payload = {
            "users": {
                "ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8": "worker"
            }
        }
        response = requests.post(
            self.BASE_URL, json=payload, headers=self.HEADERS)
        return response.status_code

    def update_project_without_id(self):
        update_url = f"{self.BASE_URL}/invalid_id"
        payload = {
            "deleted": True,
            "title": "Тестовое питон измененное"
        }
        response = requests.put(update_url, json=payload, headers=self.HEADERS)
        return response.status_code