__author__ = 'arkilic'
import datetime
import getpass

from metadataStore.dataapi.raw_commands import save_header, save_beamline_config, insert_event_descriptor, insert_event


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


def record(event=dict()):
    """
    some bs goes here
    """
    if 'scan_id' in event:
        scan_id = event['scan_id']
    else:
        raise ValueError('scan_id is required in order to record an event')
    if 'descriptor_name' in event:
        descriptor_name = event['descriptor_name']
    else:
        raise ValueError('Descriptor is required in order to record an event')
    if 'description' in event:
        description = event['description']
    else:
        description = None
    if 'owner' in event:
        owner = event['owner']
    else:
        owner = getpass.getuser()
    if 'seq_no' in event:
        seq_no = event['seq_no']
    else:
        raise ValueError('seq_no is required field')
    if 'data' in event:
        data = event['data']
    else:
        data = dict()
    try:
        insert_event(scan_id=scan_id, descriptor_name=descriptor_name, owner=owner, seq_no=seq_no, data=data)
    except:
        raise

def search():
    pass


def init_collection():
    """
    Using config file create beamline config, header, and event descriptor for a given run
    """
    pass


def end_collection():
    pass


def __verify_header_keys(key_list):
    """
    Header keys given as a list
    """
    status = False
    valid_keys = ['id', 'start_time', 'end_time', 'owner', 'scan_id', 'beamline_id', 'custom']
    for key in key_list:
        if key not in valid_keys:
            raise KeyError(str(key) + ' is not a valid key for Header')
            break
        else:
            status = True
    return status


def __verify_event_desc_keys(key_list):
    """
    Header keys given as a list
    :param key_list: keys for event_descriptor dictionary
    :type key_list: list
    """
    status = False
    valid_keys = ['id', 'header_id', 'event_type_id', 'event_type_name', 'type_descriptor', 'tag']
    for key in key_list:
        if key not in valid_keys:
            raise KeyError(str(key) + ' is not a valid key for Header')
            break
        else:
            status = True
    return status