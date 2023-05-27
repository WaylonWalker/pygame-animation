from rich.console import Console
import typer

from pygame_animation.cli.common import verbose_callback
from pygame_animation.config import config as configuration

config_app = typer.Typer()


@config_app.callback()
def config(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    "configuration cli"


@config_app.command()
def show(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    Console().print(configuration)
