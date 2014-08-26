
def listify(run_header, data_key=None):
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
    data_key : str or list, optional
        - If data_key is a valid key for an event_data entry,
        turn that event_data into a list
        - If data_key is a list of valid keys for event_data
        entries, turn those event_data keys into lists
        - If data_key is None, turn all event data keys into
        lists

    Returns
    -------
    dict
        Dict whose keys are data_key (if not None) or all
        data keys (if data_key is None) and whose values
        are the entries for those keys. Additionally there
        is a 'time' key whose values are the time steps of
        the values in the data_key lists

    """
    pass