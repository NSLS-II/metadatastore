__author__ = 'arkilic'
__version__ = '0.0.2'
from mongoengine.errors import OperationError
from metadataStore.database.databaseTables import Header, BeamlineConfig, Event
from metadataStore.sessionManager.databaseInit import metadataLogger
from pymongo import *
from metadataStore.sessionManager.databaseInit import conn

#TODO: Add ranges to searches

def save_header(run_id, run_owner, create_time, beamline_id, update_time):
    #TODO: add write_concern and safety measures to rollback
    header = None
    if update_time is None:
        update_time = create_time
    try:
        header = Header(_id=run_id, owner=run_owner, create_time=create_time,
                        update_time=update_time, beamline_id=beamline_id).save(wtimeout=100)
    except:
        metadataLogger.logger.warning('Header cannot be created')
        raise OperationError('Header cannot be created')
    return header


def list_headers():
    try:
        headers = Header.objects.all()
    except:
        metadataLogger.logger.warning('Headers cannot be accessed')
        raise OperationError('Headers cannot be accessed')
    return headers


def get_header(id):
    header_object = Header.objects(_id=id)
    return header_object


def record_event(event_id, header_id,  start_time, end_time, seqno=None, description=None, data=None):
    header_list = get_header(header_id)
    #TODO: add write_concern and safety measures to rollback
    if not header_list:
        metadataLogger.logger.warning('run_header cannot be located. Check header_id')
        raise ValueError('run_header cannot be located. Check header_id')
    try:
        event = Event(_id=event_id, headers=header_list, seqno=seqno, start_time=start_time, end_time=end_time,
                      description=description, data=data).save()
    except:
        metadataLogger.logger.warning('Event cannot be recorded')
        raise OperationError('Event cannot be recorded')
    return event


def save_beamline_config(beamline_cfg_id, header_id, energy=None, wavelength=None, i_zero=None, diffractometer=None):
    header_list = get_header(header_id)
    beamline_cfg = BeamlineConfig(_id=beamline_cfg_id, headers=header_list, enery=energy, wavelength=wavelength,
                                      i_zero=i_zero, diffractometer=diffractometer)
    try:
        beamline_cfg.save(wtimeout=100)
    except:
        metadataLogger.logger.warning('Beamline configuration cannot be saved')
        raise OperationError('Beamline configuration cannot be saved')
    return beamline_cfg


def update_header():
    pass


def update_event():
    pass


def delete_event():
    pass


def delete_header():
    """
    Delete a header and all related events, beamline configs etc
    """
    pass


def find(**kwargs):
    """
    Find by event_id, beamline_config_id, header_id
    """
    a =BeamlineConfig.objects(author__header_id=137)
    return a

    # db = conn['metaDataStore']
    # return db.header.find(**kwargs)





