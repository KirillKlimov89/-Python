import pytest

from api_client import YouGileClient


@pytest.fixture
def client():
    return YouGileClient()


@pytest.fixture
def created_project(client):
    response = client.create_project("Test Project for Cleanup")
    project_id = response.json()["id"]

    yield project_id

    client.delete_project(project_id)
