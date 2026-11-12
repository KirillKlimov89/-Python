import os

import requests


class YouGileClient:
    base_url = "https://ru.yougile.com/api-v2"

    def __init__(self):
        token = os.environ.get("YOUGILE_TOKEN")
        if not token:
            raise RuntimeError(
                "YOUGILE_TOKEN не задан. "
                "Установите переменную окружения."
            )
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title):
        return requests.post(
            f"{self.base_url}/projects",
            json={"title": title},
            headers=self.headers,
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json={"title": title},
            headers=self.headers,
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )

    def delete_project(self, project_id):
        return requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )
