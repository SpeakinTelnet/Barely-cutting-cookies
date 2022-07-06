Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================


.. _tbl-grid:

+----------------------------------------+--------------------------------------+-----------------------------------------+
| Ethereum and L2s (0x29006...)          | Monero (85tBS7YSrM5...)              | Peercoin (PBzj1ZwMDW...)                |
|                                        |                                      |                                         |
+========================================+======================================+=========================================+
| .. figure:: _qrcodes/ethereum.png      | .. figure:: _qrcodes/monero.png      | .. figure:: _qrcodes/peercoin.png       |
+----------------------------------------+--------------------------------------+-----------------------------------------+

Table of Contents
-----------------

.. toctree::
   :maxdepth: 1
   :caption: Overview

   usage
   {% if '{{ cookiecutter.scope }}' == 'public' -%}contributing
   {% endif -%}{% if '{{ cookiecutter.scope }}' == 'public' -%}authors
   {% endif -%}{% if '{{ cookiecutter.scope }}' == 'public' -%}history
   {% endif -%}

.. toctree::
   :maxdepth: 1
   :caption: Modules



Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
