""" Command line management of rate limitting """
import click

import src.controller.ratelimit


def register(root):
    """ Registers commands """
    @root.group("rate_limit")
    def rate_limit():
        pass

    @rate_limit.command("set")
    @click.argument("domain", nargs=1)
    @click.argument("limit", nargs=1)
    def set_rate_limit(domain: str, limit: float):
        """ Set the rate limit for a given domain

        :param domain: Name of the domain
        :param limit: Limit in requests per hour
        """
        try:
            limit = float(limit)
        except ValueError:
            print("Limit argument must be numerical value")
            return

        src.controller.ratelimit.set_rate_limit(domain, limit)

    @rate_limit.command("get")
    @click.argument("domain", nargs=1)
    def get_rate_limit(domain: str):
        """ Fetch the rate limit for a given domain

        :param domain: Name of the domain
        """
        limit = src.controller.ratelimit.get_rate_limit(domain)
        has_limit = src.controller.ratelimit.has_rate_limit(domain)
        if not has_limit:
            print("Warning: Limit for domain has not been set")
        print("Limit in request per hour: %s" % limit)
