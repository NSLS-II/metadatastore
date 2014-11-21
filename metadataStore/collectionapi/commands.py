__author__ = 'arkilic'
import time
import getpass
from metadataStore.dataapi.commands import insert_event
from metadataStore.dataapi.commands import save_bulk_header


def create_event(event):
    """

    Events are saved given scan_id and descriptor name and additional optional parameters.

    Required fields: scan_id, descriptor_name

    Optional fields: owner, seq_no, data, description

    :param event: Dictionary used in order to save name-value pairs for Event entries
    :type event: dict

    :raises: ConnectionFailure, NotUniqueError, ValueError

    :returns: None

    Usage:

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan'})

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
                  ... 'data':{'motor1': 13.4, 'image1': '/home/arkilic/sample.tiff'}})

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan', 'owner': 'arkilic', 'seq_no': 0,
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
                create_event(single_event)
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

