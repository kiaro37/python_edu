import pytest

@pytest.fixture
def auth_token():
    return "Bearer faketoken123"

def test_authorized_request(auth_token):
    headers = {"Authorization": auth_token}
    response = make_request_with_headers(headers)
    assert response.status_code == 200

