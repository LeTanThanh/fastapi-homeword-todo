from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..database import BaseORM

class User(BaseORM):
  __tablename__ = "users"

  id = Column(Integer, primary_key = True)
  email = Column(String(255), unique = True, index = True)
  hashed_password = Column(String(255))
