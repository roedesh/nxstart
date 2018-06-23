# -*- coding: utf-8 -*-

"""Includes tests for the 'libnx' command"""
import datetime
import os

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import directory_exists, assert_readme_has_project_and_author_name, \
    assert_makefile_has_project_and_author_name, assert_file_contains_strings, file_exists


def test_libnx_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libnx', '--clion'])
        assert not result.exception
        assert result.output.endswith('Successfully created the libnx project!\n')
        assert directory_exists()
        assert file_exists('CMakeLists.txt')
        assert_readme_has_project_and_author_name()
        assert_makefile_has_project_and_author_name()
        main_cpp_has_valid_data()


def test_libnx_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libnx', '--no-clion'])
        assert not result.exception
        assert result.output.endswith('Successfully created the libnx project!\n')
        assert directory_exists()
        assert not file_exists('CMakeLists.txt')
        assert_readme_has_project_and_author_name()
        assert_makefile_has_project_and_author_name()
        main_cpp_has_valid_data()


def main_cpp_has_valid_data():
    assert_file_contains_strings(
        os.path.join('source', 'main.cpp'),
        ['Test project', 'Ruud Schroën', datetime.datetime.now().strftime("%Y-%m-%d")]
    )
