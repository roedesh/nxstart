# -*- coding: utf-8 -*-

"""Defines the logic for the commands."""

import click

from nxstart import filebuilder
from nxstart.utils.files import check_and_create_directory
from nxstart.utils.strings import generate_folder_name_and_path


def libnx(name, author, clion, cwd):
    """
    Function that holds the logic for the 'libnx' command.

    :param name: Name of the project
    :param author: Name of the author
    :param clion: Using CLion
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.libnx.create_libnx_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    if clion:
        filebuilder.generic.modify_cmake_lists_file(folder_path, folder_name)
    else:
        filebuilder.generic.remove_cmake_lists_file(folder_path)

    click.echo("Successfully created the libnx project!")


def libt(name, author, clion, cwd):
    """
    Function that holds the logic for the 'libt' command.

    :param name: Name of the project
    :param author: Name of the author
    :param clion: Using CLion
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.libt.create_libt_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    if clion:
        filebuilder.generic.modify_cmake_lists_file(folder_path, folder_name)
    else:
        filebuilder.generic.remove_cmake_lists_file(folder_path)

    click.echo("Successfully created the libtransistor project!")


def brewjs(name, author, cwd):
    """
    Function that holds the logic for the 'brewjs' command.

    :param name: Name of the project
    :param author: Name of the author
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.brewjs.create_brewjs_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    click.echo("Successfully created the BrewJS project!")


def pynx(name, author, cwd):
    """
    Function that holds the logic for the 'pynx' command.

    :param name: Name of the project
    :param author: Name of the author
    :param cwd: Current working directory
    """
    folder_name, folder_path = generate_folder_name_and_path(name, cwd)
    check_and_create_directory(folder_path)

    filebuilder.pynx.create_pynx_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    click.echo("Successfully created the PyNX project!")
