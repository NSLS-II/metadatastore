__author__ = 'arkilic'

import random

from metadataStore.collectionapi.commands import create


s_id = random.randint(0, 10000)
create(header={'scan_id': s_id})
create(beamline_config={'scan_id': s_id})