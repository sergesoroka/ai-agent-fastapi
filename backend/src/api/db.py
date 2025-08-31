import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("A database url needs to be set")

engine = sqlmodel.create_engine(DATABASE_URL)


def db_init():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session