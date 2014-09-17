.. image:: black-and-white-dog-md.png

metadataStore
===========================

Purpose
--------------------------
Advanced techniques for a new generation of hardware will drive higher data rates for experiments at NSLS2 beamlines.
The large data volumes and data acquisition rates require high-performance logging and storage systems.
A typical experiment involves not only the raw data from detectors, but also requires additional data from the beamline
such as experiment owner, beamline_id, energy, motor positions, wavelength, etc… To date, this information is largely
held separately  and manipulated individually. metadataStore is a service that is used in order to record this sort of
metadata in beamline experiments. It is designed and implemented  with the needs of various experiments in mind,
therefore it is flexible enough to satisfy the needs of different experimental setups.

metadataStore can be used independently or embedded with the dataBroker, which utilizes an integrated approach that
integrates different data resources and makes these data resources available for data analysis clients.

Technology
-----------------------------
metadataStore backend database is mongoDb, a No-SQL database that was chosen due to its performance and flexibility.
Python(v 2.7) is chosen as language of implementation. mongoDb Python driver(pymongo) is used to perform database related
operations.


Downloading/Installing
------------------------------

Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python(version 2.7.X), pymongo (version 2.6+), six, Distutils, Git

Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a MongoDb


MongoDb Installation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

*Step 1*::

% sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

*Step 2*::

% sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

*Step 3*::

% sudo apt-get update


*Step 4*::

% sudo apt-get install -y mongodb-org

*Step 5*::

% sudo apt-get install -y mongodb-org=2.6.1 mongodb-org-server=2.6.1 mongodb-org-shell=2.6.1 mongodb-org-mongos=2.6.1mongodb-org-tools=2.6.1


metadataStore Installation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

*Step 1*::

metadataStore is available via git repository: https://github.com/arkilic/metadataStore

Clone this repository::

%git clone https://github.com/arkilic/metadataStore

*Step 2*::

metadataStore includes a setup.py script. Distutils, building and installing a module distribution using the Distutils
is one simple command to run from a terminal::

% python setup.py install

If user does not have sudo access to the machine and/or does not want to install this package for all users::

% python setup.py install --user


Getting Help
-------------------------------

metadataStore can be embedded within other applications or used interactively. If used within IPython, 'help' keyword provides information regarding routines::

% from metadataStore.userapi.commands import search
% help(search)
% search(scan_id=None, owner=None, start_time=None, beamline_id=None, end_time=None, data=False, header_id=None, tags=None, num_header=50)
%
% Provides an easy way to search Header entries inserted in metadataStore
% Usage:
%   search(scan_id=s_id)
%   search(scan_id=s_id, owner='ark*')
%   search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5))
%   search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='arkilic')
%   search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='ark*')
%   search(scan_id=s_id, start_time=datetime.datetime(2014, 4, 5), owner='arkili.')




Schema
------------------------------

Explanation goes here!

*Header Format*::

%{'status': 'In Progress',
% 'beamline_id': None,
% 'tags': ['CSX_Experiment1', 'CSX_Experiment2'],
% 'start_time': datetime.datetime(2014, 9, 16, 13, 7, 58, 299000),
% 'scan_id': 3315, 'custom': {},
% 'event_descriptors': {'event_descriptor_0': {'data_keys': ['motor5', 'motor4', 'motor3', 'list_of_1k', 'motor1', 'motor2'],
%                                              'tag': 'experimental', 'descriptor_name': 'scan',
%                                              'header_id': ObjectId('5418362efa44833ca9b08d08'),
%                                              'event_type_id': 12, '_id': ObjectId('5418362efa44833ca9b08d0a'),
%                                              'events': {
%                                                         'event_0': {'descriptor_id': ObjectId('5418362efa44833ca9b08d0a'),
%                                                                     'description': None,
%                                                                     'header_id': ObjectId('5418362efa44833ca9b08d08'),
%                                                                     'seq_no': 3,
%                                                                     'owner': 'arkilic',
%                                                                     '_id': ObjectId('5418362efa44833ca9b08d0c'),
%                                                                     'data': {u'motor5': 36, u'motor4': 71, u'motor3': 55, u'list_of_1k': [12.3, 34.5, 45.3], u'motor1': 44, u'motor2': 35}},
%                                                         'event_1': {'descriptor_id': ObjectId('5418362efa44833ca9b08d0a'),
%                                                                     'description': None,
%                                                                     'header_id': ObjectId('5418362efa44833ca9b08d08'),
%                                                                     'seq_no': 1,
%                                                                     'owner': u'arkilic',
%                                                                     '_id': ObjectId('5418362efa44833ca9b08d0b'),
%                                                                     'data': {}}}, u'type_descriptor': {}}},
% 'end_time': datetime.datetime(2014, 9, 16, 13, 7, 58, 299000),
% 'owner': u'arkilic',
% 'configs': {'config_0': {'header_id': ObjectId('5418362efa44833ca9b08d08'),
%                          '_id': ObjectId('5418362efa44833ca9b08d09'),
%                          'config_params': {}}},
%                          '_id': ObjectId('5418362efa44833ca9b08d08'),
% 'header_versions': []}



Tutorial
-----------------------------

Start here for a quick overview


Examples
-----------------------------

Examples of how to perform specific tasks
