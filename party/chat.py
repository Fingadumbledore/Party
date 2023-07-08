import redis
import json
from party import message as m

class Chat:
    def __init__(self):
        # message_count = int(db.get('message count'))
        if message_count == None:
            #db.set('message count', f"0")
            pass
    def getAllMessages(self) -> list[dict]:
        pass 
        """
        messageCount = int(db.get('message count'))
        messages = []
        for i in range(messageCount):
            message = db.hgetall(f'message {i}')
            messages.append(message)

        return messages
        """

    def insertMessage(self, content: str, author: str, timestamp: str) -> int:
        messageCount = int(db.get('message count'))
        message = m.Message(author, content, timestamp, messageCount)

        # db.hset(f'message {messageCount}', mapping=message.toJson())

        messageCount = messageCount + 1
        #db.set('message count', str(messageCount))

        return messageCount


    def convertToMessage(self, content: str, author: str, timestamp: str, id: int) -> dict:
        message = {
            'content': content,
            'author': author,
            'timestamp': timestamp,
            'id': id
        }

        return message
