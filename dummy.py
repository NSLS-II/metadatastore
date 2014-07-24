__author__ = 'arkilic'
from metadataStore.dataapi.raw_commands import *
#
import time
import random
for i in xrange(1, 100000):
    h_id = random.randint(0, 200000)
    bc_id = random.randint(200000,450000)
    ev_d_id = random.randint(100,200000)
    start = time.time()
    save_header(header_id=h_id, beamline_id='csx29', scan_id=1)
    end = time.time()
    print('Header insert time is '+ str((end-start)*1000) + ' ms')


    start = time.time()
    insert_event_descriptor(event_descriptor_id=ev_d_id, header_id=h_id, event_type_id=1, event_type_name='scan')
    end = time.time()
    print('Descriptor insert time is '+ str((end-start)*1000) + ' ms')



    start = time.time()
    hdr = find(header_id='current', contents=True)
    end = time.time()
    print('Header query time is '+str((end-start)*1000) + ' ms')

    start = time.time()
    save_beamline_config(beamline_cfg_id=bc_id, header_id=h_id, config_params={'hkl': [1,1,0]})
    end = time.time()
    print('BeamlineConfig insert time is '+str((end-start)*1000) + ' ms')

    # hdr = find(header_id='last', contents=True)
    # hdr = find(header_id=134, contents=True)