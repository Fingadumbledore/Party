import pytest
from tests import client, app

class TestStatic:
    def test_css_style(self, client):
        response = client.get('/static/css/style.css')
        assert response.status_code == 200
