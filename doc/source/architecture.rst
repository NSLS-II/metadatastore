Library Reference
=================

Collection Declarations
-----------------------

Provides information regarding MongoDB Collection template creation. This is analogous to table definitions in SQL databases

Header
^^^^^^

.. autoclass:: metadataStore.database.collections.Header
   :members: __init__, save


EventDescriptor
^^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.EventDescriptor
   :members: __init__, save

Event
^^^^^

.. autoclass:: metadataStore.database.collections.Event
   :members: __init__, save


BeamlineConfig
^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.BeamlineConfig
   :members: __init__, save



Collection API
--------------

Provides routines for data collection libraries to populate metadataStore

.. automodule:: metadataStore.collectionapi.commands
   :members:


User API
--------

Provides routines for data collection libraries to populate metadataStore

.. automodule:: metadataStore.userapi.commands
   :members:


Utility Library
---------------

.. automodule:: metadataStore.utilities.utility
   :members:
