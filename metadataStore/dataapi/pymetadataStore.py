__author__ = 'arkilic'

from metadataStore.dataapi.mongo_session_init import db
from dbConfig import collections, documents

"""
Provides routines that are smart and do the database operations in a pythonic way w/o exposing any aspect of database to client api.
This is done in a way such that database can be deployed locally to any beamline running on localhost at suggested port
and data_catalog-like applications can make use of this data_api module in order to save/restore information
"""


def insert(collection, document):
    if collection not in db.list_collections():
        #TODO: Get collections from db.listCollections()
        db.logger.warning('Cannot insert. Collection must be created before insert')
        raise ValueError('Cannot insert. Collection must be created before insert')
    else:
        db.insert(collection, document)


def create_collection(collection):
    """
    Create collection eagerly loads a collection into mongodb session using the dummy default document template
    """
    collection_list = db.list_collections()
    if collection in collection_list:
        return 'Collection has already been created'
    else:
        db.database[collection].insert(documents['default'])
        collections.append(collection)


def find(collection_name, **kwargs):
    """
    Returns a cursor to documents found given query criteria
    Return type: pymongo Cursor object
    """
    result = None
    if collection_name not in db.list_collections():
        raise ValueError('Collection with given name does not exist')
    else:
            result = db.find(collection_name, kwargs)
    return result


def query(collection_name, limit=50, **kwargs):
    """
    Returns a list of decomposed entries
    Return type: List of dictionaries
    """
    #TODO: use keywords to extract
    import pymongo
    db.database[collection_name].ensure_index([('Id', pymongo.DESCENDING)])
    cursor = find(collection_name, **kwargs)
    result = list()
    try:
        for i in xrange(limit):
            result.append(cursor.__getitem__(i))
    except IndexError:
        pass
    cursor.close()
    return result


def collection_count(name):
    return db.collection_count(collection_name=name)


def find_one():
    pass


def update():
    pass

