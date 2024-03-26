# Imports
import os
import click
import giphy_cli

#API Key import
API_KEY=os.environ["GIPHY_API_KEY"]

GighyCLI = giphy_cli()

@click.group()
def gif():
    click.echo('Make API')
    click.echo('Make CLI')


@gif.command()
@click.option('--count', default=5, help='The number of gifs to return.')
@click.option('--markdown', default=0, help='Returns the gifs in Markdown format.')

def trending_cmd(count, markdown):
    #Retrieve trending GIFs.
    results = GighyCLI.get_trending(count, markdown)
    click.echo(results)

@gif.command()
@click.option('--count', default=5, help='The number of gifs to return.')
@click.option('--markdown', default=0, help='Returns the gifs in Markdown format.')
@click.option('--lucky', default=0, help='Simlaur to Googles Im feeling lucky button, this will return a random gif.')

def search_cmd(count, markdown, query, lucky):
    #Retrieve trending GIFs.
    results = GighyCLI.get_search(count, markdown, query, lucky)
    click.echo(results)


if __name__ == "__main__":
    gif()


############Intialize the tool, give the diffent parts(that need it) API Keys