__author__ = 'arkilic'

#TODO: Database does not check whether entry exists or not prior to creation for things that are specified as unique. Add such check here or belongs to client????
#TODO: Read the default parameters from config file
#TODO: Convert user input to datetime.datetime()
from metadataStore.dataapi.metadataTools import *


def create(param_dict):
    """
    Create allows creation of a run_header and beamline_config. Routine must be provided with dictionary of dictionaries
    with keys header and beamline_config as shown below:
    Usage:
    >>> sample_dict = {'header':{'run_id': 1903, 'run_owner': 'arkilic', 'beamline_id': 'csx', 'custom': {},
                        'start_time': datetime.datetime.utcnow()},
                        'beamline_config':{'beamline_config_id': 122, 'header_id': 1903, 'wavelength': 12.345,
                        'custom': {'new_field': 'value'}}}
    >>> create(sample_dict)

    Returns: Header and BeamlineConfig objects
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
        try:
            record_event(event_id=event_id, header_id=header_id, event_type_id=event_type_id, run_id=run_id,
                         seqno=seqno, start_time=start_time, end_time=end_time, description=text, data=data)
        except OperationError:
            raise

search_keys_dict = {
    "header_id" : {
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
    "contents" : {
        "description" : ("True: returns all fields. False: returns some subset "
                         "of the fields"),
        "type" : bool,
        },
    }
def search(header_id=None, owner=None, start_time=None, text=None, update_time=None, beamline_id=None,
           contents=False, **kwargs):
    print text
    try:
        result = find(header_id=header_id, owner=owner, start_time=start_time, update_time=update_time,
                      beamline_id=beamline_id, contents=contents, text=text, **kwargs)
    except OperationError:
        raise
    return result

def search_dict(search_dict):
    return search(**search_dict)
