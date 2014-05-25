__author__ = 'arkilic'

from metadataStore.dataapi.mongo_session_tools import *
from dbConfig import collections, documents, port, host

db = init_mongoSession(host, port, documents, collections)