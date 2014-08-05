__author__ = 'arkilic'
import time
import random

from metadataStore.dataapi.raw_commands import *


h_id = random.randint(0, 200000)
bc_id = random.randint(0, 450000)
ev_d_id = random.randint(0, 200000)
start = time.time()
save_header(beamline_id='csx29', scan_id=h_id)
end = time.time()
print('Header insert time is ' + str((end-start)*1000) + ' ms')
#
start = time.time()
insert_event_descriptor(scan_id=h_id, event_type_id=1, event_type_name='scan')
end = time.time()
print('Descriptor insert time is ' + str((end-start)*1000) + ' ms')
#
start = time.time()
insert_event(scan_id=h_id, descriptor_name='scan', owner='arkilic')
end = time.time()
print('Event insert time is ' + str((end-start)*1000) + ' ms')
#
start = time.time()
hdr1 = find(scan_id='current', data=True)
end = time.time()
print('Header query time is '+str((end-start)*1000) + ' ms')
#
# start = time.time()
# hdr2 = find(header_id='current', data=False)
# print hdr2
# end = time.time()
# print('Header query time is '+str((end-start)*1000) + ' ms')

start = time.time()
hdr3 = find(scan_id=h_id, data=True)
print hdr3[hdr3.keys()[0]]['event_descriptor_0']['events']
end = time.time()
