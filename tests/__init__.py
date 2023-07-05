import pytest
from party import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
