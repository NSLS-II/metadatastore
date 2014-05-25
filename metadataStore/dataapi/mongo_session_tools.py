__author__ = 'arkilic'

from metadataStore.database.metadataStore_v01_mongodb import MetadataStore
#TODO: Read session information from configuration file
"""
session tools provide the tools for a session to be initiated, exported, stored etc...
"""


def init_mongoSession(host, port, documents, collections):
    """
    Returns a metadataStore database object db after creating documents, collections etc
    """
    db = MetadataStore(host, port)
    eager_load(db, collections, documents)
    return db


def eager_load(db, collections, documents):
    """
    Creates collections using default document template from config file with null entries
    """
    for collection in collections:
        db.insert(collection, documents['default'])

"""
Enforce document templates. Add to config dictionary
"""