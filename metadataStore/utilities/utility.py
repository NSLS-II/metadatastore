from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import six
from collections import defaultdict
import six
import itertools


def get_calib_dict(run_header):
    """
    Return the calibration dictionary that is saved in the run_header

    :param run_header: Run header to convert events to lists. Can only be one header.
    :type run_header: dict
    
    :returns: Dictionary that contains all information inside the run_header's 
    beamline_config key. If there are multiple 'configs' then the return
    value is a nested dictionary keyed on config_# for the number of config
    
    :rtype: dict

    bool
        True: Multiple 'config' sections were present, dict is a nested dict
        
        False: One 'config' section was present, dict is not a nested dict
    """
    nested = True
    calib_dict = {key: run_header['configs'][key]['config_params'] for
                  key in run_header['configs']}

    # if there is only one configs section, no need to return an extra calib
    if len(calib_dict) == 1:
        calib_dict = calib_dict[list(calib_dict)[0]]
        nested = False

    return calib_dict, nested


def get_data_keys(run_header):
    """
    Return the names of the data keys. This function assumes that there is
    only one event descriptor in a run header

    :param run_header: run header to convert events to lists. Can only be one header.
    :type run_header: dict

    :returns: List of the data keys in the run header keyed by the event_descriptor
    :rtype: list
    """
    try:
        for ev_desc_key, ev_desc_dict in six.iteritems(run_header[u'event_descriptors']):
            descriptor_name = ev_desc_dict['descriptor_name']
            try:
                for ev_key, ev_dict in six.iteritems(ev_desc_dict['events']):
                    # this assumes all events in an event_descriptor have the same keys
                    return list(ev_dict['data'])
            except KeyError as e:
                raise ValueError('Header does not include any events. Make '
                                 'sure data=True in search() and header '
                                 'includes events.\nOriginal error: {0}'.format(e))
    except KeyError as e:
        raise KeyError('Header does not include "event_descriptors". '
                       'Original Error: {0}'.format(e))


def get_data_keys_futureproof(run_header):
    """

    Return the names of the data keys. This function assumes that there is
    only one event descriptor in a run header

    **Note:** This function only works for one event_descriptor per run_header. As
    soon as we start getting multiple event_descriptors per run header this
    function will need to be modified

    :param run_header: Run header to convert events to lists. Can only be one header.
    :type run_header: dict

    :returns: List of the data keys in the run header keyed by the event_descriptor
    descriptor_name. If descriptor_name is not unique for all
    event_descriptors, see Note

    **Note:** The descriptor_name field in event_descriptors is assumed to be unique. 
    If it is not, then append the last four characters of _id to it.
    Ideally this would be something more like a PV name and less hostile than the hashed _id field

    """
    ev_keys = {}
    try:
        try:
            for (ev_desc_key, ev_desc_dict) in six.iteritems(
                    run_header[u'event_descriptors']):
                descriptor_name = ev_desc_dict['descriptor_name']
                ev_keys[ev_desc_key] = {
                    'name': ev_desc_dict['descriptor_name'],
                    'data_keys': list(
                        six.itervalues(ev_desc_dict['events']).next()['data']),
                }
        except KeyError as e:
            raise ValueError('Header does not include any events. Make '
                             'sure data=True in search() and header '
                             'includes events.'
                             '\nOriginal error: {0}'.format(e))
    except KeyError as e:
        print(e)
        raise KeyError('Header does not include "event_descriptors". '
                       '\nOriginal Error: {0}'.format(e))

    return ev_keys


def listify(run_header, data_keys=None, bash_to_lower=True):
    """Transpose the events into lists

    from this:
    run_header : {
        "event_0_data" : {"key1": "val1", "key2": "val2", ...},
        "event_1_data" : {"key1": "val1", "key2": "val2", ...},
        ...
        }

    to this:
    {"key1": [val1, val2, ...],
     "key2" = [val1, val2, ...],
     "keyN" = [val1, val2, ...],
     "time" = [time1, time2, ...],
    }

    Parameters
    ----------
    run_header : dict
        Run header to convert events to lists
    event_descriptors_key : str
        Name of the event_descriptor
    data_keys : hashable or list, optional
        - If data_key is a valid key for an event_data entry,
          turn that event_data into a list
        - If data_key is a list of valid keys for event_data
          entries, turn those event_data keys into lists
        - If data_key is None, turn all event data keys into
          lists
    bash_to_lower : boolean
        True: Compare strings after casting to lowercase
        False: Compare strings without casting to lowercase

    Returns
    -------
    dict
        data is keyed on run header data keys with an extra field 'time'
    """
    # get the keys from the run header
    header_keys = get_data_keys(run_header)
    print('header_keys: {}'.format(header_keys))
    print('data keys: {}'.format(data_keys))
    if len(header_keys) == 1:
        # turn it in to a list
        header_keys = [header_keys]
    # set defaults if necessary
    if data_keys is None:
        data_keys = header_keys

    try:
        # check for data_keys being iterable
        data_keys.__iter__()
    except AttributeError:
        # turn data_keys in to a list
        data_keys = [data_keys]

    if not 'time' in data_keys:
        data_keys.append('time')
    # forcibly cast to lower case
    if bash_to_lower:
        data_keys, header_keys = [[k.lower() for k in key_tmp] for
                                  key_tmp in (data_keys, header_keys)]

    # listify the data in the run header
    data_dict = defaultdict(list)
    for ev_desc_key, ev_desc_dict in \
            six.iteritems(run_header['event_descriptors']):
        data_key = list(ev_desc_dict['events'])
        for index, (ev_key) in enumerate(data_key):
            ev_dict = ev_desc_dict['events'][ev_key]
            # print('ev_dict[\'data\']: {}'.format(ev_dict['data']))
            for data_key, data in six.iteritems(ev_dict['data']):
                data_key = data_key.lower()
                # data_keys_in_dict = data_key in data_keys
                # print('if {} in {}: {}'.format(data_key, data_keys, data_keys_in_dict))
                if data_key in data_keys:
                    data_dict[data_key].append(data)

    return data_dict


def tablify(run_headers):
    if isinstance(run_headers, dict):
        header_keys = run_headers.keys()
        table = dict()
        desc_list = list()
        table['headers'] = header_keys
        desc_fields = list()
        for entry in header_keys:
            descriptor_keys = run_headers[entry]['event_descriptors'].keys()
            desc_list.append(descriptor_keys)
            temp = list()
            for desc in descriptor_keys:
                temp.append(run_headers[entry]['event_descriptors'][desc])
            desc_fields.append(temp)
        table['descriptor_fields'] = desc_fields
        table['event_descriptors'] = desc_list
    else:
        raise TypeError('Header must be a python dict')
    return table


if __name__ == "__main__":
    from metadataStore.userapi.commands import search
    return_dict = search(data=True, scan_id=388, owner='edill')
    print('search_dict: {0}'.format(return_dict))
    keys = list(return_dict)
    return_dict = return_dict[keys[0]]
    print('search_dict: {0}'.format(return_dict))
    keys = get_data_keys(return_dict)
    print('keys: {0}'.format(keys))
    data = listify(return_dict, u'ub')
    print("data: {0}".format(data))
    print("search_dict keys: {0}".format(list(return_dict)))

    print('calibration_dict: {0}'.format(get_calib_dict(return_dict)))
