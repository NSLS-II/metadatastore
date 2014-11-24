__author__ = 'arkilic'

import getpass
from metadataStore.dataapi.commands import insert_event


# this needs to be moved up a level or three
def validate_dict_keys(input_dict, req_set):
    """
    Validate that the required keys are in the input dictionary.

    This function returns None if the dict is valid, and raises
    `ValueError` if it is not.

    Parameters
    ----------
    input_dict : dict
        The dictionary to have it's keys validate

    req_set : iterable
        The keys that must be in the dictionary

    Raises
    ------
    `ValueError` if any of the required keys are missing
    """
    missing = []
    for k in req_set:
        if k not in input_dict:
            missing.append(k)
    if len(missing):
        missing = ', '.join('{}'.format(k) for k in missing)
        raise ValueError("The required key(s) {} are missing".format(missing))


def create_event(event):
    """
    Events are saved given scan_id and descriptor name and additional
    optional parameters.

    Required fields: scan_id, descriptor_name

    Optional fields: owner, seq_no, data, description

    Parameters
    ----------
    event : dict
         Dictionary used in order to save name-value pairs for Event entries.

         Required fields (with tautological descriptions until I find
         where they are really documented)

         ===============   ==========================
         field             value
         ===============   ==========================
         scan_id           The scan id number
         seq_no            The sequence number
         descriptor_name   The name of the descriptor
         ===============   ==========================

         Optional fields

         ===========   ============  =============
         field         description   default value
         ===========   ============  =============
         description   description   None
         owner         the owner     current user
         data          data payload  empty dict
         ===========   ============  =============

    Raises
    ------
    ConnectionFailure, NotUniqueError, ValueError

    Examples
    --------

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan'})

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan',
                  ... 'owner': 'arkilic', 'seq_no': 0,
                  ... 'data':{'motor1': 13.4,
                  ...         'image1': '/home/arkilic/sample.tiff'}})

    >>> create_event(event={'scan_id': 1344, 'descriptor_name': 'ascan',
                  ... 'owner': 'arkilic', 'seq_no': 0,
                  ... 'data':{'motor1': 13.4,
                  ...         'image1': '/home/arkilic/sample.tiff'}},
                  ... 'description': 'Linear scan')
    """
    if isinstance(event, dict):
        # validate that the required keys are in the dict
        validate_dict_keys(event, {'scan_id',
                                   'descriptor_name', 'seq_no'})
        # grab the required fields
        descriptor_name = event['descriptor_name']
        scan_id = event['scan_id']
        seq_no = event['seq_no']
        # get the optional fields, use defaults if needed
        description = event.get('description', None)
        owner = event.get('owner', getpass.getuser())
        data = event.get('data', dict())

        ret = insert_event(scan_id, descriptor_name, seq_no,
                     description=description,
                     owner=owner, data=data)
        print("the returned thing is {}".format(ret))

    elif isinstance(event, list):
        errors = []
        for idx, single_event in enumerate(event):
            try:
                create_event(single_event)
            except ValueError as ve:
                errors.append('Event {} of {} raised error: {}. \nEvent: {}'
                              ''.format(idx, len(event)-1), ve, single_event)
        if errors:
            raise ValueError(errors)
    else:
        raise ValueError("Event must be a dict or a list. You provided a {}: "
                         "{}".format(type(event), event))
