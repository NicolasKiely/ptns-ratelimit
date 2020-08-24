import os


#: Default limit for domain
default_limit = os.environ.get("DEFAULT_LIMIT", 5*60)


class DomainRates:
    """ Stores rate limits for each domain """
    #: Limits per domain
    _domain_limits = {}

    @classmethod
    def set(cls, domain: str, limit: float):
        """ Sets limit value for given domain """
        cls._domain_limits[domain] = limit

    @classmethod
    def get(cls, domain: str):
        """ Retrieves limit value for given domain """
        return cls._domain_limits.get(domain, default_limit)

    @classmethod
    def has(cls, domain: str):
        """ Check if the domain has a limit set """
        return domain in cls._domain_limits
