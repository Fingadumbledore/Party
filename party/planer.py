from pymongo import MongoClient
from datetime import datetime

class Planer:
    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False

    @classmethod
    def init(self):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.collection = self.client['partyyy']['planer']
        self.initialized = True

    @classmethod
    def getNewEvent(self):
        print("huhu")

    @classmethod
    def insertNewEvent(self, name: str, time: str):
        if not self.initialized:
            self.init()

        event = self.convertToEvent(name, time)
        self.collection.insert_one(event)
        print('Inserted event:', event)

    @classmethod
    def deleteEvent(self):
        print("huhu")

    @classmethod
    def getAllEvents(self) -> list[dict]:
        if not self.initialized:
            self.init()

        events = self.collection.find().sort('time', 1)
        return list(events)

    @classmethod
    def getNextEvents(self, count: int, skip: int) -> list[dict]:
        if not self.initialized:
            self.init()

        events = list(self.collection.find()
                      .skip(skip)
                      .limit(count)
                      .sort('time', 1))

        return events

    @classmethod
    def convertToEvent(self, name: str, time: str) -> dict:
        event = {
            'name': name,
            'time': str(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))
        }

        return event
