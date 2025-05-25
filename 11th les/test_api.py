import pytest
import requests
@pytest.fixture

def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_create_post(base_url):
    payload = {
        "title": "Automation Test",
        "body": "This is a test post",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)

    assert response.status_code == 201  # Успешное создание
    data = response.json()
    assert data["title"] == "Automation Test"