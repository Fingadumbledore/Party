import pytest
from party.chat import Message

@pytest.fixture
def message():
    message = Message('author', 'content', 'timestamp')
    yield message

class TestMessage:
    def test_toJson(self, message):
        json = message.toJson()
        assert json['author'] == 'author'
        assert json['content'] == 'content'
        assert json['timestamp'] == 'timestamp'

    def test_fromJson(self, message):
        json = message.toJson()
        message2 = Message.fromJson(json)
        assert message2.author == 'author'
        assert message2.content == 'content'
        assert message2.timestamp == 'timestamp'

    def test_equals(self, message):
        message2 = Message('author', 'content', 'timestamp')
        assert message == message2
        assert message.equals(message2)
