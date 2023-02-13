import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client