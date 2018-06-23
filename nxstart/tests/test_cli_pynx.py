# -*- coding: utf-8 -*-

"""Includes test for the 'pynx' command"""
import datetime
import os

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import assert_readme_has_project_and_author_name, assert_file_contains_strings, \
    directory_exists


def test_pynx():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'pynx'])
        assert not result.exception
        assert result.output.endswith('Successfully created the PyNX project!\n')
        assert directory_exists()
        assert_file_contains_strings(
            os.path.join('main.py'),
            ['Test project', 'Ruud Schroën', datetime.datetime.now().strftime("%Y-%m-%d")]
        )
        assert_readme_has_project_and_author_name()
