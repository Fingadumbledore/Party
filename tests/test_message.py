import pytest
from party import message as m
from tests import message

class TestMessage:
    def test_setId(self, message):
        assert message.id == 0
        message.setId(1)
        assert message.id == 1

    def test_toJson(self, message):
        json = message.toJson()
        assert json['author'] == 'author'
        assert json['content'] == 'content'
        assert json['timestamp'] == 'timestamp'
        assert json['id'] == 0

    def test_fromJson(self, message):
        json = message.toJson()
        message2 = m.Message.fromJson(json)
        assert message2.author == 'author'
        assert message2.content == 'content'
        assert message2.timestamp == 'timestamp'

    def test_equals(self, message):
        message2 = m.Message('author', 'content', 'timestamp', 0)
        assert message.equals(message2)
