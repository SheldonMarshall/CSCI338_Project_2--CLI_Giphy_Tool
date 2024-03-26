# Imports
import os
import click
from giphy_cli import GiphyCLI

#API Key import
API_KEY=os.environ["GIPHY_API_KEY"]
Giphy_CLI = GiphyCLI()

@click.group()
def gif():
    pass

@gif.command()
@click.option('--count', default=5, help='The number of gifs to return.')
@click.option('--markdown', is_flag=True, help='Returns the gifs in Markdown format.')
def trending(count, markdown):
    # Retrieve trending GIFs.
    Giphy_CLI.get_trending(API_KEY, count, markdown)

@gif.command()
@click.option('--count', default=5, help='The number of gifs to return.')
@click.option('--markdown', is_flag=True, help='Returns the gifs in Markdown format.')
@click.option('--query', prompt='Search query', help='The search string to find specific gifs.')
@click.option('--lucky', is_flag=True, help='Similar to Google’s "I’m Feeling Lucky" button, this will return a random gif.')

def search(count, markdown, query, lucky):
    #Retrieve trending GIFs.
    results = Giphy_CLI.get_search(count, markdown, query, lucky)
    click.echo(results)


if __name__ == "__main__":
    gif()


############Intialize the tool, give the diffent parts(that need it) API Keys