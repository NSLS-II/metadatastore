from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import six


_run_header_keys = ["key1", "key2", "key3"]


def get_data_keys(run_header):
    """

    Return the names of the data keys

    Parameters
    ----------
    run_header : dict
        Run header to convert events to lists

    Returns
    -------
    list
        List of the data keys in the run header
    """
    if isinstance(run_header, dict):
        print(run_header.keys())
        header_keys = list(run_header)
        for h_key in header_keys:
            descriptor_keys = run_header[h_key]['event_descriptors']
            for d_key in descriptor_keys:
                temp_e_keys = run_header[h_key]['event_descriptors'][d_key]
                if temp_e_keys.has_key('events'):
                    e_keys = list(run_header[h_key]['event_descriptors'][d_key]['events'])
                else:
                    raise ValueError('Header does not include any events. Make sure data=True in search() and header '
                                     'includes events')
                _run_header_keys = list(run_header[h_key]['event_descriptors'][d_key]['events'][e_keys[0]]['data'])
    else:
        raise TypeError('Invalid run header. Headers must be Python dictionaries not ' + str(type(run_header)))
    return _run_header_keys


def listify(run_header, data_keys=None):
    """

    Transpose the events into lists

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
    data_keys : str or list, optional
        - If data_key is a valid key for an event_data entry,
        turn that event_data into a list
        - If data_key is a list of valid keys for event_data
        entries, turn those event_data keys into lists
        - If data_key is None, turn all event data keys into
        lists

    Returns
    -------
    list, list, list
        Order is data, keys, time
        data : list of lists of data corresponding to the keys
        keys : list of names of the data lists
        time : list of times corresponding to the data
    """
    # get the keys from the run header
    run_header_keys = get_data_keys(run_header)
    if data_keys is None:
        data_keys = run_header_keys

    # listify the data in the run header

    # this is the part where arman comes in

    # ---------------------------- start temp behavior
    # pretend like the next few lines are the result of
    # listifying the run header
    time = np.arange(10)/10.
    run_header_keys = _run_header_keys
    data = []
    data.append(range(10))
    data.append(range(2, 12))
    data.append(range(4, 14))

    # ---------------------------- end temp behavior

    if data_keys == run_header_keys:
        # data_keys was None, return all
        return data, keys, time

    key_subset = []
    data_subset = []
    # check to see if data_keys is a list
    if isinstance(data_keys, list):
        for key in data_keys:
            print(run_header_keys)
            index = run_header_keys.index(key)
            data_subset.append(data.pop(index))
            key_subset.append(key)
    else:
        index = run_header_keys.index(data_keys)
        key_subset = data_keys
        data_subset = data.pop(index)

    return data_subset, key_subset, time