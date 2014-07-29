__author__ = 'arkilic'
from metadataStore.dataapi.raw_commands import *
#
import time
import random
h_id = random.randint(0, 200000)
bc_id = random.randint(0, 450000)
ev_d_id = random.randint(0, 200000)
start = time.time()
save_header(header_id=h_id, beamline_id='csx29', scan_id=1)
end = time.time()
print('Header insert time is ' + str((end-start)*1000) + ' ms')


start = time.time()
insert_event_descriptor(event_descriptor_id=ev_d_id, header_id=h_id, event_type_id=1, event_type_name='scan')
end = time.time()
print('Descriptor insert time is ' + str((end-start)*1000) + ' ms')



start = time.time()
hdr = find(header_id='current', contents=True)
end = time.time()
print('Header query time is '+str((end-start)*1000) + ' ms')

start = time.time()
save_beamline_config(beamline_cfg_id=bc_id, header_id=h_id, config_params={'hkl': [1, 1, 0]})
end = time.time()
print('BeamlineConfig insert time is '+str((end-start)*1000) + ' ms')


find(owner='arki*')
print find(owner='arkilic').keys()
print find(beamline_id='csx29').keys()

print find(start_time=datetime.datetime(2013,4, 4)).keys()

print find(header_id='current')
print find(header_id='last')
print find(end_time=datetime.datetime(2013,4, 4))
print find(start_time={'start': datetime.datetime(2012,1,1), 'end': datetime.datetime(2015,1,1)}).keys()