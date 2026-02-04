def test_country_salary_metrics(client):
    response = client.get("/metrics/country/India")
    data = response.json()

    assert data["min"] == 100000
    assert data["max"] == 100000
    assert data["avg"] == 100000


def test_job_title_average(client):
    response = client.get("/metrics/job-title/Backend Engineer")
    assert response.json()["avg_salary"] == 100000
