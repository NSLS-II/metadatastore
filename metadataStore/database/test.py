# __author__ = 'arkilic'
import time
import datetime

from metadataStore.dataapi.metadataTools import *
from metadataStore.database.databaseTables import *
from metadataStore.database.databaseTables import BeamlineConfig, Header

header1 = save_header(run_id=437, run_owner='arkilic', start_time=datetime.datetime(2014,4,10),beamline_id='xyz')
bcfg = save_beamline_config(beamline_cfg_id=1, header_id=437, wavelength=12.674)
for i in xrange(800):
    event = record_event(event_id=i, header_id=437, start_time=datetime.datetime(2014,10,1),
                         end_time=datetime.datetime.utcnow(), data={'name': ('arman'+ str(i)), 'lastname': 'arkilic'})
#
# result = find(header_id={'start': 137, 'end':437}, contents=True)
# for entry in result:
#     print entry

# result = find(owner='ark*', contents=True)
# for entry in result:
#     print entry

# result = find(header_id=437, contents=True)
# for entry in result:
#     print entry

# print find(header_id='l
start = time.time()
result = find(start_time={'start': datetime.datetime(2004, 1, 17, 0, 0),
                          'end': datetime.datetime(2040, 12, 17, 1, 1)}, contents=True)
end = time.time()
print (1000*(end-start))


for entry in result:
    print entry.keys()



# print find(header_id='last', contents=True)
start = time.time()
db = Header._get_db()
crsr3 = db['header'].find({'start_time': {'$lt': datetime.datetime(2040, 12, 17, 1, 1),
                                          '$gte': datetime.datetime(2004, 1, 17, 0, 0)}})
print crsr3.count()
end = time.time()

print (1000*(end-start))
# for i in xrange(crsr3.count()):
#     print crsr3.__getitem__(i)
