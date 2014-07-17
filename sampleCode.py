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
files = []
darks = []
file_root = "~/X1Data/LSCO_Oct13_0397/LSCO_Oct13_0397-"
file_suffix = "_0000.spe"
for i in range(121):
    idx = str(i)
    while(len(idx)) != 4:
        idx = "0" + idx
    if (i % 5) != 0:
        files.append(file_root + idx + file_suffix)
    else:
        darks.append(file_root + idx + "-DARK" + file_suffix)


log(text='LSCO_Oct13_0397 Data + dark log attempt 1', owner='edill', event_id=3, run_id=109, event_type_id=13, header_id=1903, seqno=0, data={"motor1" : 12.4, "motor2" : 15, "motor3" : 20, "detector" : files, "darks" : darks})

print search(header_id=1903)