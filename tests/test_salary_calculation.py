def test_salary_calculation_india(client):
    response = client.get("/employees/1/salary")
    data = response.json()

    assert data["gross"] == 100000
    assert data["deductions"] == 10000
    assert data["net"] == 90000
