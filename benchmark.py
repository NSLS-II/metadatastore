__author__ = 'arkilic'
from metadataStore.dataapi.pymetadataStore import *
import datetime
import time
import string
import random
import numbers

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
               'image_url': '/home/arkilic/imgs/' + str(index) + '.tiff'}
        doc_list.append(doc)
    return doc_list


def randstring(length=5):
    valid_letters = string.letters
    return ''.join((random.choice(valid_letters) for i in xrange(length)))


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


def compose_single_doc(field_num):
    """
    Creates 2 elements per field count
    """
    document = dict()
    for index in xrange(field_num):
        str_or_num = random.randint(0, 1)
        if str_or_num:
            document[randstring(5)] = random.randint(0, 100)
        else:
            document[randstring(5)] = randstring(4)
    return document


def benchmark_insert_docSize(doc_size, entry_size):
    f = open('/Users/arkilic/metadataStore/benchmark_result.txt', 'a')
    doc_list = list()
    for index in xrange(entry_size):
        document = compose_single_doc(doc_size)
        doc_list.append(document)
    start = time.time()
    insert('benchmark_logbook', doc_list)
    end = time.time()
    total_time = end-start
    print str(eRntry_size) + ' document(s) with ' + str(doc_size) + ' name-value field(s) each take a total of ' + str(total_time*1000) + ' milliseconds\n'
    f.write(str(entry_size) + ' document(s) with ' + str(doc_size) + ' name-value field(s) each take a total of ' + str(total_time*1000) + ' milliseconds\n')
    f.close()


def benchmark_find_cursor(collection_name, **kwargs):
    # f = open('/Users/arkilic/metadataStore/benchmark_result.txt', 'a')
    start = time.time()
    result = find(collection_name, **kwargs)
    end = time.time()
    total_time = end-start
    # print 'Query using ' + str(len(kwargs)) + ' fields' + ' Returning cursor took ' + str(total_time*1000) +\
    #       ' milliseconds. Cursor has ' + str(result.count()) +\
    #       ' elements\n'
    # f.write('Query using ' + str(len(kwargs)) + ' fields' + ' Returning cursor took ' + str(total_time*1000) +
    #         ' milliseconds. Cursor has ' + str(result.count()) +
    #         ' elements\n')
    # f.close()
    return result


def benchmark_find_single_from_cursor(collection_name, **kwargs):
    start = time.time()
    benchmark_find_cursor(collection_name, **kwargs)[0]
    end = time.time()
    total_time = end-start
    print 'It took ' + str(total_time*1000) + ' milliseconds'

# benchmark_insert(2000000)
# for i in (1,5, 10, 20, 50, 80, 100):
#     for j in (1, 10, 100, 1000, 10000, 100000):
#         benchmark_insert_docSize(i, j)
#

# benchmark_find_cursor('benchmark_logbook', owner='arkilic', property='scan')
print benchmark_find_cursor('benchmark_logbook', owner='arkilic', property='scan', sampleId='xyz1')
benchmark_find_single_from_cursor('benchmark_logbook', owner='arkilic', property='scan', sampleId='xyz1')

print query('benchmark_logbook', limit=10, owner='arkilic', property='scan', sampleId='xyz1', Id=1)