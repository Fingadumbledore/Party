import party.main as main
import redis
from enum import Enum

def create_app():
    return main.app

class Database(Enum):
    Messages = 0
    Users = 1
    Games = 2

messagesDB = redis.Redis(host='localhost', port=6379, db=Database.Messages.value)
users = redis.Redis(host='localhost', port=6379, db=Database.Users.value)
games = redis.Redis(host='localhost', port=6379, db=Database.Games.value)

