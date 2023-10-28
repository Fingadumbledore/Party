from pymongo import MongoClient

class team:
    status = None
    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False

    @classmethod
    def init(self, flaschenAnzahl: tuple[int, int] = None):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)['partyyy']
        self.collection = self.client['team']
    
