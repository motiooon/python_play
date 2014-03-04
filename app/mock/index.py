from pymongo import MongoClient
from faker import Factory
import datetime


class Mocker:
    def __init__(self):
        self.name = 'Mocker'
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client.people
        self.fake = Factory.create()

    def populate(self, number_of_docs=2):
        for doc in range(0, number_of_docs):
            person = {"author": self.fake.name(),
            "text": self.fake.text(),
            "tags": self.fake.random_element(array=("mongodb", "python", "pymongo")),
            "date": datetime.datetime.utcnow()}
            per = self.db.persons.insert(person)

        print "done inserting %i" % number_of_docs, 'of documents`'
