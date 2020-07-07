import click

from literal_dice.literal_dice import LiteralDice


@click.command()
@click.option('-c', '--count', default=10, help="Number of shuffles.")
@click.argument('word')
def dice(count, word):
    """Simple program to shuffle words."""
    d = LiteralDice(word)
    for i in range(count):
        click.echo(d.shuffle())
