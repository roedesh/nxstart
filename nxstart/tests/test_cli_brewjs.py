# -*- coding: utf-8 -*-

"""Includes test for the 'brewjs' command"""

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import directory_exists, file_contains_strings, APP_NAME, APP_AUTHOR, DATE_CREATED


def test_brewjs():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', APP_NAME, '-a', APP_AUTHOR, 'brewjs'])
        assert not result.exception
        assert result.output.endswith('Successfully created the BrewJS project!\n')
        assert directory_exists()
        assert file_contains_strings('Source.js', [APP_NAME, APP_AUTHOR, DATE_CREATED])
        assert file_contains_strings('package.json', [APP_NAME, APP_AUTHOR])
