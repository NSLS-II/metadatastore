__author__ = 'arkilic'
import random

from metadataStore.userapi.commands import create, record, search

h_id = random.randint(0,1000)
e_d_id = random.randint(0,2000)
e_t_id = random.randint(0,10)
b_c_id = random.randint(0,1000)
e_id = random.randint(0,1000)
create(entry_type='header', scan_id=123, header_id=h_id)
create(entry_type='event_descriptor', event_descriptor_id=e_d_id, header_id=h_id, event_type_id=e_t_id,
       type_descriptor={'my_field' + str(h_id): 'my_val' + str(e_d_id)}, tag = 'datacollection')
create(entry_type='beamline_config', beamline_cfg_id=b_c_id, header_id=h_id,
       config_params={'some_fieRld' + str(h_id): 'some_val' + str(e_d_id)})
record( event_id=e_id, descriptor_id=e_d_id, header_id=h_id, seq_no=random.randint(0,10), data={})
print search(header_id=579, contents=True)
