from metadataStore.userapi.commands import create, record, search
from numpy.random import randint
import time
import datetime
from metadataStore.sessionManager.databaseInit import db
from matplotlib.pyplot import plot, savefig, title, xlabel, ylabel, xlim, ylim, show, legend, figtext


def create_header(header_range):
    #Recursive Header Insert (Not bulk)
    result_file = open('benchmark.txt', 'a+')
    total_elapsed = 0
    x = list()
    y = list()
    s_ids = randint(low=0, high=10000000000000, size=header_range)
    for i in xrange(header_range):
        s_id = int(s_ids[i])
        benchmark_header = {'scan_id': s_id, 'owner': 'arkilic', 'start_time': datetime.datetime.utcnow(),
                            'beamline_id': 'example', ' status': 'In Progress'}
        start = time.time()
        create(header=benchmark_header)
        end = time.time()
        elapsed = (end-start)*1000
        y.append(elapsed)
        x.append(db['header'].count())
        total_elapsed += elapsed
    average = total_elapsed/header_range
    print 'Header insert took ' + str(average) + ' milliseconds in average for ' + str(header_range) + ' headers'
    result_file.write('Header took ' + str(elapsed) + ' milliseconds in average over ' + str(header_range) +
                      ' headers\n')
    result_file.close()
    return x, y, average


def record_event(event_count):
    result_file = open('benchmark.txt', 'a+')
    total_elapsed = 0
    x = list()
    y = list()
    s_id_single_nds = randint(low=0, high=10000000000000, size=event_count)
    for i in xrange(event_count):
        s_id_single_nd = int(s_id_single_nds[i])
        profiling_header = {'scan_id': s_id_single_nd, 'owner': 'arkilic', 'start_time': datetime.datetime.utcnow(),
                            'beamline_id': 'csx', }
        create(header=profiling_header)

        sample_event_descriptor = {'scan_id': s_id_single_nd, 'descriptor_name': 'scan', 'event_type_id': 0,
                                   'tag': 'experimental', 'type_descriptor': {'attribute1': 'value1',
                                                                              'attribute2': 'value2'}}
        create(event_descriptor=sample_event_descriptor)
        start = time.time()
        record(scan_id=s_id_single_nd, descriptor_name='scan', seq_no=0, owner='arkilic', description='some text')
        end = time.time()
        elapsed = (end-start)*1000
        y.append(elapsed)
        x.append(db['event'].count())
        total_elapsed += elapsed
    average = total_elapsed/event_count
    print 'Event insert took ' + str(average) + ' milliseconds in average for ' + str(event_count) + ' events'
    result_file.write('Event insert took ' + str(average) + ' milliseconds in average for ' + str(event_count) +
                      ' events')
    return x, y, average


def generate_plot(x, y, data_points):
    #Generate Figure
    x_1 = x[0:data_points]
    lbl = str(data_points)+' headers'
    res = plot(x_1, y, 'o', label=lbl)
    title('Header Insert Time vs Number of Headers in metadataStore')
    ylim(0, 8)
    xlabel('Number of Headers in Database')
    ylabel('Header insert time (ms)')
    savefig('/Users/arkilic/Desktop/header_insert_performance_' + str(data_points) + '.png')
    return res


def generate_event_plot(x, y, data_points):
    #Generate Figure
    x_1 = x[0:data_points]
    lbl = str(data_points)+' events'
    res = plot(x_1, y, 'o', label=lbl)
    title('Event Insert Time vs Number of Headers in metadataStore')
    ylim(0, 8)
    xlabel('Number of Events in Database')
    txt = str(data_points) + ' events inserted'
    figtext(0, 8, 'boxed italics text in data coords', style='italic', bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    ylabel('Event insert time (ms)')
    savefig('/Users/arkilic/Desktop/event_insert_performance_' + str(data_points) + '.png')
    return res

create_header(1)