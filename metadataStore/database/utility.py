__author__ = 'arkilic'
import datetime
import six

def validate_start_time(time_entry):
    if isinstance(time_entry, datetime.datetime):
        res = time_entry
    else:
        raise TypeError('start_time must be a datetime object')
    return res


def validate_end_time(time_entry):
    if isinstance(time_entry, datetime.datetime):
        res = time_entry
    elif time_entry is None:
        res = None
    else:
        raise TypeError('end_time must be a datetime object')
    return res


def validate_string(entry):
    """ Will cast from unicode to string

    Parameters
    ----------
    entry : str, unicode or something that can be cast to string or unicode
    """
    if six.PY2:
        entry = str(entry)
    elif six.PY3:
        entry = six.text_type(entry)
    print('entry value: {}, type: {}'.format(entry, type(entry)))
    if isinstance(entry, str):
        res = entry
    elif entry is None:
        res = None
    else:
        raise TypeError('Entry must be a python string')
    return res


def validate_dict(entry):
    if isinstance(entry, dict):
        res = entry
    else:
        raise TypeError('Entry must be a dictionary')
    return res


def validate_list(entry):
    if isinstance(entry, list):
        res = entry
    else:
        raise TypeError('Entry must be a list')
    return res


def validate_int(entry):
    if isinstance(entry, int):
        res = entry
    else:
        raise TypeError('Entry must be an integer')
    return res

