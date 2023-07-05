from tests import client, app

class TestServer:
    def test_root(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_api(self, client):
        response = client.get("/api")
        assert response.status_code == 200

