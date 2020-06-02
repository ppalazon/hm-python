import textwrap

import click
import requests

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language):
    """The hypermodern Python project."""
    try:
        data = wikipedia.random_page(language=language)
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
