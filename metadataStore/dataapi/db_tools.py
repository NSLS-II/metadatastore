__author__ = 'arkilic'
__version__ = '0.0.2'
from metadataStore.database.collection import Header, BeamlineConfig, Event
from metadataStore.dataapi import session_init
#TODO: Add ranges to searches
#TODO: Add logging


def save_header(run_id, run_owner, run_start_time, run_end_time, beamline_id):
    #TODO: add write_concern and safety measures to rollback
    header = Header(_id=run_id, owner=run_owner, start_time=run_start_time,
                    end_time =run_end_time, beamline_id=beamline_id).save()


def get_header(run_id, run_owner=None, run_start_time=None, run_end_time=None, beamline_id=None):
    header = Header.objects(_id=run_id)
    return header


def record_event(event_id, header_id, seqno, description, data):
    header_list = get_header(header_id)
    if not header_list:
        #logger
        raise ValueError('run_header cannot be located. Chek header_id')
    try:
        event = Event(_id=event_id, headers=header_list, seqno=seqno, description=description, data=data).save()
    except:
        raise
    return event


def save_beamline_config(header_id, energy, wavelength, i_zero, diffractometer, beamline_cfg_id=None):
    header_list = get_header(header_id)
    if not header_list:
        #logger
        raise ValueError('run_header cannot be located. Chek header_id')
    if beamline_cfg_id is None:
        beamline_cfg = BeamlineConfig(headers=header_list, enery=energy, wavelength=wavelength,
                                      i_zero=izero, diffractometer=diffractometer)
    else:
        beamline_cfg = BeamlineConfig(_id= beamline_cfg_id, headers=header_list, enery=energy, wavelength=wavelength,
                                      i_zero=izero, diffractometer=diffractometer)
    try:
        beamline_cfg.save()
    except:
        #logger
        raise
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


def find():
    """
    Find by event_id, beamline_config_id, header_id
    """
    pass
