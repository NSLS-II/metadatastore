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
create(header=[{'scan_id': s_id, 'tags': ['CSX_collection', 'arman']}, {'scan_id': s_id2}]) #Bulk Header create

create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'ascan', 'event_type_id': 13, 'tag': 'experimental'})

"""
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0})
>>> record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})
"""

#TODO: Fix whatever is wrong with bulk insert on events beacuse something is seriously wrong
record(event=[{'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0},
              {'scan_id': s_id, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'}])


record({'scan_id': s_id, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})

query_a = search(scan_id=s_id, data=True)

print query_a['header_0']['event_descriptors']['event_descriptor_0']['descriptor_name']
print query_a['header_0']['event_descriptors']['event_descriptor_1']['descriptor_name']

print query_a['header_0']['event_descriptors']['event_descriptor_0']['data_keys']
print query_a['header_0']['event_descriptors']['event_descriptor_1']['data_keys']
