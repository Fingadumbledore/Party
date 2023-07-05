from tests import client, app

class TestServer:
    def test_root(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_api(self, client):
        response = client.get("/api")
        assert response.status_code == 200

    def test_api_mate(self, client):
        response = client.get("/api/mate")
        assert response.status_code == 200

    def test_api_mate_status(self, client):
        response = client.get("/api/mate/status")
        assert response.status_code == 200

    def test_api_mate_trinken(self, client):
        response = client.post("/api/mate/trinken")
        assert response.status_code == 200

    def test_api_chat(self, client):
        response = client.get("/api/chat/")
        assert response.status_code == 200

    def test_api_chat_messages_1(self, client):
        response = client.get("/api/chat/messages/1")
        assert response.status_code == 200

    def test_api_chat_messages_2(self, client):
        response = client.get("/api/chat/messages/1/1")
        assert response.status_code == 200

    def test_api_chat_new_message(self, client):
        response = client.post("/api/chat/new_message")
        assert response.status_code == 200

    def test_api_music(self, client):
        response = client.get("/api/music")
        assert response.status_code == 200

    def test_api_music_skip(self, client):
        response = client.post("/api/music/skip")
        assert response.status_code == 200

    def test_api_music_queue(self, client):
        response = client.get("/api/music/queue")
        assert response.status_code == 200

    def test_api_music_add_song(self, client):
        response = client.post("/api/music/add_song")
        assert response.status_code == 200
