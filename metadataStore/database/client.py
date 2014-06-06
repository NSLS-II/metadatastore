__author__ = 'arkilic'
__version__ = '0.0.2'
from mongoengine import connect
from pymongo.errors import ConnectionFailure
import logging


class MongoConnection(object):
    def __init__(self, db_name, host, port):
        """
        Constructor: MongoClient, Database, and native python loggers are created
        """
        self.logger = logging.getLogger('MetadataStore')
        log_handler = logging.FileHandler('/var/tmp/MetaDataStore.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.WARNING)
        self.host = host
        self.port = port
        self.db_name = db_name
        try:
            self.conn = connect(self.db_name, host=self.host, port=self.port)
        except:
            self.logger.warning('MongoClient cannot be created')
            raise ConnectionFailure('MongoClient cannot be created')
