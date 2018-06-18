import os

import click

from nxstart import filebuilder


def cpp(name, author, clion, cwd):
    """
    Command that generates a libnx project.

    :param name: Name of the project
    :param author: Name of the author
    :param clion: Using CLion
    :param cwd: Current working directory
    """
    folder_name = name.lower().replace(" ", "_")
    folder_path = os.path.join(cwd, folder_name)

    if os.path.exists(folder_path):
        click.echo('Directory at %s is not empty.' % folder_path, err=True)
        raise click.Abort()

    os.makedirs(folder_path)
    filebuilder.cpp.create_libnx_project(folder_path, name, author)
    filebuilder.generic.create_readme_file(folder_path, name)

    if clion:
        filebuilder.cpp.create_cmake_lists_file(folder_path, folder_name)

    click.echo("Successfully created the libnx project!")
