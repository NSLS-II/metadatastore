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

start = time.time()
insert_event_descriptor(scan_id=h_id, event_type_id=1, descriptor_name='scan')
end = time.time()
print('Descriptor insert time is ' + str((end-start)*1000) + ' ms')

start = time.time()
hdr3 = save_beamline_config(scan_id=h_id, config_params={'nam1': 'val'})
end = time.time()

start = time.time()
insert_event(scan_id=h_id, descriptor_name='scan', owner='arkilic', seq_no=0)
end = time.time()
print('Event insert time is ' + str((end-start)*1000) + ' ms')




start = time.time()
insert_event(scan_id=h_id, descriptor_name='scan', owner='arkilic', seq_no=1)
end = time.time()
print('Event insert time is ' + str((end-start)*1000) + ' ms')

start = time.time()
insert_event(scan_id=h_id, descriptor_name='scan', owner='arkilic', seq_no=2)
end = time.time()
print('Event insert time is ' + str((end-start)*1000) + ' ms')
#



# hdr3 = find(scan_id=h_id, data=True)
# print hdr3['header_0']['event_descriptors']['event_descriptor_0']['events'].keys()


start = time.time()
hdr1 = find(scan_id='current', data=True)
end = time.time()
print('Header query time is '+str((end-start)*1000) + ' ms')

start = time.time()
hdr2 = find(scan_id='current', data=False)
end = time.time()
print('Header query time is '+str((end-start)*1000) + ' ms')

start = time.time()
hdr3 = find(scan_id=h_id , data=False, num_header=4)
hdr3 = find(scan_id=h_id , data=False, num_header=4)
hdr3 = find(scan_id=h_id , data=False, num_header=4)
hdr2 = find(scan_id='current', data=False)
end = time.time()

# for entry in hdr3:
#     print entry.keys()

