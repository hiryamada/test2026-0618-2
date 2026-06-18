from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_weather_returns_sunny_forecast() -> None:
    response = client.get("/weather")

    assert response.status_code == 200
    assert response.json() == {"forecast": "晴れ"}
