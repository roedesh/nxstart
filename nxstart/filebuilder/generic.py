# -*- coding: utf-8 -*-

"""Includes generic functions such as copying the README.md file."""

import os
import shutil

from nxstart.utils.files import get_full_path, replace_in_file


def create_readme_file(folder_path, name):
    """
    Copies the README.md file from the templates folder to folder_path,
    and will use name as the title of the document.

    :param folder_path: Path to copy the file to
    :param name: Project name to use as the title
    """
    template_readme_file = get_full_path(os.path.join('templates', 'README.md'))
    shutil.copy2(template_readme_file, folder_path)

    new_readme_file = os.path.join(folder_path, 'README.md')
    new_readme_file_replacements = {
        'APP_NAME_PLACEHOLDER': name
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
