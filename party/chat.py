from pymongo import MongoClient
from datetime import datetime

class Chat:
    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False

    @classmethod
    def init(self):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.collection = self.client['partyyy']['messages']
        self.initialized = True


    @classmethod
    def getAllMessages(self)-> list[dict]:
        messages = self.collection.find().sort('timestamp', 1)
        return list(messages)
    
    @classmethod
    def insertMessage(self, content: str, author: str, timestamp: str):
        if not (self.initialized): self.init()
        message = self.convertToMessage(content, author, timestamp)
        self.collection.insert_one(message)
        print('inserted message')

    @classmethod
    def getNextNMessages(self, count: int, skip: int) -> list[dict]:
        messages = list(self.collection.find()
                    .skip(skip)
                    .limit(count)
                    .sort('timestamp', 1))

        return messages

    @classmethod
    def convertToMessage(self, content: str, author: str, timestamp: str) -> dict:
        message = {
            'text': content,
            'sender': author,
            'timestamp': str(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
        }

        return message
