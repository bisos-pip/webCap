====================================
bisos.webCap: BISOS Web Capabilities
====================================

.. contents::
   :depth: 3
..

Overview
========

*bisos.webCap* provides general facilities for creation of Web
Capabilities.

bisos.webCap is a python package that uses the
`PyCS-Framework <https://github.com/bisos-pip/pycs>`__.

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `Scope of BISOS Web Capabilities
   Foundations <#scope-of-bisos-web-capabilities-foundations>`__

   -  `NGINX <#nginx>`__
   -  `Python Back-End <#python-back-end>`__
   -  `React Front End <#react-front-end>`__

-  `BISOS Web Apps <#bisos-web-apps>`__

   -  `csPlayer <#csplayer>`__
   -  `ByName Sites <#byname-sites>`__
   -  `ByName Factory <#byname-factory>`__

-  `Relevant Resources <#relevant-resources>`__
-  `Installation <#installation>`__

   -  `Installation With pip <#installation-with-pip>`__
   -  `Installation With pipx <#installation-with-pipx>`__
   -  `Post Installation Basic
      Testing <#post-installation-basic-testing>`__

-  `Usage <#usage>`__

   -  `Local Usage (system
      command-line) <#local-usage-system-command-line>`__

-  `Documentation and Blee-Panels <#documentation-and-blee-panels>`__

   -  `bisos.webCap Blee-Panels <#bisoswebcap-blee-panels>`__

-  `Support <#support>`__
-  `Planned Improvements <#planned-improvements>`__

Scope of BISOS Web Capabilities Foundations
===========================================

NGINX
-----

=============== ================= =======
nginx           BISOS Module Name Comment
virtual domains                   
=============== ================= =======

Python Back-End
---------------

======== ============== =========
django   djangoAdmin.cs Comment
postgres                
Gunicorn                Not uwsgi
systemd                 
======== ============== =========

React Front End
---------------

+---------------------------------------------------+-----------------+---------+
| react                                             | BISOS Resources | Comment |
+---------------------------------------------------+-----------------+---------+
| gatsby                                            |                 |         |
+---------------------------------------------------+-----------------+---------+
| reveal.js                                         |                 |         |
+---------------------------------------------------+-----------------+---------+
| https://github.com/bouzidanas/react-reveal-slides |                 |         |
+---------------------------------------------------+-----------------+---------+

BISOS Web Apps
==============

csPlayer
--------

ByName Sites
------------

ByName Factory
--------------

Relevant Resources
==================

-  https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-debian-11
-  https://tutos.readthedocs.io/en/latest/source/ndg.html

Installation
============

The sources for the bisos.webCap pip package are maintained at:
https://github.com/bisos-pip/webCap.

The bisos.webCap pip package is available at PYPI as
https://pypi.org/project/bisos.webCap

You can install bisos.webCap with pip or pipx.

Installation With pip
---------------------

If you need access to bisos.webCap as a python module, you can install
it with pip:

.. code:: bash

   pip install bisos.webCap

Installation With pipx
----------------------

If you only need access to bisos.webCap on command-line, you can install
it with pipx:

.. code:: bash

   pipx install bisos.webCap

Post Installation Basic Testing
-------------------------------

After the installation, run some basic tests:

.. code:: bash

   webCap.cs
   webCap networking.interfaces.lo.bindings

Usage
=====

Local Usage (system command-line)
---------------------------------

``webCap.cs`` does the equivalent of webCap.

.. code:: bash

   bin/webCap.cs

Documentation and Blee-Panels
=============================

bisos.webCap is part of ByStar Digital Ecosystem http://www.by-star.net.

This module's primary documentation is in the form of Blee-Panels.
Additional information is also available in:
http://www.by-star.net/PLPC/180047

bisos.webCap Blee-Panels
------------------------

bisos.webCap Blee-Panles are in ./panels directory. From within Blee and
BISOS these panles are accessible under the Blee "Panels" menu.

See
`file:./panels/_nodeBase_/fullUsagePanel-en.org <./panels/_nodeBase_/fullUsagePanel-en.org>`__
for a starting point.

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Planned Improvements
====================

-  Enumerate applicabilities: telecom/SON, datacenter, CMIP-MOs
-  py3/bisos/webCap/tocsModule\ :sub:`csu`.py
