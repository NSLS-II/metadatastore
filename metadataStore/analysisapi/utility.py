from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import six
from collections import defaultdict
import six
import itertools


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
    # print('run_header: {0}'.format(list(run_header)))
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

    Note: This function only works for one event_descriptor per run_header. As
    soon as we start getting multiple event_descriptors per run header this
    function will need to be modified

    Parameters
    ----------
    run_header : dict
        Run header to convert events to lists. Can only be one header.

    Returns
    -------
    dict
        List of the data keys in the run header keyed by the event_descriptor
        descriptor_name. If descriptor_name is not unique for all
        event_descriptors, see Notes 1

    Notes
    -----
    1. the descriptor_name field in event_descriptors is assumed to be unique.
       If it is not, then append the last four characters of _id to it.
       Ideally this would be something more like a PV name and less hostile
       than the hashed _id field

    """
    # print('run_header: {0}'.format(list(run_header)))
    ev_keys = {}
    try:
        # get the event descriptor keys
        # ev_desc_names = [ev_desc_dict['descriptor_name'] for ev_desc_dict in
        #                  six.itervalues(run_header[u'event_descriptors'])]
        # if len(ev_desc_names) != len(set(ev_desc_names)):
        #     # there is at least one name collision in ev_desc_keys
        #     raise NotImplementedError("You passed me a run header with "
        #                               "multiple event_descriptors of the same "
        #                               "name. I cannot handle this yet. Go yell"
        #                               " at Arman or Eric.\nDescriptor names: "
        #                               "{0}".format(ev_desc_names))
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
            #
            # try:
            #     for ev_key, ev_dict in six.iteritems(ev_desc_dict['events']):
            #         # this assumes all events in an event_descriptor have the
            #         # same keys. Which they should...
            #         return list(ev_dict['data'])
            # except KeyError as e:
            #     raise ValueError('Header does not include any events. Make '
            #                      'sure data=True in search() and header '
            #                      'includes events.'
            #                      '\nOriginal error: {0}'.format(e))
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
    # print('data_keys: {0}'.format(data_keys))
    # forcibly cast to lower case
    if bash_to_lower:
        data_keys, header_keys = [[k.lower() for k in key_tmp] for
                                  key_tmp in (data_keys, header_keys)]

    # listify the data in the run header
    data_dict = defaultdict(list)
    # print('data_dict keys: {0}'.format(list(data_dict)))
    for ev_desc_key, ev_desc_dict in \
            six.iteritems(run_header['event_descriptors']):
        data_key = list(ev_desc_dict['events'])
        # data_key.sort(key=lambda x: int(x.split("_")[-1]))
        # print("sorted data keys: {0}".format(data_key))
        for index, (ev_key) in enumerate(data_key):
            ev_dict = ev_desc_dict['events'][ev_key]
            for data_key, data in six.iteritems(ev_dict['data']):
                if data_key in data_keys:
                    data_dict[data_key].append(data)

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
    data = listify(search_dict, u'ub')
    print("data: {0}".format(data))
    print("search_dict keys: {0}".format(list(search_dict)))
