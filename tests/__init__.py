import pytest
from party import create_app, Database, chat as c, MateMarke
from party import message as m
from party.mate import MateKiste


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
    chat = c.Chat()
    yield chat

@pytest.fixture
def message():
    message = m.Message('author', 'content', 'timestamp', 0)
    yield message

@pytest.fixture
def mateKiste():
    mateKiste = MateKiste(20, MateMarke.ClubMate)
    yield mateKiste

