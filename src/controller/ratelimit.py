""" Controller logic for managing rate limits """
import src.models.ratelimit


def set_rate_limit(domain: str, limit: float):
    """ Sets internal rate limit of a domain

    :param domain: Name of the domain
    :param limit: Limit in request per hour
    """
    if not isinstance(domain, str):
        raise ValueError("Domain must be a string")

    if type(limit) not in (int, float):
        raise ValueError("Limit must be numeric")

    if limit < 0:
        raise ValueError("Limit must be zero or positive")

    src.models.ratelimit.DomainRates.set(
        domain, limit
    )


def get_rate_limit(domain: str):
    """ Fetches internal rate limit of a domain

    :param domain: Name of the domain
    :return: Numerical limit in requests per hour
    """
    return src.models.ratelimit.DomainRates.get(domain)


def has_rate_limit(domain: str):
    """ Returns whether or not rate limit has been set for domain

    :param domain: Name of the domain
    :return: True iff rate limit has been set
    """
    return src.models.ratelimit.DomainRates.has(domain)
