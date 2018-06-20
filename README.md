# nx-start

> Project generator for Nintendo Switch homebrews. A work in progress.

[![PyPI version](https://badge.fury.io/py/nxstart.svg)](https://badge.fury.io/py/nxstart)
[![Build status](https://travis-ci.org/roedesh/nxstart.svg?branch=master)](https://travis-ci.org/roedesh/nxstart)

## Features
- Generate a C/C++ ([libnx](https://github.com/switchbrew/libnx)) project using `nxstart cpp`
- Generate a Javascript ([BrewJS](https://github.com/BrewJS)) project using `nxstart js`

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest), a package manager for
Python.

```bash
pip install nxstart
```

Don't have pip installed? Try installing it, by running this from the
command line:

```bash
curl "https://bootstrap.pypa.io/get-pip.py" | python
```

Or, you can [download the source code](#) for `nxstart` and then run:
```bash
python setup.py install
```
You may need to run the above commands with ``sudo``.

## Creating a C/C++ (libnx) project
Run `nxstart cpp`. It will ask for a project name, author name and if you are 
using CLion (IDE by Jetbrains). If you say yes to CLion, `CMakeLists.txt` will be included.

The following project structure will be created:

```
project
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
```

## Creating a Javascript (BrewJS) project
Run `nxstart js`. It will ask for a project name and author name. The following project structure will be created:

```
project
│   .editorconfig      
│   HOW-TO-RUN.txt  // Explains how to run a BrewJS app on the Switch
│   index.js        // Your main application file
│
└───assets
│   
```

## Skip prompts
To skip the prompts, provide the necessary flags. For example:
```bash
nxstart -n "My new project" -a "John Doe" cpp --clion
```

Or if you don't use CLion:
```bash
nxstart -n "My new project" -a "John Doe" cpp --no-clion
```

Support for 
[PyNX](https://github.com/nx-python/PyNX) projects will be added soon.
