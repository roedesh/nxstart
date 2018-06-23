# -*- coding: utf-8 -*-

"""Includes tests for the functions in nxstart.utils.files"""

import os
import shutil

from nxstart.tests.helpers import DIRECTORY_NAME
from nxstart.utils.files import check_and_create_directory, PROJECT_ROOT, get_full_path


def test_get_full_path():
    path = os.path.join(PROJECT_ROOT, 'test.py')
    path_two = get_full_path('test.py')
    assert path == path_two


def test_check_and_create_directory():
    new_folder_path = os.path.join(PROJECT_ROOT, 'tests', DIRECTORY_NAME)

    check_and_create_directory(new_folder_path)
    assert os.path.isdir(new_folder_path)
    shutil.rmtree(new_folder_path)
