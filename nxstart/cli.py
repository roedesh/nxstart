# -*- coding: utf-8 -*-

"""Defines the app context and commands."""

import os

import click
from nxstart.version import __version__ as version

from nxstart import app


class Context(object):
    """
    Context to be passed to the sub-commands.
    """

    def __init__(self):
        self.name = None
        self.author = None
        self.cwd = os.getcwd()


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group()
@click.option('--name', '-n', default=None, help='The name of your project')
@click.option('--author', '-a', default=None, help='The full name of the author')
@pass_context
def cli(ctx, name, author):
    click.echo("""
                                                             
 #    # #    #        ####  #####   ##   #####  #####    
 ##   #  #  #        #        #    #  #  #    #   #      
 # #  #   ##   #####  ####    #   #    # #    #   #      
 #  # #   ##              #   #   ###### #####    #      
 #   ##  #  #        #    #   #   #    # #   #    #      
 #    # #    #        ####    #   #    # #    #   #                                                          
    """)
    click.echo('v%s - by roedesh <Ruud Schroën>' % version)
    if not name:
        name = click.prompt('Please enter the name of your project', type=str)
    if not author:
        author = click.prompt('Please enter your name', type=str)
    ctx.name = name
    ctx.author = author


@cli.command('libnx', short_help='create a new libnx project (C++)')
@click.option('--clion/--no-clion', default=False, prompt='Are you using CLion?', help='include CMakeLists.txt')
@pass_context
def libnx(ctx, clion):
    """
    Command for generating a libnx project.

    :param ctx: Context
    :param clion: Using CLion
    """
    app.libnx(ctx.name, ctx.author, clion, ctx.cwd)


@cli.command('libt', short_help='create a new libtransistor project (C)')
@click.option('--clion/--no-clion', default=False, prompt='Are you using CLion?', help='include CMakeLists.txt')
@pass_context
def libt(ctx, clion):
    """
    Command for generating a libtransistor project.

    :param ctx: Context
    :param clion: Using CLion
    """
    app.libt(ctx.name, ctx.author, clion, ctx.cwd)


@cli.command('brewjs', short_help='create a new BrewJS project (Javascript)')
@pass_context
def brewjs(ctx):
    """
    Command for generating a BrewJS project.

    :param ctx: Context
    """
    app.brewjs(ctx.name, ctx.author, ctx.cwd)


@cli.command('pynx', short_help='create a new PyNX project (Python)')
@pass_context
def pynx(ctx):
    """
    Command for generating a PyNX project.

    :param ctx: Context
    """
    app.pynx(ctx.name, ctx.author, ctx.cwd)
