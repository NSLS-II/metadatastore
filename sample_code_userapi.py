__author__ = 'arkilic'

import random
from metadataStore.userapi.commands import create, record, search


s_id = random.randint(0, 10000)
seq_n = random.randint(0, 10)
create(header={'scan_id': s_id})
create(beamline_config={'scan_id': s_id})
create(event_descriptor={'scan_id': s_id, 'event_type_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n)
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n, data={'name': 'value'})
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n, data={'name': 'value'}, description='some entry')
print search(owner='arkilic')