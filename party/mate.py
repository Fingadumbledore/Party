from pymongo import MongoClient
from enum import Enum
import random


def generate_kiste(count: int) -> list[bool]:
    return [random.choice([True]) for _ in range(count)]


class MateKiste():
    status = None
    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False
    FlaschenBreite = 5
    FlaschenHoehe = 4

    @classmethod
    def init(self, flaschenAnzahl: tuple[int, int] = None):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)['partyyy']
        self.collection = self.client['mate']

        self.collection.delete_many({}) # delete all

        if flaschenAnzahl is not None:
            self.FlaschenBreite = flaschenAnzahl[0]
            self.FlaschenHoehe = flaschenAnzahl[1]

        flaschenAnzahl = self.FlaschenBreite * self.FlaschenHoehe

        self.collection.insert_one({'mateKiste': True, 'status': generate_kiste(flaschenAnzahl)})
        self.initialized = True

    @classmethod
    def getStatus(self) -> list[bool]:
        return list(self.collection.find_one()['status']) # wir haben nur 1 ding da drinne, was geupdated wird

    @classmethod
    def removeAt(self, x: int, y: int):
        position = y * self.FlaschenBreite + x
        self.collection.update_one({'mateKiste': True}, {'$set': {'status.' + str(position): False}})
