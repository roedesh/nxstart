# -*- coding: utf-8 -*-

"""Includes test for the 'js' command"""

from click.testing import CliRunner

from nxstart.cli import cli


def test_brewjs():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'brewjs'])
    assert not result.exception
    assert result.output.endswith('Successfully created the BrewJS project!\n')


