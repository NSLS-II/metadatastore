__author__ = 'arkilic'
__version__ = '0.0.2'
from metadataStore.database.collection_depot import Header, BeamlineConfig, Event
from metadataStore.dataapi.session_init import db

#TODO: Add ranges to searches
#TODO: Add logging


def save_header(run_id, run_owner, create_time, beamline_id, update_time=None):
    #TODO: add write_concern and safety measures to rollback
    header_list = list_headers()
    for header in header_list:
        if header['_id'] == run_id:
            raise ValueError('Given run_id for the header exists')
        else:
            if update_time is None:
                update_time = create_time
            try:
                header = Header(_id=run_id, owner=run_owner, create_time=create_time,
                                update_time=update_time, beamline_id=beamline_id).save()
            except:
                raise
    return header


def list_headers():
    headers = Header.objects.all()
    headers_list = list()
    for header in headers:
        temp = dict()
        temp['_id'] = header._id
        temp['create_time'] = header.create_time
        temp['update_time'] = header.update_time
        temp['owner'] = header.owner
        headers_list.append(temp)
    return headers_list


def get_header(id):
    header_list = list_headers()
    print header_list
    for entry in header_list:
        if entry['_id'] == id:
            return entry
        else:
            return None


def record_event(event_id, header_id, seqno, description, start_time, end_time, data):
    header_list = get_header(header_id)

    #TODO: add write_concern and safety measures to rollback
    if not header_list:
        #logger
        raise ValueError('run_header cannot be located. Check header_id')
    try:
        event = Event(_id=event_id, headers=header_list, seqno=seqno, start_time=start_time, end_time=end_time,
                      description=description, data=data).save()
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

