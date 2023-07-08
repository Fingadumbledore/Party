import party.main as main
from enum import Enum

def create_app():
    return main.app

class MateMarke(Enum):
    ClubMate = "Club Mate"
    FloraPower = "Flora Power"
    MioMioMate = "MioMio Mate"
