
class Message:
    def __init__(self, author: str, content: str, timestamp: str, id: int = 0):
        self.author = author
        self.content = content
        self.timestamp = timestamp
        self.id = id

    def toJson(self) -> dict:
        json = {
            'author': self.author,
            'content': self.content,
            'timestamp': self.timestamp,
            'id': self.id
        }

        return json

    @staticmethod
    def fromJson(json: dict):
        self = Message('', '', '')
        self.author = json['author']
        self.content = json['content']
        self.timestamp = json['timestamp']
        self.id = json['id']

        return self

    def equals(self, message) -> bool:
        return self.author == message.author and self.content == message.content and self.timestamp == message.timestamp and self.id == message.id

    def generateid(self) -> None:
        self.id = 1

    def setId(self, id: int) -> None:
        self.id = id
        def __eq__(self, other):
            return self.author == other.author and self.content == other.content and self.timestamp == other.timestamp and self.id == other.id
