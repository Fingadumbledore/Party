from datetime import datetime, timedelta
from faker import Faker
import pymongo

fake = Faker()

def get_connection():
    CONNECTION_STRING = 'mongodb://localhost:27017/'
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['partyyy']['messages']

connection = get_connection()

fmt = '%Y-%m-%d %H:%M:%S'
now = datetime.now()

def generate_message(i: int):
    date = now - timedelta(days=i)
    date = date.strftime(fmt)
    message = {
        'sender': fake.name(),
        'text': fake.sentence() + ' ' + fake.sentence(),
        'timestamp': date
    }
    connection.insert_one(message)

MESSAGE_COUNT = 150
for i in range(MESSAGE_COUNT):
    generate_message(i)
