__author__ = 'arkilic'

from metadataStore.dataapi.mongo_session_init import db

"""
Provides routines that are smart and do the database operations in a pythonic way w/o exposing any aspect of database to client api.
This is done in a way such that database can be deployed locally to any beamline running on localhost at suggested port
and data_catalog-like applications can make use of this data_api module in order to save/restore information
"""

