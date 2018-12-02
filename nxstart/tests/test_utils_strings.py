# -*- coding: utf-8 -*-

"""Includes tests for the functions in nxstart.utils.strings"""

import os

from nxstart.tests.helpers import APP_NAME, DIRECTORY_NAME
from nxstart.utils.strings import generate_folder_name_and_path


def test_generate_folder_name_and_path():
    cwd = os.getcwd()
    folder_name, folder_path = generate_folder_name_and_path(APP_NAME, cwd)
    assert folder_name == DIRECTORY_NAME
    assert folder_path == os.path.join(cwd, folder_name)
