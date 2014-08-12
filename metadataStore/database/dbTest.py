__author__ = 'arkilic'
import random
import time

from metadataStore.database.databaseTables import *

for i in xrange(0,100):
    start = time.time()
    a = Header(start_time=datetime.datetime.utcnow(), scan_id=random.randint(100,1000000000), end_time=None).save(wtimeout=100, write_concern={'w': 1})
    end = time.time()
    print('It took ' + str((end-start)*1000) + 'milliseconds')

