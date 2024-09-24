from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from configparser import ConfigParser

# Note - The "connect string" shown in db_connection only goes so far as to specify the
# database name, which defaults to 'postgres' if you just hit enter.   in this case.
# Be sure to create the proper schema in the postgresql database BEFORE trying to run
# this code, SQLAlchemy will not do that for you.


config = ConfigParser()
config.read('config.ini')               # the config.ini file has to be in the working directory.

schema = config['schema']['schema name']
Base = declarative_base(metadata=MetaData(schema=schema))
metadata = Base.metadata
