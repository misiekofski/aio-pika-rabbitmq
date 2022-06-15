import datetime
import time
import json

from faker import Faker


class MessageData:
    def __init__(self):
        fake = Faker()
        self.current_date = datetime.datetime.now()
        self.email = fake.email()
        self.username = fake.first_name()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.phone = fake.phone_number()
        self.address = fake.address()
        self.about = fake.paragraph(nb_sentences=5)

    def get_json(self):
        message = {
            'timestamp': datetime.datetime.timestamp(self.current_date)*1000,
            'email': self.email,
            'username': self.first_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'city': self.address,
            'about': self.about
        }
        return json.dumps(message)
