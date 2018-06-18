import click

from nxstart import app
from nxstart.utils.files import get_full_path


@click.command()
@click.option('--name', prompt=True)
@click.option('--author', prompt=True)
@click.option('--clion', prompt=True)
def app_test_wrapper(name, author, clion):
    app.cpp(name, author, clion, get_full_path(''))