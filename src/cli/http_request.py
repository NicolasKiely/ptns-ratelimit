""" Command line management for sending http requests """
import click

import src.controller.http_request


def register(root):
    """ Registers commands """
    @root.group("http")
    def http():
        pass

    @http.command("get")
    @click.argument("domain", nargs=1)
    @click.argument("path", nargs=1)
    def get(domain: str, path: str):
        """ Send HTTP GET request to a url

        :param domain: Domain to send to
        :param path: Document path
        """
        results = src.controller.http_request.http_get(domain, path)
        print(results)
