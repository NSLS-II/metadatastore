__author__ = 'arkilic'
__version__ = '0.0.2'
from mongoengine.errors import OperationError
from metadataStore.database.databaseTables import Header, BeamlineConfig, Event
from metadataStore.sessionManager.databaseInit import metadataLogger
import re
import datetime

#TODO: Mongoengine index creation pattern


def save_header(run_id, run_owner, start_time, beamline_id, update_time):
    #TODO: add write_concern and safety measures to rollback
    if update_time is None:
        update_time = start_time
    try:
        header = Header(_id=run_id, owner=run_owner, start_time=start_time,
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
    #TODO: add end_time to each header with given _id once event recorded
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


def __update_header():
    #TODO: Once event is complete this routine is triggered to update the end_time of the event
    pass


def delete_event():
    pass


def delete_header():
    """
    Delete a header and all related events, beamline configs etc
    """
    #TODO: Delete all relational data alongside this?
    pass


def find(header_id=None, owner=None, start_time=None, update_time=None, beamline_id=None):
    """
    Find by event_id, beamline_config_id, header_id
    As of MongoEngine 0.8 the querysets utilise a local cache.
    So iterating it multiple times will only cause a single query.
    If this is not the desired behavour you can call no_cache (version 0.8.3+)
     to return a non-caching queryset.
     Usage:
     >>> find(header_id=130)
     >>> find(header_id=[130,123,145,247,...])
     >>> find(header_id={'start': 129, 'end': 141})
     >>> find(create_time=date.datetime(2014, 6, 13, 17, 51, 21, 987000)))
      >>> find(create_time=date.datetime(2014, 6, 13, 17, 51, 21, 987000)))
      >>> find(create_time={'start': datetime.datetime(2014, 6, 13, 17, 51, 21, 987000),'end': datetime.datetime(2014, 6, 13, 17, 51, 21, 987000)})
      >>> find(event_time=datetime.datetime(2014, 6, 13, 17, 51, 21, 987000)
      >>> find(event_time={'start': datetime.datetime(2014, 6, 13, 17, 51, 21, 987000})
    # """
    supported_wildcard = ['*', '.', '?']
    query_dict = dict()
    if owner is not None:
        for entry in supported_wildcard:
            if entry in owner:
                query_dict['owner'] = {'$regex': re.compile(owner, re.IGNORECASE)}
                break
            else:
                query_dict['owner'] = owner
    if header_id is not None:
        if isinstance(header_id, list):
            if len(header_id) == 1:
                query_dict['_id'] = header_id[0]
            else:
                query_dict['_id'] = {'$in': header_id}
        elif isinstance(header_id, dict):
            query_dict['_id'] = {'$gte': header_id['start'], '$lte': header_id['end']}
        else:
            query_dict['_id'] = header_id

    if start_time is not None:
        if isinstance(start_time, list):
            for time_entry in start_time:
                __validate_time(time_entry)
            query_dict['start_time'] = {'$in': start_time}
        elif isinstance(start_time, dict):
            #TODO: Replace validate time input with list avoid multiple lines of code
            __validate_time(start_time['start'])
            __validate_time(start_time['end'])
            query_dict['start_time'] = {'$gte': start_time['start'], '$lt': start_time['end']}
        else:
            if __validate_time(start_time):
                query_dict['start_time'] = {'$gte': start_time,
                                            '$lt': datetime.datetime.utcnow()}
    if beamline_id is not None:
        for entry in supported_wildcard:
            if entry in beamline_id:
                query_dict['beamline_id'] = {'$regex': re.compile(beamline_id, re.IGNORECASE)}
                break
            else:
                query_dict['beamline_id'] = beamline_id



    print query_dict
    header_info = find_header(query_dict)
    #TODO: Once header_id is obtained pull all beamline_config and events, pack them into a list and export ;)
    return header_info


def __validate_time(time_entry):
    if isinstance(time_entry, datetime.datetime):
        flag = True
    else:
        raise TypeError('Date must be datetime object')
    return flag


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

