import pytest
import requests

@pytest.fixture
def auth_headers():
    token = "123qwe456zxc"
    return {
        "Autorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_fake_token(auth_headers):
    response = requests.get(f"{base_url()}/posts/1", headers=auth_headers)
    assert response.status_code == 200