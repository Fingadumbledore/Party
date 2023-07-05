import pytest
from party import create_app, Database, chat


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client

@pytest.fixture
def message_redis():
    messagesDB = redis.Redis(host='localhost', port=6379, db=Database.Messages.value)
    yield messagesDB

@pytest.fixture
def chat():
    chat = chat.Chat()
    yield chat
