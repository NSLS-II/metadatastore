from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import six


_run_header_keys = ["key1", "key2", "key3"]


def get_data_keys(run_header):
    """

    Return the names of the data keys. This function assumes that there is
    only one event descriptor in a run header

    Parameters
    ----------
    run_header : dict
        Run header to convert events to lists. Can only be one header.

    Returns
    -------
    list
        List of the data keys in the run header keyed by the event_descriptor
        name
    """
    # if isinstance(run_header, dict):
    print('run_header: {0}'.format(list(run_header)))
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
    dict
        data is keyed on run header data keys with an extra field 'time'
    """
    # get the keys from the run header
    run_header_keys = get_data_keys(run_header)
    if data_keys is None:
        data_keys = run_header_keys

    # listify the data in the run header

    # this is the part where arman comes in
    data_dict = {}
    if isinstance(data_keys, list):
        for key in data_keys:
            data_dict[key] = []
    else:
        data_dict[data_keys] = []
    data_dict['time'] = []
    print('data_dict keys: {0}'.format(list(data_dict)))
    for ev_desc_key, ev_desc_dict in six.iteritems(run_header['event_descriptors']):
        data_key = list(ev_desc_dict['events'])
        # data_key.sort(key=lambda x: int(x.split("_")[-1]))
        print("sorted data keys: {0}".format(data_key))
        for index, (ev_key) in enumerate(data_key):
            ev_dict = ev_desc_dict['events'][ev_key]
            for data_key, data in six.iteritems(ev_dict['data']):
                if data_key in list(data_dict):
                    data_dict[data_key].append(data)
    #
    # # ---------------------------- start temp behavior
    # # pretend like the next few lines are the result of
    # # listifying the run header
    # time = np.arange(10)/10.
    # run_header_keys = _run_header_keys
    # data = []
    # data.append(range(10))
    # data.append(range(2, 12))
    # data.append(range(4, 14))
    #
    # # ---------------------------- end temp behavior

    if data_keys == run_header_keys:
        # data_keys was None, return all
        return data_dict

    data_dict_subset = {}

    key_subset = []
    data_subset = []
    data_dict_subset = {}
    # check to see if data_keys is a list
    if isinstance(data_keys, list):
        for key in data_keys:
            data_dict_subset[key] = data_dict[key]
    else:
        index = data_keys.index(data_keys)
        data_dict_subset = data_dict

    data_dict = data_dict_subset
    return data_dict

if __name__ == "__main__":
    from metadataStore.userapi.commands import search
    search_dict = search(data=True, scan_id=388, owner='edill')
    print('search_dict: {0}'.format(search_dict))
    keys = list(search_dict)
    search_dict = search_dict[keys[0]]
    print('search_dict: {0}'.format(search_dict))
    keys = get_data_keys(search_dict)
    print('keys: {0}'.format(keys))
    data = listify(search_dict, 'wavelength')
    print("data: {0}".format(data))
    print("search_dict keys: {0}".format(list(search_dict)))
