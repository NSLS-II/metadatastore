__author__ = 'arkilic'
from metadataStore.userapi.commands import create

create(entry_type='header', scan_id=123, header_id=13)
create(entry_type='beamline_config')