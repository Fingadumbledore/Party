from tests import client, app

class TestMate:
    def test_api_mate(self, client):
        response = client.get("/api/mate")
        assert response.status_code == 200

    def test_api_mate_status(self, client):
        response = client.get("/api/mate/status")
        assert response.status_code == 200

    def test_api_mate_trinken(self, client):
        response = client.post("/api/mate/trinken")
        assert response.status_code == 200
