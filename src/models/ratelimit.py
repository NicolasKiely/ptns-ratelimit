import os
from src.models import schema


#: Default limit for domain
default_limit = os.environ.get("DEFAULT_LIMIT", 5*60)


class DomainRates:
    """ Stores rate limits for each domain """
    @classmethod
    def set(cls, domain: str, limit: float):
        """ Sets limit value for given domain """
        session = schema.DB.get_session()
        domain_rate = schema.DomainRateModel(
            domain_name=domain, rate_limit=limit
        )
        session.add(domain_rate)
        session.commit()

    @classmethod
    def get(cls, domain: str):
        """ Retrieves limit value for given domain """
        session = schema.DB.get_session()
        result = session.query(schema.DomainRateModel).filter(
            schema.DomainRateModel.domain_name == domain
        ).first()
        if result is None:
            return default_limit
        return result.rate_limit

    @classmethod
    def has(cls, domain: str):
        """ Check if the domain has a limit set """
        session = schema.DB.get_session()
        result = session.query(schema.DomainRateModel).filter(
            schema.DomainRateModel.domain_name == domain
        ).count()
        return result > 0
