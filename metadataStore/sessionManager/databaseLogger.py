__author__ = 'arkilic'
__version__ = '0.0.2'

import logging
import getpass


def create_file_logger(filename):
    if not filename.endswith('.log'):
        filename += '.log'
    return logging.FileHandler(filename)


class DbLogger(object):
    def __init__(self, db_name, host, port):
        """
        Constructor: MongoClient, Database, and native python loggers are created
        """
        self.logger = logging.getLogger('MetadataStore')
        print self.logger
        log_root = '/tmp/MetaDataStore'
        try:
            log_handler = create_file_logger(log_root)
        except IOError:
            # probably permission denied because of user permissions
            log_root += '_{}'.format(getpass.getuser())
            log_handler = create_file_logger(log_root)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.WARNING)
        self.host = host
        self.port = port
        self.db_name = db_name
