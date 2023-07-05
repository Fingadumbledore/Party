from tests import client, app, chat

class TestChat:
    def test_api_chat(self, client):
        response = client.get("/api/chat/")
        assert response.status_code == 200

    def test_insertMessage(self, chat):
        messageId = chat.insertMessage('test', 'testAuthor', 'testTimestamp')
        assert messageId > 0
        messages = chat.getAllMessages()

    def test_api_chat_messages_count(self, client):
        response = client.get("/api/chat/messages/1")
        assert response.status_code == 200

    def test_api_chat_messages_count_offset(self, client):
        response = client.get("/api/chat/messages/1/1")
        assert response.status_code == 200

    def test_api_chat_new_message(self, client):
        response = client.post("/api/chat/new_message")
        assert response.status_code == 200

    def test_get_all_messages(self, chat):
        messages = chat.getAllMessages()
        assert len(messages) > 0
        assert type(messages) == list
        assert type(messages[0]) == dict
        assert type(messages[0]['content']) == str
        assert type(messages[0]['author']) == str
        assert type(messages[0]['timestamp']) == str
        assert type(messages[0]['id']) == int

    def test_convertToMessage(self, chat):
        message = chat.convertToMessage('test', 'test', 'test', 0)
        assert type(message) == dict
        assert type(message['content']) == str
        assert type(message['author']) == str
        assert type(message['timestamp']) == str
        assert type(message['id']) == int

