import redis
import json
from party import messagesDB as db

class Chat:
    def __init__(self):
        message_count = int(db.get('message count'))
        if message_count == None:
            db.set('message count', 0)
    def getAllMessages(self) -> list[dict]:
        messageCount = int(db.get('message count'))
        messages = []
        for i in range(messageCount):
            message = db.get(f'message {i}')
            messages.append(json.loads(message))

        return messages

    def insertMessage(self, content: str, author: str, timestamp: str) -> int:
        messageCount = int(db.get('message count'))
        message = convertToMessage(content, author, timestamp, messageCount)

        db.set(f'message {messageCount}', json.dumps(message))

        messageCount = messageCount + 1
        db.set('message count', messageCount)

        return messageCount


    def convertToMessage(self, content: str, author: str, timestamp: str, id: int) -> dict:
        message = {
            'content': content,
            'author': author,
            'timestamp': timestamp,
            'id': id
        }

        return message

class Message:
    def __init__(self, author: str, content: str, timestamp: str):
        self.author = author
        self.content = content
        self.timestamp = timestamp

    def toJson(self) -> dict:
        json = {
            'author': self.author,
            'content': self.content,
            'timestamp': self.timestamp
        }

        return json

    def fromJson(self, json: dict):
        self.author = json['author']
        self.content = json['content']
        self.timestamp = json['timestamp']

    def equals(self, message) -> bool:
        return self.author == message.author and self.content == message.content and self.timestamp == message.timestamp
