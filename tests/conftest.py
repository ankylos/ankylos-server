import pytest
from web import create_app
from flask.testing import FlaskClient
from flask.app import Flask

# pytest-flask module for easy app testing
@pytest.fixture
def app() -> Flask:
    from config import TestingConfig

    app = create_app(TestingConfig())
    return app


@pytest.fixture
def client(app) -> FlaskClient:
    with app.test_client() as client:
        return client
