__author__ = 'arkilic'

import random
import time
from metadataStore.collectionapi.commands import create, record, search

s_id = random.randint(0, 10000)
s_id2 = random.randint(0, 10000)
"""
>>> create(header={'scan_id': s_id})
>>> create(beamline_config={'scan_id': s_id})
"""
create(header=[{'scan_id': s_id}, {'scan_id': s_id2}]) #Bulk Header create

create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
"""
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0})
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})
"""
record(event=[{'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0},
              {'scan_id': s_id, 'descriptor_name': 'scan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'}])
print search(scan_id=s_id)
print search(scan_id=s_id, owner='ark*')
some_list = list()
for i in xrange(10000):
    some_list.append({'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': i})
start = time.time()
record(event=some_list)
end = time.time()
print 'It took ' + str((end-start)*1000) + ' milliseconds to process bulk inserts'