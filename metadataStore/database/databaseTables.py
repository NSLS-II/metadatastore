__author__ = 'arkilic'
from mongoengine import *
from mongoengine.fields import *


class Header(Document):
    _id = IntField(primary_key=True, unique=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=False)
    update_time = DateTimeField()
    owner = StringField(max_length=20, required=True)
    beamline_id = StringField(max_length=20, required=True)
    custom = DictField(required=False)
    meta = {
        'indexes': ['-_id', '-start_time']
    }



class BeamlineConfig(DynamicDocument):
    _id = IntField(primary_key=True, required=False)
    headers = ListField(ReferenceField('Header', reverse_delete_rule=DO_NOTHING), required=True)
    energy = FloatField()
    wavelength = FloatField()
    i_zero = FloatField()
    custom = DictField(required=False)
    diffractometer = DictField()


class Event(DynamicDocument):
    _id = IntField(primary_key=True, unique=True, required=True)
    headers = ListField(ReferenceField('Header', reverse_delete_rule=DO_NOTHING), required=True)
    seqno = IntField()
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    description = StringField(max_length=50)
    data = DictField()
    meta = {
        'indexes': ['-headers']
    }


#TODO: Read and add fields to beamline_config and events from config file for a given session
