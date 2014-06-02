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
    print str(entry_size) + ' document(s) with ' + str(doc_size) + ' name-value field(s) each take a total of '\
        + str(total_time*1000) + ' milliseconds\n'
    f.write(str(entry_size) + ' document(s) with ' + str(doc_size) + ' name-value field(s) each take a total of '
        + str(total_time*1000) + ' milliseconds\n')
    f.close()


def benchmark_query(collection_name, **kwargs):
    f = open('/Users/arkilic/metadataStore/benchmark_result.txt', 'a')
    field_count = len(kwargs.keys())
    start = time.time()
    result = query(collection_name, limit=50, **kwargs)
    end = time.time()
    total_time = (end - start)*1000
    print 'Query with ' + str(field_count) + ' fields searched that returns + ' + str(len(result)) + ' documents with ' \
          + str(total_time) + ' milliseconds'
    f.write('Query with ' + str(field_count) + ' fields searched that returns + ' + str(len(result)) + ' documents with ' \
            + str(total_time) + ' milliseconds\n')
    f.close()


create_collection('benchmark_logbook')

benchmark_insert(100000)
# start = time.time()
# query('benchmark_logbook', Id=1,  limit=10)
# end = time.time()
# print 'It has been ' + str((end-start)*1000) + ' milliseconds'

benchmark_query('benchmark_logbook', Id=1)
benchmark_query('benchmark_logbook', Id=3, text='composed_doc3')
benchmark_query('benchmark_logbook', text='composed_doc3')
benchmark_query('benchmark_logbook', sampleId='xyz5')
benchmark_query('benchmark_logbook', Id=4, text='composed_doc4', sampleId='xyz4')
benchmark_query('benchmark_logbook', Id=5, text='composed_doc5', sampleId='xyz5', image_url='/home/arkilic/imgs/5.tiff')
benchmark_query('benchmark_logbook', Id=3, text='composed_doc3')
benchmark_query('benchmark_logbook', Id=4, text='composed_doc4', sampleId='xyz4')
benchmark_query('benchmark_logbook', Id=5, text='composed_doc5', sampleId='xyz5', image_url='/home/arkilic/imgs/5.tiff')
benchmark_query('benchmark_logbook', owner='arkilic')