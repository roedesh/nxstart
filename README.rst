nx-start
########

Project generator for Nintendo Switch homebrews.

.. image:: https://travis-ci.org/roedesh/nxstart.svg?branch=master
    :target: https://travis-ci.org/roedesh/nxstart



Features
========
- Generate a libnx (C++) project using ``nxstart libnx``
- Generate a libtransistor (C) project using ``nxstart libt``
- Generate a BrewJS (Javascript) project using ``nxstart brewjs``
- Generate a PyNX (Python) project using ``nxstart pynx``


Installation
============

Install from PyPi using `pip <http://www.pip-installer.org/en/latest>`_, a package manager for
Python.

.. code-block:: bash

     $ pip install nxstart


Don't have pip installed? Try installing it, by running this from the
command line:

.. code-block:: bash

     $ curl https://bootstrap.pypa.io/get-pip.py | python

Or, you can `download the source code <https://github.com/roedesh/nxstart>`_ for ``nxstart`` and then run:

.. code-block:: bash

     $ python setup.py install

You may need to run the above commands with ``sudo``.

Generating a libnx (C++) project
================================
Run ``nxstart libnx``. It will ask for a project name, author name and if you are
using CLion (IDE by Jetbrains). If you say yes to CLion, ``CMakeLists.txt`` will be included.

The following project structure will be generated:

.. code-block:: bash

    project
    │   .editorconfig
    │   .gitignore
    │   CMakeLists.txt  // Only if you use CLion
    │   Makefile
    │   icon.jpg
    │   README.md
    │
    └───data
    │
    └───include
    │
    └───source
        │   main.cpp    // Your main application file


Generating a libtransistor (C) project
======================================
Run ``nxstart libt``. It will ask for a project name, author name and if you are
using CLion (IDE by Jetbrains). If you say yes to CLion, ``CMakeLists.txt`` will be included.

The following project structure will be generated:

.. code-block:: bash

    project
    │   .editorconfig
    │   .gitignore
    │   CMakeLists.txt  // Only if you use CLion
    │   main.c
    │   Makefile
    │   icon.jpg
    │   README.md
    │

Generating a BrewJS (Javascript) project
========================================
Run ``nxstart brewjs``. It will ask for a project name, author name. The following project structure will be generated:

.. code-block:: bash

    project
    │   .editorconfig
    │   .gitignore
    │   package.json
    │   Source.js        // Your main application file
    │   README.md
    │
    └───assets
    │

Generating a PyNX (Python) project
==================================
Run ``nxstart pynx``. It will ask for a project name, author name. The following project structure will be generated:

.. code-block:: bash

    project
    │   .editorconfig
    │   .gitignore
    │   main.py        // Your main application file
    │   README.md
    │

Skip prompts
============
To skip the prompts, provide the necessary flags. For example:

.. code-block:: bash

     $ nxstart -n "My new project" -a "John Doe" libnx --clion

Or if you don't use CLion:

.. code-block:: bash

     $ nxstart -n "My new project" -a "John Doe" libnx --no-clion

Running tests
=============
Tests can be run with the `pytest` command. If you are contributing code, make sure all tests are green before
submitting a PR.