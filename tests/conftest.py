import pytest
from fastapi.testclient import TestClient
from typing import Generator
from dotenv import load_dotenv
from app.auth.internal_auth import check_internal_auth
from app.main import app
from app.db.base import *  # noqa


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def app_settings():
    from app.core.config import settings

    return settings


@pytest.fixture(scope="module")
def client() -> Generator:
    app.dependency_overrides[check_internal_auth] = lambda: None

    with TestClient(app) as c:
        yield c
