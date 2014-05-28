__author__ = 'arkilic'
import datetime
from metadataStore.dataapi.pymetadataStore import *
import time

#Create a collection that will hold entries. (Logbook in Olog terminology)
create_collection('my_collection')

#Define documents to be inserted into database. These documents can be as flexible as possible.
sample_document1 = {'name': 'experimenter',
                    'owner': 'arkilic',
                    'property': 'scan',
                    'start_time':datetime.datetime.utcnow(),
                    'end_time': datetime.datetime.utcnow(),
                    'Id': 1,
                    'userId': 1234,
                    'sampleId': 'xyz',
                    'text': 'composed_doc',
                    'image_url': '/home/arkilic/imgs/some1.tiff'}

sample_document2 = {'name': ' ',
                    'owner': 'arkilic',
                    'property': 'scan',
                    'start_time':datetime.datetime.utcnow(),
                    'end_time': datetime.datetime.utcnow(),
                    'Id': 2,
                    'userId': 1234,
                    'sampleId': 'xyz',
                    'text': 'composed_doc',
                    'image_url': '/home/arkilic/imgs/some2.tiff'}

#Save entries into a python list in order to be able to insert in bulk
entry_list = list()
entry_list.append(sample_document1)
entry_list.append(sample_document2)

#Dump data into database
insert('my_collection', entry_list)

#Query database for given owner, Id, and or any other user defined parameter
#find routines returns the cursor object that is a python iterator. simple indexing [index] or __getitem__ routine
#can be used to
#Warning: Please make sure limit is set properly. The limit is set manually currently. Future releases of this tool will
#smartly allocate a limit unless enforced manually this way

print query('my_collection',limit=5, owner='arkilic', sampleId='xyz')