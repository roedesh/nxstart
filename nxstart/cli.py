import click
import os

from nxstart import app


class Context(object):
    """
    Context to be passed to the 'cpp' and 'js' methods.
    """

    def __init__(self):
        self.name = None
        self.author = None
        self.cwd = os.getcwd()


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group()
@click.option('--name', '-n', default=None, prompt='Project name', help='The name of your project')
@click.option('--author', '-a', default=None, prompt='Author name',
              help='The full name of the author')
@pass_context
def cli(ctx, name, author):
    ctx.name = name
    ctx.author = author


@cli.command('cpp', short_help='generate a new libnx project')
@click.option('--clion/--no-clion', default=False, prompt='Are you using CLion?', help='include CMakeLists.txt')
@pass_context
def cpp(ctx, clion):
    app.cpp(ctx.name, ctx.author, clion, ctx.cwd)


@cli.command('js', short_help='generate a new BrewJS project')
@pass_context
def js(ctx):
    app.js(ctx.name, ctx.author, ctx.cwd)
