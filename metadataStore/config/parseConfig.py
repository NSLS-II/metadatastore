__author__ = 'arkilic'

from metadataStore.config.__conf import conf_dict


database = conf_dict.get('metadataStore', 'database')
host = conf_dict.get('metadataStore', 'host')
port = conf_dict.get('metadataStore', 'port')