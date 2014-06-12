__author__ = 'arkilic'
__version__ = '0.0.2'
from metadataStore.dataapi.metadataTools import *
import time
import datetime

start_time = datetime.datetime.utcnow()
# start = time.time()
# save_header(run_id=3, run_owner='arkilic', create_time=start_time, beamline_id='csx')

save_header(run_id=0, run_owner='arkilic', create_time=datetime.datetime.utcnow(),
            beamline_id='xyz34', update_time=None)
# print get_header(3)
# end = time.time()
# print 'Header insert takes ' + str((end-start)*1000) + ' milliseconds'
#
#
# record_event(event_id=1935,header_id=1903, start_time= datetime.datetime.utcnow(), end_time= datetime.datetime.utcnow(), description='sample event record given event_id and header')
#
#

# for i in xrange(1000):
#     id = (98+i)
#     data = {'name': 'value', 'motor': 13.4}
#     start = time.time()
#     record_event(event_id=id, header_id=3, seqno=i, description='text', data=data, start_time = start,
#                  end_time=datetime.datetime.utcnow())
#     end = time.time()
#     print 'Event insert takes' + str((end-start)*1000) + ' milliseconds'