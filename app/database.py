from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:%s@localhost/todo?charset=utf8mb4" % quote_plus("Aa@123456")

engine = create_engine(
  SQLALCHEMY_DATABASE_URL
)

if not database_exists(engine.url):
  create_database(engine.url)

SessionLocal = sessionmaker(
  autocommit = False,
  autoflush = False,
  bind = engine
)

BaseORM = declarative_base()
