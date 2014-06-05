__author__ = 'arkilic'
import time
import datetime

from metadataStore.database.client import MongoConnection
from metadataStore.database.collection import Header, BeamlineConfig, Event

MongoConnection('test', 'kronos.nsls2.bnl.gov', 27017)

header = Header(_id=0, owner='arkilic', start_time=datetime.datetime.utcnow(),
                end_time=datetime.datetime.utcnow(), beamline_id='xyz').save()
for i in xrange(100):
    start = time.time()
    cfg = BeamlineConfig(headers=[header], wavelength=(234.5+i)).save()
    end = time.time()
    print 'Header takes ' + str((end-start)*1000) + ' milliseconds'
    # print BeamlineConfig.objects(headers__in=[header])


eventA = Event(_id=7, headers=[header], data={'motor1': 193}).save()


evr = Event.objects(headers__all=[header])
print evr[0].data