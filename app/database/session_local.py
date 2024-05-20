from sqlalchemy.orm import sessionmaker

from .engine import mysql_engine

SessionLocal = sessionmaker(
  autocommit = False,
  autoflush = False,
  bind = mysql_engine
)
