# -*- coding: utf-8 -*-

"""Includes test for the 'pynx' command"""

from click.testing import CliRunner

from nxstart.cli import cli


def test_pynx():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'pynx'])
    assert not result.exception
    assert result.output.endswith('Successfully created the PyNX project!\n')


