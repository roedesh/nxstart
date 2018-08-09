# -*- coding: utf-8 -*-

"""Includes test for the 'pynx' command"""

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import readme_has_project_and_author_name, file_contains_strings, \
    directory_exists, APP_NAME, APP_AUTHOR, DATE_CREATED


def test_pynx():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', APP_NAME, '-a', APP_AUTHOR, 'pynx'])
        assert not result.exception
        assert result.output.endswith('Successfully created the PyNX project!\n')
        assert directory_exists()
        assert file_contains_strings('main.py', [APP_NAME, APP_AUTHOR, DATE_CREATED])
        assert readme_has_project_and_author_name()
