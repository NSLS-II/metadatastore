__author__ = 'arkilic'
import datetime
import six

def validate_time(time_entry):
    try:
        datetime.datetime.fromtimestamp(time_entry)
    except Exception:
        raise TypeError('time must be a timestamp (float).'
                        '\nYou provided: {}'
                        '\n\tIt has type: {}'.format(time_entry,
                                                     type(time_entry)))
    return time_entry


def validate_string(entry):
    """ Will cast from unicode to string

    Parameters
    ----------
    entry : str, unicode or something that can be cast to a string.
        Must be a string because of pymongo/Javascript requirements
    """

    if six.PY2:
        entry = str(entry)
    elif six.PY3:
        entry = six.text_type(entry)
    if isinstance(entry, str):
        res = entry
    elif entry is None:
        res = None
    else:
        raise TypeError('Entry must be a python string.'
                        '\nYou provided: {}'
                        '\n\tIt has type: {}'.format(entry,
                                                     type(entry)))
    return res


def validate_dict(entry):
    if isinstance(entry, dict):
        res = entry
    else:
        raise TypeError('Entry must be a dictionary.'
                        '\nYou provided: {}'
                        '\n\tIt has type: {}'.format(entry,
                                                     type(entry)))
    return res


def validate_list(entry):
    if isinstance(entry, list):
        res = entry
    else:
        raise TypeError('Entry must be a list.'
                        '\nYou provided: {}'
                        '\n\tIt has type: {}'.format(entry,
                                                     type(entry)))
    return res


def validate_int(entry):
    if isinstance(entry, int):
        res = entry
    else:
        raise TypeError('Entry must be an integer.'
                        '\nYou provided: {}'
                        '\n\tIt has type: {}'.format(entry,
                                                     type(entry)))
    return res

