# -*- coding: utf-8 -*-

"""Contains helper functions to use in tests"""

import datetime
import os

# Some constants to be used in tests
APP_NAME = "Test project"
APP_AUTHOR = "Ruud Schroën"
DATE_CREATED = datetime.datetime.now().strftime("%Y-%m-%d")
DIRECTORY_NAME = "test_project"


def directory_exists(folder_name=DIRECTORY_NAME):
    """
    Check if a folder exists
    """
    return os.path.isdir(folder_name)


def file_exists(file_path):
    """
    Check if the file at file_path exists.

    :param file_path: File to check
    """
    return os.path.isfile(os.path.join(DIRECTORY_NAME, file_path))


def file_contains_strings(file_path, strings):
    """
    Make sure that each given string is in the file.

    :param file_path: File to check
    :param strings: List of strings
    """
    with open(os.path.join(DIRECTORY_NAME, file_path), "r") as file:
        data = file.read().replace("\n", "")
        for s in strings:
            if s not in data:
                return False
    return True


def readme_has_project_and_author_name():
    """
    Checks that the README.md contains the project and author name.
    """
    return file_contains_strings("README.md", [APP_NAME, APP_AUTHOR])


def makefile_has_project_and_author_name():
    """
    Check that the Makefile contains the project and author name.
    """
    return file_contains_strings("Makefile", [APP_NAME, APP_AUTHOR])
