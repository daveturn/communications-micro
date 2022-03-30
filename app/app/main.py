from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.app.db.init_db import  get_session, DatabaseName
from app.app.core.config import settings


app = FastAPI()


# @app.on_event("startup")
# async def on_startup():
#     await init_db()

get_datawarehouse_session = get_session(DatabaseName.DATAWAREHOUSE)
get_read_only_prod_session = get_session(DatabaseName.TURN_READ_ONLY_PROD)


@app.get("/")
async def hello():
    return {"success": True}

@app.get("/run")
async def root(
        datawarehouse_session: Session = Depends(get_datawarehouse_session),
        read_only_prod_session: Session = Depends(get_read_only_prod_session)
        
        ):
    '''
        Example of how to add database dependencies to an endpoint
    '''

    pass
