__author__ = 'arkilic'

from pymongo import MongoClient
import logging


class MetadataStore(object):
    def __init__(self, host, port):
        """
        Constructor: MongoClient, Database, and native python loggers are created
        """
        self.logger = logging.getLogger('MetadataStore')
        log_handler = logging.FileHandler('/var/tmp/MetaDataStore.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.WARNING)
        self.client = MongoClient(host, port)
        self.db = self.client.metadataStore

    def create_collection(self, name, owner):
        pass







# a = MetadataStore('localhost', 27017)
# print a.db.random_logbook.find()