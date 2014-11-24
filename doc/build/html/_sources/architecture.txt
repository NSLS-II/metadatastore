Library Reference
==================================


Collection Declarations
---------------------------------

Provides information regarding MongoDB Collection template creation. This is analogous to table definitions in SQL databases

Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.Header
   :members: __init__


EventDescriptor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.EventDescriptor
   :members: __init__

Event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.Event
   :members: __init__


BeamlineConfig
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: metadataStore.database.collections.BeamlineConfig
   :members: __init__



Collection API
--------------------------------------

Provides routines for data collection libraries to populate metadataStore

.. automodule:: metadataStore.collectionapi.commands
   :members:


User API
-------------------------------------

Provides routines for data collection libraries to populate metadataStore

.. automodule:: metadataStore.userapi.commands
   :members:


Data API
----------------------------------

Includes the raw commands. Developers/expert users can create a set of new behaviors using this module.

.. automodule:: metadataStore.dataapi.commands
   :members:


Utiliy Library
-----------------------------------

.. automodule:: metadataStore.utilities.utility
   :members:


