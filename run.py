import click

import src.cli.http_request
import src.cli.ratelimit


@click.group()
def root():
    pass


src.cli.ratelimit.register(root)
src.cli.http_request.register(root)


if __name__ == "__main__":
    root()
