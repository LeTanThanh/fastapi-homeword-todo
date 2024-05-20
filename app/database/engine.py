from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

from urllib.parse import quote_plus

DATABASE_URL = "mysql+pymysql://root:%s@localhost/fastapi-homeword-todo?charset=utf8mb4" % quote_plus("Aa@123456")

mysql_engine = create_engine(
  DATABASE_URL
)

if not database_exists(mysql_engine.url):
  create_database(mysql_engine.url)
