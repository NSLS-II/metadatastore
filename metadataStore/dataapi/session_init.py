__author__ = 'arkilic'
from dbConfig import database, host, port
from metadataStore.database.client import MongoConnection

MongoConnection(db_name=database, host=host, port=port)
