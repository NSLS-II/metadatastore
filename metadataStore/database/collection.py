__author__ = 'arkilic'
from mongoengine import *


class Header(Document):
    _id = IntField(primary_key=True, unique=True)
    owner = StringField(max_length=20, required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    beamline_id = StringField(max_length=20, required=True)


class BeamlineConfig(DynamicDocument):
    headers = ListField(ReferenceField(Header), required=True)
    energy = FloatField()
    wavelength = FloatField()
    i_zero = FloatField()
    diffractometer = DictField()


class Event(DynamicDocument):
    _id = IntField(primary_key=True, unique=True)
    headers = ListField(ReferenceField(Header), required=True)
    seqno = IntField()
    description = StringField(max_length=50)
    data = DictField()

    #read from config file with name and data type information

