__author__ = 'arkilic'
from dbConfig import database, host, port
from metadataStore.database.client import MongoConnection

adapter = MongoConnection(db_name=database, host=host, port=port)
conn = adapter.get_conn()
db = conn.metaDataStore
