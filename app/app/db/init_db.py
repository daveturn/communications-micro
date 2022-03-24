
from email.generator import Generator
from typing import Callable
import sqlalchemy
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from enum import Enum, auto

# Define your database names here.
# Enum used here to reduce chance of typos
class DatabaseName(Enum):
    DATABASE = auto()
from app.app.core.config import settings

# Make all models available for SQLModel.metadata.create_all to create tables
from .base import *


# To allow for multiple database connections to be set up in one app, get_session references this map
# to determine which credentials to use for a specific connection
DATABASE_URLS: dict[DatabaseName,str] = {
    DatabaseName.DATABASE: settings.SQLALCHEMY_DATABASE_URI,
    }



def _get_session_closure() -> Callable[[],Callable[[DatabaseName],Session]]:
    engines: dict[DatabaseName,sqlalchemy.engine.Engine] = {}

    def _get_engine(database_name:DatabaseName) -> sqlalchemy.engine.Engine:
        engine = engines.get(database_name)
        if not engine:
            database_url = DATABASE_URLS.get(database_name)
            engine = create_engine(database_url)
            engines[database_name] = engine

            if database_name == DatabaseName.DATABASE:
                SQLModel.metadata.create_all(engine)
        
        return engine

    def get_session(database_name: DatabaseName) -> Session:
        engine = _get_engine(database_name)

        def get_session_inner() -> Generator:
            with Session(engine) as session:
                yield session
            session.close()
        return get_session_inner

    return get_session
    

get_session = _get_session_closure()
