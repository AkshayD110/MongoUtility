import mongoConnection
import config

def get_connection(whichDb):
    #if it is PerfLab
    if(whichDb==1):
        new_connection = mongoConnection.Connection(config.PERF_LAB['mongo_router_ip'],
                                                    config.PERF_LAB['mongo_port'],
                                                    config.PERF_LAB['mongo_username'],
                                                    config.PERF_LAB['mongo_password'])

    #if it is Perf04-softLayer
    elif(whichDb==2):
        new_connection = mongoConnection.Connection(config.STORAGE_LAB['mongo_router_ip'],
                                                    config.STORAGE_LAB['mongo_port'],
                                                    config.STORAGE_LAB['mongo_username'],
                                                    config.STORAGE_LAB['mongo_password'])
    #if it is StroageLab
    elif(whichDb==3):
        new_connection = mongoConnection.Connection(config.STORAGE_LAB['mongo_router_ip'],
                                                    config.STORAGE_LAB['mongo_port'],
                                                    config.STORAGE_LAB['mongo_username'],
                                                    config.STORAGE_LAB['mongo_password'])

    else:
        print("Enter an appropriate value")

def document_count():
    pass
