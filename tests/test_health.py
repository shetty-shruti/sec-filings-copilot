from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_ask_validates_input() -> None:
    assert client.post("/ask", json={"question": ""}).status_code == 422
