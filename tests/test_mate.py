from tests import client, app, mateKiste
from party import MateMarke

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

    def test_eineTrinken(self, mateKiste):
        mateKiste.eineTrinken()
        assert mateKiste.getFlaschenAnzahl() == 19

    def test_getFlaschenAnzahl(self, mateKiste):
        assert mateKiste.getFlaschenAnzahl() == 20

    def test_getMarke(self, mateKiste):
        assert mateKiste.getMarke() == MateMarke.ClubMate

    def test_getMarkeName(self, mateKiste):
        assert mateKiste.getMarkeName() == "Club Mate"

    def test_toDict(self, mateKiste):
        assert mateKiste.toDict() == {
            'flaschen_anzahl': 20,
            'marke': 'Club Mate'
        }
