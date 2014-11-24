__author__ = 'arkilic'

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from metadataStore.config.parseConfig import database, host, port
from metadataStore.sessionManager.databaseLogger import DbLogger


conn = MongoClient(host=host, port=int(port))
db = conn['metaDataStore']


metadataLogger = DbLogger(db_name=database, host=host, port=int(port))
