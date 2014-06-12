# __author__ = 'arkilic'
import time
import datetime

from metadataStore.dataapi.metadataTools import *
from metadataStore.database.databaseTables import *
from metadataStore.database.databaseTables import BeamlineConfig, Header


header = Header(_id=140, owner='arkilic', create_time=datetime.datetime.utcnow(), update_time=datetime.datetime.utcnow(), beamline_id='xyz')

start = time.time()
header = save_header(run_id=130, run_owner='arkilic', create_time=datetime.datetime.utcnow(), update_time=datetime.datetime.utcnow(), beamline_id='xyz')
end = time.time()
print 'It takes ' + str((end-start)*1000) + ' milliseconds'



header = save_header(run_id=137, run_owner='arkilic', create_time=datetime.datetime.utcnow(),
                     update_time=datetime.datetime.utcnow(), beamline_id='xyzaag')


BeamlineConfig(_id=219, headers=[header]).save()

bcfg = save_beamline_config(header_id=130, beamline_cfg_id=7)


bcfg = save_beamline_config(header_id=130, beamline_cfg_id=317)

print BeamlineConfig.objects()