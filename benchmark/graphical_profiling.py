__author__ = 'arkilic'
from benchmark.userapi import *
from metadataStore.userapi.commands import record, create, search
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


#Profile Single Header Insert with Defaults
s_id_single = int(randint(low=0, high=10000000000000, size=1)[0])
graphviz = GraphvizOutput()
graphviz.output_file = '/Users/arkilic/Desktop/single_header_profile_defaults.png'
with PyCallGraph(output=graphviz):
    profiling_header = {'scan_id': s_id_single}
    create(header=profiling_header)

#Profile Single Header Insert without Defaults
s_id_single_nd = int(randint(low=0, high=10000000000000, size=1)[0])
graphviz = GraphvizOutput()
graphviz.output_file = '/Users/arkilic/Desktop/single_header_profile_no_defaults.png'
with PyCallGraph(output=graphviz):
    profiling_header = {'scan_id': s_id_single_nd, 'owner': 'arkilic', 'start_time': datetime.datetime.utcnow(),
                        'beamline_id': 'csx', }
    create(header=profiling_header)

#Profile EventDescriptor Insert with Defaults
graphviz = GraphvizOutput()
graphviz.output_file = '/Users/arkilic/Desktop/single_type_descriptor_profile_defaults.png'
with PyCallGraph(output=graphviz):
    sample_event_descriptor = {'scan_id': s_id_single, 'descriptor_name': 'scan', 'event_type_id': 0}
    create(event_descriptor=sample_event_descriptor)

#Profile EventDescriptor Insert without Defaults
graphviz = GraphvizOutput()
graphviz.output_file = '/Users/arkilic/Desktop/single_type_descriptor_profile_no_defaults.png'
with PyCallGraph(output=graphviz):
    sample_event_descriptor = {'scan_id': s_id_single, 'descriptor_name': 'scan', 'event_type_id': 0,
                               'tag': 'experimental', 'type_descriptor': {'attribute1': 'value1',
                                                                          'attribute2': 'value2'}}
    create(event_descriptor=sample_event_descriptor)

graphviz = GraphvizOutput()
graphviz.output_file = '/Users/arkilic/Desktop/single_event_no_data_profiling.png'
with PyCallGraph(output=graphviz):
    record(scan_id=s_id_single, descriptor_name='scan', seq_no=0, owner='arkilic', description='some text')

some_data = {'motor1': 12.3, 'motor2': 13.3, 'motor3': 14.3, 'motor5': 45.4, 'motor6': 24.3}

graphviz.output_file = '/Users/arkilic/Desktop/single_event_with_data_profiling.png'
with PyCallGraph(output=graphviz):
    record(scan_id=s_id_single, descriptor_name='scan', seq_no=0, owner='arkilic', description='some text')