# -*- coding: utf-8 -*-

"""Includes functions for copying the PyNX template files."""

import datetime
import os
from distutils.dir_util import copy_tree

from nxstart.utils.files import get_full_path, replace_in_file


def create_pynx_project(folder_path, name, author):
    """
    Copies the files from templates/base to folder_path and modifies Makefile and source/main.cpp
    to include the project name, author name and current date.

    :param folder_path: Path to copy the files to
    :param name: Name of the project
    :param author: Name of the author
    """
    template_folder = get_full_path(os.path.join('templates', 'pynx'))
    copy_tree(template_folder, folder_path)

    main_cpp_file = os.path.join(folder_path, 'main.py')
    main_cpp_replacements = {
        'APP_AUTHOR_PLACEHOLDER': author,
        'APP_NAME_PLACEHOLDER': name,
        'DATE_PLACEHOLDER': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    replace_in_file(main_cpp_file, main_cpp_replacements)
