{{ cookiecutter.project_name }}
=========================================

{{ cookiecutter.project_short_description }}
{% if cookiecutter.private_repo == "n" %}
Installation
------------

.. readme-install-start

{{ cookiecutter.project_name }} can be installed using ``pip`` as follows:

.. code-block:: console

   $ pip install {{ cookiecutter.project_name }}

.. readme-install-end

Usage
-----

Refer to the `full documentation <https://{{ cookiecutter.project_name }}.readthedocs.io>`_
for the in-depth usage.

.. readme-usage-start

Prerequisite
************

* TODO

Basic Usage
***********

* TODO

.. readme-usage-end

Donate 
------

.. readme-donate-start

I made this has a fun side project and it's free for anyone to use.
If you like it and wish to donate here's a few of my crypto wallets. 

.. _tbl-grid:

+----------------------------------------+--------------------------------------+-----------------------------------------+
| Ethereum and L2s (0x29006...)          | Monero (85tBS7YSrM5...)              | Peercoin (PBzj1ZwMDW...)                |
|                                        |                                      |                                         |
+========================================+======================================+=========================================+
| |EthereumQR|                           | |MoneroQR|                           | |PeercoinQR|                            |
+----------------------------------------+--------------------------------------+-----------------------------------------+

.. |EthereumQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/{{ cookiecutter.project_name }}/master/docs/_qrcodes/ethereum.png
  :width: 300
  :alt: EthereumQR

.. |MoneroQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/{{ cookiecutter.project_name }}/master/docs/_qrcodes/monero.png
  :width: 300
  :alt: MoneroQR

.. |PeercoinQR| image:: https://raw.githubusercontent.com/SpeakinTelnet/{{ cookiecutter.project_name }}/master/docs/_qrcodes/peercoin.png
  :width: 300
  :alt: PeerCoinQR

.. readme-donate-end

* Free software: MIT
* Documentation: https://{{ cookiecutter.project_name }}.readthedocs.io.

Credits
-------

* TODO

⊂(▀¯▀⊂)
{% endif %}
