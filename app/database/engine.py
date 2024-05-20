from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

from urllib.parse import quote_plus

from .engine_url import ENGINE_URL

mysql_engine = create_engine(
  ENGINE_URL
)

if not database_exists(mysql_engine.url):
  create_database(mysql_engine.url)
