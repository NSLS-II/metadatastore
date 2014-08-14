__author__ = 'arkilic'

import random

from metadataStore.collectionapi.commands import create, record, search

s_id = random.randint(0, 10000)
create(header={'scan_id': s_id})
create(beamline_config={'scan_id': s_id})
create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'seq_no': 0})
record(event={'scan_id': s_id, 'descriptor_name': 'scan', 'owner': 'arkilic', 'seq_no': 0,
              'data': {'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'},'description': 'Linear scan'})
search(scan_id=s_id)
search(scan_id=s_id, owner='ark*')