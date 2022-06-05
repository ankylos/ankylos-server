import pytest
from web import create_app

# pytest-flask module for easy app testing
@pytest.fixture
def app():
    from config import TestingConfig
    app = create_app(TestingConfig)
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
