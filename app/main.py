from fastapi import FastAPI
from fastapi_utils.timing import add_timing_middleware
import logging

from app.middleware.LogUnsuccessfulResponse import (
    LoggingMiddleware,
)
from app.mailchimp.api.router import mailchimp_router

logger = logging.Logger(__name__, level=logging.DEBUG)
logger.setLevel(logging.DEBUG)


# from sqlmodel import Session
# from app.db.init_db import get_session, DatabaseName
# from app.core.config import settings


app = FastAPI()
app.add_middleware(LoggingMiddleware)

add_timing_middleware(
    app,
    record=logger.info,
    prefix="app",
)

# get_datawarehouse_session = get_session(DatabaseName.DATAWAREHOUSE)
# get_read_only_prod_session = get_session(DatabaseName.TURN_READ_ONLY_PROD)


@app.get("/")
async def hello():
    return True


@app.get("/run")
async def root(
    # datawarehouse_session: Session = Depends(get_datawarehouse_session),
    # read_only_prod_session: Session = Depends(get_read_only_prod_session)
):
    """
    Example of how to add database dependencies to an endpoint
    """

    pass


app.include_router(mailchimp_router)
