__author__ = 'arkilic'
from metadataStore.dataapi.raw_commands import *
import datetime
#

update_header_end_time(1345, datetime.datetime(1999,4,14))

insert_event(event_id=13456, header_id=1345, descriptor_id=1345, description=None, owner=getpass.getuser(), seq_no=None,
             data={'motor': 12.4567})
# save_header(header_id=1908, beamline_id='csx12')
# for entry in list_headers():
#     print entry._id
#
# save_header(header_id=1910, scan_id=12)
# for entry in list_headers():
#     print entry._id
# save_header(header_id=1345, custom={'field1': 'value1', 'field2': 'value2'})
# insert_event_descriptor(event_descriptor_id=1345, header_id=1345, event_type_id=0, event_type_name='scan')
# insert_event_descriptor(event_descriptor_id=1345, header_id=1345, event_type_id=0, event_type_name='scan',
#                         type_descriptor={'custom_field': 'value', 'custom_field2': 'value2'}, tag='analysis')
# for entry in list_event_descriptors():
#     print entry.event_type_name