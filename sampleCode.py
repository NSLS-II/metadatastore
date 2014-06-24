__author__ = 'arkilic'
import datetime
from metadataStore.userapi.commands import *
import time




sample_dict = {'header':{'header_id':1903, 'owner': 'arkilic', 'beamline_id': 'csx', 'custom': {}},
    'beamline_config':{'beamline_config_id': 12, 'header_id': 1903, 'wavelength':12.345,
    'custom':{'new_field': 'value'}}}


create(sample_dict)