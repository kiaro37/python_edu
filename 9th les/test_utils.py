import pytest


@pytest.fixture
def sample_user():
        return {"name": "Masha", "age": 25, "is_active": True}