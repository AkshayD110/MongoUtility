import mongoConnection


def document_count(whichDb):
    mongo_client = mongoConnection.Connection.connectToMongo(whichDb)
