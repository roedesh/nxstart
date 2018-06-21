# -*- coding: utf-8 -*-

"""Includes tests for the 'libnx' command"""

from click.testing import CliRunner

from nxstart.cli import cli


def test_libnx_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libnx', '--clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libnx project!\n')


def test_libnx_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libnx', '--no-clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libnx project!\n')
