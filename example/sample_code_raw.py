__author__ = 'arkilic'
import time
import random
from metadataStore.dataapi.commands import save_header, insert_event_descriptor, save_beamline_config, insert_event
from metadataStore.dataapi.commands import db, find, find2


h_id = random.randint(0, 200000)
h_id2 = random.randint(0, 200000)

bc_id = random.randint(0, 450000)
ev_d_id = random.randint(0, 200000)
start = time.time()
save_header(beamline_id='csx29', scan_id=h_id, tags=['arman', 123], header_versions=[0, 1, 3], header_owner='arman')
end = time.time()
print('Header insert time is ' + str((end-start)*1000) + ' ms')

start = time.time()
insert_event_descriptor(scan_id=h_id, event_type_id=1, descriptor_name='scan')
end = time.time()
print('Descriptor insert time is ' + str((end-start)*1000) + ' ms')

start = time.time()
hdr3 = save_beamline_config(scan_id=h_id, config_params={'nam1': 'val'})
end = time.time()

start = time.time()
insert_event(scan_id=h_id, descriptor_name='scan', owner='arkilic', seq_no=0, data={'motor1':12.44})
end = time.time()
print('Event insert time is ' + str((end-start)*1000) + ' ms')



sample_result = find(owner='arman', data=True, event_classifier={'data.motor1': 12.44})
print sample_result.keys()
print sample_result['header_0']

hdr, bcfg, e_desc, events = find2(scan_id=h_id)

print hdr.keys()
print e_desc.keys()
print events.keys()

print events[events.keys()[0]]['header_id']

print hdr[events[events.keys()[0]]['header_id']]
print e_desc[events[events.keys()[0]]['descriptor_id']]
