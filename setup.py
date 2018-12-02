from setuptools import setup, find_packages

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Get the version number
version = {}
with open(os.path.join(dir_path, "nxstart", "version.py")) as fp:
    exec(fp.read(), version)


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="nxstart",
    description="Nintendo Switch homebrew project generator",
    long_description=readme(),
    long_description_content_type="text/markdown",
    version=version["__version__"],
    url="https://github.com/roedesh/nxstart",
    author="Ruud Schroën",
    license="MIT",
    keywords="nintendo switch libnx nx homebrew project generator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        nxstart=nxstart.cli:cli
    """,
    project_urls={
        "Bug Reports": "https://github.com/roedesh/nxstart/issues",
        "Source": "https://github.com/roedesh/nxstart",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
)
