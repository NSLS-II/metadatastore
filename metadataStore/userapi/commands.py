__author__ = 'arkilic'

#TODO: Database does not check whether entry exists or not prior to creation for things that are specified as unique. Add such check here
#TODO: Read the default parameters from config file
from metadataStore.dataapi.metadataTools import *


def create(type, fields={}):
    #TODO:
    if type is 'header':
        print 'create header'
    elif type is 'beamline_config':
        print 'create beamline config given header id'
    elif type is 'event':
        print 'create event given header id'
    else:
        raise ValueError(str(type) + ' not a valid type choice')
    """
    Creates a run_header, beamline_config, or event with provided a header_id
    """


def insert():
    """
    Inserts events into specified or default run_header
    """
    #TODO: unless run_header _id is specified, use last run_id to insert events
    pass


def insert_config():
    pass


def update_config():
    pass


def update():
    pass


def delete():
    pass


def search():
    pass
