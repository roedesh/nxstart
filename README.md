# nx-start

> Project generator for Nintendo Switch homebrews.

[![PyPI version](https://badge.fury.io/py/nxstart.svg)](https://badge.fury.io/py/nxstart)
[![Build status](https://travis-ci.org/roedesh/nxstart.svg?branch=master)](https://travis-ci.org/roedesh/nxstart)

## Table of Contents

<!--ts-->
   * [Features](#features)
   * [Installation](#installation)
   * [Generating a libnx (C++) project](#generating-a-libnx-c++-project)
   * [Generating a libtransistor (C) project](#generating-a-libtransistor-c-project)
   * [Generating a BrewJS project](#generating-a-brewjs-javascript-project)
   * [Generating a PyNX project](#generating-a-pynx-python-project)
   * [Skip prompts](#skip-prompts)
<!--te-->

## Features
- Generate a [libnx](https://github.com/switchbrew/libnx) (C++) project using `nxstart libnx`
- Generate a [libtransistor](https://github.com/reswitched/libtransistor) (C) project using `nxstart libt`
- Generate a [BrewJS](https://github.com/BrewJS) (Javascript) project using `nxstart brewjs`
- Generate a [PyNX](https://github.com/nx-python/PyNX) (Python) project using `nxstart pynx`

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

## Generating a libnx (C++) project
Run `nxstart libnx`. It will ask for a project name, author name and if you are 
using CLion (IDE by Jetbrains). If you say yes to CLion, `CMakeLists.txt` will be included.

The following project structure will be generated:

```
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
```

## Generating a libtransistor (C) project
Run `nxstart libt`. It will ask for a project name, author name and if you are 
using CLion (IDE by Jetbrains). If you say yes to CLion, `CMakeLists.txt` will be included.

The following project structure will be generated:

```
project
│   .editorconfig 
│   .gitignore
│   CMakeLists.txt  // Only if you use CLion
│   main.c          // Your main application file
│   Makefile
│   icon.jpg
│   README.md           
│
```

## Generating a BrewJS (Javascript) project
Run `nxstart brewjs`. It will ask for a project name and author name. The following project structure will be generated:

```
project
│   .editorconfig 
│   .gitignore     
│   index.js        // Your main application file
│   README.md   
│
└───assets
│   
```

## Generating a PyNX (Python) project
Run `nxstart pynx`. It will ask for a project name and author name. The following project structure will be generated:

```
project
│   .editorconfig 
│   .gitignore     
│   main.py        // Your main application file
│   README.md   
│   
```

## Skip prompts
To skip the prompts, provide the necessary flags. For example:
```bash
nxstart -n "My new project" -a "John Doe" libnx --clion
```

Or if you don't use CLion:
```bash
nxstart -n "My new project" -a "John Doe" libnx --no-clion
```