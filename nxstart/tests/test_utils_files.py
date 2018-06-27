# -*- coding: utf-8 -*-

"""Includes tests for the functions in nxstart.utils.files"""

import os

from nxstart.tests.helpers import DIRECTORY_NAME, assert_file_contains_strings
from nxstart.utils.files import check_and_create_directory, PROJECT_ROOT, get_full_path, replace_in_file


def test_get_full_path():
    path = os.path.join(PROJECT_ROOT, 'test.py')
    path_two = get_full_path('test.py')
    assert path == path_two


def test_check_and_create_directory(tmpdir):
    new_folder_path = tmpdir.join(DIRECTORY_NAME)

    check_and_create_directory(new_folder_path)
    assert os.path.isdir(new_folder_path)


def test_replace_in_file(tmpdir):
    new_test_file_path = tmpdir.join('testfile.txt')
    with open(new_test_file_path, 'w') as f:
        f.write('TEXT_PLACEHOLDER')
    replace_in_file(new_test_file_path, {
        'TEXT_PLACEHOLDER': 'NEW_TEXT',
    })
    assert_file_contains_strings(new_test_file_path, ['NEW_TEXT'])

