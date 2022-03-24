import pytest
import pytest_asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest_asyncio.fixture
async def turn_engine(app_settings):
    engine = create_engine(
        app_settings.TEST_TURN_READ_ONLY_DATABASE_URI,)
    return engine


@pytest_asyncio.fixture
async def turn_session(turn_engine):
    meta = SQLModel.metadata
    with Session(turn_engine) as session:  
        yield session
