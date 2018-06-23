# -*- coding: utf-8 -*-

"""Includes generic functions such as copying the README.md file."""

import os

from nxstart.utils.files import replace_in_file


def modify_readme_file(folder_path, name, author):
    """
    Simple helper for modifying README.md files.

    :param folder_path: Path where the README.md file is
    :param name: Project name
    :param author: Project author
    """
    new_readme_file = os.path.join(folder_path, 'README.md')
    new_readme_file_replacements = {
        'APP_NAME_PLACEHOLDER': name,
        'APP_AUTHOR_PLACEHOLDER': author

    }
    replace_in_file(new_readme_file, new_readme_file_replacements)


def remove_cmake_lists_file(folder_path):
    """
    Removes the CMakeLists.txt file inside the folder at folder_path.

    :param folder_path: Path to created folder
    """
    cmake_lists_file = os.path.join(folder_path, 'CMakeLists.txt')
    os.remove(cmake_lists_file)


def modify_cmake_lists_file(folder_path, folder_name):
    """
    Modifies the CMakeLists.txt file from folder_path, and will use folder_name as the project name.

    :param folder_path: Path to created folder
    :param folder_name: Project folder name
    """
    cmake_lists_file = os.path.join(folder_path, 'CMakeLists.txt')
    cmake_lists_file_replacements = {
        'FOLDER_NAME_PLACEHOLDER': folder_name
    }
    replace_in_file(cmake_lists_file, cmake_lists_file_replacements)
