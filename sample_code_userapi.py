__author__ = 'arkilic'

import random
from metadataStore.userapi.commands import create, record, search


<<<<<<< Temporary merge branch 1
s_id = random.randint(0, 10000)
seq_n = random.randint(0, 10)
=======
s_id = random.randint(0, 1000000)
seq_n = random.randint(0, 10)
print s_id
print search(scan_id=s_id)
print("s_id: {0}".format(s_id))
print("seq_n: {0}".format(seq_n))
>>>>>>> Temporary merge branch 2
create(header={'scan_id': s_id})
create(beamline_config={'scan_id': s_id})
create(event_descriptor={'scan_id': s_id, 'event_type_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n)
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n, data={'name': 'value'})
record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n, data={'name': 'value'}, description='some entry')
print search(owner='arkilic')