__author__ = 'arkilic'
import getpass

from metadataStore.dataapi.raw_commands import *

#TODO: Use whoosh to add "did you mean ....?" for misspells
#TODO: Make datetime user friendly

def create(entry_type, **kwargs):
    """
    Create allows creation of a run_header and beamline_config. Routine must be provided with dictionary of dictionaries
    with keys header and beamline_config as shown below:
    >>> create(entry_type='header', header_id=1345, scan_id=14, custom={'field1': 'value1', 'field2': 'value2'})
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

#####################################TODO: Implement the rest of the goodies here##################
    elif entry_type is 'event_descriptor':
        print 'descriptor'
    elif entry_type is 'beamline_config':
        print 'config'

    else:
        raise ValueError(str(entry_type) + ' is not a valued entry type')






# def log(text, owner, event_id, header_id, event_type_id, run_id, seqno=None, start_time=datetime.datetime.utcnow(),
#         end_time=datetime.datetime.utcnow(), data={}):
#     """
#     Creates an event entry to save experimental/data analysis progress. metadataStore can be used standalone without/
#     dataBroker.
#     :param text: Data Collection and/or analysis description
#     :type text: str or unicode
#     :param event_id: Unique mongodb _id field assigned to a given event
#     :type event_id: int
#     :param header_id: Run_header _id that event belongs to
#     :type header_id: int
#     :param event_type_id: int
#     :type event_type_id:
#     :param run_id: int
#     :type run_id:
#     :param seqno: int
#     :type seqno:
#     :param start_time: formatted datetime of event
#     :type start_time: datetime
#     :param end_time: formatted datetime
#     :type end_time: datetime
#
#     *Usage:*
#     >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45)
#     >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45,
#         ... data={'motor1': [12,45,67,87,42], 'motor2': [22,55,77,17,12], 'wavelength': [3.45, 1.34, 6.45, 5.13, 4.67]})
#     >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45,
#         ... start_time=datetime.datetime(2014,4,5,12,55,1000)
#
#     :returns: None
#     """
#     #TODO: Make time range search user friendly: replace datetime with string time formatting
#     try:
#         insert_event(event_id=event_id, header_id=header_id, event_type_id=event_type_id, run_id=run_id,
#                      seqno=seqno, start_time=start_time, end_time=end_time, description=text, data=data)
#     except OperationError:
#         raise
#
#
# def search(header_id=None, owner=None, start_time=None, text=None, update_time=None, beamline_id=None,
#            contents=False, **kwargs):
#     #TODO: Modify according to changes in log() and raw_commands
#     #TODO: Make time range search user friendly: replace datetime with string time formatting
#     try:
#         result = find(header_id=header_id, owner=owner, start_time=start_time, update_time=update_time,
#                       beamline_id=beamline_id, contents=contents, text=text, **kwargs)
#     except OperationError:
#         raise
#     return result

