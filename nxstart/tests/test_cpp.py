import os
import shutil

from click.testing import CliRunner

from nxstart.tests.base import app_test_wrapper
from nxstart.utils.files import get_full_path


def test_with_clion():
    runner = CliRunner()
    result = runner.invoke(app_test_wrapper, input='Test Project\nRuud Schroën\ny\n')
    cleanup()
    assert not result.exception
    assert result.output.endswith('Successfully created the libnx project!\n')


def cleanup():
    folder = get_full_path('test_project')
    if os.path.exists(folder):
        shutil.rmtree(get_full_path('test_project'))
