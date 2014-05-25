__author__ = 'arkilic'

from metadataStore.dataapi.mongo_session_init import db
from dbConfig import collections, documents

"""
Provides routines that are smart and do the database operations in a pythonic way w/o exposing any aspect of database to client api.
This is done in a way such that database can be deployed locally to any beamline running on localhost at suggested port
and data_catalog-like applications can make use of this data_api module in order to save/restore information
"""


def insert(collection, document):
    if collection not in collections:
        #TODO: Get collections from db.listCollections()
        db.logger.warning('Cannot insert. Collection must be created before insert')
        raise ValueError('Cannot insert. Collection must be created before insert')
    else:
        db.insert(collection, document)


def create_collection(collection):
    """
    Create collection eagerly loads a collection into mongodb session using the dummy default document template
    """
    if collection in collections:
        raise ValueError('Collection has already been created')
    else:
        db.database[collection].insert(documents['default'])
        collections.append(collection)


def find(collection_name, **kwargs):
    """
    Replace with wildcards
    """
    result = None
    if collection_name not in collections:
        raise ValueError('Collection with given name does not exist')
    else:
            result = db.find(collection_name, kwargs)
    return result


def find_one():
    pass


def count():
    pass
