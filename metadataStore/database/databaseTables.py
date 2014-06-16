__author__ = 'arkilic'
from mongoengine import *
from mongoengine.fields import *


class Header(Document):
    _id = IntField(primary_key=True, unique=True)
    create_time = DateTimeField(required=True)
    update_time = DateTimeField()
    owner = StringField(max_length=20, required=True)
    beamline_id = StringField(max_length=20, required=True)
    meta = {
        'indexes': ['-_id']
    }



class BeamlineConfig(DynamicDocument):
    _id = IntField(primary_key=True, required=False)
    headers = ListField(ReferenceField('Header', reverse_delete_rule=CASCADE), required=True)
    energy = FloatField()
    wavelength = FloatField()
    i_zero = FloatField()
    diffractometer = DictField()


class Event(DynamicDocument):
    _id = IntField(primary_key=True, unique=True, required=True)
    headers = ListField(ReferenceField('Header', reverse_delete_rule=CASCADE), required=True)
    seqno = IntField()
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    description = StringField(max_length=50)
    data = DictField()
    meta = {
        'indexes': ['-_id']
    }


#TODO: Read and add fields to beamline_config and events from config file for a given session
#TODO: Ensure/create indexing. how is this handled via mongoengine ORM