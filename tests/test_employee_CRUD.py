def test_create_employee(client):
    response = client.post(
        "/employees",
        json={
            "full_name": "Apoorva Sharma",
            "job_title": "Backend Engineer",
            "country": "India",
            "salary": 100000
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Apoorva Sharma"
    assert data["id"] is not None


def test_get_employee(client):
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_employee(client):
    response = client.put(
        "/employees/1",
        json={"salary": 120000},
    )
    assert response.status_code == 200
    assert response.json()["salary"] == 120000


def test_delete_employee(client):
    response = client.delete("/employees/1")
    assert response.status_code == 204
