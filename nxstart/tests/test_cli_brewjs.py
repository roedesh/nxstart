# -*- coding: utf-8 -*-

"""Includes test for the 'brewjs' command"""
import datetime

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import directory_exists, assert_file_contains_strings


def test_brewjs():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'brewjs'])
        assert not result.exception
        assert result.output.endswith('Successfully created the BrewJS project!\n')
        assert directory_exists()
        assert_file_contains_strings(
            'index.js',
            ['Test project', 'Ruud Schroën', datetime.datetime.now().strftime("%Y-%m-%d")]
        )
