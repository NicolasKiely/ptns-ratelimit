import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine


#: Base Schema to inherit
SchemaBase = declarative_base()


class DB:
    """ Database wrapper class """
    _engine = None
    _db_connect_string = None
    _session_maker = None

    @classmethod
    def get_engine(cls):
        """ Return sqlalchemy db engine """
        if cls._engine is None:
            cls._engine = create_engine(cls.get_db_connection_string())
        return cls._engine

    @classmethod
    def get_db_connection_string(cls):
        """ Return connection string for database """
        if cls._db_connect_string is None:
            try:
                cls._db_connect_string = os.environ["DB_CONNECTION"]
            except KeyError:
                print(
                    "Error, need to set database connection '%s' environment var!" %
                    "DB_CONNECTION"
                  )
                exit(1)
        return cls._db_connect_string

    @classmethod
    def get_session(cls):
        """ Returns db session """
        if cls._session_maker is None:
            cls._session_maker = sessionmaker(bind=cls.get_engine())
        return cls._session_maker()


class DomainRateModel(SchemaBase):
    """ SQL model for domain rates """
    __tablename__ = "domain_rate"

    pk = Column(Integer, primary_key=True)

    #: Name of domain
    domain_name = Column(String)

    #: Rate limit
    rate_limit = Column(Float)


#: Instantiate models with the db connections
SchemaBase.metadata.create_all(DB.get_engine())
