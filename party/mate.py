from party import MateMarke as Marke

class MateKiste:
    def __init__(self, flaschen_anzahl: int, marke: Marke):
        self.flaschen_anzahl = flaschen_anzahl
        self.marke = marke

    def eineTrinken(self):
        self.flaschen_anzahl = self.flaschen_anzahl - 1

    def getFlaschenAnzahl(self) -> int:
        return self.flaschen_anzahl

    def getMarke(self) -> Marke:
        return self.marke

    def getMarkeName(self) -> str:
        return self.marke.value
