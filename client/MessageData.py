import datetime
import json

from faker import Faker
import random


class MessageData:
    def __init__(self):
        fake = Faker()
        self.timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")
        self.email = fake.email()
        self.username = fake.first_name()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.phone = fake.phone_number()
        self.address = fake.address()
        self.about = fake.paragraph(nb_sentences=5)

    def get_json(self):
        message = {
            'timestamp': self.timestamp,
            'email': self.email,
            'username': self.first_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'city': self.address,
            'about': self.about
        }
        return json.dumps(message)
