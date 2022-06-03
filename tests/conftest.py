import pytest
from fastapi.testclient import TestClient
from typing import Generator
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from app.main import app
from app.db.base import *  # noqa
import pytest_asyncio


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def app_settings():
    from app.core.config import settings

    return settings


@pytest_asyncio.fixture
async def engine(app_settings):
    engine = create_engine(
        app_settings.TEST_DATABASE_URI,
    )
    return engine


@pytest_asyncio.fixture
async def session(engine):
    meta = SQLModel.metadata
    meta.schema = "freshdesk"
    meta.drop_all(engine)
    meta.create_all(engine)
    with Session(engine) as session:
        yield session

    meta.drop_all(engine)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
