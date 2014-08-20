__author__ = 'arkilic'

import os.path
import ConfigParser
from os import path


def check_config_file():
    result = False
    if path.isfile('/etc/dataBroker.conf'):
        result = True
    if path.isfile(os.path.expanduser('~/dataBroker.conf')):
        result = True
    if path.isfile('dataBroker.conf'):
        result = True
    return result

def __loadConfig():
    cf=ConfigParser.SafeConfigParser()
    if check_config_file():
        cf.read([
            '/etc/dataBroker.conf',
            os.path.expanduser('~/dataBroker.conf'),
            'dataBroker.conf'
        ])
    else:
        raise IOError('Configuration file does not exist')
    return cf


conf_dict = __loadConfig()