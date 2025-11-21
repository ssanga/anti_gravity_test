from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/", follow_redirects=False)
    # Expect a redirect (307 Temporary Redirect is default for FastAPI redirects usually, or 302/303 depending on implementation)
    # In our code we used RedirectResponse(url="/docs"), which defaults to 307.
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

def test_read_pets():
    response = client.get("/pets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
