# -*- coding: utf-8 -*-

"""Includes functions for copying the libtransistor template files."""

import datetime
import os
from distutils.dir_util import copy_tree

from nxstart.utils.files import get_full_path, replace_in_file


def create_libt_project(folder_path, name, author):
    """
    Copies the files from templates/base to folder_path and modifies Makefile and source/main.cpp
    to include the project name, author name and current date.

    :param folder_name: Created folder name
    :param folder_path: Path to copy the files to
    :param name: Name of the project
    :param author: Name of the author
    """
    template_folder = get_full_path(os.path.join('templates', 'libt'))
    copy_tree(template_folder, folder_path)

    main_c_file = os.path.join(folder_path, 'main.c')
    main_c_replacements = {
        'APP_AUTHOR_PLACEHOLDER': author,
        'APP_NAME_PLACEHOLDER': name,
        'DATE_PLACEHOLDER': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    replace_in_file(main_c_file, main_c_replacements)

    makefile = os.path.join(folder_path, 'Makefile')
    makefile_replacements = {
        'APP_NAME_PLACEHOLDER': name,
        'APP_AUTHOR_PLACEHOLDER': author
    }
    replace_in_file(makefile, makefile_replacements)
