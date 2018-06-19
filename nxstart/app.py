import os

import click

from nxstart import filebuilder
from nxstart.utils.files import check_and_create_directory
from nxstart.utils.strings import generate_folder_name_and_path


def cpp(name, author, clion, cwd):
    """
    Command that generates a libnx project.

    :param name: Name of the project
    :param author: Name of the author
    :param clion: Using CLion
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.cpp.create_libnx_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    if clion:
        filebuilder.cpp.create_cmake_lists_file(folder_path, folder_name)

    click.echo("Successfully created the libnx project!")


def js(name, author, cwd):
    """
    Command that generates a BrewJS project.

    :param name: Name of the project
    :param author: Name of the author
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.js.create_brewjs_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    click.echo("Successfully created the BrewJS project!")






