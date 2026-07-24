from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Page Pulse API Running"


def test_valid_audit():

    response = client.post(
        "/audit",
        json={
            "url": "https://google.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "status_code" in data
    assert "response_time_ms" in data


def test_invalid_url():

    response = client.post(
        "/audit",
        json={
            "url": "not_a_url"
        }
    )

    assert response.status_code == 422