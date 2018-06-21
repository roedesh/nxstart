# -*- coding: utf-8 -*-

"""Defines the app context and commands."""

import click
import os

from nxstart import app


class Context(object):
    """
    Context to be passed to the subcommands.
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
    """
    Main command group.

    :param ctx: Context
    :param name: Project name
    :param author: Project author
    """
    ctx.name = name
    ctx.author = author


@cli.command('libnx', short_help='generate a new libnx project')
@click.option('--clion/--no-clion', default=False, prompt='Are you using CLion?', help='include CMakeLists.txt')
@pass_context
def libnx(ctx, clion):
    """
    Command for generating a libnx project.

    :param ctx: Context
    :param clion: Using CLion
    """
    app.libnx(ctx.name, ctx.author, clion, ctx.cwd)


@cli.command('brewjs', short_help='generate a new BrewJS project')
@pass_context
def brewjs(ctx):
    """
    Command for generating a BrewJS project.

    :param ctx: Context
    """
    app.brewjs(ctx.name, ctx.author, ctx.cwd)


@cli.command('pynx', short_help='generate a new PyNX project')
@pass_context
def pynx(ctx):
    """
    Command for generating a BrewJS project.

    :param ctx: Context
    """
    app.pynx(ctx.name, ctx.author, ctx.cwd)
