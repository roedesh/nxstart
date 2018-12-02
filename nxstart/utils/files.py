# -*- coding: utf-8 -*-

"""Includes functions for working with the filesystem."""

import os
from os.path import dirname, join

import click

PROJECT_ROOT = dirname(dirname(__file__))  # nxstart project directory


def get_full_path(*path):
    """
    Get full path within project directory.

    :param path: Path to join with PROJECT_ROOT
    :return Path to file or directory within project
    """
    return join(PROJECT_ROOT, *path)


def replace_in_file(file, replacements):
    """
    Replace strings with the replacements in the given file.

    :param file: File to replace strings in
    :param replacements: {string to replace: replacement, }
    """
    lines = []
    with open(file) as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            lines.append(line)
    with open(file, "w") as outfile:
        for line in lines:
            outfile.write(line)


def check_and_create_directory(folder_path):
    """
    Try to create the directory at folder_path. If the directory already exists, abort the application.

    :param folder_path: Directory to create
    """
    if os.path.exists(folder_path):
        click.echo("Directory at %s is not empty." % folder_path, err=True)
        raise click.Abort()

    os.makedirs(folder_path)
