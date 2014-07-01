__author__ = 'arkilic'

import os.path
import ConfigParser


def __loadConfig():
    cf=ConfigParser.SafeConfigParser()
    cf.read([
        '/etc/dataBroker.conf',
        os.path.expanduser('~/dataBroker.conf'),
        'dataBroker.conf'
    ])
    return cf


conf_dict = __loadConfig()