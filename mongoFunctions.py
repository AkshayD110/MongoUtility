import mongoConnection
import config

def get_connection(whichDb):
    #if it is PerfLab
    if(whichDb==1):
        new_connection = mongoConnection.Connection(config.DB1_CONFIG['mongo_router_ip'],
                                                    config.DB1_CONFIG['mongo_port'],
                                                    config.DB1_CONFIG['mongo_username'],
                                                    config.DB1_CONFIG['mongo_password'])

    #if it is Perf04-softLayer
    elif(whichDb==2):
        new_connection = mongoConnection.Connection(config.DB1_CONFIG['mongo_router_ip'],
                                                    config.DB1_CONFIG['mongo_port'],
                                                    config.DB1_CONFIG['mongo_username'],
                                                    config.DB1_CONFIG['mongo_password'])
    #if it is StroageLab
    elif(whichDb==3):
        new_connection = mongoConnection.Connection(config.DB1_CONFIG['mongo_router_ip'],
                                                    config.DB1_CONFIG['mongo_port'],
                                                    config.DB1_CONFIG['mongo_username'],
                                                    config.DB1_CONFIG['mongo_password'])

    else:
        print("Enter an appropriate value")

def document_count():
    pass
