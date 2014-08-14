__author__ = 'arkilic'

import getpass
import datetime

from pymongo.errors import OperationFailure

from metadataStore.sessionManager.databaseInit import metadataLogger

from metadataStore.dataapi.raw_commands import save_header, save_beamline_config, insert_event, insert_event_descriptor, find


logger = metadataLogger.logger

#TODO: Use whoosh to add "did you mean ....?" for misspells


def create(header=None, beamline_config=None, event_descriptor=None):
    """
    Create header, beamline_config, and event_descriptor

    Parameters
    ----------
    :param header: Header attribute-value pairs
    :type header: dict

    :param beamline_config: BeamlineConfig attribute-value pairs
    :type beamline_config: dict

    :param event_descriptor: EventDescriptor attribute-value pairs
    :type event_descriptor: dict

    :raises: TypeError, ValueError, ConnectionFailure, NotUniqueError

    :returns: None

    Usage:

    >>> sample_header = {'scan_id': 1234}
    >>> create(header=sample_header)

    >>> create(header={'scan_id': 1235, 'start_time': datetime.datetime.utcnow(), 'beamline_id': 'my_beamline'})

    >>> create(header={'scan_id': 1235, 'start_time': datetime.datetime.utcnow(), 'beamline_id': 'my_beamline',
    ...                 'owner': 'arkilic'})

    >>> create(header={'scan_id': 1235, 'start_time': datetime.datetime.utcnow(), 'beamline_id': 'my_beamline',
    ...                 'owner': 'arkilic', 'custom': {'attribute1': 'value1', 'attribute2':'value2'}})

    >>> create(beamline_config={'scan_id': s_id})

    >>> create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})

    >>> create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental',
    ...                          'type_descriptor':{'attribute1': 'value1', 'attribute2': 'value2'}})

    >>> sample_event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental',
    ...                          'type_descriptor':{'attribute1': 'value1', 'attribute2': 'value2'}})
    >>> sample_header={'scan_id': 1235, 'start_time': datetime.datetime.utcnow(), 'beamline_id': 'my_beamline',
    ...                 'owner': 'arkilic', 'custom': {'attribute1': 'value1', 'attribute2':'value2'}})
    >>> create(event_descriptor=sample_event_descriptor, header=sample_header)

    >>> create(beamline_config={'scan_id': 1234})

    >>> create(beamline_config={'scan_id': 1234, 'config_params': {'attribute1': 'value1', 'attribute2': 'value2'}})

    >>> sample_event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental',
    ...                          'type_descriptor':{'attribute1': 'value1', 'attribute2': 'value2'}})
    >>> sample_header={'scan_id': 1235, 'start_time': datetime.datetime.utcnow(), 'beamline_id': 'my_beamline',
    ...                 'owner': 'arkilic', 'custom': {'attribute1': 'value1', 'attribute2':'value2'}})
    >>> sample_beamline_config = {'scan_id': 1234, 'config_params': {'attribute1': 'value1', 'attribute2': 'value2'}}
    >>> create(header=sample_header, event_descriptor=sample_event_descriptor, beamline_config=sample_beamline_config)
    """
    if header is not None:
        if isinstance(header, dict):
            if 'scan_id' in header:
                if isinstance(header['scan_id'], int):
                    scan_id = header['scan_id']
                else:
                    raise TypeError('scan_id must be an integer')
            else:
                raise ValueError('scan_id is a required field')
            if 'start_time' in header:
                start_time = header['start_time']
            else:
                start_time = datetime.datetime.utcnow()
            if 'owner' in header:
                owner = header['owner']
            else:
                owner = getpass.getuser()
            if 'beamline_id' in header:
                beamline_id = header['beamline_id']
            else:
                beamline_id = None
            if 'custom' in header:
                custom = header['custom']
            else:
                custom = dict()
            if 'status' in header:
                status = header['status']
            else:
                status = 'In Progress'
            try:
                save_header(scan_id=scan_id, header_owner=owner, start_time=start_time, beamline_id=beamline_id,
                            status=status, custom=custom)
            except:
                raise
        else:
            raise TypeError('Header must be a Python dictionary ')

    if beamline_config is not None:
        if isinstance(beamline_config, dict):
            if 'scan_id' in beamline_config:
                scan_id = beamline_config['scan_id']
            else:
                raise ValueError('scan_id is a required field')
            if 'config_params' in beamline_config:
                config_params = beamline_config['config_params']
            else:
                config_params = dict()
            try:
                save_beamline_config(scan_id=scan_id, config_params=config_params)
            except:
                raise
        else:
            raise TypeError('BeamlineConfig must be a Python dictionary')

    if event_descriptor is not None:
        if isinstance(event_descriptor, dict):
            if 'scan_id' in event_descriptor:
                scan_id = event_descriptor['scan_id']
            else:
                raise ValueError('scan_id is required for EventDescriptor entries')
            if 'event_type_id' in event_descriptor:
                event_type_id = event_descriptor['event_type_id']
            else:
                event_type_id = None
            if 'descriptor_name' in event_descriptor:
                descriptor_name = event_descriptor['descriptor_name']
            else:
                raise ValueError('descriptor_name is required for EventDescriptor')
            if 'type_descriptor' in event_descriptor:
                type_descriptor = event_descriptor['type_descriptor']
            else:
                type_descriptor = dict()
            if 'tag' in event_descriptor:
                tag = event_descriptor['tag']
            else:
                tag = None
            try:
                insert_event_descriptor(scan_id=scan_id, event_type_id=event_type_id, descriptor_name=descriptor_name,
                                        type_descriptor=type_descriptor, tag=tag)
            except:
                raise
        else:
            raise TypeError('EventDescriptor must be a Python dictionary')


def record(scan_id, descriptor_name, seq_no, owner=getpass.getuser(), data=dict(), description=None):
    """
    Events are saved given scan_id and descriptor name and additional optional parameters

    Parameters
    ----------
    :param scan_id: Unique run identifier
    :type scan_id: int, required

    :param descriptor_name: EventDescriptor that serves as an Event header
    :type descriptor_name: str, required

    :param seq_no: Data point sequence number
    :type seq_no: int, required

    :param owner: Run owner(default: unix session owner)
    :type owner: str, optional

    :param data: Serves as an experimental data storage structure
    :type data: dict, optional

    :param description: Provides user specified text to describe a given event
    :type description: str, optional

    :raises: ConnectionFailure, NotUniqueError, ValueError

    Usage:
    >>> record(scan_id=135, descriptor_name='some_scan', seq_no=0)

    >>> record(scan_id=135, descriptor_name='some_scan', seq_no=1, owner='arkilic')

    >>> record(scan_id=135, descriptor_name='some_scan', seq_no=2, data={'name': 'value'})

    >>> record(scan_id=135, descriptor_name='some_scan', seq_no=2, data={'name': 'value'},
           ... description='some entry')
    """

    try:
        insert_event(scan_id=scan_id, descriptor_name=descriptor_name, owner=owner, seq_no=seq_no, data=data,
                     description=description)
    except:
        raise

search_keys_dict = {
    'scan_id': {
        'description': 'The unique identifier of the run',
        'type': int},
    'owner': {
        'description': 'The user name of the person that created the header',
        'type': str},
    'start_time': {
        'description': 'The start time in utc',
        'type': datetime},
    'text': {
        'description': 'The description that the owner associated with the run',
        'type': str},
    'beamline_id': {
        'description': 'The identifier of the beamline.  Ex: CSX, SRX, etc...',
        'type': str},
    'data': {
        'description': 'True: returns all fields. False: returns some subset of the fields',
        'type': bool}}


def search(owner=None, start_time=None, end_time=None, scan_id=None,
           data=False, num_header=50):
    """
    Search the experimental database with the provided search keys. If no search
    keys are provided, the default behavior is to return nothing.

    Parameters
    ----------
    :param owner: User name to search on
    :type owner:str, optional

    :param start_time: Only return results after start_time
    :type start_time: datetime, optional

    :param end_time:Only return results before start_time
    :type end_time: datetime, optional

    :param scan_id : Search by specific scan_id.  If scan_id is a string, search() will try
                     to cast it to an integer.  If this fails, an error message will be logged
    :type scan_id: int, optional

    :param data: True: Add data to the returned dictionary
                 False: Don't include data in the returned dictionary. If data is a string, search() will test to see
                  if it's value is "True" or "False" and
    :type data: bool, optional

    :raise: TypeError, OperationError, ValueError

    :returns list :
        If the combination of search parameters finds something, a list of
        dictionaries is returned/
        If the combination of search parameters finds nothing or no search
        parameters are provided, None is returned
    """
    err_msg = ""
    search_dict = {}
    try:
        scan_id = int(scan_id)
    except ValueError:
        # this will be caught in the type checking
        pass
    if not isinstance(data, bool):
        if data is "True":
            data = True
        elif data is "False":
            data = False
        else:
            pass

    params_list = [('owner', owner, str), ('start_time', start_time, datetime),
                   ('end_time', end_time, datetime), ('scan_id', scan_id, int),
                   ('data', data, bool)]
    for (name, value, param_type) in params_list:
        logger.info("name: {0}, param: {1}, param_type: {2}".format(name,
                                                                    value,
                                                                    param_type))
        if (value is not None) and (not isinstance(value, param_type)):
            err_msg += ("Error: Your '{0}' value is {1} and its class is {2}. "
                        "Please provide a {3} object to use this search "
                        "key\n").format(name, value, value.__class__,
                                        param_type)
            continue
        search_dict[name] = value

    if err_msg != "":
        logger.error(err_msg)
    logger.info("Search dictionary: {0}".format(search_dict))
    try:
        result = find(num_header=num_header, **search_dict)
    except OperationFailure:
        raise
    return result