# nx-start

> Project generator for Nintendo Switch homebrews. A work in progress.

[![PyPI version](https://badge.fury.io/py/nxstart.svg)](https://badge.fury.io/py/nxstart)

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest), a package manager for
Python.

```
pip install nxstart
```

Don't have pip installed? Try installing it, by running this from the
command line:

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

Or, you can [download the source code](#) for `nxstart` and then run:
```
python setup.py install
```
You may need to run the above commands with ``sudo``.

## Getting Started
To create a C/C++ libnx project simply run `nxstart cpp`. It will ask for a project name, author name and if you are 
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

To skip the prompts, provide the necessary flags. For example:
```
nxstart -n "My new project" -a "John Doe" cpp --clion
```

Or if you don't use CLion:
```
nxstart -n "My new project" -a "John Doe" cpp --no-clion
```

Support for 
[PyNX](https://github.com/nx-python/PyNX) and [BrewJS](https://github.com/BrewJS) projects will be added soon.