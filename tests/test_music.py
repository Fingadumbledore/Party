from tests import client, app

class TestMusic:
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
