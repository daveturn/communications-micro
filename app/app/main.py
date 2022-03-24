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
    from app.app.freshdesk.tasks import UpdateFreshdeskDataTask
    from app.app.freshdesk.client import FreshdeskClient
    freshdesk = FreshdeskClient(
        api_key=settings.FRESHDESK_API_KEY,
        domain=settings.FRESHDESK_DOMAIN_NAME,
        version=settings.FRESHDESK_API_VERSION
    )
    task = UpdateFreshdeskDataTask(
        freshdesk=freshdesk,
        datawarehouse_session=datawarehouse_session,
        read_only_prod_session=read_only_prod_session
    )

    try:
        await task.run()
        return {"success": True}
    except Exception as e:
        return {"success": False, 'Error': e}
