# -*- coding: utf-8 -*-

"""Includes functions for copying the libnx template files."""

import datetime
import os
import shutil
from distutils.dir_util import copy_tree

from nxstart.utils.files import get_full_path, replace_in_file


def create_libnx_project(folder_path, name, author):
    """
    Copies the files from templates/base to folder_path and modifies Makefile and source/main.cpp
    to include the project name, author name and current date.

    :param folder_path: Path to copy the files to
    :param name: Name of the project
    :param author: Name of the author
    """
    template_folder = get_full_path(os.path.join('templates', 'cpp'))
    copy_tree(template_folder, folder_path)

    main_cpp_file = os.path.join(folder_path, 'source', 'main.cpp')
    main_cpp_replacements = {
        'APP_AUTHOR_PLACEHOLDER': author,
        'APP_NAME_PLACEHOLDER': name,
        'DATE_PLACEHOLDER': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    replace_in_file(main_cpp_file, main_cpp_replacements)

    makefile = os.path.join(folder_path, 'Makefile')
    makefile_replacements = {
        'APP_NAME_PLACEHOLDER': name,
        'APP_AUTHOR_PLACEHOLDER': author
    }
    replace_in_file(makefile, makefile_replacements)


def create_cmake_lists_file(folder_path, folder_name):
    """
    Copies the CMakeLists.txt file from the templates folder to folder_path,
    and will use folder_name as the project name.

    This is useful for people who use CLion as their IDE.

    :param folder_path: Path to copy the file to
    :param folder_name: Project folder name
    """
    template_cmake_lists_file = get_full_path(os.path.join('templates', 'CMakeLists.txt'))
    shutil.copy2(template_cmake_lists_file, folder_path)

    cmake_lists_file = os.path.join(folder_path, 'CMakeLists.txt')
    cmake_lists_file_replacements = {
        'FOLDER_NAME_PLACEHOLDER': folder_name
    }
    replace_in_file(cmake_lists_file, cmake_lists_file_replacements)
