from party.chat import Chat
from faker import Faker

fake = Faker()

Chat.init()

def generate_message():
    Chat.insertMessage(fake.text(), fake.name(), fake.date_time().isoformat())

MESSAGE_COUNT = 100000
for i in range(MESSAGE_COUNT):
    generate_message()
