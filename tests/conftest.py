import pytest

from app.api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()
