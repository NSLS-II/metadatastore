__author__ = 'arkilic'
from mongoengine import *


class Header(DynamicDocument):
    _id = IntField(primary_key=True, unique=True)
    owner = StringField(max_length=20, required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    beamline_id = StringField(max_length=20, required=True)


class BeamlineConfig(DynamicDocument):
    _id = IntField(primary_key=True, unique=True)
    headers = ListField(ReferenceField(Header), required=True)
    energy = FloatField()
    wavelength = FloatField()
    i_zero = FloatField()
    diffractometer = DictField()


class Event(DynamicDocument):
    _id = IntField(primary_key=True, unique=True, required=True)
    headers = ListField(ReferenceField(Header), required=True)
    seqno = IntField()
    description = StringField(max_length=50)
    data = DictField()
    meta = {
        'indexes': ['_id']
    }


#TODO: Read and add fields to beamline_config and events from config file for a given session
#TODO: Ensure/create indexing. how is this handled via mongoengine ORM