# -*- coding: utf-8 -*-

"""Includes tests for the 'cpp' command"""

from click.testing import CliRunner

from nxstart.cli import cli


def test_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'cpp', '--clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libnx project!\n')


def test_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'cpp', '--no-clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libnx project!\n')
