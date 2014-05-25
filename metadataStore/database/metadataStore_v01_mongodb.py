__author__ = 'arkilic'

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging


class MetadataStore(object):
    #TODO: Make sure existing collections are retrieved from the database
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
        try:
            self.client = MongoClient(host, port)
        except:
            self.logger.warning('MongoClient cannot be created')
            raise ConnectionFailure('MongoClient cannot be created')
        self.database = self.client['metaDataStore']
#Database operations

    def add_user(self, name, password, read_only=True):
        pass

    def remove_user(self, name):
        pass

    def authenticate(self):
        pass

    def mongo_command(self, command):
        """
        Sends a command directly to the database. Closest behavior pymongo has to ORM's core
        """
        pass

    def create_collection(self, name, **kwargs):
        pass

    def list_collections(self):
        return self.database.collection_names()

    def current_op(self):
        """
        Get information regarding current operations running
        """
        pass

    def drop_collection(self, name_or_collection):
        """
        Drop a collection either by name or collection object
        """
        pass

    def error(self):
        """
        Returns the latest error occured in the database
        """

    def session_logout(self):
        """
        Close connection between this client
        """
#client operations

    def insert(self, collection, document):
        try:
            self.database[collection].insert(document)
        except:
            self.logger.warning('Insert failed. Cannot connect to database')
            raise ConnectionFailure('Insert failed. Cannot connect to database')

    def save(self, document):
        pass

    def update(self, document):
        pass

    def remove(self, condition):
        pass

    def find(self, collection, condition):
        if condition is None:
            try:
                result = self.database[collection].find()
            except:
                self.logger.warning('Query failed. Cannot connect to database')
                raise ConnectionFailure('Query failed. Cannot connect to database')
        else:
            try:
                result = self.database[collection].find(condition)
            except:
                self.logger.warning('Query failed. Cannot connect to database')
                raise ConnectionFailure('Query failed. Cannot connect to database')
        return result

    def find_one(self, condition):
        pass

    def parallel_scan(self, num_cursors):
        pass

    def count(self):
        """
        Returns number of documents in a collection
        """
        pass

    def create_index(self):
        pass

    def ensure_index(self):
        pass

    def drop_index(self):
        pass

    def reindex(self):
        pass

    def options(self):
        pass

    def aggregate(self):
        pass

    def group(self, key, condition, initial, reduce, finalize=None, **kwargs):
        pass

    def rename(self, collection_name, new_name):
        pass

    def map_reduce(self):
        pass

    def find_and_modify(self):
        pass

#Bulk operations
    def bulk_insert(self, document_list):
        """
        >>> from pprint import pprint
        >>>
        >>> bulk = db.test.initialize_ordered_bulk_op()
        >>> # Remove all documents from the previous example.
        ...
        >>> bulk.find({}).remove()
        >>> bulk.insert({'_id': 1})
        >>> bulk.insert({'_id': 2})
        >>> bulk.insert({'_id': 3})
        >>> bulk.find({'_id': 1}).update({'$set': {'foo': 'bar'}})
        >>> bulk.find({'_id': 4}).upsert().update({'$inc': {'j': 1}})
        >>> bulk.find({'j': 1}).replace_one({'j': 2})
        >>> result = bulk.execute()
        >>> pprint(result)
        {'nInserted': 3,
         'nMatched': 2,
         'nModified': 2,
         'nRemoved': 10000,
         'nUpserted': 1,
         'upserted': [{u'_id': 4, u'index': 5}],
         'writeConcernErrors': [],
         'writeErrors': []}

        """
