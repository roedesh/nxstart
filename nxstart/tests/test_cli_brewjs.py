# -*- coding: utf-8 -*-

"""Includes test for the 'brewjs' command"""

import os

from click.testing import CliRunner

from nxstart.cli import cli
from nxstart.tests.helpers import (APP_AUTHOR, APP_NAME, DATE_CREATED,
                                   DIRECTORY_NAME, directory_exists,
                                   file_contains_strings)


def test_brewjs():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["-n", APP_NAME, "-a", APP_AUTHOR, "brewjs"])
        assert not result.exception
        assert result.output.endswith("Successfully created the BrewJS project!\n")
        assert directory_exists(os.path.join(DIRECTORY_NAME, "assets"))
        assert file_contains_strings("Source.js", [APP_NAME, APP_AUTHOR, DATE_CREATED])
        assert file_contains_strings("package.json", [APP_NAME, APP_AUTHOR])
