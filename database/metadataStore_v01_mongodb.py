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
        try:
            self.client = MongoClient(host, port)
        except:
            self.logger.warning('MongoClient cannot be created')
            raise Exception('MongoClient cannot be created')
        self.db = self.client.metadataStore
        #TODO: template_depot and collection depot will parse json-like run_headers from confiration file
        self.template_depot = dict()
        self.collection_depot = list()

    def create_document_template(self, name,fields):
        """
        Creates a document template and appends it to template_depot
        """
        if isinstance(fields, list):
            composed_collection = dict()
            for field in fields:
                composed_collection[field] = None
            self.template_depot[name] = composed_collection
        else:
            raise ValueError('fields must be of type python list')
    
    def create_collection(self, name):
        """
        Creates a collection with specified name that is used for grouping documents in a logbook-like way
        """
        try:
            collection = self.db.name
            self.collection_depot.append(collection)
        except:
            self.logger.warning('Collection cannot be created')
            raise Exception('Collection cannot be created')

    def add_to_doc(self, template_name, field):
        if template_name not in self.template_depot.keys():
            raise ValueError('Document template with specified name does not exist')
        else:
            temp = self.template_depot[template_name] 
            temp[field] = None
            self.template_depot[template_name] = temp

    def remove_from_doc(self, template_name, field):
        if template_name not in self.template_depot.keys():
            raise ValueError('Document template with specified name does not exist')
        else:
            temp = self.template_depot[template_name] 
            new_temp = dict()
            for name in temp.keys():
                if name is not field:
                    new_temp[name] = temp[name]
            self.template_depot[template_name] = new_temp

    def delete_document_template(self, template_name):
        if template_name not in self.template_depot.keys():
            raise ValueError('Document template with specified name does not exist')
        else:
            self.template_depot.pop(template_name, None)


a = MetadataStore('localhost', 27017)
#print a.db.random_logbook.find()
a.create_document_template('arman', ['name'])
print a.template_depot
a.add_to_doc('arman', 'yeni')
print a.template_depot
a.remove_from_doc('arman', 'yeni')
print a.template_depot
a.delete_document_template('arman')
print a.template_depot
a.create_collection('logs_1')
