from fastapi import FastAPI

from .database.base_orm import BaseORM
from .database.engine import mysql_engine

from .models.user import User

BaseORM.metadata.create_all(bind = mysql_engine)

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "hello"}
