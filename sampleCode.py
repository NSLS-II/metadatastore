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
log(text='my first text log attempt', owner='arkilic', event_id=0, header_id=1903, seq_no=0)

#Data Logging with default end_date= datetime.datetime.utcnow()
sample_data = {'motor1': 12, 'motor2': 15, 'temp': -145.4, 'crystal': [90, 45, 45],
               'url': '/Users/arkilic/Desktop/Screen Shot 2014-06-24 at 2.26.42 PM.png'}

log(text='my second log attempt', owner='arkilic', event_id=1, header_id=1903,
    start_time=datetime.datetime(2014,1,1), data=sample_data, seq_no=1)


#Search logged Entry with given id
search(header_id=1903, custom={'ark':1}, contents=True)

search(start_time = {'start': datetime.datetime(2013, 6, 13, 17, 51, 21, 987000),
                     'end': datetime.datetime(2014, 6, 26, 17, 51, 21, 987000)})
# search(event_id=0, contents=True)