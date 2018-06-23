# -*- coding: utf-8 -*-

"""Includes tests for the 'libt' command"""

import datetime
import os
from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import directory_exists, assert_readme_has_project_and_author_name, \
    assert_makefile_has_project_and_author_name, file_exists, assert_file_contains_strings, APP_AUTHOR, APP_NAME, \
    DATE_CREATED


def test_libt_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', APP_NAME, '-a', APP_AUTHOR, 'libt', '--clion'])
        assert not result.exception
        assert result.output.endswith('Successfully created the libtransistor project!\n')
        assert directory_exists()
        assert file_exists('CMakeLists.txt')
        assert_readme_has_project_and_author_name()
        assert_makefile_has_project_and_author_name()
        main_c_has_valid_data()


def test_libt_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', APP_NAME, '-a', APP_AUTHOR, 'libt', '--no-clion'])
        assert not result.exception
        assert result.output.endswith('Successfully created the libtransistor project!\n')
        assert directory_exists()
        assert not file_exists('CMakeLists.txt')
        assert_readme_has_project_and_author_name()
        assert_makefile_has_project_and_author_name()
        main_c_has_valid_data()


def main_c_has_valid_data():
    assert_file_contains_strings('main.c', [APP_NAME, APP_AUTHOR, DATE_CREATED])
