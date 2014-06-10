__author__ = 'arkilic'
import time
import datetime

from metadataStore.database.client import MongoConnection
from metadataStore.dataapi.db_tools import *
from metadataStore.database.collection_depot import *

MongoConnection('test', 'kronos.nsls2.bnl.gov', 27017)

header = save_header(run_id=36, run_owner='arkilic', create_time=datetime.datetime.utcnow(),
                     update_time=datetime.datetime.utcnow(), beamline_id='xyz')

