from fastapi import FastAPI

from .database import BaseORM
from .database import engine

from .models.user import User

BaseORM.metadata.create_all(bind = engine)

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "hello"}
