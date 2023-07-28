from pymongo import MongoClient

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
        messages = self.collection.find().sort('timestamp', -1)
        return list(messages)
    
    @classmethod
    def insertMessage(self, content: str, author: str, timestamp: str):
        message = self.convertToMessage(content, author, timestamp)
        print(message)
        self.collection.insert_one(message)
        print('inserted message')

    @classmethod
    def getNextNMessages(self, count: int, skip: int) -> list[dict]:
        return list(self.collection.find()
                    .skip(skip)
                    .limit(count)
                    .sort('timestamp', -1))

    @classmethod
    def convertToMessage(self, content: str, author: str, timestamp: str) -> dict:
        message = {
            'content': content,
            'sender': author,
            'timestamp': timestamp,
        }

        return message
