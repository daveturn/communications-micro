from email.generator import Generator
from typing import Callable
import sqlalchemy
from sqlmodel import create_engine, Session
from enum import Enum, auto


# Define your database names here.
# Enum used here to reduce chance of typos
class DatabaseName(Enum):
    DATABASE = auto()


from app.core.config import settings  # noqa

# Make all models available for SQLModel.metadata.create_all to create tables
from .base import *  # noqa


# To allow for multiple database connections to be set up in one app, \
# get_session references this map
# to determine which credentials to use for a specific connection
DATABASE_URLS: dict[DatabaseName, str] = {
    DatabaseName.DATABASE: ""  # settings.SQLALCHEMY_DATABASE_URI,
}


def _get_session_closure() -> (
    Callable[[DatabaseName], Callable[..., Generator]]
):
    engines: dict[DatabaseName, sqlalchemy.engine.Engine] = {}

    def _get_engine(database_name: DatabaseName) -> sqlalchemy.engine.Engine:
        engine = engines.get(database_name)
        if not engine:
            database_url = DATABASE_URLS.get(database_name)
            if not database_url:
                raise Exception(
                    f"No database url found for name: {database_name}"
                )
            engine = create_engine(database_url)
            engines[database_name] = engine

            # if database_name == DatabaseName.ADVISE_DB_URI:
            #     SQLModel.metadata.create_all(engine)

        return engine

    def get_session(database_name: DatabaseName) -> Callable[..., Generator]:
        engine = _get_engine(database_name)

        def get_session_inner() -> Generator[
            Session, None, None  # type: ignore
        ]:
            # mypy complains with this line.
            # It says there is no __enter__ or __exit__ in Session
            # but there definitely is
            with Session(engine) as session:  # type: ignore
                yield session
            session.close()

        return get_session_inner

    return get_session


get_session = _get_session_closure()
