# -*- coding: utf-8 -*-

"""Includes functions for copying the BrewJS template files."""

import datetime
import os
from distutils.dir_util import copy_tree

from nxstart.utils.files import get_full_path, replace_in_file


def create_brewjs_project(folder_path, name, author):
    """
    Copies the files from templates/js to folder_path and modifies index.js to include the author name.

    :param folder_path: Path to copy the files to
    :param name: Name of the project
    :param author: Name of the author
    """
    template_folder = get_full_path(os.path.join('templates', 'js'))
    copy_tree(template_folder, folder_path)

    main_js_file = os.path.join(folder_path, 'index.js')
    main_js_replacements = {
        'APP_AUTHOR_PLACEHOLDER': author,
        'APP_NAME_PLACEHOLDER': name,
        'DATE_PLACEHOLDER': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    replace_in_file(main_js_file, main_js_replacements)