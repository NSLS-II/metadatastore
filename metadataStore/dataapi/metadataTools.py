__author__ = 'arkilic'
__version__ = '0.0.2'
from mongoengine.errors import OperationError
from metadataStore.database.databaseTables import Header, BeamlineConfig, Event
from metadataStore.sessionManager.databaseInit import metadataLogger
import re


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


def find(header_id=None, owner=None, create_time=None, update_time=None, ):
    """
    Find by event_id, beamline_config_id, header_id
    As of MongoEngine 0.8 the querysets utilise a local cache.
    So iterating it multiple times will only cause a single query.
    If this is not the desired behavour you can call no_cache (version 0.8.3+)
     to return a non-caching queryset.
    # """
    wild_cards = ['*', '.', '$']
    query_dict = dict()
    if owner is not None:
        for entry in wild_cards:
            if entry in owner:
                query_dict['owner'] = {'$regex': re.compile(owner, re.IGNORECASE)}
                break
            else:
                query_dict['owner'] = owner
    if header_id is not None:
        if isinstance(header_id, list):
            if len(header_id) == 2:
                query_dict['_id'] = {'$gte': header_id[1], '$lte': header_id[0]}
            elif len(header_id) == 1:
                query_dict['_id'] = header_id[0]
            else:
                query_dict['_id'] = {'$in': header_id}
        else:
            query_dict['_id'] = header_id

    if create_time is not None:
        #TODO: Implement similar range search on create_time as in header_id
        pass

    print query_dict
    header_info = find_header(query_dict)
    #TODO: Once header_id is obtained pull all beamline_config and events, pack them into a list and export ;)
    return header_info


def find_header(query_dict):
    collection = Header._get_collection()
    return collection.find(query_dict)


def find_event(header_ids, **kwargs):
    kwargs['headers'] = [header_ids]
    collection = Event._get_collection()
    return collection.find(kwargs)


def find_beamline_config(header_ids, **kwargs):
    kwargs['headers'] = [header_ids]
    collection = BeamlineConfig._get_collection()
    return collection.find(kwargs)

