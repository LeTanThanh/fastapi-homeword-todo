from sqlalchemy.engine import URL

from .envs import MYSQL_HOST
from .envs import MYSQL_USERNAME
from .envs import MYSQL_PASSWORD
from .envs import MYSQL_DATABASE
from .envs import MYSQL_QUERY

ENGINE_URL = URL(
  drivername = "mysql+pymysql",
  host = MYSQL_HOST,
  username = MYSQL_USERNAME,
  password = MYSQL_PASSWORD,
  port = 3306,
  database= MYSQL_DATABASE,
  query = MYSQL_QUERY
)
