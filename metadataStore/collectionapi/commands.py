__author__ = 'arkilic'
import time
import getpass
from metadataStore.dataapi.commands import save_header, save_beamline_config, insert_event_descriptor, insert_event
from metadataStore.dataapi.commands import save_bulk_header
from metadataStore.dataapi.commands import find, get_event_descriptor_hid_edid, db


def create(header=None, beamline_config=None, event_descriptor=None):
    """
    Create header, beamline_config, and event_descriptor given dictionaries with appropriate name-value pairs.

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
                start_time = time.time()
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
            if 'tags' in header:
                tags = header['tags']
            else:
                tags = list()
            if 'header_versions' in header:
                header_versions = header['header_versions']
            else:
                header_versions = list()
            if 'status' in header:
                status = header['status']
            else:
                status = 'In Progress'
            try:
                save_header(scan_id=scan_id, header_owner=owner, start_time=start_time, beamline_id=beamline_id,
                            status=status, tags=tags, header_versions=header_versions, custom=custom)
            except:
                raise
        elif isinstance(header, list):
            header_list = list()
            for single_header in header:
                if 'scan_id' in single_header:
                    if isinstance(single_header['scan_id'], int):
                        scan_id = single_header['scan_id']
                    else:
                        raise TypeError('scan_id must be an integer')
                else:
                    raise ValueError('scan_id is a required field')
                if 'start_time' in single_header:
                    start_time = single_header['start_time']
                else:
                    start_time = time.time()
                if 'owner' in single_header:
                    owner = single_header['owner']
                else:
                    owner = getpass.getuser()
                if 'beamline_id' in single_header:
                    beamline_id = single_header['beamline_id']
                else:
                    beamline_id = None
                if 'custom' in single_header:
                    custom = single_header['custom']
                else:
                    custom = dict()
                if 'tags' in single_header:
                    tags = single_header['tags']
                else:
                    tags = list()
                if 'header_versions' in single_header:
                    header_versions = single_header['header_versions']
                else:
                    header_versions = list()
                if 'status' in single_header:
                    status = single_header['status']
                else:
                    status = 'In Progress'
                header_list.append(single_header)
            save_bulk_header(header_list=header_list)
        else:
            raise TypeError('Header must be a Python dictionary or list of Python dictionaries ')

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
            if 'data_keys' in event_descriptor:
                data_keys = event_descriptor['data_keys']
            else:
                raise ValueError('data keys are required for EventDescriptor entries')

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
                                        data_keys=data_keys, type_descriptor=type_descriptor, tag=tag)
            except:
                raise
        else:
            raise TypeError('EventDescriptor must be a Python dictionary')


def record(event):
    """

    Events are saved given scan_id and descriptor name and additional optional parameters.

    Required fields: scan_id, descriptor_name

    Optional fields: owner, seq_no, data, description

    :param event: Dictionary used in order to save name-value pairs for Event entries
    :type event: dict

    :raises: ConnectionFailure, NotUniqueError, ValueError

    :returns: None

    Usage:

    >>> record(event={'scan_id': 1344, 'descriptor_name': 'ascan'})

    >>> record(event={'scan_id': 1344, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
                  ... 'data':{'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'}})

    >>> record(event={'scan_id': 1344, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
                  ... 'data':{'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'}},'description': 'Linear scan')
    """
    if isinstance(event, dict):
        if 'scan_id' in event:
            scan_id = event['scan_id']
        else:
            raise ValueError('scan_id is required in order to record an event')
        if 'descriptor_name' in event:
            descriptor_name = event['descriptor_name']
        else:
            raise ValueError('descriptor_name is required in order to record an event')
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
            insert_event(scan_id=scan_id, descriptor_name=descriptor_name, owner=owner, seq_no=seq_no, data=data,
                         description=description)
        except:
            raise
    elif isinstance(event, list):
        # bulk = db['event'].initialize_ordered_bulk_op()
        errors = []
        for idx, single_event in enumerate(event):
            try:
                record(single_event)
            except ValueError as ve:
                errors.append('Event {} of {} raised error: {}. \nEvent: {}'
                              ''.format(idx, len(event)-1), ve, single_event)
        if errors:
            raise ValueError(errors)
        #     composed_dict = dict()
        #     if 'scan_id' in single_event:
        #         composed_dict['scan_id'] = single_event['scan_id']
        #     else:
        #         raise ValueError('scan_id is required in order to record an single_event')
        #     if 'descriptor_name' in single_event:
        #         composed_dict['descriptor_name'] = single_event['descriptor_name']
        #     else:
        #         raise ValueError('Descriptor is required in order to record an single_event')
        #     if 'description' in single_event:
        #         composed_dict['description'] = single_event['description']
        #     else:
        #         composed_dict['description'] = None
        #     if 'owner' in single_event:
        #         composed_dict['owner'] = single_event['owner']
        #     else:
        #         composed_dict['owner'] = getpass.getuser()
        #     if 'seq_no' in single_event:
        #         composed_dict['seq_no'] = single_event['seq_no']
        #     else:
        #         raise ValueError('seq_no is required field')
        #     if 'data' in single_event:
        #         composed_dict['data'] = single_event['data']
        #     else:
        #         composed_dict['data'] = dict()
        #     header_id, descriptor_id = get_event_descriptor_hid_edid(single_event['descriptor_name'],
        #                                                              single_event['scan_id'])
        #     composed_dict['header_id'] = header_id
        #     composed_dict['descriptor_id'] = descriptor_id
        #     bulk.insert(composed_dict)
        # bulk.execute()
    else:
        raise ValueError("Event must be a dict or a list. You provided a {}: "
                         "{}".format(type(event), event))



def search(scan_id=None, owner=None, start_time=None, beamline_id=None, end_time=None, data=False,
           header_id=None, tags=None, num_header=50, event_classifier=dict()):
    """
    Provides an easy way to search Header entries inserted in metadataStore

    :param scan_id: Unique identifier for a given run
    :type scan_id: int

    :param owner: run header owner(unix user by default)
    :type owner: str

    :param start_time: Header creation time
    :type start_time: datetime.datetime object

    :param beamline_id: beamline descriptor
    :type beamline_id: str

    :param end_time: Header status time
    :type end_time: datetime.datetime object

    :param data: data field for collection routines to save experiemental progress
    :type data: dict

    :raises: TypeError, OperationError, ValueError

    :returns: Dictionary

    >>> search(scan_id=s_id)
    >>> search(scan_id=s_id, owner='ark*')
    >>> search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5))
    >>> search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='arkilic')
    >>> search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='ark*')
    >>> search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='arkili.')
    """
    result = find(scan_id=scan_id, owner=owner, start_time=start_time, beamline_id=beamline_id, end_time=end_time,
                  data=data, tags=tags, header_id=header_id, num_header=num_header, event_classifier=event_classifier)
    return result
