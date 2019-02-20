import pymongo
from pymongo import MongoClient
import ssl
import config

class Connection:
    def __init__(self,  whichDb):
        self.whichDb = whichDb



    def connectToMongo(self):
        if (self.whichDb == 1):
            mongoserver= config.PERF_LAB['mongo_router_ip']
            port = config.PERF_LAB['mongo_port']
            username = config.PERF_LAB['mongo_username']
            password = config.PERF_LAB['mongo_password']
            client = MongoClient(host=mongoserver, port=port, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
            client.the_database.authenticate(username, password, mechanism='SCRAM-SHA-1', source='admin')
            return client

        elif (self.whichDb == 2):
            mongoserver = config.PERF04_SOFTLAYER_LAB['mongo_router_ip']
            port = config.PERF04_SOFTLAYER_LAB['mongo_port']
            username = config.PERF04_SOFTLAYER_LAB['mongo_username']
            password = config.PERF04_SOFTLAYER_LAB['mongo_password']
            client = MongoClient(host=mongoserver, port=port, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
            client.the_database.authenticate(username, password, mechanism='SCRAM-SHA-1', source='admin')
            return client

        elif (self.whichDb == 3):
            mongoserver = config.STORAGE_LAB['mongo_router_ip']
            port = config.STORAGE_LAB['mongo_port']
            username = config.STORAGE_LAB['mongo_username']
            password = config.STORAGE_LAB['mongo_password']
            client = MongoClient(host=mongoserver, port=port, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
            client.the_database.authenticate(username, password, mechanism='SCRAM-SHA-1', source='admin')
            return client

        else:
            return "Enter one of the following values for selecting DB. " \
                   "1" \
                   "2" \
                   "3"

        # db = client[self.tenant]
        # print("connected")
        # collection = db['compliance_audit_indexed']
        # numberOfRecords = collection.count()
        # print(numberOfRecords)
