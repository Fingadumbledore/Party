from tests import client, app

class TestChat:
    def test_api_chat(self, client):
        response = client.get("/api/chat/")
        assert response.status_code == 200

    def test_api_chat_messages_count(self, client):
        response = client.get("/api/chat/messages/1")
        assert response.status_code == 200

    def test_api_chat_messages_count_offset(self, client):
        response = client.get("/api/chat/messages/1/1")
        assert response.status_code == 200

    def test_api_chat_new_message(self, client):
        response = client.post("/api/chat/new_message")
        assert response.status_code == 200
