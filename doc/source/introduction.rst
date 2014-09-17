Overview
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
metadataStore is available via git repository: https://github.com/arkilic/metadataStore

You clone this repository::

%git clone https://github.com/arkilic/metadataStore


metadataStore includes a setup.py script. Distutils, building and installing a module distribution using the Distutils
is one simple command to run from a terminal::

% python setup.py install

If user does not have sudo access to the machine and/or does not want to install this package for all users::

% python setup.py install --user


Getting Help
-------------------------------
Python Docs and contact information



Schema
------------------------------


Tutorial
-----------------------------

Start here for a quick overview


Examples
-----------------------------

Examples of how to perform specific tasks
