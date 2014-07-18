__author__ = 'arkilic'
import datetime
from metadataStore.userapi.commands import *
import time
import datetime


"""
Sample dictionary used for creating a sample run_header and beamline_config
"""
####Create a new header and beamline config######
sample_dict = {'header': {'run_id': 1903, 'run_owner': 'arkilic', 'beamline_id': 'csx', 'custom': {},
                          'start_time': datetime.datetime.utcnow()},
                'beamline_config':{'beamline_config_id': 122, 'header_id': 1903,
                                   'wavelength': 12.345, 'custom': {'new_field': 'value'}}}
create(sample_dict)


#Create only the header
sample_dict2 = {'header': {'run_id': 1905, 'run_owner': 'arkilic', 'beamline_id': 'csx', 'custom': {},
                           'start_time': datetime.datetime.utcnow()},
                'beamline_config': {}}
create(sample_dict2)

#Create only beamline_config
sample_dict3 = {'header': {},'beamline_config': {'beamline_config_id': 1234, 'header_id': 1903, 'wavelength': 12.345,
                                                 'custom': {'some_field': 'some_value'}}}
create(sample_dict3)
##########################################################

####Create Log entries####################################
#Simple text logging
# for i in xrange(100000):
#     text_field = 'my first text log attempt'
#     run_id_field = 109 + i
#     event_type_id = 34
#     start = time.time()
#     log(text=text_field, owner='arkilic', event_id=i, run_id=run_id_field, event_type_id=34,
#         header_id=1903)
#     end = time.time()
#     print str((end-start)*1000) + ' ms'


text_field = 'my first text log attempt'
# run_id_field = 109 + i
event_type_id = 34
start = time.time()
print search(event_type=34, contents=True)
end = time.time()
print str((end-start)*1000) + ' ms'