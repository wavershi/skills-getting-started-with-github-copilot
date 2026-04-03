from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_get_activities_returns_success_and_data():
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
