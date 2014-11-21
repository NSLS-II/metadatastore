__author__ = 'edill'

from metadataStore.userapi.commands import search

ret_dict = search(scan_id=110)

print(ret_dict)