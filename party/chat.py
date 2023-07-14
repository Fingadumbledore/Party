from pymongo import MongoClient

class Chat:
    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False

    @classmethod
    def init(self):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)['partyyy']
        self.collection = self.client['messages']
        self.initialized = True


    @classmethod
    def getAllMessages(self)-> list[dict]:
        return list(self.collection.find())

    @classmethod
    def insertMessage(self, content: str, author: str, timestamp: str):
        self.collection.insert_one(self.convertToMessage(content, author, timestamp))

    @classmethod
    def getNext100Messages(self, skip: int) -> list[dict]:
        return list(self.collection.find()
                                   .skip(skip)
                                   .limit(100))

    @classmethod
    def convertToMessage(self, content: str, author: str, timestamp: str) -> dict:
        message = {
            'content': content,
            'author': author,
            'timestamp': timestamp,
        }

        return message
