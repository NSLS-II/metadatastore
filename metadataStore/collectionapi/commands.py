__author__ = 'arkilic'
from metadataStore.dataapi.raw_commands import save_header


def create(header=None, beamline_config=None, event_descriptor=None):
    """
    Create header, beamline_config, and event_descriptor
    """
    if header is not None:
        if isinstance(header, dict):
            hdr_keys = header.keys()
            if __verify_header_keys(hdr_keys):
                save_header(header_id=header['id'], start_time = header['start_time'])
        else:
            raise TypeError('Header must be a Python dictionary ')
    if beamline_config is not None:
        if isinstance(beamline_config, dict):
            pass
        else:
            raise TypeError('BeamlineConfig must be a Python dictionary')
    if event_descriptor is not None:
        if isinstance(event_descriptor, dict):
            pass
        else:
            raise TypeError('EventDescriptor must be a Python dictionary')


def insert(collection, param_dict):
    #TODO: Make sure collection exists
    #TODO: Make sure given collection, param_dict is appropriate
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


create(header={'id': 112})