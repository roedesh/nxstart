from setuptools import setup, find_packages

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Get the version number
version = {}
with open(os.path.join(dir_path, 'nxstart', 'version.py')) as fp:
    exec(fp.read(), version)

# Get the long description from the README file
with open(os.path.join(dir_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nxstart',
    description='Nintendo Switch homebrew project generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version['__version__'],
    url='https://github.com/roedesh/nxstart',
    author='Ruud Schroën',
    license='MIT',
    keywords='nintendo switch libnx nx homebrew project generator',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        nxstart=nxstart.cli:cli
    ''',
    project_urls={
        'Bug Reports': 'https://github.com/roedesh/nxstart/issues',
        'Source': 'https://github.com/roedesh/nxstart',
    },
)
