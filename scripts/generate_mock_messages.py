from faker import Faker
import pymongo

fake = Faker()

def get_connection():
    CONNECTION_STRING = 'mongodb://localhost:27017/'
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['partyyy']['messages']

connection = get_connection()

def generate_message():
    message = {
        'sender': fake.name(),
        'text': fake.sentence() * 2,
        'timestamp': fake.date_time_this_year()
    }
    connection.insert_one(message)

MESSAGE_COUNT = 1000
for i in range(MESSAGE_COUNT):
    generate_message()
