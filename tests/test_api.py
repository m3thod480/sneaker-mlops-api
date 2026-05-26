from fastapi.testclient import TestClient

from app.main import app
from pathlib import Path

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_endpoint():
    image_path = Path("tests/test_images/airmax97.jpg")

    with open(image_path, "rb") as image_file:
        response = client.post(
            "/predict",
            files={"file": ("airmax97.jpg", image_file, "image/jpeg")}
        )

    data = response.json()

    assert response.status_code == 200
    assert "predicted_class" in data
    assert "confidence" in data
    assert "top_predictions" in data
    assert isinstance(data["top_predictions"], list)