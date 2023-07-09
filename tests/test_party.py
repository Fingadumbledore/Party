from tests import client, app
from flask import render_template

class TestServer:
    def test_root(self, client):
        response = client.get("/")
        assert response.headers["Location"] == "/login"
        # get if response html is same as template
        assert response.data == render_template("login.html")

    def test_api(self, client):
        response = client.get("/api")
        assert response.status_code == 200


    """
    def test_favicon(self, client):
        response = client.get("/favicon.ico")
        assert response.status_code == 200
    """
