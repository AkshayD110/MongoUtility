import pymongo
from pymongo import MongoClient
import ssl

class Connection:
    def __init__(self, mongoserver, port, username, password):
        self.mongoserver = mongoserver
        self.port = port
        self.username = username
        self.password = password


    def connectToMongo(self):

        client = MongoClient(host=self.mongoserver, port=self.port, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        client.the_database.authenticate(self.username, self.password, mechanism='SCRAM-SHA-1', source='admin')
        return client
        # db = client[self.tenant]
        # print("connected")
        # collection = db['compliance_audit_indexed']
        # numberOfRecords = collection.count()
        # print(numberOfRecords)
