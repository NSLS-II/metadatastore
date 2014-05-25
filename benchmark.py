__author__ = 'arkilic'
from metadataStore.dataapi.pymetadataStore import *
import datetime
import time
import matplotlib.pyplot as plt

def compose_document(document_count):
    doc_list = list()
    for index in xrange(document_count):
        doc = {'name': 'experimenter' + str(index),
               'owner': 'arkilic',
               'property': 'scan',
               'start_time':datetime.datetime.utcnow(),
               'end_time': datetime.datetime.utcnow(),
               'Id': index,
               'userId': 1234,
               'sampleId': 'xyz' + str(index),
               'text': 'composed_doc' + str(index),
               'image_url': '/home/arkilic/imgs/' + str(index) + '.tiff',
               'name2': 'experimenter' + str(index),
               'owner2': 'arkilic',
               'property2': 'scan',
               'start_time2':datetime.datetime.utcnow(),
               'end_time2': datetime.datetime.utcnow(),
               'Id2': index,
               'userId2': 1234,
               'sampleId2': 'xyz' + str(index),
               'text2': 'composed_doc' + str(index),
               'image_url2': '/home/arkilic/imgs/' + str(index) + '.tiff'}
        doc_list.append(doc)
    return doc_list


def benchmark_insert(count):
    f = open('/Users/arkilic/metadataStore/benchmark_result.txt', 'a')
    document_list = compose_document(count)
    # create_collection('benchmark_logbook')
    start = time.time()
    insert('benchmark_logbook', document_list)
    end = time.time()
    total_time = end-start
    print str(count) + ' inserts take ' + str(total_time*1000) + ' milliseconds'
    f.write(str(count) + ' inserts take ' + str(total_time*1000) + ' milliseconds\n')
    f.close()
    return count, total_time

create_collection('benchmark_logbook')
x = list()
y = list()
for entry in (1, 1, 10, 100, 1000, 10000, 100000,1000000):
    (a, b) = benchmark_insert(entry)
    x.append(a)
    y.append(b)

plt.plot(x,y)
plt.show()

start = time.time()
result = find('benchmark_logbook', owner='arkilic', Id=1, image_url='/home/arkilic/imgs/1.tiff')
end = time.time()
elapsed = end-start
print 'Time it takes to find entries with specific logbook, owner, id, and image_url is ' + str(elapsed*1000) +\
      ' milliseconds'
print result.count()