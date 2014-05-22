Mongolog
========

Mongodb Implementation of Olog

Overview
------

Mongolog utilizes the NoSQL nature of MongoDB in order to make Olog-like logging capabilities

Architecture
-------

MongoDB collections are "logbooks" in Olog terms. MongoDB documents will be used to host text, owner, tag, create/modify date, attribute names and values as well as attachments.

Database is composed of two parts. Python interface is used for both create and experimental logging tools portions.
 Python data structures such as dictionaries will be used frequently as they have json-like structure. RESTful web services will be available for web interfaces and EXLog like libraries.

