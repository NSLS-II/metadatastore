__author__ = 'arkilic'

from metadataStore.dataapi.raw_commands import *

#TODO: Use whoosh to add "did you mean ....?" for misspells
#TODO: Make datetime user friendly


def create(header=None, beamline_config=None, event_descriptor=None):
    """
    Create header, beamline_config, and event_descriptor

    :param header: Header attribute-value pairs
    :type header: dict
    :param beamline_config: BeamlineConfig attribute-value pairs
    :type beamline_config: dict
    :param event_descriptor: EventDescriptor attribute-value pairs
    :type event_descriptor: dict
    :Raises: TypeError, ValueError, ConnectionFailure, NotUniqueError
    :returns: None
    """
    if header is not None:
        if isinstance(header, dict):
            if 'scan_id' in header:
                scan_id = header['scan_id']
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
            if 'event_type_name' in event_descriptor:
                event_type_name = event_descriptor['event_type_name']
            else:
                raise ValueError('event_type_name is required for EventDescriptor')
            if 'type_descriptor' in event_descriptor:
                type_descriptor = event_descriptor['type_descriptor']
            else:
                type_descriptor = dict()
            if 'tag' in event_descriptor:
                tag = event_descriptor['tag']
            else:
                tag = None
            try:
                insert_event_descriptor(scan_id=scan_id, event_type_id=event_type_id, event_type_name=event_type_name,
                                        type_descriptor=type_descriptor, tag=tag)
            except:
                raise
        else:
            raise TypeError('EventDescriptor must be a Python dictionary')


def record(scan_id, descriptor_name, seq_no, owner=getpass.getuser(), data=dict(), description=None):
    """
    Events are saved given scan_id and descriptor name and additional optional parameters
    :param scan_id: Unique run identifier
    :type scan_id: int
    :param descriptor_name: EventDescriptor that serves as an Event header
    :type descriptor_name: str
    :param seq_no: Data point sequence number
    :type seq_no: int
    :param owner: Run owner(default: unix session owner)
    :type owner: str
    :param data: Serves as an experimental data storage structure
    :type data: dict
    :Raises: ConnectionFailure, NotUniqueError, ValueError

    Required fields: scan_id, descriptor_name, seq_no
    Optional fields: owner, data, description

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
    "scan_id" : {
        "description" : "The unique identifier of the run",
        "type" : str,
        },
    "owner" : {
        "description" : "The user name of the person that created the header",
        "type" : str,
        },
    "start_time" : {
        "description" : "The start time in utc",
        "type" : datetime,
        },
    "text" : {
        "description" : "The description that the 'owner' associated with the run",
        "type" : str,
        },
    "update_time" : {
        "description" : "??",
        "type" : datetime,
        },
    "beamline_id" : {
        "description" : "The identifier of the beamline.  Ex: CSX, SRX, etc...",
        "type" : str,
        },
    "data" : {
        "description" : ("True: returns all fields. False: returns some subset "
                         "of the fields"),
        "type" : bool,
        },
    }

def search(owner=None, start_time=None, end_time=None, scan_id=None, data=False):
    #TODO: Modify according to changes in log() and raw_commands
    #TODO: Make time range search user friendly: replace datetime with string time formatting
    if isinstance(scan_id, str):
        scan_id = int(scan_id)
    if isinstance(data, str):
        data = data == "True"
    try:
        result = find(owner=owner, start_time=start_time, end_time=end_time, scan_id=scan_id, data=data)
    except OperationError:
        raise
    return result