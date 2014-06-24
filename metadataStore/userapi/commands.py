__author__ = 'arkilic'

#TODO: Database does not check whether entry exists or not prior to creation for things that are specified as unique. Add such check here
#TODO: Read the default parameters from config file
from metadataStore.dataapi.metadataTools import *


def create(param_dict):
    """
    sample_dict = {'header':{'header_id':1903, 'owner': 'arkilic', 'beamline_id': 'csx', 'custom': {}},
    'beamline_config':{'beamline_config_id': 12, 'header_id': 1903, 'wavelenght':12.345,
    'custom':{'new_field': 'value}}}
    """
    if isinstance(param_dict, dict):
        try:
            header_dict = param_dict['header']
            beamline_cfg_dict = param_dict['beamline_config']
        except:
            raise KeyError('Input dictionary must have appropriate keys. Please check sample_dict')
    else:
        raise TypeError('Input must be a dictionary. Please check sample_dict')


def log():
    pass


def search():
    pass
