__author__ = 'arkilic'

from metadataStore.dataapi.raw_commands import *

#TODO: Use whoosh to add "did you mean ....?" for misspells
#TODO: Make datetime user friendly

def create(entry_type, **kwargs):
    """
    Create allows creation of a run_header and beamline_config. Routine must be provided with dictionary of dictionaries
    with keys header and beamline_config as shown below:
    >>> create(entry_type='header', header_id=1345, scan_id=14, custom={'field1': 'value1', 'field2': 'value2'})
    >>> create(entry_type='header', header_id=1345, owner='arkilic', scan_id=14,
            ...custom={'field1': 'value1', 'field2': 'value2'})
    >>> create(entry_type='header', header_id=1345, owner='arkilic', scan_id=14, start_time=datetime.datetime.utcnow(),
            ...custom={'field1': 'value1', 'field2': 'value2'})
    EventDescriptor Creation
    >>> create(entry_type='event_descriptor', header_id=1345, event_type_id=1, event_type_name='scan')
    >>> create(entry_type='event_descriptor', header_id=1345, event_type_id=1, event_type_name='scan',
           ... type_descriptor={'attribute': 'value'})
    BeamlineConfig Creation
    >>> create(entry_type='beamline_config', header_id=1345)
    >>> create(entry_type='beamline_config', header_id=1345, config_params={'attribute': 'value', 'attributex': 'valuex'})
    """
    if entry_type is 'header':
        if kwargs.has_key('header_id'):
            _id = kwargs['header_id']
        else:
            raise ValueError('header_id is required for run header creation')
        if kwargs.has_key('scan_id'):
            scan_id = kwargs['scan_id']
        else:
            raise ValueError('scan_id is required for run header creation')
        if kwargs.has_key('owner'):
            header_owner = kwargs['owner']
        else:
            header_owner = getpass.getuser()
        if kwargs.has_key('start_time'):
            start_time = kwargs['start_time']
        else:
            start_time = datetime.datetime.utcnow()
        if kwargs.has_key('beamline_id'):
            beamline_id = kwargs['beamline_id']
        else:
            beamline_id = None
        if kwargs.has_key('custom'):
            custom = kwargs['custom']
        else:
            custom = dict()
        status = 'In Progress'
        save_header(header_id=_id, scan_id=scan_id, header_owner=header_owner, start_time=start_time,
                    beamline_id=beamline_id, status=status, custom=custom)
    elif entry_type is 'event_descriptor':
        if kwargs.has_key('event_descriptor_id'):
            _id = kwargs['event_descriptor_id']
        else:
            raise ValueError('event_descriptor_id is a required field for event_descriptor')
        if kwargs.has_key('header_id'):
            h_id = kwargs['header_id']
        else:
            raise ValueError('header_id is a required field for event_descriptor')
        if kwargs.has_key('event_type_id'):
            ev_type_id = kwargs['event_type_id']
        else:
            raise ValueError('event_type_id is a required field for event_descriptor')
        if kwargs.has_key('event_type_name'):
            ev_type_name = kwargs['event_type_name']
        else:
            ev_type_name = None
        if kwargs.has_key('type_descriptor'):
            type_descriptor = kwargs['type_descriptor']
        else:
            type_descriptor = dict()
        if kwargs.has_key('tag'):
            tag = kwargs['tag']
        else:
            tag = None
        insert_event_descriptor(event_descriptor_id=_id, header_id=h_id, event_type_id=ev_type_id,
                                event_type_name=ev_type_name, type_descriptor=type_descriptor, tag=tag)
    elif entry_type is 'beamline_config':
        if kwargs.has_key('beamline_cfg_id'):
            b_c_id = kwargs['beamline_cfg_id']
        else:
            raise ValueError('beamline_cfg_id is required to create beamline_config entry')
        if kwargs.has_key('header_id'):
            h_id = kwargs['header_id']
        else:
            raise ValueError('header_id is required to create beamline_config entry')
        if kwargs.has_key('config_params'):
            config_params = kwargs['config_params']
        else:
            config_params = dict()
        save_beamline_config(beamline_cfg_id=b_c_id, header_id=h_id, config_params=config_params)
    else:
        raise ValueError(str(entry_type) + ' is not a valued entry type')


def record( event_id, descriptor_id, header_id='current', owner=getpass.getuser(), seq_no=None, data={}):
    """
    Creates an event entry to save experimental/data analysis progress. metadataStore can be used standalone without/
    dataBroker.
    :param event_id: Unique mongodb _id field assigned to a given event
    :type event_id: int
    :param header_id: Run_header _id that event belongs to
    :type header_id: int
    :param event_descriptor_id: int
    :type event_descriptor_id
    :param seq_no: int
    :type seq_no:
    :param start_time: formatted datetime of event
    :type start_time: datetime
    :param end_time: formatted datetime
    :type end_time: datetime

    *Usage:*
    >>> record(event_id=134, event_type_id=0, )

    :returns: None
    """
    #TODO: Make time range search user friendly: replace datetime with string time formatting

    try:
        insert_event(event_id=event_id, header_id=header_id, descriptor_id=descriptor_id,owner=owner,
                     seq_no=seq_no, data=data)
    except OperationError:
        raise


def search(header_id=None, owner=None, start_time=None, end_time=None, scan_id=None,
           contents=False, **kwargs):
    #TODO: Modify according to changes in log() and raw_commands
    #TODO: Make time range search user friendly: replace datetime with string time formatting
    #TODO: Add tag search
    try:
        result = find(header_id=header_id, owner=owner, start_time=start_time, end_time=end_time,
                      scan_id=scan_id, contents=contents, **kwargs)
    except OperationError:
        raise
    return result

