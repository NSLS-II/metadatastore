__author__ = 'arkilic'
from ..dataapi.raw_commands import insert_event, save_header, insert_event_descriptor, save_beamline_config


def create(header=None, beamline_config=None, event_descriptor=None):
    """
    Create header, beamline_config, and event_descriptor
    """
    if header is not None:
        if isinstance(header,dict):
            h_keys = header.keys()

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
    valid_keys = ['id', 'start_time', 'end_time', 'owner', 'scan_id', 'beamline_id', 'custom']
    for key in key_list:
        if key not in valid_keys:
            raise KeyError(str(key) + ' is not a valid key for Header')
            break


def __verify_event_desc_keys(key_list):
    """
    Header keys given as a list
    """
    valid_keys = ['id', 'header_id', 'event_type_id', 'event_type_name', 'type_descriptor', 'tag']
    for key in key_list:
        if key not in valid_keys:
            raise KeyError(str(key) + ' is not a valid key for Header')
            break