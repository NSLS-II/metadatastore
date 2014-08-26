__author__ = 'arkilic'

import datetime
import random as rd
from benchmark.userapi import *
import matplotlib.pylab as plt

plt.figure(0)
xa, ya, avg = create_header(10)
plt1, = generate_plot(xa, ya, 10)

xb, yb, avg2 = create_header(100)
plt2, = generate_plot(xb, yb, 100)

xc, yc, avg3 = create_header(1000)
plt3, = generate_plot(xc, yc, 1000)

xd, yd, avg4 = create_header(10000)
plt4, = generate_plot(xd, yd, 10000)

legend([plt4, plt3, plt2, plt1], ["10K Headers", "1k Headers",
                                  "100 Headers", "10 Headers"])
savefig('/Users/arkilic/Desktop/header_insert_result.png')

plt.figure(1)
plot([10, 100, 1000, 10000], [avg, avg2, avg3, avg4], 'o')
title('Average Header Insert Time vs. Number of Headers')
ylim(0, 1)
savefig('/Users/arkilic/Desktop/header_insert_average.png')

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