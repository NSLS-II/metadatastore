__author__ = 'arkilic'
import six
import random
import time
from metadataStore.collectionapi.commands import create, record, search

s_id = random.randint(0, 10000)
s_id2 = random.randint(0, 10000)
"""
>>> create(header={'scan_id': s_id})
>>> create(beamline_config={'scan_id': s_id})
"""
# create(header=[{'scan_id': s_id, 'tags': ['CSX_collection', 'arman']}, {'scan_id': s_id2}]) #Bulk Header create

create(header={'scan_id': s_id, 'tags': ['CSX_collection', 'arman']})

#TODO: Bulk header create does not create using the default!!!!

data = {'motor4': 13.4, 'image1': '/home/arkilic/sample.tiff'}
create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental', 'data_keys': list(six.iterkeys(data))})
create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'ascan', 'event_type_id': 13, 'tag': 'experimental', 'data_keys': list(six.iterkeys(data))})

"""
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0})
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})
"""

record(event=[{'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0},
              {'scan_id': s_id, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
              'data': data,'description': 'Linear scan'}])

record(event={'scan_id': s_id, 'seq_no': 2, 'descriptor_name': 'scan'})
# record({'scan_id': s_id, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
#               'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})

query_a = search(scan_id=s_id, data=True)
print s_id
#Fix insert
print query_a['header_0'].keys()
#TODO: Fix collection api search
print query_a['header_0']['event_descriptors']['event_descriptor_0']['events']
print query_a['header_0']['event_descriptors']['event_descriptor_1']['events']

record(event={'scan_id': s_id, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'some_motor_1': 16.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})

res = search(owner='arkilic', data=True, event_classifier={'data.some_motor_1': 16.4})
# for entry in res:
#     print res[entry]['event_descriptors']['event_descriptor_1']