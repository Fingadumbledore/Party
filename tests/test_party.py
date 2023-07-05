from tests import client, app

class TestServer:
    def test_root(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert b"<title>Party Controller</title>" in response.data
        assert b"<h1>Party Controller</h1>" in response.data
        assert b"/static/css/style.css" in response.data



    def test_api(self, client):
        response = client.get("/api")
        assert response.status_code == 200


    """
    def test_favicon(self, client):
        response = client.get("/favicon.ico")
        assert response.status_code == 200
    """
