
from metadataStore.userapi.commands import create, record, search
import random as rd
import time


from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):
########Empty database tests##########
    result_file = open('benchmark.txt', 'r+')
    total_elapsed_1 = 0

    for i in xrange(1000):
        s_id = rd.randint(0,10000000)
        start = time.time()
        benchmark_header = {'scan_id': s_id}
        create(header=benchmark_header) 
        end = time.time()
        elapsed = (end-start)*1000
        total_elapsed_1 += elapsed

elapsed = total_elapsed_1/1000
print 'Header insert with all defaults took ' + str(elapsed) + 'milliseconds in average over 1000 headers'
result_file.write('Header insert with all defaults took ' + str(elapsed) + 'milliseconds in average over 1000 headers\n')
result_file.close()

    
#Database test with 1000 run headers 1 event_descriptor & 1 event per header



#Database test with 1000 run headers 1 event_descriptor & 100 events per header


#Database test with 1000 run headers 1 event_descriptor & 100 events per header


#Database test with 1000 run headers 1 event_descriptor & 1000 events per header


#Database test with 1000 run headers 1 event_descriptor & 10000 events per header



#Database test with 10000 run headers 1 event_descriptor & 1 event per header


#Database test with 10000 run headers 1 event_descriptor & 100 events per header




#Database test with 10000 run headers 1 event_descriptor & 1000 events per header


#Database test with 10000 run headers 1 event_descriptor & 10000 events per header




##### Partially Filled Database with 10000 run headers and 100 events per header#######



