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
        messages = self.collection.find()
        print(messages)
        return list(messages)
    
    @classmethod
    def insertMessage(self, content: str, author: str, timestamp: str):
        self.collection.insert_one(self.convertToMessage(content, author, timestamp))


    @classmethod
    def getNextNMessages(self, count: int, skip: int) -> list[dict]:
        return list(self.collection.find()
                    .skip(skip)
                    .limit(count))

    @classmethod
    def convertToMessage(self, content: str, author: str, timestamp: str) -> dict:
        message = {
            'content': content,
            'author': author,
            'timestamp': timestamp,
        }
        print(message)

        return message
