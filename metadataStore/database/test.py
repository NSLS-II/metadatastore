# __author__ = 'arkilic'
import time
import datetime

from metadataStore.dataapi.metadataTools import *
from metadataStore.database.databaseTables import *
from metadataStore.database.databaseTables import BeamlineConfig, Header


bcfg = save_beamline_config(beamline_cfg_id=1, header_id=437, wavelength=12.674)
for i in xrange(400):
    event = record_event(event_id=i, header_id=437, start_time=datetime.datetime(2014,10,1),
                         end_time=datetime.datetime.utcnow(), data={'name': ('arman'+ str(i)), 'lastname': 'arkilic'})
#
# result = find(header_id={'start': 137, 'end':437}, contents=True)
# for entry in result:
#     print entry

# result = find(owner='ark*', contents=True)
# for entry in result:
#     print entry

result = find(owner='arkili.', contents=True)
for entry in result:
    print entry

# print find(header_id='l


# print find(header_id='last', contents=True)

# db = Header._get_db()
# crsr3 = db['header'].find({'start_time': {'$lt': datetime.datetime(2040, 12, 17, 1, 1),
#                                           '$gte': datetime.datetime(2004, 1, 17, 0, 0)}})
# for i in xrange(crsr3.count()):
#     print crsr3.__getitem__(i)
