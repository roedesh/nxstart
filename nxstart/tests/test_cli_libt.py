# -*- coding: utf-8 -*-

"""Includes tests for the 'libt' command"""

from click.testing import CliRunner

from nxstart.cli import cli


def test_libt_with_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libt', '--clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libtransistor project!\n')


def test_libt_without_clion():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['-n', 'Test project', '-a', 'Ruud Schroën', 'libt', '--no-clion'])
    assert not result.exception
    assert result.output.endswith('Successfully created the libtransistor project!\n')
