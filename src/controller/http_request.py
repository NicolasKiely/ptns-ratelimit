import requests


def http_get(domain: str, path: str):
    """ Fetch resource """
    accepted_protocol = any(
        [domain.startswith("http://"), domain.startswith("https://")]
    )
    if not accepted_protocol:
        raise ValueError("Domain protocol not recognized (eg http://)")

    print("Getting url %s%s" % (domain, path))
    r = requests.get(domain + path)
    results = r.text
    return results
