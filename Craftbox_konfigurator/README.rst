========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/Craftbox_konfigurator/badge/?style=flat
    :target: https://readthedocs.org/projects/Craftbox_konfigurator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/DanielKuty/Craftbox_konfigurator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/DanielKuty/Craftbox_konfigurator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/DanielKuty/Craftbox_konfigurator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/DanielKuty/Craftbox_konfigurator

.. |requires| image:: https://requires.io/github/DanielKuty/Craftbox_konfigurator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/DanielKuty/Craftbox_konfigurator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/DanielKuty/Craftbox_konfigurator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/DanielKuty/Craftbox_konfigurator

.. |version| image:: https://img.shields.io/pypi/v/Craftbox-konfigurator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/Craftbox-konfigurator

.. |commits-since| image:: https://img.shields.io/github/commits-since/DanielKuty/Craftbox_konfigurator/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/DanielKuty/Craftbox_konfigurator/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/Craftbox-konfigurator.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/Craftbox-konfigurator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/Craftbox-konfigurator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/Craftbox-konfigurator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/Craftbox-konfigurator.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/Craftbox-konfigurator


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install Craftbox-konfigurator

Documentation
=============

https://Craftbox_konfigurator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
