import pytest

from app.api import web_app


@pytest.fixture
def client():
    web_app.config["TESTING"] = True
    return web_app.test_client()
