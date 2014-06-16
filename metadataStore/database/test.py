# __author__ = 'arkilic'
import time
import datetime

from metadataStore.dataapi.metadataTools import *
from metadataStore.database.databaseTables import *
from metadataStore.database.databaseTables import BeamlineConfig, Header


# header = Header(_id=140, owner='arkilic', create_time=datetime.datetime.utcnow(),
#                 update_time=datetime.datetime.utcnow(), beamline_id='xyz')
#
# start = time.time()
# header = save_header(run_id=130, run_owner='arkilic', create_time=datetime.datetime.utcnow(),
#                      update_time=datetime.datetime.utcnow(), beamline_id='xyz')
# end = time.time()
# print 'It takes ' + str((end-start)*1000) + ' milliseconds'
#
#
#
header = save_header(run_id=237, run_owner='arkilic', create_time=datetime.datetime.utcnow(),
                     update_time=datetime.datetime.utcnow(), beamline_id='xyzaag')
#
#
# BeamlineConfig(_id=219, headers=[header]).save()
#
# bcfg = save_beamline_config(header_id=130, beamline_cfg_id=7)
#
#
# # bcfg = save_beamline_config()
#
# print Header.objects(owner__contains='ark')
# print BeamlineConfig.objects(author__owner='arkilic')
#
#
# print Event.objects(headers=1903)


# crsr1 = find_beamline_config(header_ids=130, _id=90)
# for i in xrange(crsr1.count()):
#     print crsr1.__getitem__(i)
#
crsr2 = find(header_id=[237, 130, 137], owner='ark*')
for i in xrange(crsr2.count()):
    print crsr2.__getitem__(i)



#
#
# db = Header._get_db()
# # crsr3 = db['header'].find({'_id': 130})
# # for i in xrange(crsr3.count()):
# #     print crsr3.__getitem__(i)
# print db.header.find({'_id': {'$in':[130, 137, 237]}}).count()