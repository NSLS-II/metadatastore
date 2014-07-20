__author__ = 'arkilic'
from metadataStore.dataapi.raw_commands import *


def create(param_dict):
    """
    Create allows creation of a run_header and beamline_config. Routine must be provided with dictionary of dictionaries
    with keys header and beamline_config as shown below:

    >>> sample_dict = {'header':{'run_id': 1903, 'run_owner': 'arkilic', 'beamline_id': 'csx', 'custom': {},
                        'start_time': datetime.datetime.utcnow()},
                        'beamline_config':{'beamline_config_id': 122, 'header_id': 1903, 'wavelength': 12.345,
                        'custom': {'new_field': 'value'}}}
    >>> create(sample_dict)

    :return: Header and BeamlineConfig objects
    """
    if isinstance(param_dict, dict):
        try:
            header_dict = param_dict['header']
            beamline_cfg_dict = param_dict['beamline_config']
            if header_dict:
               id = header_dict['run_id']
               owner = header_dict['run_owner']
               start_time = header_dict['start_time']
               beamline_id = header_dict['beamline_id']
               custom_field = header_dict['custom']
            if beamline_cfg_dict:
                b_id = beamline_cfg_dict['beamline_config_id']
                bh_id = beamline_cfg_dict['header_id']
            if beamline_cfg_dict.has_key('energy'):
                energy = beamline_cfg_dict['energy']
            else:
                energy = None
            if beamline_cfg_dict.has_key('wavelength'):
                wavelength = beamline_cfg_dict['wavelength']
            else:
                wavelength = None
            if beamline_cfg_dict.has_key('i_zero'):
                i_zero = beamline_cfg_dict['i_zero']
            else:
                i_zero = None
            if beamline_cfg_dict.has_key('diffractometer'):
                diffractometer = beamline_cfg_dict['diffractometer']
            else:
                diffractometer = {}
            if beamline_cfg_dict.has_key('custom'):
                custom = beamline_cfg_dict['custom']
            else:
                custom = dict()
        except KeyError:
            raise
        try:
            if header_dict:
                header = save_header(run_id=id, run_owner=owner, start_time=start_time, beamline_id=beamline_id,
                                     custom=custom_field)
            else:
                header = None
            print beamline_cfg_dict
            if beamline_cfg_dict:
                bcfg = save_beamline_config(beamline_cfg_id=b_id, header_id=bh_id, energy=energy, wavelength=wavelength,
                                            i_zero=i_zero, custom=custom)
            else:
                bcfg = None
        except OperationError:
            raise
    else:
        raise TypeError('Input must be a dictionary. Please check sample_dict in python docs')
    return header, bcfg


def log(text, owner, event_id, header_id, event_type_id, run_id, seqno=None, start_time=datetime.datetime.utcnow(),
        end_time=datetime.datetime.utcnow(), data={}):
    """
    Creates an event entry to save experimental/data analysis progress. metadataStore can be used standalone without/
    dataBroker.
    :param text: Data Collection and/or analysis description
    :type text: str or unicode
    :param event_id: Unique mongodb _id field assigned to a given event
    :type event_id: int
    :param header_id: Run_header _id that event belongs to
    :type header_id: int
    :param event_type_id: int
    :type event_type_id:
    :param run_id: int
    :type run_id:
    :param seqno: int
    :type seqno:
    :param start_time: formatted datetime of event
    :type start_time: datetime
    :param end_time: formatted datetime
    :type end_time: datetime

    *Usage:*
    >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45)
    >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45,
        ... data={'motor1': [12,45,67,87,42], 'motor2': [22,55,77,17,12], 'wavelength': [3.45, 1.34, 6.45, 5.13, 4.67]})
    >>> log(text='sample entry', owner='arkilic', event_id=1335, header_id=498, event_type_id=4, run_id=45,
        ... start_time=datetime.datetime(2014,4,5,12,55,1000)

    :returns: None
    """
    #TODO: Make time range search user friendly: replace datetime with string time formatting
    try:
        insert_event(event_id=event_id, header_id=header_id, event_type_id=event_type_id, run_id=run_id,
                     seqno=seqno, start_time=start_time, end_time=end_time, description=text, data=data)
    except OperationError:
        raise


def search(header_id=None, owner=None, start_time=None, text=None, update_time=None, beamline_id=None,
           contents=False, **kwargs):
    #TODO: Modify according to changes in log() and raw_commands
    #TODO: Make time range search user friendly: replace datetime with string time formatting
    try:
        result = find(header_id=header_id, owner=owner, start_time=start_time, update_time=update_time,
                      beamline_id=beamline_id, contents=contents, text=text, **kwargs)
    except OperationError:
        raise
    return result

