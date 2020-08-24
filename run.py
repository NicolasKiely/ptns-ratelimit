import click

import src.cli.ratelimit


@click.group()
def root():
    pass


src.cli.ratelimit.register(root)


if __name__ == "__main__":
    root()
