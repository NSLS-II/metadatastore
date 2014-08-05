__author__ = 'arkilic'
from mongoengine import IntField, DateTimeField, DictField, StringField
from mongoengine import ReferenceField, Document, DO_NOTHING


class Header(Document):
    """
    :param _id: hashed primary key generated by mongodb database engine
    :type _id: ObjectID pointer object(see pymongo documentation for details)
    :param start_time: run header initialization timestamp
    :type start_time: datetime object
    :param end_time: run header close timestamp
    :type  end_time: datetime object
    :param owner: data collection or system defined user info
    :type owner: string
    :param header_id: foreign key pointing back to header
    :param beamline_id: descriptor for beamline
    :type beamline_id: string
    :param custom: dictionary field for custom information
    :type custom: dictionary
    """
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=False)
    owner = StringField(max_length=20, required=True)
    scan_id = IntField(required=True, unique=True)
    status = StringField(max_length=20)
    beamline_id = StringField(max_length=20, required=False)
    custom = DictField(required=False)
    meta = {'indexes': ['-_id', '-start_time', '-owner']}


class EventDescriptor(Document):
    """
    :param _id: data collection defined hashed primary key
    :type _id: integer 
    :param header_id: foreign key pointing back to header
    :type header_id: integer
    :param event_type_id: event type integer descriptor generated by
    :type event_type_id: integer
    :param event_type_name: event type string descriptor
    :type event_type_name: string
    :param event_type_descriptor: dictionary that defines fields and field data types for a given event type
    :type event_type_descriptor: dictionary
    """
    header_id = ReferenceField('Header', reverse_delete_rule=DO_NOTHING, required=True)
    event_type_id = IntField(min_value=0)
    event_type_name = StringField(max_length=10, required=True)
    type_descriptor = DictField()
    tag = StringField(max_length=20)
    meta = {'indexes': ['-header_id', '-event_type_id', '-event_type_name']}


class Event(Document):
    """
    :param _id: hashed primary key
    :type param _id: ObjectID pointer object(see pymongo documentation for details)
    :param even_descriptor_id: foreign key pointing back to event_descriptor
    :type event_descriptor_id: integer
    :param description: User generated text field
    :type description: string
    :param seq_no: sequence number for the data collected
    :type seq_no: integer
    :param owner: data collection or system defined user info
    :type owner: string
    :param data: data point name-value pair container
    :type data: dictionary
    """
    event_descriptor_id = ReferenceField('EventDescriptor', reverse_delete_rule=DO_NOTHING, required=True)
    description = StringField(max_length=50)
    header_id = ReferenceField('Header', reverse_delete_rule=DO_NOTHING, required=True)
    seq_no = IntField(min_value=0)
    owner = StringField(max_length=10)
    data = DictField()
    meta = {
        'indexes': ['-event_descriptor_id', '-header_id', '-data']
    }


class BeamlineConfig(Document):
    """
    :param beamline_id: beamline descriptor
    :type beamline_id: string
    :param header_id: foreign key pointing back to header
    :type header_id: integer
    :param config_params: configuration parameter name-value container
    :type config_params: dictionary
    """
    header_id = ReferenceField('Header', reverse_delete_rule=DO_NOTHING, required=True)
    config_params = DictField()
