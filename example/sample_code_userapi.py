__author__ = 'arkilic'

import random
from metadataStore.userapi.commands import create, record, search
import time


s_id = random.randint(0, 10000)
seq_n = random.randint(0, 10)
print("s_id: {0}".format(s_id))
print("seq_n: {0}".format(seq_n))

create(header={'scan_id': s_id})
create(beamline_config={'scan_id': s_id})
create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
some_list = [12.3, 34.5, 45.3]

data_dict = {'list_of_1k': some_list, 'motor1': random.randint(0, 90), 'motor2': random.randint(0, 90),
                     'motor3': random.randint(0, 90), 'motor4': random.randint(0, 90), 'motor5': random.randint(0, 90)}
record(scan_id=s_id, descriptor_name='scan', seq_no=1)
record(scan_id=s_id, descriptor_name='scan', seq_no=3, data=data_dict)


# for i in xrange(100):
#     s_id = random.randint(0, 10000000)
#     create(header={'scan_id': s_id})
#     create(event_descriptor={'scan_id': s_id, 'descriptor_name': 'scan', 'event_type_id': 12, 'tag': 'experimental'})
#
#     for i in xrange(10):
#         some_list.append(float(i))
#         data_dict = {'list_of_1k': some_list, 'motor1': random.randint(0, 90), 'motor2': random.randint(0, 90),
#                      'motor3': random.randint(0, 90), 'motor4': random.randint(0, 90), 'motor5': random.randint(0, 90)}
#         start = time.time()
#         record(scan_id=s_id, descriptor_name='scan', seq_no=seq_n, data=data_dict, description='some entry')
#         end = time.time()
#         elapsed = (end - start)*1000
# #        print 'It took ' + str(elapsed) + ' milliseconds to record one event'

a = search(scan_id=s_id, owner='arkilic', data=True)
print a.keys()
print a['header_0']['event_descriptors']['event_descriptor_0']['data_keys']
some_id = a['header_0']['_id']

print some_id


query_b = search(header_id=some_id,data=True)
print query_b['header_0']['event_descriptors']['event_descriptor_0']['data_keys']
