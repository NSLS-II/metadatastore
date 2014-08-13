__author__ = 'arkilic'

import logging
import getpass
import datetime
from collections import OrderedDict
from metadataStore.dataapi.raw_commands import save_header, save_beamline_config, insert_event, insert_event_descriptor, find
logger = logging.getLogger(__name__)

#TODO: Use whoosh to add "did you mean ....?" for misspells
#TODO: Use metadataLogger class instance from sessionInit instead of on the fly logging object


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
                if isinstance(header['scan_id'], int):
                    scan_id = header['scan_id']
                else:
                    raise TypeError('scan_id must be an integer')
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


search_keys_dict = OrderedDict()
search_keys_dict["scan_id"] = {
    "description": "The unique identifier of the run",
    "type": int,
    }
search_keys_dict["owner"] = {
    "description": "The user name of the person that created the header",
    "type": str,
    }
search_keys_dict["start_time"] = {
    "description": "The start time in utc",
    "type": datetime.datetime,
    }
search_keys_dict["end_time"] = {
    "description": "The end time in utc",
    "type": datetime.datetime,
    }
search_keys_dict["data"] = {
    "description": ("True: returns all fields. False: returns some subset "
                     "of the fields"),
    "type": bool,
    }


def validate(var_dict, target_dict=search_keys_dict):
    """
    Helper function to validate parameter input, strip 'None' parameters
    and attempt to cast input parameters of the wrong type to the correct
    type

    Parameters
    ----------
    var_dict : dict
        Dictionary whose keys are in target_dict and whose values are to be
        type checked against the "type" field in the target_dict. None values
        cannot be typechecked and are thus added to the return_dict as None.
    target_dict : dict
        Dictionary whose keys are input parameter names and whose value is
        a dict with "description" and "type" keys.

    Returns
    -------
    dict
        Validated dictionary whose keys are all in target_dict and whose
        values are correctly typed or None

    Raises
    ------
    ValueError
        - If any of the input parameters are not correctly typed or they
        cannot be cast to the correct type
        - If var_dict has no entries.
        - If target_dict has no entries.
    KeyError
        If any of the keys in var_dict are not in target_dict
    """
    # check to make sure input dictionaries have keys
    if not var_dict:
        raise ValueError("var_dict has no keys")
    if not target_dict:
        raise ValueError("target_dict has no keys")

    # init the dict to return
    typechecked_dict = {}

    for key in var_dict:
        try:
            # will raise a KeyError if key is not in target_dict
            target_type = target_dict[key]["type"]
        except KeyError:
            raise KeyError("key [[{0}]] is not in the target_dict. Typechecking"
                           " cannot proceed".format(key))
        # get the value
        val = var_dict[key]
        # typecheck the value
        try:
            # STRING -> BOOL
            if target_type == bool and isinstance(val, str):
                val = val.lower()
                if val == "true":
                    val = True
                elif val == "false":
                    val = False
                else:
                    raise ValueError()
            # try to cast it to the target_type
            val = target_type(val)
        except ValueError:
            raise ValueError("key [[{0}]] has a value of [[{1}]] which cannot "
                             "be cast to [[{2}]]".format(key, val, target_type))

        # add the kv pair to the typechecked dict. Note that None values are
        # still added to the dictionary
        typechecked_dict[key] = val

    return typechecked_dict


def search(owner=None, start_time=None, end_time=None, scan_id=None,
           data=False):
    """
    Search the experimental database with the provided search keys. If no search
    keys are provided, the default behavior is to return nothing.

    Parameters
    ----------
    owner : str, optional
        User name to search on
    start_time : datetime, optional
        Only return results after start_time
    end_time : datetime, optional
        Only return results before start_time
    scan_id : int, optional
        Search by specific scan_id.  If scan_id is a string, search() will try
        to cast it to an integer.  If this fails, an error message will be
        be logged
    data : bool, optional
        True: Add data to the returned dictionary
        False: Don't include data in the returned dictionary
        If data is a string, search() will test to see if it's value is "True"
        or "False" and

    Returns
    -------
    list :
        If the combination of search parameters finds something, a list of
        dictionaries is returned/
        If the combination of search parameters finds nothing or no search
        parameters are provided, None is returned

    Raises
    ------
    ValueError
        If any of the input parameters are not correctly typed

    """
    #TODO: Modify according to changes in log() and raw_commands
    #TODO: Make time range search user friendly: replace datetime with string time formatting

    search_dict = {}

    # construct a dictionary whose keys are input parameter names and whose
    # values are the input parameter values. Drop values which are None
    # get the number of arguments
    argcount = search.func_code.co_argcount
    # get the input parameter names
    varnames = search.func_code.co_varnames[:argcount]
    # create the list of input parameter values
    varvals = [owner, start_time, end_time, scan_id, data]
    for name, val in zip(varnames, varvals):
        if val is not None:
            search_dict[name] = val

    # validate the search dictionary
    search_dict = validate(search_dict, search_keys_dict)

    # log the search dictionary as info
    logger.info("Search dictionary: {0}".format(search_dict))
    # actually perform the search
    try:
        result = find(**search_dict)
    except OperationError:
        raise
    return result