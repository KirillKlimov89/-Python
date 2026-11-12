def test_create_project_positive(client):
    response = client.create_project("My Test Project")

    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_create_project_negative(client):
    response = client.create_project("")

    assert response.status_code == 400
    assert "error" in response.json()


def test_update_project_positive(client, created_project):
    response = client.update_project(
        created_project, "Updated Project Title"
    )

    assert response.status_code == 200


def test_update_project_negative(client):
    response = client.update_project(
        "00000000-0000-0000-0000-000000000000",
        "New Title",
    )

    assert response.status_code == 404


def test_get_project_positive(client, created_project):
    response = client.get_project(created_project)

    assert response.status_code == 200
    assert "id" in response.json()


def test_get_project_negative(client):
    response = client.get_project(
        "00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404
